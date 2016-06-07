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
import AccuracyMetrics
import numpy as np

arPath = '/home/minh/Desktop/Google_Data/final/AutoRegression1-3(first_500)(lag7cmle)'
emaPath = '/home/minh/Desktop/Google_Data/final/EMA1-3(first_500)'
gru13Path = '/home/minh/Desktop/Google_Data/final/GRU1-3(first_500)'

chdir(gru13Path)
with open('sample_moments_500.csv','rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

print('length sample_moments: ', len(sample_moments))

gruMSEList = []
arMSEList = []
emaMSEList = []

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

    arPredictList = []
    arRealList = []
    for filename in listdir(arPath):
        splitted = filename.split('_')
        splitted2 = splitted[2].split('.')
        if str(splitted2[0]) == str(sample_moments[i]) and splitted[0] == 'predicted':
            arPredictname = filename
        elif str(splitted2[0])==str(sample_moments[i]) and splitted[0] == 'realvalue':
            arRealname = filename
    chdir(arPath)
    with open(arPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            arPredictList.append(line)
    with open(arRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            arRealList.append(line)

    emaPredictList = []
    emaRealList = []
    for filename in listdir(emaPath):
        splitted = filename.split('_')
        splitted2 = splitted[2].split('.')
        if str(splitted2[0]) == str(sample_moments[i]) and splitted[0] == 'predicted':
            emaPredictname = filename
        elif str(splitted2[0])==str(sample_moments[i]) and splitted[0] == 'realvalue':
            emaRealname = filename
    chdir(emaPath)
    with open(emaPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            emaPredictList.append(line)
    with open(emaRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            emaRealList.append(line)

    gruMSEList.append(AccuracyMetrics.averageMSE(predictList=gruPredictList,testList=gruRealList,root=True))
    arMSEList.append(AccuracyMetrics.averageMSE(predictList=arPredictList,testList=arRealList,root=True))
    emaMSEList.append(AccuracyMetrics.averageMSE(predictList=emaPredictList,testList=emaRealList,root=True))
positiveCount=0
negativeCount=0
print('length gruMSEList:',len(gruMSEList))
print('length arMSEList:',len(arMSEList))
for i in xrange(len(gruMSEList)):
    if gruMSEList[i]<emaMSEList[i]:
        positiveCount +=1
    else:
        negativeCount +=1
print('positiveCount:', positiveCount)
print('negativeCount:', negativeCount)

print('gru mse mean:', np.mean(gruMSEList),'gru mse variance:',np.var(gruMSEList))
print('ar mse mean:', np.mean(arMSEList),'ar mse variance:',np.var(arMSEList))
print('ema mse mean:', np.mean(emaMSEList),'ar mse variance:',np.var(emaMSEList))
#AccuracyMetrics.plotLines(graphList=[(gruMSEList[:100],'gruMSE'),(arMSEList[:100],'arMSE')],colorList=['b-','r-'])
