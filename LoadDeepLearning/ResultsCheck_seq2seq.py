__author__ = 'Minh'

import platform
from os import listdir, chdir, path
import csv
import sys
import math
import numpy as np
import Algorithms

if (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed'
    chdir(dirPath)

chdir(dirPath)
predictFileName = 'predicted_8107_20epochs.csv'
testFileName = 'test_data_8107_20epochs.csv'
predictLength = 6
prediction = []
test = []

with open(predictFileName,'rb') as f:
    reader = csv.reader(f)
    for line in reader:
        prediction.append(line[1])
    prediction = prediction[1:]

with open(testFileName, 'rb') as f:
    reader = csv.reader(f)
    for line in reader:
        test.append(line[1])
    test = test[1:]

processedPrediction = []
processedTest = []
for i in xrange(len(prediction)):
    for j in xrange(predictLength):
        processedPrediction.append([int(prediction[i][(j*3):(j*3+3)])])

for i in xrange(len(test)):
    for j in xrange(predictLength):
        processedTest.append(int(test[i][(j*3):(j*3+3)]))

averageMSE = Algorithms.averageMSE(processedPrediction,processedTest,False)

print('seq2seqLSTM MSE: ', averageMSE)

print('level 5: ',Algorithms.percentOfRightPredictions(processedPrediction, processedTest, 5))
print('level 10: ',Algorithms.percentOfRightPredictions(processedPrediction, processedTest, 10))
print('level 15: ',Algorithms.percentOfRightPredictions(processedPrediction, processedTest, 15))