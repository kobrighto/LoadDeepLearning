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

gru13Path = '/home/minh/Desktop/Google_Data/final/GRU1-3(first_500)'
chdir(gru13Path)

MSEList = []

for filename in listdir(gru13Path):
    if filename.startswith('predicted'):
        with open(filename,'rb') as f:
            lineCount = 0
            reader = csv.reader(f)
            for line in reader:
                lineCount+=1
                if lineCount==5:
                    curMSEList=line[1:]
                elif lineCount>5:
                    break
        MSEList.append(curMSEList)

resultepochs = []
for i in xrange(2000):
    curMSE = 0
    count = 0
    for j in xrange(len(MSEList)):
        count+=1
        curMSE+=float(MSEList[j][i])
    curMSE/=count
    resultepochs.append(curMSE)
for i in xrange(len(resultepochs)):
    print('cur epoch:',i,'result:',resultepochs[i])

