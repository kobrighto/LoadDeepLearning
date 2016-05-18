import VectorAutoRegress as var
from random import sample
import csv
from os import chdir,listdir
import platform
from time import gmtime, strftime
import matplotlib.pyplot as plt
import ResultsCheck
import numpy as np

dirPathGRU16 = '/home/minh/Desktop/Google_Data/processed/GRU1-6'
dirPathGRU26 = '/home/minh/Desktop/Google_Data/processed/GRU2-6'
dirPathGRU112 = '/home/minh/Desktop/Google_Data/processed/GRU1-12'
dirPathGRU212 = '/home/minh/Desktop/Google_Data/processed/GRU2-12'
dirPathGRU13 = '/home/minh/Desktop/Google_Data/processed/GRU1-3'
dirPathGRU23 = '/home/minh/Desktop/Google_Data/processed/GRU2-3'

mseGRU16Result = [0]*2000
for fileName in listdir(dirPathGRU16):
    if fileName.startswith('predicted'):
        with open(dirPathGRU16+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,2001):
                        mseGRU16Result[j-1]+=float(line[j])
for i in xrange(len(mseGRU16Result)):
    mseGRU16Result[i]/=30

mseGRU26Result = [0]*2000
for fileName in listdir(dirPathGRU26):
    if fileName.startswith('predicted'):
        with open(dirPathGRU26+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,len(line)):
                        mseGRU26Result[j-1]+=float(line[j])
for i in xrange(len(mseGRU26Result)):
    mseGRU26Result[i]/=30

mseGRU112Result = [0]*2000
for fileName in listdir(dirPathGRU112):
    if fileName.startswith('predicted'):
        with open(dirPathGRU112+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,len(line)):
                        mseGRU112Result[j-1]+=float(line[j])
for i in xrange(len(mseGRU112Result)):
    mseGRU112Result[i]/=30

mseGRU212Result = [0]*2000
for fileName in listdir(dirPathGRU212):
    if fileName.startswith('predicted'):
        with open(dirPathGRU212+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,len(line)):
                        mseGRU212Result[j-1]+=float(line[j])
for i in xrange(len(mseGRU212Result)):
    mseGRU212Result[i]/=30

mseGRU13Result = [0]*2000
for fileName in listdir(dirPathGRU13):
    if fileName.startswith('predicted'):
        with open(dirPathGRU13+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,len(line)):
                        mseGRU13Result[j-1]+=float(line[j])
for i in xrange(len(mseGRU13Result)):
    mseGRU13Result[i]/=30

mseGRU23Result = [0]*2000
for fileName in listdir(dirPathGRU23):
    if fileName.startswith('predicted'):
        with open(dirPathGRU23+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for j in xrange(1,len(line)):
                        mseGRU23Result[j-1]+=float(line[j])
for i in xrange(len(mseGRU23Result)):
    mseGRU23Result[i]/=30

npGRU16 = np.array(mseGRU16Result)
npGRU26 = np.array(mseGRU26Result)
npGRU112 = np.array(mseGRU112Result)
npGRU212 = np.array(mseGRU212Result)
npGRU13 = np.array(mseGRU13Result)
npGRU23 = np.array(mseGRU23Result)

for i in xrange(100,2001,200):
    print('GRU16 mean from ', i, ' to ', (i+200), ' is: ', np.mean(npGRU16[i:(i+200)]))
    print('GRU26 mean from ', i, ' to ', (i+200), ' is: ', np.mean(npGRU26[i:(i+200)]))
    print('GRU112 mean from ', i, ' to ', (i+200), ' is: ', np.mean(npGRU112[i:(i+200)]))
    print('GRU212 mean from ', i, ' to ', (i+200), ' is: ', np.mean(npGRU212[i:(i+200)]))
    print('GRU13 mean from ', i, ' to ', (i+200), ' is: ', np.mean(npGRU13[i:(i+200)]))
    print('GRU23 mean from ', i, ' to ', (i+200), ' is: ', np.mean(npGRU23[i:(i+200)]))
    print('GRU16 variance from ', i, ' to ', (i+200), ' is: ', np.var(npGRU16[i:(i+200)]))
    print('GRU26 variance from ', i, ' to ', (i+200), ' is: ', np.var(npGRU26[i:(i+200)]))
    print('GRU112 variance from ', i, ' to ', (i+200), ' is: ', np.var(npGRU112[i:(i+200)]))
    print('GRU212 variance from ', i, ' to ', (i+200), ' is: ', np.var(npGRU212[i:(i+200)]))
    print('GRU13 variance from ', i, ' to ', (i+200), ' is: ', np.var(npGRU13[i:(i+200)]))
    print('GRU23 variance from ', i, ' to ', (i+200), ' is: ', np.var(npGRU23[i:(i+200)]))
    print('')

"""print('iRNN mean: ', np.mean(npiRNN), ', and variance: ', np.var(npiRNN[500:3000]))
print('GRU mean: ', np.mean(npGRU), ', and variance: ', np.var(npGRU[500:3000]))
print('LSTM mean: ', np.mean(npLSTM), ', and variance: ', np.var(npLSTM[500:3000]))

ResultsCheck.plotLines([(mseGRU16Result,'mseiRNN'),(mseGRU13Result,'mseGRU'),
                        (mseGRU23Result,'mseLSTM')],['b-','r-','m-'])"""