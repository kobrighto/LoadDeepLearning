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

def regressiveStep(inputList, paramsList, numOfSteps):
    #paramsList_reverse = paramsList[::-1]
    tempList = []
    for i in xrange(len(inputList)):
        tempList.append(inputList[i])
    predictionList = []
    for i in xrange(numOfSteps):
        prediction = 0
        for i in xrange(len(paramsList)):
            if i==0:
                prediction+=paramsList[i]
            else:
                prediction+=paramsList[i]*tempList[len(tempList)-i]
        tempList.append(prediction)
        predictionList.append(prediction)
    return predictionList

def regress(trainList,lag):
    ar_mod = AR(trainList)
    if lag<=0:
        ar_res = ar_mod.fit()
    else:
        ar_res = ar_mod.fit(lag)
    ar_res = ar_res.params
    print('ar_res:',ar_res)
    return ar_res

def autoRegression(lineNumber, meanLoad, trainingPercent, trainingStep, inputvector, labelvector, lag):
    if (platform.node() == "woosungpil-PC"):
        dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
    elif (platform.node()=="minh-titan"):
        dirPath = '/home/minh/Desktop/Google_Data/processed/'
    elif (platform.node()=="Minh_Desktop1"):
        dirPath = 'E:\Google_Data\processed'
    chdir(dirPath)
    cpuList,memList = Utilities.meanLoad(lineNumber,meanLoad)

    markPoint = int(trainingPercent*len(cpuList))
    trainList = cpuList[:markPoint]

    numOfSteps = labelvector[1]
    ar_res = regress(trainList,lag)

    startPoint = markPoint + inputvector[0]*inputvector[1]
    realValueList = []
    predictList = []
    for i in xrange(startPoint,len(cpuList)-labelvector[1]+1):
        curReal = []
        for j in xrange(numOfSteps):
            curReal.append(cpuList[i+j])
        curPredict = regressiveStep(cpuList[:i],ar_res,numOfSteps)
        realValueList.append(curReal)
        predictList.append(curPredict)
    return(realValueList,predictList)

dirPath = '/home/minh/Desktop/Google_Data/final/AutoRegression1-3(first_500)(lag6)'
chdir(dirPath)

sample_moments = []

with open('sample_moments_500.csv','rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

print('length sample_moments: ', len(sample_moments))

for i in xrange(len(sample_moments)):
    realvalueList, predictList = autoRegression(lineNumber=int(sample_moments[i]), meanLoad=30, trainingPercent=0.9, trainingStep=1,
                                                inputvector=(1,3), labelvector=(1,6), lag=6)
    realname = 'realvalue_AR_' + str(sample_moments[i]) + '.csv'
    predictname = 'predicted_AR_' + str(sample_moments[i]) + '.csv'

    chdir(dirPath)
    with open(realname,'wb') as f:
        writer = csv.writer(f)
        writer.writerows(realvalueList)
    with open(predictname,'wb') as f:
        writer = csv.writer(f)
        writer.writerows(predictList)
    print('finish ', str(i+1), ' machine')