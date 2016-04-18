__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv
import bisect

dirpath = "E:\Google_Data\processed"
chdir(dirpath)
print (listdir('.'))

machineList=[]
lastline=[]

with open("machineList.csv", "rb") as f:
    reader = csv.reader(f)
    for i,line in enumerate(reader):
        if not lastline or line[0]!=lastline[0] or ((not line[1]) and (not line[2])) \
                or (((not lastline[1]) and (not lastline[2]))):
            curList = [int(line[0]),line[1],line[2],"true"]
            bisect.insort_left(machineList,curList)
        else:
            if line[1]!=lastline[1] or line[2]!=lastline[2]:
                toRemove = [int(lastline[0]),lastline[1],lastline[2],"true"]
                machineList.remove(toRemove)
                curList = [int(line[0]),line[1],line[2],"false"]
                bisect.insort_left(machineList,curList)
        lastline = line

with open("machineList_dupcheck.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(machineList)