
import pandas as pd
from random import random
from os import listdir, chdir, path
import platform
import Utilities
import numpy as np
import csv
from time import gmtime, strftime

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers import recurrent
from keras.initializations import normal, identity

def VecAR(lineNumber,meanLoad,modelName,trainingPercent,trainingStep,inputvector,labelvector,in_neurons,out_neurons,
          hidden_neurons,batchsize,nb_epochs,dropRate,activation,loss,optimizer):
    modelType = None
    if modelName == "LSTM":
        modelType = recurrent.LSTM
    elif modelName == "iRNN":
        modelType = recurrent.SimpleRNN
    elif modelName == "GRU":
        modelType = recurrent.GRU

    fileName = str(modelName) + "_" + str(lineNumber)+ "_" + strftime("%Y-%m-%d %H:%M") + ".csv"

    settings = []

    settings.append("lineNumber: " + str(lineNumber))
    settings.append("meanLoad: " + str(meanLoad))
    settings.append("modelName: " + str(modelName))
    settings.append("trainingPercent: " + str(trainingPercent))
    settings.append("trainingStep: " + str(trainingStep))
    settings.append("inputvector: " + str(inputvector))
    settings.append("labelvector: " + str(labelvector))
    settings.append("in_neurons: " + str(in_neurons))
    settings.append("out_neurons: " + str(out_neurons))
    settings.append("hidden_neurons: " + str(hidden_neurons))
    settings.append("batchsize: " + str(batchsize))
    settings.append("nb_epochs: " + str(nb_epochs))
    settings.append("dropRate: " + str(dropRate))
    settings.append("activation: " + str(activation))
    settings.append("loss: " + str(loss))
    settings.append("optimizer: " + str(optimizer))

    cpuList, memList = Utilities.meanLoad(lineNumber,meanLoad)

    markPoint = int(trainingPercent*len(cpuList))
    trainList = cpuList[:markPoint]
    testList = cpuList[markPoint:]
    X_train,y_train = Utilities.makeTrainorTestList(trainList=trainList,trainingStep=trainingStep,inputvector=inputvector
                                                             ,labelvector=labelvector)
    X_test,y_test = Utilities.makeTrainorTestList(trainList=testList,trainingStep=1,inputvector=inputvector
                                                           ,labelvector=labelvector)

    model = Sequential()
    if modelType == recurrent.SimpleRNN:
        model.add(modelType(input_dim=in_neurons,output_dim=hidden_neurons,
                            init=lambda shape: normal(shape, scale=0.001),
                            inner_init=lambda shape: identity(shape, scale=1.0),
                            return_sequences=False))
    else:
        model.add(modelType(input_dim=in_neurons,output_dim=hidden_neurons,return_sequences=False))
    model.add(Dropout(dropRate))

    model.add(Dense(input_dim=hidden_neurons,output_dim=out_neurons))

    model.add(Activation(activation))

    model.compile(loss=loss, optimizer=optimizer)

    print ('Evaluate seq2seqLSTM...')

    hist = model.fit(X_train, y_train, batch_size=batchsize, nb_epoch=nb_epochs, show_accuracy=True, verbose=2,
              validation_data=(X_test,y_test))

    predicted = model.predict(X_test)

    history = hist.history

    tempList = history.items()
    historyList = []
    for i in xrange(len(tempList)):
        aList = [tempList[i][0]]
        for j in xrange(len(tempList[i][1])):
            aList.append(tempList[i][1][j])
        historyList.append(aList)

    with open("predicted_" + fileName,'wb') as f:
        writer = csv.writer(f)
        writer.writerows(historyList)
        writer.writerows([settings])
        writer.writerows(predicted)
    with open("realvalue_" + fileName, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(historyList)
        writer.writerows([settings])
        writer.writerows(y_test)
