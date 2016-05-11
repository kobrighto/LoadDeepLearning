import VectorAutoRegress as var
from random import sample
import csv
from os import chdir
import platform
from time import gmtime, strftime

#Total number of machine lines: 12583
#sample_moments = sample(xrange(1,12584),50)
dirPathGRU = '/home/minh/Desktop/Google_Data/processed/iRNN1-6'
dirPathiRNN = '/home/minh/Desktop/Google_Data/processed/GRU1-6'

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

chdir(dirPathiRNN)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,trainingPercent=0.9,trainingStep=1,inputvector=(1,6),
              labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,nb_epochs=500,dropRate=0.5,
              activation="linear",loss="mean_squared_error",optimizer="rmsprop",modelName="iRNN")

chdir(dirPathGRU)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,trainingPercent=0.9,trainingStep=1,inputvector=(1,6),
              labelvector=(1,6),in_neurons=6,out_neurons=6,hidden_neurons=100,batchsize=5,nb_epochs=500,dropRate=0.5,
              activation="linear",loss="mean_squared_error",optimizer="rmsprop",modelName="GRU")

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