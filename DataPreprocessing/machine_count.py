__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv
import bisect

dirpath = "E:\Google_Data\processed"
chdir(dirpath)
print (listdir('.'))

trueCount = 0
falseCount = 0
totalCount = 0

with open("machineList_dupcheck.csv", "rb") as f:
    reader = csv.reader(f)
    for i,line in enumerate(reader):
        if (line[3]=="false"):
            falseCount+=1
            totalCount+=1
        else:
            trueCount+=1
            totalCount+=1

print ("False Count: " + str(falseCount) + ", True Count: " + str(trueCount) + ", Total Count: " + str(totalCount))