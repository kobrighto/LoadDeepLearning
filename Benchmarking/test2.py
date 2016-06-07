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

arPath = '/home/minh/Desktop/Google_Data/final/AutoRegression1-3(first_500)'

number = 12088

arPredictList = []
arRealList = []

for filename in listdir(arPath):
    splitted = filename.split('_')
    splitted2 = splitted[2].split('.')
    if str(splitted2[0]) == str(number) and splitted[0] == 'predicted':
        arPredictname = filename
    elif str(splitted2[0])==str(number) and splitted[0] == 'realvalue':
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