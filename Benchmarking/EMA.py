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
        curPredict = emaStep(cpuList[:i],weight,lag,numOfSteps)
        realValueList.append(curReal)
        predictList.append(curPredict)
    return (realValueList, predictList)

dirPath = '/home/minh/Desktop/Google_Data/final/EMA1-3(last_500)(0.95)(order10)'
chdir(dirPath)

sample_moments = []

with open('sample_moments_500_second.csv','rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

print('length sample_moments: ', len(sample_moments))

for i in xrange(len(sample_moments)):
    realvalueList, predictList = ema(lineNumber=int(sample_moments[i]), meanLoad=30, trainingPercent=0.9, trainingStep=1,
                                                inputvector=(1,3), labelvector=(1,6), weight=0.95, lag=10)
    realname = 'realvalue_EMA_' + str(sample_moments[i]) + '.csv'
    predictname = 'predicted_EMA_' + str(sample_moments[i]) + '.csv'

    chdir(dirPath)
    with open(realname,'wb') as f:
        writer = csv.writer(f)
        writer.writerows(realvalueList)
    with open(predictname,'wb') as f:
        writer = csv.writer(f)
        writer.writerows(predictList)
    print('finish ', str(i+1), ' machine')