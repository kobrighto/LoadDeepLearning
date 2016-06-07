from statsmodels.tsa.ar_model import AR
import matplotlib.pyplot as plt
from os import listdir, chdir, path
import csv
import sys
import math
from pandas import ewma
import platform
import Utilities
import AccuracyMetrics
import numpy as np

gru13Path = '/home/minh/Desktop/Google_Data/final/GRU1-6-12(first_500)'
polyFitPath = '/home/minh/Desktop/Google_Data/final/LastState1-3(first_500)'

chdir(gru13Path)
with open('sample_moments_500.csv','rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

print('length sample_moments: ', len(sample_moments))

gruMSEList = []
polyMSEList = []

for i in xrange(len(sample_moments)):
    for filename in listdir(gru13Path):
        splitted = filename.split('_')
        if splitted[2]==str(sample_moments[i]) and splitted[0] == 'predicted':
            gruPredictname = filename
        elif splitted[2]==str(sample_moments[i]) and splitted[0] == 'realvalue':
            gruRealname = filename

    lineCount = 0
    gruPredictList = []
    gruRealList = []
    chdir(gru13Path)
    with open(gruPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gruPredictList.append(line)
    lineCount = 0
    with open(gruRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gruRealList.append(line)
    lineCount = 0

    polyPredictList = []
    polyRealList = []
    for filename in listdir(polyFitPath):
        splitted = filename.split('_')
        splitted2 = splitted[2].split('.')
        if str(splitted2[0]) == str(sample_moments[i]) and splitted[0] == 'predicted':
            polyPredictname = filename
        elif str(splitted2[0])==str(sample_moments[i]) and splitted[0] == 'realvalue':
            polyRealname = filename
    chdir(polyFitPath)
    with open(polyPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            polyPredictList.append(line)
    with open(polyRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            polyRealList.append(line)

    gruMSEList.append(AccuracyMetrics.averageMSE(predictList=gruPredictList,testList=gruRealList,root=True))
    polyMSEList.append(AccuracyMetrics.averageMSE(predictList=polyPredictList,testList=polyRealList,root=True))

positiveCount=0
negativeCount=0
print('length gruMSEList:',len(gruMSEList))
print('length arMSEList:',len(polyMSEList))
for i in xrange(len(gruMSEList)):
    if gruMSEList[i]<polyMSEList[i]:
        positiveCount +=1
    else:
        negativeCount +=1
print('positiveCount:', positiveCount)
print('negativeCount:', negativeCount)

print('gru mse mean:', np.mean(gruMSEList),'gru mse variance:',np.var(gruMSEList))
print('poly mse mean:', np.mean(polyMSEList),'poly mse variance:',np.var(polyMSEList))