__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv
import bisect
import sys
from datetime import datetime

# Each line contain 6 columns, including: machineID, CPU capacity, memory capacity, true/false, CPU usage, mem usage

sourcePath = 'E:\Google_Data\processed'
chdir(sourcePath)

count = 0

csv.field_size_limit(sys.maxint)
machineList = []

with open("usage_unconverted_1.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        if count%1000 == 0:
                print('Current Time: ' + str(datetime.now()) + ', Number of lines processed: ' + str(count))
        count+=1
        cpuCapacity = float(line[1])
        memCapacity = float(line[2])
        cpuList = line[4].split(",")
        memList = line[5].split(",")
        convertedCPUList = []
        convertedmemList = []
        for i in xrange(0,len(cpuList)):
            if i==0:
                converted = (float(cpuList[i][1:].strip())) / cpuCapacity
            elif i==len(cpuList)-1:
                converted = (float(cpuList[i][:-1].strip())) / cpuCapacity
            else:
                converted = (float(cpuList[i].strip())) / cpuCapacity
            converted = round(converted*100,1)
            convertedCPUList.append(converted)
        for i in xrange(0,len(memList)):
            if i==0:
                converted = (float(memList[i][1:].strip())) / memCapacity
            elif i==len(cpuList)-1:
                converted = (float(memList[i][:-1].strip())) / memCapacity
            else:
                converted = (float(memList[i].strip())) / memCapacity
            converted = round(converted*100,1)
            convertedmemList.append(converted)
        machineList.append((line[0],line[1],line[2],line[3],convertedCPUList,convertedmemList))

print(len(machineList))
print(len(machineList[0]))

with open("usage_converted_1.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(machineList)
