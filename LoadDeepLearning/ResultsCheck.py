__author__ = 'Minh'

import platform
from os import listdir, chdir, path
import csv
import sys
import math

if (platform.platform()=="Linux-3.19.0-25-generic-x86_64-with-Ubuntu-14.04-trusty"):
    dirPath = '/home/minh/Desktop/Google_Data/processed'

chdir(dirPath)
filename = 'predictionResult.csv'
lineCount = 1
prediction = []
test = []

with open(filename,'rb') as f:
    reader = csv.reader(f)
    for line in enumerate(reader):
        if lineCount==1:
            prediction = line[1]
        elif lineCount==2:
            test = line[1]
        lineCount+=1

numCount = 0
difference = 0
for i in xrange(len(prediction)):
    curPrediction = (float(prediction[i])*10)+5
    curTest = float(test[i])
    difference+=(curPrediction-curTest)*(curPrediction-curTest)
    numCount+=1
accuracy = math.sqrt(difference/numCount)

print('Accuracy (RMSE): ', accuracy)