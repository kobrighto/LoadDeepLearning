import VectorAutoRegress as var
from random import sample
import csv
from os import chdir,listdir
import platform
from time import gmtime, strftime
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

print('Start program: ', dt.datetime.now().strftime('%H:%M:%S'))

if (platform.node() == "woosungpil-PC"):
    dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
elif (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed/'
elif (platform.node()=="Minh_Desktop1"):
    dirPath = 'E:\Google_Data\processed'
chdir(dirPath)

n1 = dt.datetime.now()
var.VecAR(1,meanLoad=30,modelName="iRNN",trainingPercent=0.9,trainingStep=1,
          inputvector=(2,6),labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,
          nb_epochs=100,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")
n2 = dt.datetime.now()

n3 = dt.datetime.now()
var.VecAR(1,meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
          inputvector=(2,6),labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,
          nb_epochs=100,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")
n4 = dt.datetime.now()

n5 = dt.datetime.now()
var.VecAR(1,meanLoad=30,modelName="LSTM",trainingPercent=0.9,trainingStep=1,
          inputvector=(2,6),labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,
          nb_epochs=100,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")
n6 = dt.datetime.now()


print('Start iRNN: ', n1.strftime('%H:%M:%S'))
print('End iRNN: ', n2.strftime('%H:%M:%S'))
print('Elapsed iRNN: ', (n2-n1).seconds)

print('Start GRU: ', n3.strftime('%H:%M:%S'))
print('End GRU: ', n4.strftime('%H:%M:%S'))
print('Elapsed GRU: ', (n4-n3).seconds)

print('Start LSTM: ', n5.strftime('%H:%M:%S'))
print('End LSTM: ', n6.strftime('%H:%M:%S'))
print('Elapsed LSTM: ', (n6-n5).seconds)