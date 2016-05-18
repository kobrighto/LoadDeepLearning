import VectorAutoRegress as var
from random import sample
import csv
from os import chdir,listdir
import platform
from time import gmtime, strftime
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

if (platform.node() == "woosungpil-PC"):
    dirPath = 'C:\Users\woosungpil\Desktop\Rawdata'
elif (platform.node()=="minh-titan"):
    dirPath = '/home/minh/Desktop/Google_Data/processed/'
elif (platform.node()=="Minh_Desktop1"):
    dirPath = 'E:\Google_Data\processed'
chdir(dirPath)

sample_moments = sample(xrange(1,12584),500)

print('len sample_moments:',len(sample_moments))

with open('sample_moments_500.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows([sample_moments])

"""sample_moments = []
with open('sample_moments_30.csv', 'rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

for i in xrange(len(sample_moments)):
    sample_moments[i]=int(sample_moments[i])
sample_moments.sort()
print('length: ', len(sample_moments))
print(sample_moments)"""