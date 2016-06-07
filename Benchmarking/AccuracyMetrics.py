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

def averageMSE(predictList,testList,root):
    totalMSE = 0
    count = 0
    for i in xrange(len(predictList)):
        for j in xrange(len(predictList[i])):
            count+=1
            totalMSE+=(float(predictList[i][j])-float(testList[i][j]))*(float(predictList[i][j])-float(testList[i][j]))
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

def plotLines(graphList,colorList):
    xAxis = xrange(len(graphList[0][0]))
    legendList = []
    for i in xrange(len(graphList)):
        plt.plot(xAxis,graphList[i][0],colorList[i])
        legendList.append(graphList[i][1])
    plt.legend(legendList, loc='upper left')
    plt.show()