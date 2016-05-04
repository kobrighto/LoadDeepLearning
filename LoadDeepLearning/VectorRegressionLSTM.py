import pandas as pd
from random import random
from os import listdir, chdir, path
import platform
import DataPostProcessing
import numpy as np

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM, SimpleRNN
from keras.initializations import normal, identity

in_neurons = 6
out_neurons = 6
hidden_neurons = 100
nb_epochs = 200

model = Sequential()

model.add(LSTM(input_dim=in_neurons,output_dim=hidden_neurons,return_sequences=False))
#model.add(LSTM(input_dim=hidden_neurons,output_dim=hidden_neurons, return_sequences=False))
model.add(Dropout(0.5))

model.add(Dense(input_dim=hidden_neurons,output_dim=out_neurons))

model.add(Activation("linear"))
#model.add(Activation('relu'))

#model.compile(loss="mean_squared_error", optimizer="rmsprop")
model.compile(loss="mean_squared_error", optimizer="adam")

cpuList, memList = DataPostProcessing.meanLoad(9218,30)
#cpuList, memList = DataPostProcessing.sampling(12236,2)

markPoint = int(0.9*len(cpuList))
trainList = cpuList[:markPoint]
testList = cpuList[markPoint:]
X_train,y_train = DataPostProcessing.makeTrainorTestList(trainList=trainList,trainingStep=1,inputvector=(3,6)
                                                         ,labelvector=(1,6))
X_test,y_test = DataPostProcessing.makeTrainorTestList(trainList=testList,trainingStep=1,inputvector=(3,6)
                                                       ,labelvector=(1,6))

print ('Evaluate seq2seqLSTM...')

model.fit(X_train, y_train, batch_size=5, nb_epoch=nb_epochs, show_accuracy=True,
          validation_data=(X_test,y_test))

predicted = model.predict(X_test)

pd.DataFrame(predicted).to_csv("predicted_8107_20epochs_regress.csv")
pd.DataFrame(y_test).to_csv("test_data_8107_20epochs_regress.csv")

# and maybe plot it
#pd.DataFrame(y_test[:100]).plot("test_data.csv")