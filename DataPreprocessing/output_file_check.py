__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv
import bisect
import sys

#total Machine: 12615, false: 7:, true: 12608

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
print(str((endTime-startTime)/1000000 + 1))

print(str((endTime/1000000)-600+1))

dirpath = "E:\Google_Data\processed"
chdir(dirpath)
print (listdir('.'))

machineCount = 0

csv.field_size_limit(sys.maxint)

with open("usage_unconverted_1.csv", "r") as f:
    reader=csv.reader(f)
    for line in reader:
        machineCount+=1
        if machineCount%1000==0:
            print('Current number of machines: ' + str(machineCount))

print('Total number of machines: ' + str(machineCount))

lastline = ""

templist = []

with open("usage_unconverted_1.csv", "r") as f:
    reader = csv.reader(f)
    row1 = next(reader)
    templist = row1[5].split(",")
    print(templist[24999])
    print ('Length: ' + str(len(templist)))
    print '\n'.join(str(p) for p in templist)