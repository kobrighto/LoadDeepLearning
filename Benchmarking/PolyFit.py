__author__ = 'Minh'

import numpy as np
import matplotlib.pyplot as plt
from os import listdir, chdir, path
import csv
import sys
import math
from pandas import ewma
import platform
import Utilities

def polyFit(lineNumber,meanLoad,trainingPercent,trainingStep,inputvector,labelvector,order):
    if (platform.node() == "woosungpil-PC"):
        dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
    elif (platform.node()=="minh-titan"):
        dirPath = '/home/minh/Desktop/Google_Data/processed/'
    elif (platform.node()=="Minh_Desktop1"):
        dirPath = 'E:\Google_Data\processed'
    chdir(dirPath)
    cpuList,memList = Utilities.meanLoad(lineNumber,meanLoad)

    markPoint = int(trainingPercent*len(cpuList))
    """yList = cpuList[:markPoint]
    xList = []
    for i in xrange(len(yList)):
        xList.append(i+1)
    z = np.polyfit(xList,yList,order)
    zEst = np.poly1d(z)"""

    numOfSteps = labelvector[1]

    startPoint = markPoint + inputvector[0]*inputvector[1]
    realValueList = []
    predictList = []
    for i in xrange(startPoint,len(cpuList)-labelvector[1]+1):
        yList = cpuList[:i]
        xList = []
        for k in xrange(len(yList)):
            xList.append(k+1)
        z = np.polyfit(xList,yList,order)
        zEst = np.poly1d(z)
        curReal = []
        curPredict = []
        for j in xrange(numOfSteps):
            curReal.append(cpuList[i+j])
            curPredict.append(zEst(i+j+1))
        realValueList.append(curReal)
        predictList.append(curPredict)
    return(realValueList,predictList)

dirPath = '/home/minh/Desktop/Google_Data/final/PolyFit1-3(first_500)(order5)'
chdir(dirPath)

sample_moments = []

with open('sample_moments_500.csv','rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

print('length sample_moments: ', len(sample_moments))

for i in xrange(len(sample_moments)):
    realvalueList, predictList = polyFit(lineNumber=int(sample_moments[i]), meanLoad=30, trainingPercent=0.9, trainingStep=1,
                                                inputvector=(1,3), labelvector=(1,6), order=10)
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