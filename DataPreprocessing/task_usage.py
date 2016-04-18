__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv

dirPath = "E:\Google_Data\processed"
chdir(dirPath)

class Machine_cpu(object):
    def __init__(self, machineID=None, cpuCapacity=None, status=None, cpuList=None):
        self.machineID = machineID
        self.cpuCapacity = cpuCapacity
        self.status = status
        self.cpuList = cpuList

class Machine_mem(object):
    def __init__(self, machineID=None, memCapacity=None, status=None, memList=None):
        self.machineID = machineID
        self.memCapacity = memCapacity
        self.status = status
        self.memList = memList

machineList = []

filename = "machineList_dupcheck.csv"
#filename = "part-00000-of-00500.csv.gz"

#duration: 2505600 seconds, or 2505601 'list items'
with open(filename, "r") as f:
    reader=csv.reader(f)
    for i,line in enumerate(reader):
        listofzeros = [0] * 26000
        machineList.append([line[0], line[1], line[3], listofzeros])

with open("test_cpu.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(machineList)

machineList = []

with open(filename, "r") as f:
    reader=csv.reader(f)
    for i,line in enumerate(reader):
        listofzeros = [0] * 26000
        machineList.append([line[0], line[2], line[3], listofzeros])

with open("test_mem.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(machineList)