__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv
from datetime import datetime

#duration: 2505600 seconds, time range from 0 to 2505600
outFileNo = 1
startTime = 0
endTime = 0
if outFileNo == 100:
    startTime = (outFileNo-1)*25000
    endTime = 2505600
else:
    startTime = (outFileNo-1)*25000
    endTime = (outFileNo*25000)-1

startTime = (startTime + 600)*1000000
endTime = (endTime + 600) * 1000000
print("Start time: " + str(startTime) + ", End time: " + str(endTime))

dirPath = 'E:\Google_Data\processed'
chdir(dirPath)
timingFile = 'timingList.csv'

timingList = []
fileToProcessList = []

with open('timingList.csv', 'r') as f:
    reader = csv.reader(f)
    for i,line in enumerate(reader):
        timingList.append([line[0],line[1],line[2]])

for item in timingList:
    print("current item: " + str(item))
    if int(item[2])<startTime:
        pass
    elif int(item[1])>endTime:
        break
    else:
        fileToProcessList.append('part-' + str(item[0]).zfill(5) + '-of-00500.csv.gz')

"""dataPath = 'E:\Google_Data\clusterdata-2011-2\\task_usage'
chdir(dataPath)

lineCount = 0

with gzip.open (fileToProcessList[0], 'r') as f:
    reader = csv.reader(f)
    for i,line in enumerate(reader):
        lineCount += 1

print(fileToProcessList)
print('lineCount: ' + str(lineCount))"""

chdir(dirPath)

machineList = []
filename = "machineList_dupcheck.csv"

with open(filename, "r") as f:
    reader=csv.reader(f)
    print('Number of zeros: ' + str((endTime-startTime)/1000000 + 1))
    for i,line in enumerate(reader):
        listofzeros = [0] * ((endTime-startTime)/1000000 + 1)
        machineList.append([line[0], line[1], line[2], line[3], listofzeros, listofzeros])

dataPath = 'E:\Google_Data\clusterdata-2011-2\\task_usage'
chdir(dataPath)

print ("done 1!")
count = 0

print ('Number of files to process: ' + str(len(fileToProcessList)))
for name in fileToProcessList:
    with gzip.open(name,'r') as f:
        reader = csv.reader(f)
        for i,line in enumerate(reader):
            if count%10000 == 0:
                print('Current Time: ' + str(datetime.now()) + ', Number of lines processed: ' + str(count))
            curStartTime = line[0]
            curEndTime = line[1]
            curMachineID = line[4]
            curcpuusage = line[5]
            curmemusage = line[6]
            checked = False
            for item in machineList:
                if int(item[0])==int(curMachineID):
                    checked = True
                    minInterval = max(startTime, int(curStartTime))
                    maxInterval = min(endTime, int(curEndTime))
                    #print('range: ' + str((minInterval/1000000)-600) + ', ' + str((maxInterval/1000000)-600))
                    for inter in xrange((minInterval/1000000)-600,(maxInterval/1000000)-600+1,1):
                        print(str((maxInterval/1000000)-600+1))
                        item[4][inter] += float(curcpuusage)
                        item[5][inter] += float(curmemusage)
            if checked==False:
                print("Did not find the Machine ID: " + str(curMachineID))
            checked=False
            count+=1


chdir(dirPath)

with open("usage_unconverted_1.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(machineList)
