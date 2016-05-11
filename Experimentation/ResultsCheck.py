import VectorAutoRegress as var
from random import sample
import csv
from os import chdir,listdir
import platform
from time import gmtime, strftime
import matplotlib.pyplot as plt
import Algorithms

dirPath66 = '/home/minh/Desktop/Google_Data/processed/Input6-6'
dirPath56 = '/home/minh/Desktop/Google_Data/processed/Input5-6'
dirPath46 = '/home/minh/Desktop/Google_Data/processed/Input4-6'
dirPath36 = '/home/minh/Desktop/Google_Data/processed/Input3-6'
dirPath26 = '/home/minh/Desktop/Google_Data/processed/Input2-6'
dirPath16 = '/home/minh/Desktop/Google_Data/processed/Input1-6'
dirPathList = [dirPath16,dirPath26,dirPath36,dirPath46,dirPath56,dirPath66]

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

sample_moments = []
with open('/home/minh/Desktop/Google_Data/processed/sample_moments.csv', 'rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

"""mse16 = [0]*500
for fileName in listdir(dirPath16):
    if fileName.startswith('predicted_LSTM_2180'):
        pass
    elif fileName.startswith('predicted'):
        with open(dirPath16+'/'+fileName,'r') as f:
            reader = csv.reader(f)
            for line in reader:
                if line[0]=='val_loss':
                    for i in xrange(1,len(line)):
                        mse16[i-1]+=float(line[i])

for i in xrange(len(mse16)):
    mse16[i]/=49"""

mseResults = []

for i in xrange(len(dirPathList)):
    curmse = [0]*500
    for fileName in listdir(dirPathList[i]):
        if fileName.startswith('predicted_LSTM_2180'):
            pass
        elif fileName.startswith('predicted'):
            with open(dirPathList[i]+'/'+fileName,'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    if line[0]=='val_loss':
                        for j in xrange(1,len(line)):
                            curmse[j-1]+=float(line[j])
    for i in xrange(len(curmse)):
        curmse[i]/=49
    mseResults.append(curmse)


"""sample_moments.remove('2180')
mseEMA = 0
mseEMAresults = []

for i in xrange(len(sample_moments)):
    realValueList,predictList = Algorithms.ema(lineNumber=int(sample_moments[i]), meanLoad=30, trainingPercent=0.9,
                                               trainingStep=1,inputvector=(1,6), labelvector=(1,6),
                                               weight=0.95, lag=10)
    curEMA = Algorithms.averageMSE(predictList,realValueList,False)
    mseEMA+=curEMA
    mseEMAresults.append(curEMA)
    print('len: ', len(mseEMAresults))
    print('last mseEMA result: ', curEMA)
mseEMA/=49
mseEMAList = [mseEMA]*500"""

sample_moments.remove('2180')
mseAR = 0
mseARresults = []

for i in xrange(len(sample_moments)):
    realValueList,predictList = Algorithms.autoRegression(lineNumber=int(sample_moments[i]), meanLoad=30,
                                                          trainingPercent=0.9,trainingStep=1,inputvector=(1,6),
                                                          labelvector=(1,6), lag=10)
    curAR = Algorithms.averageMSE(predictList,realValueList,False)
    mseAR+=curAR
    mseARresults.append(curAR)
    print('len: ', len(mseARresults))
    print('last mseEMA result: ', curAR)
mseAR/=49
mseARList = [mseAR]*500

plotLines([(mseResults[0],'mse16'),(mseARList,'mseAR')],['b-','r-'])
"""plotLines([(mseResults[0][100:],'mse16'),(mseResults[1][100:],'mse26'),(mseResults[2][100:],'mse36'),
           (mseResults[3][100:],'mse46'),(mseResults[4][100:],'mse56'),(mseResults[5][100:],'mse66')],
          ['b-','r-','g-','c-','m-','y-'])"""