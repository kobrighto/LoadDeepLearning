import VectorAutoRegress as var
from random import sample
import csv
from os import chdir,listdir
import platform
from time import gmtime, strftime
import matplotlib.pyplot as plt
import ResultsCheck
import numpy as np

dirPathGRU = '/home/minh/Desktop/Google_Data/processed/GRU1-3'
dirPathiRNN = '/home/minh/Desktop/Google_Data/processed/iRNN1-3'
dirPathLSTM = '/home/minh/Desktop/Google_Data/processed/LSTM1-3'

count = 0
mseLSTMResult = [0]*3000

for fileName in listdir(dirPathLSTM):
    if fileName.startswith('predicted'):
        with open(dirPathLSTM+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,len(line)):
                        mseLSTMResult[j-1]+=float(line[j])
for i in xrange(len(mseLSTMResult)):
    mseLSTMResult[i]/=30

count = 0
mseiRNNResult = [0]*3000

for fileName in listdir(dirPathiRNN):
    if fileName.startswith('predicted'):
        with open(dirPathiRNN+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,len(line)):
                        mseiRNNResult[j-1]+=float(line[j])
for i in xrange(len(mseiRNNResult)):
    mseiRNNResult[i]/=30

count = 0
mseGRUResult = [0]*3000

for fileName in listdir(dirPathGRU):
    if fileName.startswith('predicted'):
        with open(dirPathGRU+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,len(line)):
                        mseGRUResult[j-1]+=float(line[j])
for i in xrange(len(mseGRUResult)):
    mseGRUResult[i]/=30

npLSTM = np.array(mseLSTMResult)
npGRU = np.array(mseGRUResult)
npiRNN = np.array(mseiRNNResult)

startPoint = 100
endPoint = 2901
step = 100

for i in xrange(startPoint,endPoint,step):
    print('iRNN mean from ', i, ' to ', (i+step), ' is: ', np.mean(npiRNN[i:(i+step)]))
    print('GRU mean from ', i, ' to ', (i+step), ' is: ', np.mean(npGRU[i:(i+step)]))
    print('LSTM mean from ', i, ' to ', (i+step), ' is: ', np.mean(npLSTM[i:(i+step)]))
    print('iRNN variance from ', i, ' to ', (i+step), ' is: ', np.var(npiRNN[i:(i+step)]))
    print('GRU variance from ', i, ' to ', (i+step), ' is: ', np.var(npGRU[i:(i+step)]))
    print('LSTM variance from ', i, ' to ', (i+step), ' is: ', np.var(npLSTM[i:(i+step)]))
    print('')

"""print('iRNN mean: ', np.mean(npiRNN), ', and variance: ', np.var(npiRNN[500:3000]))
print('GRU mean: ', np.mean(npGRU), ', and variance: ', np.var(npGRU[500:3000]))
print('LSTM mean: ', np.mean(npLSTM), ', and variance: ', np.var(npLSTM[500:3000]))"""

"""ResultsCheck.plotLines([(mseiRNNResult,'mseiRNN'),(mseGRUResult,'mseGRU'),
                        (mseLSTMResult,'mseLSTM')],['b-','r-','m-'])"""