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

#f = open("C:\Users\woosungpil\Desktop\minh.txt", 'w')
f = open("C:\Users\woosungpil\Desktop\minh1.txt", 'r')
lines = f.readlines()
f.close()

f = open("C:\Users\woosungpil\Desktop\minh2.txt", 'w')
for i in xrange(2000):
   str = lines[i]
   str1 = str.replace('[','')
   str2 = str1.replace(']','')
   f.write("%s" % str2)
   print(i+1)
f.close()
#cpuList_list = []
#f.write("-----mean-----\n")
#for i in xrange(2000):
#    cpuList, memList =  sp.meanLoad(i+1, 41761)
#    f.write("%s\n" % cpuList)
#    print(i+1)


#f.write("-----mean-----\n")
#for i in xrange(2000):
#    cpuList, memList =  sp.meanLoad(i+1, 1)
#    mean = np.mean(cpuList)
#    f.write("%s\n" % mean)
#    print(i+1)

#f.write("-----std-----\n")
#for i in xrange(2000):
#    cpuList, memList =  sp.meanLoad(i+1, 1)
#    std = np.std(cpuList)
#    f.write("%s\n" % std)
#    print(i+1)

f.close()

#length = len(cpuList)
#traincpu,trainmem,testcpu,testmem,traincpulabels,trainmemlabels,testcpulabels,testmemlabels = DataPostProcessing.makeTrainTestLists(cpuList,memList,30,int(0.9*len(cpuList)),30,1)

#print(cpuList)