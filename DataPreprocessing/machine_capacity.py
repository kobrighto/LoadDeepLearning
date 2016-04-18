__author__ = 'Minh'

from os import listdir, chdir, path
import gzip
import csv
import bisect

dirpath = "E:\Google_Data\clusterdata-2011-2"
chdir(dirpath)
print (listdir('.'))

machineList=[]

print (sorted(listdir('task_events'))[-1])

for fn in sorted(listdir('machine_events')):
    fp = path.join('machine_events', fn)
    with gzip.open(fp, "r") as f:
        reader = csv.reader(f)
        for i,line in enumerate(reader):
            curList = [int(line[1]),line[4],line[5]]
            #print(curList)
            bisect.insort_left(machineList, curList)

writepath = "E:\Google_Data\processed"
chdir(writepath)

with open("machineList.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(machineList)

"""f = open('machineList.txt','w')

for inner_list in machineList:
    for element in inner_list:
        f.write(str(element)+",")
    f.write("\n")

f.close()"""
