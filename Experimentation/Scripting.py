import VectorAutoRegress as var
from random import sample
import csv
from os import chdir
import platform
from time import gmtime, strftime

#Total number of machine lines: 12583
#sample_moments = sample(xrange(1,12584),50)

dirPath46 = '/home/minh/Desktop/Google_Data/processed/Input4-6'
dirPath36 = '/home/minh/Desktop/Google_Data/processed/Input3-6'
dirPath26 = '/home/minh/Desktop/Google_Data/processed/Input2-6'
dirPath16 = '/home/minh/Desktop/Google_Data/processed/Input1-6'
dirPath66 = '/home/minh/Desktop/Google_Data/processed/Input6-6'

if (platform.node() == "woosungpil-PC"):
    dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
elif (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed/'
elif (platform.node()=="Minh_Desktop1"):
    dirPath = 'E:\Google_Data\processed'
chdir(dirPath)

sample_moments = []

with open('sample_moments.csv', 'rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

"""with open('sample_moments.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows([sample_moments])"""

chdir(dirPath46)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,trainingPercent=0.9,trainingStep=1,inputvector=(4,6),
              labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,nb_epochs=500,dropRate=0.5,
              activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath36)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,trainingPercent=0.9,trainingStep=1,inputvector=(3,6),
              labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,nb_epochs=500,dropRate=0.5,
              activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath26)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,trainingPercent=0.9,trainingStep=1,inputvector=(2,6),
              labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,nb_epochs=500,dropRate=0.5,
              activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath16)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,trainingPercent=0.9,trainingStep=1,inputvector=(1,6),
              labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,nb_epochs=500,dropRate=0.5,
              activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath66)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,trainingPercent=0.9,trainingStep=1,inputvector=(6,6),
              labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,nb_epochs=500,dropRate=0.5,
              activation="linear",loss="mean_squared_error",optimizer="rmsprop")

#Example:
"""
    lineNumber = 9218
    meanLoad = 30

    trainingPercent = 0.9
    trainingStep = 1
    inputvector = (6,6)
    labelvector = (1,6)

    in_neurons = 6
    out_neurons = 6
    hidden_neurons = 128
    batchsize = 5
    nb_epochs = 2

    dropRate = 0.5
    activation = "linear"
    loss = "mean_squared_error"
    optimizer = "rmsprop"
"""