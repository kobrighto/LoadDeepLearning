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
#arPath2 = '/home/minh/Desktop/Google_Data/final/AutoRegression1-3(first_500)'
gru13Path = '/home/minh/Desktop/Google_Data/final/GRU1-3(first_500)'

chdir(gru13Path)
with open('sample_moments_500.csv','rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

gruPredictList = []
gruRealList = []
arPredictList = []
arRealList = []

for i in xrange(len(sample_moments)):
    for filename in listdir(gru13Path):
        splitted = filename.split('_')
        if splitted[2]==str(sample_moments[i]) and splitted[0] == 'predicted':
            gruPredictname = filename
        elif splitted[2]==str(sample_moments[i]) and splitted[0] == 'realvalue':
            gruRealname = filename

    lineCount = 0

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

for curStep in xrange(6):
    curMSE = 0
    count = 0
    for i in xrange(len(arPredictList)):
        count+=1
        curMSE+=(float(arPredictList[i][curStep])-float(arRealList[i][curStep]))*(float(arPredictList[i][curStep])-float(arRealList[i][curStep]))
    curMSE/=count
    print('ar','curStep:',curStep,'curMSE:',curMSE,'count:',count)

for curStep in xrange(6):
    curMSE = 0
    count = 0
    for i in xrange(len(gruPredictList)):
        count+=1
        curMSE+=(float(gruPredictList[i][curStep])-float(gruRealList[i][curStep]))*(float(gruPredictList[i][curStep])-float(gruRealList[i][curStep]))
    curMSE/=count
    print('gru','curStep:',curStep,'curMSE:',curMSE,'count:',count)