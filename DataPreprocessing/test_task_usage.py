__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv
import sys
import bisect

dirPath = "E:\Google_Data\processed"
chdir(dirPath)

count = 1
csv.field_size_limit(sys.maxint)

with open("usage_converted_1.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        if count%1000==0:
            print("Current count: " + str(count))
        if count<10:
            print("first line: " + str(line[0]) + ", " + str(line[1]) + ", " + str(line[2]) + ", " + str(line[3]))
            curList = line[4].split(",")
            curList2 = line[5].split(",")
            for i in xrange(0,10):
                print(curList[i] + ", " + curList2[i])
        """elif count==12607:
            print("second line: " + str(line[0]) + ", " + str(line[1]) + ", " + str(line[2]) + ", " + str(line[3]))
            curList = line[4].split(",")
            curList2 = line[5].split(",")
            for i in xrange(0,10):
                print(curList[i] + ", " + curList2[i])
        elif count==12608:
            print("third line: " + str(line[0]) + ", " + str(line[1]) + ", " + str(line[2]) + ", " + str(line[3]))
            curList = line[4].split(",")
            curList2 = line[5].split(",")
            for i in xrange(0,10):
                print(curList[i] + ", " + curList2[i])
        elif count==12609:
            print("fourth line: " + str(line[0]) + ", " + str(line[1]) + ", " + str(line[2]) + ", " + str(line[3]))
            curList = line[4].split(",")
            curList2 = line[5].split(",")
            for i in xrange(0,10):
                print(curList[i] + ", " + curList2[i])"""
        count+=1