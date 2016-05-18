import VectorAutoRegress as var
from random import sample
import csv
from os import chdir
import platform
from time import gmtime, strftime

#Total number of machine lines: 12583
#sample_moments = sample(xrange(1,12584),50)
dirPath66 = '/home/minh/Desktop/Google_Data/processed/GRU6-6'
dirPath56 = '/home/minh/Desktop/Google_Data/processed/GRU5-6'
dirPath46 = '/home/minh/Desktop/Google_Data/processed/GRU4-6'
dirPath36 = '/home/minh/Desktop/Google_Data/processed/GRU3-6'
dirPath26 = '/home/minh/Desktop/Google_Data/processed/GRU2-6'
dirPath13 = '/home/minh/Desktop/Google_Data/processed/GRU1-3'
dirPath23 = '/home/minh/Desktop/Google_Data/processed/GRU2-3'
dirPath112 = '/home/minh/Desktop/Google_Data/processed/GRU1-12'
dirPath212 = '/home/minh/Desktop/Google_Data/processed/GRU2-12'


if (platform.node() == "woosungpil-PC"):
    dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
elif (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed/'
elif (platform.node()=="Minh_Desktop1"):
    dirPath = 'E:\Google_Data\processed'
chdir(dirPath)

sample_moments = []

with open('sample_moments_1000.csv', 'rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

print('length sample_moments: ', len(sample_moments))

"""with open('sample_moments.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows([sample_moments])"""

"""chdir(dirPath26)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(2,6),labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath13)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(1,3),labelvector=(1,6),in_neurons=3,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath23)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(2,3),labelvector=(1,6),in_neurons=3,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath112)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(1,12),labelvector=(1,6),in_neurons=12,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath36)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(3,6),labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath46)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(4,6),labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath56)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(5,6),labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")

chdir(dirPath66)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(6,6),labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")"""

chdir(dirPath212)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="GRU",trainingPercent=0.9,trainingStep=1,
              inputvector=(2,12),labelvector=(1,6),in_neurons=12,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=2000,dropRate=0.5,activation="linear",loss="mean_squared_error",optimizer="rmsprop")

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