from __future__ import print_function

from os import listdir, chdir, path
import gzip
import csv
import sys
import matplotlib.pyplot as plt
from datetime import datetime
import platform
import DataPostProcessing

if (platform.platform()=="Linux-3.19.0-25-generic-x86_64-with-Ubuntu-14.04-trusty"):
    dirPath = '/home/minh/Desktop/Google_Data/processed'
    chdir(dirPath)
    filename = 'usage_1_minute_total_converted_no_duplicates.csv'

"""def makeLists(lineNumber, interval):
    dirPath = '/home/minh/Desktop/Google_Data/processed'
    chdir(dirPath)
    filename = 'usage_1_minute_total_converted_no_duplicates.csv'

    csv.field_size_limit(sys.maxsize)
    cpuList = []
    memList = []
    lineCount = 1

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if lineCount>lineNumber:
                break
            elif lineCount==lineNumber:
                cpuList = line[4].split(',')
                memList = line[5].split(',')
                break
            else:
                lineCount+=1
        for i in range(0,len(cpuList)):
            if i==0:
                cpuList[i]=float(cpuList[i][1:].strip())
            elif i==len(cpuList)-1:
                cpuList[i]=float(cpuList[i][:-1].strip())
        for i in range(0,len(memList)):
            if i==0:
                memList[i]=float(memList[i][1:].strip())
            elif i==len(memList)-1:
                memList[i]=float(memList[i][:-1].strip())
        resultcpuList=[]
        resultmemList=[]
        for i in xrange(0,len(cpuList),interval):
            resultcpuList.append(cpuList[i])
            resultmemList.append(memList[i])
        for i in xrange(len(resultcpuList)):
            if float(resultcpuList[i])>100:
                resultcpuList[i]=100
            if float(resultmemList[i])>100:
                resultmemList[i]=100
        return (resultcpuList, resultmemList)"""

#markPoint: length of the training set
def makeTrainTestLists(cpuList,memList,markPoint,length,times):
    traincpuList = cpuList[:markPoint]
    trainmemList = memList[:markPoint]
    testcpuList = cpuList[markPoint-length:]
    testmemList = cpuList[markPoint-length:]
    for i in xrange(len(traincpuList)):
        traincpuList[i]=int(float(traincpuList[i])*times)
        trainmemList[i]=int(float(trainmemList[i])*times)
    for i in xrange(len(testcpuList)):
        testcpuList[i]=int(float(testcpuList[i])*times)
        testmemList[i]=int(float(testmemList[i])*times)
    finaltraincpuList =[]
    finaltrainmemList = []
    finaltestcpuList = []
    finaltestmemList = []
    finaltraincpuLabels = traincpuList[length:]
    finaltrainmemLabels = trainmemList[length:]
    finaltestcpuLabels = testcpuList[length:]
    finaltestmemLabels = testmemList[length:]
    for i in xrange(len(traincpuList)-length):
        subcpuList = []
        submemList = []
        for j in xrange(length):
            subcpuList.append(traincpuList[i+j])
            submemList.append(trainmemList[i+j])
        finaltraincpuList.append(subcpuList)
        finaltrainmemList.append(submemList)
    for i in xrange(len(testcpuList)-length):
        subcpuList = []
        submemList = []
        for j in xrange(length):
            subcpuList.append(testcpuList[i+j])
            submemList.append(testmemList[i+j])
        finaltestcpuList.append(subcpuList)
        finaltestmemList.append(submemList)
    return (finaltraincpuList,finaltrainmemList,finaltestcpuList,finaltestmemList,
            finaltraincpuLabels,finaltrainmemLabels,finaltestcpuLabels,finaltestmemLabels)

"""def round(traincpu,trainmem,testcpu,testmem,traincpulabels,trainmemlabels,testcpulabels,testmemlabels,times):
    for i in xrange(len(traincpu)):
        traincpu[i]=int(traincpu[i]*times)
        trainmem[i]=int(trainmem[i]*times)
        traincpulabels[i]=int(traincpulabels[i]*times)
        trainmemlabels[i]=int(trainmemlabels[i]*times)
    for i in xrange(len(testcpu)):
        testcpu[i]=int(testcpu[i]*times)
        testmem[i]=int(testmem[i]*times)
        testcpulabels[i]=int(testcpulabels[i]*times)
        testmemlabels[i]=int(testmemlabels[i]*times)"""

cpuList,memList = DataPostProcessing.meanLoad(10,1)
#cpuList, memList = makeLists(10,2)
print('cpuList length:', len(cpuList))

"""traincpu,trainmem,testcpu,testmem,traincpulabels,trainmemlabels,testcpulabels,testmemlabels \
    = makeTrainTestLists(cpuList,memList,16000,50,1)"""

traincpu,trainmem,testcpu,testmem,traincpulabels,trainmemlabels,testcpulabels,testmemlabels \
    = DataPostProcessing.makeTrainTestLists(cpuList,memList,30,int(0.75*len(cpuList)),30,1)

"""for i in xrange(len(testcpulabels)):
    print(testcpulabels[i])"""

#keras deep learning from here
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.initializations import normal, identity
from keras.layers.recurrent import SimpleRNN, LSTM
from keras.optimizers import RMSprop
from keras.utils import np_utils


batch_size = 5
nb_classes = 10
nb_epochs = 100
hidden_units = 100

learning_rate = 1e-6
clip_norm = 1.0

"""woo = np.array([[1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]],np.int32)

woo = np.array(traincpu, np.int32)"""

trainList = np.array(traincpu, np.int32)


# convert class vectors to binary class matrices
"""woo_label_raw = np.array([0,0,0,0,0,1,1,1,1,1],np.int32)
woo_label = np_utils.to_categorical(woo_label_raw, nb_classes)"""

"""templabels=[]
print(traincpulabels[len(traincpulabels)-1])
num = 57
traincpulabels.append(num)
traincpulabels.append(num)
traincpulabels.append(num)
traincpulabels.append(num)
for i in range(len(traincpulabels)-4):
    tempnum = (traincpulabels[i] + traincpulabels[i+1] + traincpulabels[i+2] + traincpulabels[i+3] + traincpulabels[i+4])/5

    if tempnum/10==10:
        templabels.append(9)
    else:
        templabels.append(int(tempnum/10))"""

convertedlabels = []
for i in xrange(len(traincpulabels)):
    if traincpulabels[i]/10==10:
        convertedlabels.append(9)
    else:
        convertedlabels.append(int(traincpulabels[i]/10))


#woo_label_raw = np.array(traincpulabels, np.int32)
#woo_label_raw = np.array(templabels, np.int32)
#woo_label = np_utils.to_categorical(woo_label_raw, nb_classes)

trainList_label_raw = np.array(convertedlabels, np.int32)
trainList_label = np_utils.to_categorical(trainList_label_raw, nb_classes)

#print (woo[0])
#print("label")
#print(woo_label[0])
#labels range from 0-999

#woo_label = np.array([1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1],np.int32)

#new_woo = woo.reshape((10,4,1))
#new_woo = woo.reshape((len(traincpu),50,1))
trainList_reshape = trainList.reshape((len(traincpu)),30,1)
#reshape((number_of_data,30,1))

#new_woo_label = woo_label.reshape(10,2)
trainList_label_reshape = trainList_label.reshape((len(traincpu),10))
#reshape((number_of_data,number_of_classes))
#number_of_classes = 1001 currently

"""templabels=[]
num1 = 57
testcpulabels.append(num1)
testcpulabels.append(num1)
testcpulabels.append(num1)
testcpulabels.append(num1)

for i in range(len(testcpulabels)-4):
    tempnum = (testcpulabels[i] + testcpulabels[i+1] + testcpulabels[i+2] + testcpulabels[i+3] + testcpulabels[i+4])/5
    if tempnum/10==10:
        templabels.append(9)
    else:
        templabels.append(int(tempnum/10))"""

convertedlabels = []
for i in xrange(len(testcpulabels)):
    if traincpulabels[i]/10==10:
        convertedlabels.append(9)
    else:
        convertedlabels.append(int(traincpulabels[i]/10))

#woo_test = np.array(testcpu, np.int32)
#woo_label_raw_test = np.array(templabels, np.int32)

testList = np.array(testcpu, np.int32)
testList_label_raw = np. array(convertedlabels, np.int32)

#woo_label_test = np_utils.to_categorical(woo_label_raw_test, nb_classes)
testList_label = np_utils.to_categorical(testList_label_raw, nb_classes)

testList_reshape = testList.reshape((len(testcpu)),30,1)
testList_label_reshape = testList_label.reshape(len(testcpu),10)

#new_woo_test = woo_test.reshape((len(testcpu),50,1))
#new_woo_label_test = woo_label_test.reshape(len(testcpu),10)


print('Evaluate IRNN...')
model = Sequential()
model.add(SimpleRNN(output_dim=hidden_units,
                    init=lambda shape: normal(shape, scale=0.001),
                    inner_init=lambda shape: identity(shape, scale=1.0),
                    activation='relu', input_shape=trainList_reshape.shape[1:]))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
rmsprop = RMSprop(lr=learning_rate)
model.compile(loss='categorical_crossentropy', optimizer=rmsprop)

"""model.fit(new_woo, new_woo_label, batch_size=batch_size, nb_epoch=nb_epochs,
          show_accuracy=True, verbose=1)"""
model.fit(trainList_reshape, trainList_label_reshape, batch_size=batch_size, nb_epoch=nb_epochs,
          show_accuracy=True, verbose=1)

#scores = model.evaluate(new_woo_test, new_woo_label_test, show_accuracy=True, verbose=0)

predictions = model.predict_classes(testList_reshape, batch_size=batch_size, verbose = 1)

with open('predictionResult.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows([predictions,testcpulabels])


"""print('IRNN test score:', scores[0])
print('IRNN test accuracy:', scores[1])

print('Compare to LSTM...')
model = Sequential()
model.add(LSTM(hidden_units, input_shape=new_woo.shape[1:]))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
rmsprop = RMSprop(lr=learning_rate)
model.compile(loss='categorical_crossentropy', optimizer=rmsprop)

model.fit(new_woo, new_woo_label, batch_size=batch_size, nb_epoch=nb_epochs,
          show_accuracy=True, verbose=1, validation_data=(new_woo_test, new_woo_label_test))

scores = model.evaluate(new_woo_test, new_woo_label_test, show_accuracy=True, verbose=0)
print('LSTM test score:', scores[0])
print('LSTM test accuracy:', scores[1])"""