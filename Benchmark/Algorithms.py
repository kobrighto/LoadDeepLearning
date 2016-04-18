__author__ = 'Minh'

from statsmodels.tsa.ar_model import AR
import matplotlib.pyplot as plt
from os import listdir, chdir, path
import csv
import sys
import math
from pandas import ewma

def regressiveStep(inputList, paramsList):
    paramsList_reverse = paramsList[::-1]
    prediction = 0
    for i in xrange(len(paramsList_reverse)):
        if i==0:
            prediction+=paramsList_reverse[i]
        else:
            prediction+=paramsList_reverse[i]*inputList[len(inputList)-i]
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
            error = (predictList[i][j]-testList[i+j])/testList[i+j]
            if abs(error)*100<errorLevel:
                rightPredictions+=1
    percent = float(rightPredictions)/float(totalCount)
    return (percent*100)

dirPath="E:/Google_Data/processed"
chdir(dirPath)

lineCount = 1

csv.field_size_limit(sys.maxint)
cpuUsage = []
memUsage = []

with open('usage_1_minute_total_converted_no_duplicates.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        if lineCount>1:
            break
        cpuUsage = line[4].split(',')
        cpuUsage[0]=cpuUsage[0][1:]
        cpuUsage[len(cpuUsage)-1]=cpuUsage[len(cpuUsage)-1][:-1]
        memUsage = line[5].split(',')
        memUsage[0]=memUsage[0][1:]
        memUsage[len(memUsage)-1]=memUsage[len(memUsage)-1][:-1]
        lineCount+=1

for i in xrange(len(cpuUsage)):
    cpuUsage[i] = float(cpuUsage[i])
    memUsage[i] = float(memUsage[i])

"""print(len(cpuUsage))

predictList,testList = autoRegression(cpuUsage,31320,-1,3)

print(averageMSE(predictList, testList, True))

print('level 5: ',percentOfRightPredictions(predictList, testList, 5))
print('level 25: ',percentOfRightPredictions(predictList, testList, 25))
print('level 45: ',percentOfRightPredictions(predictList, testList, 45))
print('level 65: ',percentOfRightPredictions(predictList, testList, 65))
print('level 85: ',percentOfRightPredictions(predictList, testList, 85))
print('level 100: ',percentOfRightPredictions(predictList, testList, 100))

plot2Lines(predictList, 'predict', testList, 'test')"""

list = [1,3,5,6,7,9,3,4]
predictionList, testList = ema(list,4,0.9,3,2)
print('testList: ', testList)
print('predictionList: ', predictionList)
