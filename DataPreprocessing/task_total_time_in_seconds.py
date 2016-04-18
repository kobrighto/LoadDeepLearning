__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv
import bisect

dirPath = "E:\Google_Data\clusterdata-2011-2\\task_usage"
chdir(dirPath)
#print (listdir('.'))
#print (dirPath)

filename = "part-00499-of-00500.csv.gz"

#starting time is already known
smallestTime = 600000000
biggestTime = 0

with gzip.open(filename, "r") as f:
    reader=csv.reader(f)
    for i,line in enumerate(reader):
        if int(line[1])>biggestTime:
            biggestTime=int(line[1])

duration = int(biggestTime) - int(smallestTime)
print ("smallestTime: " + str(smallestTime) + ", biggestTime: " + str(biggestTime) + ", duration: " + str(duration))

print ("duration in seconds: " + str(duration/1000000))