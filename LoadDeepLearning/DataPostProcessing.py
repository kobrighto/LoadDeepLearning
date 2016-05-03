__author__ = 'Minh'

import platform
from os import listdir, chdir, path
import csv
import sys
import numpy as np

if (platform.node() == "woosungpil-PC"):
    dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
elif (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed'
elif (platform.node()=="Minh_Desktop1"):
    dirPath = 'E:\Google_Data\processed'

def sampling(lineNo, noOfMinutes):
    csv.field_size_limit(sys.maxint)
    chdir(dirPath)
    lineCount = 1
    cpuList = []
    memList = []
    with open('usage_1_minute_total_converted_no_duplicates.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if lineCount>lineNo:
                break
            elif lineCount==lineNo:
                cpuList = line[4].split(',')
                cpuList[0] = cpuList[0][1:]
                cpuList[len(cpuList)-1] = cpuList[len(cpuList)-1][:-1]
                memList = line[5].split(',')
                memList[0] = memList[0][1:]
                memList[len(memList)-1] = memList[len(memList)-1][:-1]
                break
            else:
                lineCount+=1

    for i in xrange(len(cpuList)):
        if float(cpuList[i])>100:
            cpuList[i]=100
        if float(memList[i])>100:
            memList[i]=100
    finalcpulist = []
    finalmemlist = []
    for i in xrange(0,len(cpuList),noOfMinutes):
        finalcpulist.append(float(cpuList[i]))
        finalmemlist.append(float(memList[i]))
    return(finalcpulist, finalmemlist)

def meanLoad(lineNo, noOfMinutes):
    csv.field_size_limit(sys.maxint)
    chdir(dirPath)
    lineCount = 1
    cpuList = []
    memList = []
    with open('usage_1_minute_total_converted_no_duplicates.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            if lineCount>lineNo:
                break
            elif lineCount==lineNo:
                cpuList = line[4].split(',')
                cpuList[0] = cpuList[0][1:]
                cpuList[len(cpuList)-1] = cpuList[len(cpuList)-1][:-1]
                memList = line[5].split(',')
                memList[0] = memList[0][1:]
                memList[len(memList)-1] = memList[len(memList)-1][:-1]
                break
            else:
                lineCount+=1
            
    #print('Done 1')
    for i in xrange(len(cpuList)):
        if float(cpuList[i])>100:
            cpuList[i]=100
        if float(memList[i])>100:
            memList[i]=100
    i = 0
    meanCPUList = []
    meanMemList = []
    while i+noOfMinutes-1<len(cpuList):
        sumCPU = 0
        sumMem = 0
        for j in xrange(noOfMinutes):
            sumCPU += float(cpuList[i+j])
            sumMem += float(memList[i+j])
        meanCPUList.append(sumCPU/noOfMinutes)
        meanMemList.append(sumCPU/noOfMinutes)
        i+=noOfMinutes
    for i in xrange(len(meanCPUList)):
        meanCPUList[i]=int(meanCPUList[i])
        meanMemList[i]=int(meanMemList[i])
    return (meanCPUList, meanMemList)

def appendZero(number,length):
    number = str(number)
    for i in xrange(length-len(number)):
        number = '0'+number
    return number

def makeListSequence(trainList,trainingStep,inputvector,labelvector):
    traincpuList = []
    for i in xrange(0,len(trainList)-inputvector[0]*inputvector[1]-labelvector[0]*labelvector[1]+1
                    ,trainingStep):
        for j in xrange(inputvector[0]):
            curString = ''
            for k in xrange(inputvector[1]):
                curString+=appendZero(int(round(trainList[i+j*inputvector[1]+k])),3)
            traincpuList.append(curString)
    traincpuLabels = []
    for i in xrange(inputvector[0]*inputvector[1],len(trainList)-labelvector[0]*labelvector[1]+1
                    ,trainingStep):
        curString = ''
        for j in xrange(labelvector[1]):
            curTotal = 0.0
            for k in xrange(labelvector[0]):
                curTotal += trainList[i+j*labelvector[0]+k]
            curMean = int(round(curTotal/float(labelvector[0])))
            curString+=appendZero(curMean,3)
        traincpuLabels.append(curString)
    return(traincpuList,traincpuLabels)

def makeTrainorTestList(trainList,trainingStep,inputvector,labelvector):
    traincpuList = []
    for i in xrange(0,len(trainList)-inputvector[0]*inputvector[1]-labelvector[0]*labelvector[1]+1
                    ,trainingStep):
        subcpuList = []
        for j in xrange(inputvector[0]):
            subList = []
            for k in xrange(inputvector[1]):
                subList.append(trainList[i+j*inputvector[1]+k])
            subcpuList.append(subList)
        traincpuList.append(subcpuList)
    traincpuLabels = []
    for i in xrange(inputvector[0]*inputvector[1],len(trainList)-labelvector[0]*labelvector[1]+1
                    ,trainingStep):
        subcpulabels = []
        for j in xrange(labelvector[1]):
            curTotal = 0.0
            for k in xrange(labelvector[0]):
                curTotal += trainList[i+j*labelvector[0]+k]
            curMean = curTotal/float(labelvector[0])
            subcpulabels.append(curMean)
        traincpuLabels.append(subcpulabels)
    for i in xrange(len(traincpuList)):
        for j in xrange(len(traincpuList[i])):
            for k in xrange(len(traincpuList[i][j])):
                if traincpuList[i][j][k]<100:
                    traincpuList[i][j][k] = '0'+str(int(traincpuList[i][j][k]))
                else:
                    traincpuList[i][j][k] = str(int(traincpuList[i][j][k]))
    for i in xrange(len(traincpuLabels)):
        for j in xrange(len(traincpuLabels[i])):
            if traincpuLabels[i][j]<100:
                traincpuLabels[i][j] = '0'+str(int(traincpuLabels[i][j]))
            else:
                traincpuLabels[i][j] = str(int(traincpuLabels[i][j]))
    return(np.array(traincpuList),np.array(traincpuLabels))



#inputvector example: (15x3), labelvector example: (15x6), pairCount example: 6946
#markPoint: number of trainingPairs
def makeTrainTestList_backup(cpuList,markPoint,inputvector,labelvector):
    traincpuList = []
    traincpuLabels = []
    for i in xrange(0,len(cpuList)-inputvector[0]*inputvector[1]+1,inputvector[1]):
        subcpuList = []
        for j in xrange(inputvector[0]):
            subList = []
            for k in xrange(inputvector[1]):
                subList.append(cpuList[i+j*inputvector[1]+k])
            subcpuList.append(subList)
        traincpuList.append(subcpuList)
    for i in xrange(inputvector[1]*inputvector[0],len(cpuList)-labelvector[0]*labelvector[1]+1,inputvector[1]):
        subcpulabels = []
        for j in xrange(labelvector[1]):
            curTotal = 0.0
            for k in xrange(labelvector[0]):
                curTotal+=cpuList[i+j*labelvector[0]+k]
            curMean = curTotal/float(labelvector[0])
            subcpulabels.append(curMean)
        traincpuLabels.append(subcpulabels)

    pairCount = -1
    if len(traincpuList)>len(traincpuLabels):
        pairCount=len(traincpuLabels)
    else:
        pairCount=len(traincpuList)
    print('Total number of vector pairs: ', pairCount)
    traincpuList = traincpuList[:pairCount]
    traincpuLabels = traincpuLabels[:pairCount]
    markPoint = int(markPoint)
    finaltraincpulist = np.array(traincpuList[:markPoint])
    finaltraincpulabels = np.array(traincpuLabels[:markPoint])
    finaltestcpulist = np.array(traincpuList[markPoint:])
    finaltestcpulabels = np.array(traincpuLabels[markPoint:])
    return (finaltraincpulist,finaltraincpulabels,finaltestcpulist,finaltestcpulabels)

#meanLabel: labels are made from mean of ? number of load values
def makeTrainTestLists_backup2(cpuList,memList,meanLabel,markPoint,length,times):
    traincpuList = cpuList[:markPoint]
    trainmemList = memList[:markPoint]
    testcpuList = cpuList[markPoint-length+1:]
    testmemList = memList[markPoint-length+1:]
    finaltraincpuList =[]
    finaltrainmemList = []
    finaltestcpuList = []
    finaltestmemList = []
    for i in xrange(len(traincpuList)-length+1):
        subcpuList = []
        submemList = []
        for j in xrange(length):
            subcpuList.append(traincpuList[i+j])
            submemList.append(trainmemList[i+j])
        finaltraincpuList.append(subcpuList)
        finaltrainmemList.append(submemList)
    for i in xrange(len(testcpuList)-meanLabel-length+1):
        subcpuList = []
        submemList = []
        for j in xrange(length):
            subcpuList.append(testcpuList[i+j])
            submemList.append(testmemList[i+j])
        finaltestcpuList.append(subcpuList)
        finaltestmemList.append(submemList)
    finaltraincpulabels = []
    finaltrainmemlabels = []
    for i in xrange(length,len(traincpuList)+1,1):
        sumcpu = 0
        summem = 0
        for j in xrange(meanLabel):
            sumcpu+=float(cpuList[i+j])
            summem+=float(memList[i+j])
        finaltraincpulabels.append(sumcpu/meanLabel)
        finaltrainmemlabels.append(summem/meanLabel)
    finaltestcpulabels = []
    finaltestmemlabels = []
    for i in xrange(length,len(testcpuList)-meanLabel+1,1):
        sumcpu = 0
        summem = 0
        for j in xrange(meanLabel):
            sumcpu+=float(testcpuList[i+j])
            summem+=float(testmemList[i+j])
        finaltestcpulabels.append(sumcpu/meanLabel)
        finaltestmemlabels.append(summem/meanLabel)
    if times>0:
        for i in xrange(len(traincpuList)):
            traincpuList[i]=int(float(traincpuList[i])*times)
            trainmemList[i]=int(float(trainmemList[i])*times)
        for i in xrange(len(testcpuList)):
            testcpuList[i]=int(float(testcpuList[i])*times)
            testmemList[i]=int(float(testmemList[i])*times)
    return (finaltraincpuList,finaltrainmemList,finaltestcpuList,finaltestmemList,
            finaltraincpulabels,finaltrainmemlabels,finaltestcpulabels,finaltestmemlabels)

"""trainList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
traincpu, trainlabels = makeListSequence(trainList,trainingStep=1,inputvector=[1,2],labelvector=[3,2])
print('traincpu: ', traincpu)
print('trainlabels: ', trainlabels)"""
