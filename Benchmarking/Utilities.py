__author__ = 'Minh'

import platform
from os import listdir, chdir, path
import csv
import sys
import numpy as np

"""if (platform.node() == "woosungpil-PC"):
    dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
elif (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed'
elif (platform.node()=="Minh_Desktop1"):
    dirPath = 'E:\Google_Data\processed'"""

def sampling(lineNo, noOfMinutes):
    csv.field_size_limit(sys.maxint)
    #chdir(dirPath)
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

def meanLoadS(lineNo, noOfMinutes, samplingRate):
    csv.field_size_limit(sys.maxint)
    csv.field_size_limit(sys.maxint)
    #chdir(dirPath)
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
    sampledcpuList = []
    meanCPUList = []
    meanMemList = []
    for i in xrange(0,len(cpuList),samplingRate):
        sampledcpuList.append(cpuList[i])
    toMean=int(noOfMinutes/samplingRate)
    i=0
    while i+toMean-1<len(sampledcpuList):
        sumCPU = 0
        for j in xrange(toMean):
            sumCPU+=float(sampledcpuList[i+j])
        meanCPUList.append(sumCPU/toMean)
        i+=1
    return meanCPUList

def meanLoad(lineNo, noOfMinutes):
    csv.field_size_limit(sys.maxint)
    #chdir(dirPath)
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
    return (meanCPUList, meanMemList)

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
    return(np.array(traincpuList),np.array(traincpuLabels))