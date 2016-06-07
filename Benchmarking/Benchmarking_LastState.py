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

#polyFitPath = '/home/minh/Desktop/Google_Data/final/LastState1-6-12(first_500)'
polyFitPath = '/home/minh/Desktop/Google_Data/final/EMA1-6-12(first_500)(0.95)(order10)'

polyMSEList = []

polyPredictList = []
polyRealList = []
chdir(polyFitPath)
predictedCount = 0
realCount = 0
for filename in listdir(polyFitPath):
    splitted = filename.split('_')
    splitted2 = splitted[2].split('.')
    if splitted[0] == 'predicted':
        curmachineNo = splitted2[0]
        predictedCount+=1
        polyPredictname = filename
        with open(polyPredictname,'rb') as f:
            reader = csv.reader(f)
            for line in reader:
                polyPredictList.append(line)
        for filename2 in listdir(polyFitPath):
            splitted3 = filename2.split('_')
            splitted4 = splitted3[2].split('.')
            if splitted3[0] == 'realvalue' and splitted4[0]==curmachineNo:
                realCount+=1
                polyRealname = filename2
                with open(polyRealname,'rb') as f:
                    reader = csv.reader(f)
                    for line in reader:
                        polyRealList.append(line)
print('predictedCount:',predictedCount,'realCount:',realCount)
print('length polyPredictList:',len(polyPredictList),'length polyRealList:',len(polyRealList))

polyMSEList.append(AccuracyMetrics.averageMSE(predictList=polyPredictList,testList=polyRealList,root=True))

print('length lastStateMSEList:',len(polyMSEList))

print('lastState mse mean:', np.mean(polyMSEList),'lastState mse variance:',np.var(polyMSEList))