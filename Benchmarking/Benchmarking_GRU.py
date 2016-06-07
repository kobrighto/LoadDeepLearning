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

gru13Path = '/home/minh/Desktop/Minh/GRU1-3'
gru16Path = '/home/minh/Desktop/Minh/GRU1-6'
gru112Path = '/home/minh/Desktop/Minh/GRU1-12'
gru23Path = '/home/minh/Desktop/Minh/GRU2-3'
gru26Path = '/home/minh/Desktop/Minh/GRU2-6'
gru212Path = '/home/minh/Desktop/Minh/GRU2-12'

chdir(gru13Path)
with open('sample_moments_30.csv','rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

gru13PredictList = []
gru13RealList = []
gru16PredictList = []
gru16RealList = []
gru112PredictList = []
gru112RealList = []
gru23PredictList = []
gru23RealList = []
gru26PredictList = []
gru26RealList = []
gru212PredictList = []
gru212RealList = []

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
                gru13PredictList.append(line)
    lineCount = 0
    with open(gruRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru13RealList.append(line)
    lineCount = 0

    for filename in listdir(gru16Path):
        splitted = filename.split('_')
        if splitted[2]==str(sample_moments[i]) and splitted[0] == 'predicted':
            gruPredictname = filename
        elif splitted[2]==str(sample_moments[i]) and splitted[0] == 'realvalue':
            gruRealname = filename

    lineCount = 0
    chdir(gru16Path)
    with open(gruPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru16PredictList.append(line)
    lineCount = 0
    with open(gruRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru16RealList.append(line)
    lineCount = 0

    for filename in listdir(gru112Path):
        splitted = filename.split('_')
        if splitted[2]==str(sample_moments[i]) and splitted[0] == 'predicted':
            gruPredictname = filename
        elif splitted[2]==str(sample_moments[i]) and splitted[0] == 'realvalue':
            gruRealname = filename

    lineCount = 0
    chdir(gru112Path)
    with open(gruPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru112PredictList.append(line)
    lineCount = 0
    with open(gruRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru112RealList.append(line)
    lineCount = 0

    for filename in listdir(gru23Path):
        splitted = filename.split('_')
        if splitted[2]==str(sample_moments[i]) and splitted[0] == 'predicted':
            gruPredictname = filename
        elif splitted[2]==str(sample_moments[i]) and splitted[0] == 'realvalue':
            gruRealname = filename

    lineCount = 0
    chdir(gru23Path)
    with open(gruPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru23PredictList.append(line)
    lineCount = 0
    with open(gruRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru23RealList.append(line)
    lineCount = 0

    for filename in listdir(gru26Path):
        splitted = filename.split('_')
        if splitted[2]==str(sample_moments[i]) and splitted[0] == 'predicted':
            gruPredictname = filename
        elif splitted[2]==str(sample_moments[i]) and splitted[0] == 'realvalue':
            gruRealname = filename

    lineCount = 0
    chdir(gru26Path)
    with open(gruPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru26PredictList.append(line)
    lineCount = 0
    with open(gruRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru26RealList.append(line)
    lineCount = 0

    for filename in listdir(gru212Path):
        splitted = filename.split('_')
        if splitted[2]==str(sample_moments[i]) and splitted[0] == 'predicted':
            gruPredictname = filename
        elif splitted[2]==str(sample_moments[i]) and splitted[0] == 'realvalue':
            gruRealname = filename

    lineCount = 0
    chdir(gru212Path)
    with open(gruPredictname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru212PredictList.append(line)
    lineCount = 0
    with open(gruRealname,'rb') as f:
        reader = csv.reader(f)
        for line in reader:
            lineCount+=1
            if lineCount>7:
                gru212RealList.append(line)
    lineCount = 0

print('gru13:',AccuracyMetrics.averageMSE(predictList=gru13PredictList,testList=gru13RealList,root=True))
print('gru16:',AccuracyMetrics.averageMSE(predictList=gru16PredictList,testList=gru16RealList,root=True))
print('gru112:',AccuracyMetrics.averageMSE(predictList=gru112PredictList,testList=gru112RealList,root=True))
print('gru23:',AccuracyMetrics.averageMSE(predictList=gru23PredictList,testList=gru23RealList,root=True))
print('gru26:',AccuracyMetrics.averageMSE(predictList=gru26PredictList,testList=gru26RealList,root=True))
print('gru212:',AccuracyMetrics.averageMSE(predictList=gru212PredictList,testList=gru212RealList,root=True))