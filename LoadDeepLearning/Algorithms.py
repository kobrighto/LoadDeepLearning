__author__ = 'Minh'

from statsmodels.tsa.ar_model import AR
import matplotlib.pyplot as plt
from os import listdir, chdir, path
import csv
import sys
import math
from pandas import ewma
import DataPostProcessing
import platform

def regressiveStep(inputList, paramsList):
    #paramsList_reverse = paramsList[::-1]
    prediction = 0
    for i in xrange(len(paramsList)):
        if i==0:
            prediction+=paramsList[i]
        else:
            prediction+=paramsList[i]*inputList[len(inputList)-i]
    return prediction

#curPoint always starts at 0 (curPoint for easier implementation)
def emaStep(inputList, weight, curPoint, lag):
    if curPoint==lag-1:
        return inputList[len(inputList)-lag]
    else:
        return (weight*inputList[len(inputList)-curPoint-1] + (1-weight)*emaStep(inputList,weight,curPoint+1,lag))

def ema(inputList,markPoint,weight,lag,numOfSteps):
    testList = inputList[markPoint:]
    trainingList = inputList[:markPoint]
    predictionList = []
    for i in xrange(len(testList)-numOfSteps+1):
        curPrediction = []
        tempList = inputList[:(markPoint+i)]
        for j in xrange(numOfSteps):
            curPrediction.append(emaStep(tempList,weight,0,lag))
            lastPrediction = emaStep(tempList,weight,0,lag)
            tempList.append(lastPrediction)
        predictionList.append(curPrediction)
    return (predictionList, testList)

def autoRegression(inputList, markPoint, lag, numOfSteps):
    testList = inputList[markPoint:]
    trainingList = inputList[:markPoint]
    ar_mod = AR(trainingList)
    ar_res=[]
    if lag<=0:
        ar_res = ar_mod.fit()
    else:
        ar_res = ar_mod.fit(lag)
    predictionList = []
    ar_res = ar_res.params
    #print(ar_res)
    for i in xrange(len(testList)-numOfSteps+1):
        curPrediction = []
        tempList = inputList[:(markPoint+i)]
        for j in xrange(numOfSteps):
            curPrediction.append(regressiveStep(tempList,ar_res))
            lastprediction = regressiveStep(tempList,ar_res)
            tempList.append(lastprediction)
        predictionList.append(curPrediction)
    return (predictionList, testList)

# 2 lists must have the same length
def plot2Lines(predictList, predictListname, secondList, secondListname):
    xAxis = xrange(len(predictList))
    tempList = []
    for i in xrange(len(predictList)):
        tempList.append(predictList[i][0])
    plt.plot(xAxis, tempList, 'b-')
    plt.plot(xAxis, secondList, 'r-')
    plt.legend([predictListname, secondListname], loc='upper left')
    plt.show()

def averageMSE(predictList, testList, root):
    totalMSE = 0
    count = 0
    for i in xrange(len(predictList)):
        for j in xrange(len(predictList[i])):
            count+=1
            totalMSE+=(predictList[i][j]-testList[i+j])*(predictList[i][j]-testList[i+j])
    totalMSE/=count
    if root==True:
        totalMSE=math.sqrt(totalMSE)
    return totalMSE

def percentOfRightPredictions(predictList, testList, errorLevel):
    rightPredictions = 0
    totalCount = 0
    for i in xrange(len(predictList)):
        for j in xrange(len(predictList[i])):
            totalCount+=1
            if abs(float(predictList[i][j])-float(testList[i+j]))<=errorLevel:
                rightPredictions+=1
    percent = float(rightPredictions)/float(totalCount)
    return (percent*100)

cpuList, memList = DataPostProcessing.meanLoad(8107,15)

print(len(cpuList))
print(len(memList))

predictList,testList = autoRegression(cpuList,int(0.9*(len(cpuList))),-1,6)

print('averageMSE of AR:', averageMSE(predictList, testList, True))

print('level 5: ',percentOfRightPredictions(predictList, testList, 5))
print('level 10: ',percentOfRightPredictions(predictList, testList, 10))
print('level 15: ',percentOfRightPredictions(predictList, testList, 15))

predictList, testList = ema(cpuList,int(0.9*(len(cpuList))),0.95,20,6)

print('averageMSE of EMA:', averageMSE(predictList, testList, True))

print('level 5: ',percentOfRightPredictions(predictList, testList, 5))
print('level 10: ',percentOfRightPredictions(predictList, testList, 10))
print('level 15: ',percentOfRightPredictions(predictList, testList, 15))

#plot2Lines(predictList, 'prediction', testList, 'test')