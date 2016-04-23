# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:55:57 2016

@author: woosungpil
"""

from os import listdir, chdir, path
import gzip
import csv
import sys
import matplotlib.pyplot as plt
from datetime import datetime
import platform
import DataPostProcessing as sp
import numpy as np

#total number of lines (machines): 12583
noOfMachines = 12583

if (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed'
    chdir(dirPath)

csv.field_size_limit(sys.maxint)

finalmean = []
finalstd = []

with open('usage_1_minute_total_converted_no_duplicates.csv', 'r') as f:
    cpuList = []
    memList = []
    lineCount = 0
    reader = csv.reader(f)
    for line in reader:
        lineCount+=1
        if lineCount%100 == 0:
            print('Current Time: ' + str(datetime.now()) + ', Number of lines processed: ' + str(lineCount))
            print(cpuList[len(cpuList)-1])
            print(memList[len(memList)-1])
        cpuList = line[4].split(',')
        cpuList[0] = cpuList[0][1:]
        cpuList[len(cpuList)-1] = cpuList[len(cpuList)-1][:-1]
        memList = line[5].split(',')
        memList[0] = memList[0][1:]
        memList[len(memList)-1] = memList[len(memList)-1][:-1]
        for i in xrange(len(cpuList)):
            cpuList[i]=float(cpuList[i])
        for i in xrange(len(memList)):
            memList[i]=float(memList[i])
        cpumean = np.mean(cpuList)
        memorymean = np.mean(memList)
        finalmean.append([lineCount,cpumean,memorymean])
        cpustd = np.std(cpuList)
        memorystd = np.std(memList)
        finalstd.append([lineCount,cpustd,memorystd])

with open('mean_all_machines.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(finalmean)

with open('variance_all_machines.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(finalstd)


#f = open("C:\Users\woosungpil\Desktop\minh1.txt", 'r')
#lines = f.readlines()
#f.close()

#f = open("C:\Users\woosungpil\Desktop\minh2.txt", 'w')
#for i in xrange(2000):
#   str = lines[i]
#   str1 = str.replace('[','')
#   str2 = str1.replace(']','')
#   f.write("%s" % str2)
#   print(i+1)
#f.close()

#cpuList_list = []
#f.write("-----mean-----\n")
#for i in xrange(2000):
#    cpuList, memList =  sp.meanLoad(i+1, 41761)
#    f.write("%s\n" % cpuList)
#    print(i+1)

#length = len(cpuList)
#traincpu,trainmem,testcpu,testmem,traincpulabels,trainmemlabels,testcpulabels,testmemlabels = DataPostProcessing.makeTrainTestLists(cpuList,memList,30,int(0.9*len(cpuList)),30,1)

#print(cpuList)