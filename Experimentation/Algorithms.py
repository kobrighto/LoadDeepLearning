__author__ = 'Minh'

from statsmodels.tsa.ar_model import AR
import matplotlib.pyplot as plt
from os import listdir, chdir, path
import csv
import sys
import math
from pandas import ewma
import platform
import Utilities

def emaStep(testList, weight, lag, numOfSteps):
    resultList = []
    tempList = []
    for i in xrange(len(testList)):
        tempList.append(testList[i])
    for i in xrange(numOfSteps):
        weightList = [0]*lag
        operatorList = []
        for i in xrange(len(weightList)):
            if i==0:
                weightList[i]=weight
            elif i==len(weightList)-1:
                weightList[i]=(1-weight)**i
            else:
                weightList[i]=((1-weight)**i) * weight
        for i in xrange(len(tempList)-1,len(tempList)-lag-1,-1):
            operatorList.append(tempList[i])
        result = 0
        for i in xrange(len(weightList)):
            result += weightList[i]*operatorList[i]
        resultList.append(result)
        tempList.append(result)
    return resultList

def ema(lineNumber, meanLoad, trainingPercent, trainingStep, inputvector, labelvector, weight, lag):
    if (platform.node() == "woosungpil-PC"):
        dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
    elif (platform.node()=="minh-titan"):
        dirPath = '/home/minh/Desktop/Google_Data/processed/'
    elif (platform.node()=="Minh_Desktop1"):
        dirPath = 'E:\Google_Data\processed'
    chdir(dirPath)
    cpuList,memList = Utilities.meanLoad(lineNumber,meanLoad)

    markPoint = int(trainingPercent*len(cpuList))
    startPoint = markPoint + inputvector[0]*inputvector[1]-1

    numOfSteps = labelvector[1]
    realValueList = []
    predictList = []
    for i in xrange(startPoint,len(cpuList)-labelvector[1]):
        curReal = []
        for j in xrange(numOfSteps):
            curReal.append(cpuList[i+j])
        curPredict = emaStep(cpuList[:startPoint],weight,lag,numOfSteps)
        realValueList.append(curReal)
        predictList.append(curPredict)
    return (realValueList, predictList)

def averageMSE(predictList,testList,root):
    totalMSE = 0
    count = 0
    for i in xrange(len(predictList)):
        for j in xrange(len(predictList[i])):
            count+=1
            totalMSE+=(predictList[i][j]-testList[i][j])*(predictList[i][j]-testList[i][j])
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
