__author__ = 'Minh'

import platform
from os import listdir, chdir, path
import csv
import sys

if (platform.platform()=='Windows-7-6.1.7601-SP1'):
    dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
elif (platform.platform()=="Linux-3.19.0-25-generic-x86_64-with-Ubuntu-14.04-trusty"):
    dirPath = '/home/minh/Desktop/Google_Data/processed'

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
    return (meanCPUList, meanMemList)

#meanLabel: labels are made from mean of ? number of load values
def makeTrainTestLists(cpuList,memList,meanLabel,markPoint,length,times):
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