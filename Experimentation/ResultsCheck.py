import VectorAutoRegress as var
from random import sample
import csv
from os import chdir,listdir
import platform
from time import gmtime, strftime
import matplotlib.pyplot as plt

dirPath66 = '/home/minh/Desktop/Google_Data/processed/Input6-6'
dirPath56 = '/home/minh/Desktop/Google_Data/processed/Input5-6'
dirPath46 = '/home/minh/Desktop/Google_Data/processed/Input4-6'
dirPath36 = '/home/minh/Desktop/Google_Data/processed/Input3-6'
dirPath26 = '/home/minh/Desktop/Google_Data/processed/Input2-6'
dirPath16 = '/home/minh/Desktop/Google_Data/processed/Input1-6'

def plotLines(graphList,colorList):
    xAxis = xrange(len(graphList[0][0]))
    legendList = []
    for i in xrange(len(graphList)):
        plt.plot(xAxis,graphList[i][0],colorList[i])
        legendList.append(graphList[i][1])
    plt.legend(legendList, loc='upper left')
    plt.show()

def plot2Lines(predictList, predictListname, secondList, secondListname):
    xAxis = xrange(len(predictList))
    tempList = []
    for i in xrange(len(predictList)):
        tempList.append(predictList[i][0])
    plt.plot(xAxis, tempList, 'b-')
    plt.plot(xAxis, secondList, 'r-')
    plt.legend([predictListname, secondListname], loc='upper left')
    plt.show()

rmse16 = [0]*500
for fileName in listdir(dirPath16):
    if fileName.startswith('predicted'):
        with open(dirPath16+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for i in xrange(1,len(line)):
                        rmse16[i-1]+=float(line[i])

for i in xrange(len(rmse16)):
    rmse16[i]/=50

plotLines([(rmse16[100:],'rmse16')],['b-'])