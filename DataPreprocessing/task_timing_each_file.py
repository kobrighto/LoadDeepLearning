__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv

dirPath = "E:\Google_Data\clusterdata-2011-2"
chdir(dirPath)

timingList = []
fileNo = 0

for fn in sorted(listdir('task_usage')):
    smallestTime = 0
    biggestTime = 0
    fp = path.join('task_usage', fn)
    with gzip.open(fp, "r") as f:
        reader=csv.reader(f)
        row1=next(reader)
        smallestTime=int(row1[0])
    with gzip.open(fp, "r") as f:
        reader = csv.reader(f)
        for i,line in enumerate(reader):
            if int(line[0])<smallestTime:
                smallestTime = int(line[0])
            if int(line[1])>biggestTime:
                biggestTime = int(line[1])
    timingList.append([str(fileNo), str(smallestTime), str(biggestTime)])
    print ("Current file number: " + str(fileNo) + ", Current smallestTime: " + str(smallestTime) +
           ", Current biggestTime: " + str(biggestTime))
    fileNo += 1

with open("timingList.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(timingList)