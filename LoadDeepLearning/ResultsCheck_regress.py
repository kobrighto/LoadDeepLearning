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
predictFileName = 'predicted_8107_20epochs_regress.csv'
testFileName = 'test_data_8107_20epochs_regress.csv'
predictLength = 6
prediction = []
test = []

with open(predictFileName,'rb') as f:
    reader = csv.reader(f)
    prediction = list(reader)

with open(testFileName, 'rb') as f:
    reader = csv.reader(f)
    test = list(reader)

processedPrediction = []
for i in xrange(len(prediction)):
    for j in xrange(1,len(prediction[i])):
        processedPrediction.append([float(prediction[i][j])])

processedTest = []
for i in xrange(len(test)):
    for j in xrange(1,len(test[i])):
        processedTest.append(float(test[i][j]))

"""mse = 0
for i in xrange(len(processedTest)):
    mse+=(float(processedPrediction[i])-float(processedTest[i])) * \
         (float(processedPrediction[i])-float(processedTest[i]))
rmse = np.sqrt(mse/len(processedTest))"""

averageMSE = Algorithms.averageMSE(processedPrediction,processedTest,False)

print('seq2seqLSTM RMSE: ', averageMSE)

print('level 5: ',Algorithms.percentOfRightPredictions(processedPrediction, processedTest, 5))
print('level 10: ',Algorithms.percentOfRightPredictions(processedPrediction, processedTest, 10))
print('level 15: ',Algorithms.percentOfRightPredictions(processedPrediction, processedTest, 15))

"""print('length processedTest: ', len(processedTest))
print('processedTest: ', processedTest)
print('processedPrediction: ', processedPrediction)"""