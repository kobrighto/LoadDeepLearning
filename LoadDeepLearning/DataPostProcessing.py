__author__ = 'Minh'

import platform
from os import listdir, chdir, path
import csv
import sys

if (platform.platform()=='Windows-7-6.1.7601-SP1'):
    dirPath = 'E:/Google_Data/processed'

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
    print('Done 1')
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