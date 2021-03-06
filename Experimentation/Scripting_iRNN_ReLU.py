import VectorAutoRegress as var
from random import sample
import csv
from os import chdir
import platform
from time import gmtime, strftime

#Total number of machine lines: 12583
#sample_moments = sample(xrange(1,12584),50)
dirPathiRNN = '/home/minh/Desktop/Google_Data/processed/iRNN1-3'

if (platform.node() == "woosungpil-PC"):
    dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
elif (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed/'
elif (platform.node()=="Minh_Desktop1"):
    dirPath = 'E:\Google_Data\processed'
chdir(dirPath)

sample_moments = []

with open('sample_moments_30.csv', 'rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

print('length sample_moments:',len(sample_moments))

"""with open('sample_moments.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows([sample_moments])"""

chdir(dirPathiRNN)
for i in xrange(len(sample_moments)):
    var.VecAR(lineNumber=int(sample_moments[i]),meanLoad=30,modelName="iRNN",trainingPercent=0.9,trainingStep=1,
              inputvector=(1,3),labelvector=(1,6),in_neurons=3,out_neurons=6,hidden_neurons=100,batchsize=5,
              nb_epochs=3000,dropRate=0.5,activation="relu",loss="mean_squared_error",optimizer="rmsprop")