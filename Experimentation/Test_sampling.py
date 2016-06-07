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

with open('sample_moments_500.csv','rb') as f:
    reader = csv.reader(f)
    for line in reader:
        old_sample_moments = line

for i in xrange(len(old_sample_moments)):
    old_sample_moments[i]=int(old_sample_moments[i])

new_sample_moments = xrange(1,12584)
to_sampling = list(set(new_sample_moments) - set(old_sample_moments))

print('len old_sample:',len(old_sample_moments))
print('len new_sample:',len(new_sample_moments))
print('len to_sampling:',len(to_sampling))

sampling = sample(to_sampling,500)
print('len sampling:',len(sampling))

with open('sample_moments_500_second.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows([sampling])

"""sample_moments = sample(xrange(1,12584),500)

print('len sample_moments:',len(sample_moments))

with open('sample_moments_500.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows([sample_moments])

sample_moments = []
with open('sample_moments_30.csv', 'rb') as f:
    reader = csv.reader(f)
    for line in reader:
        sample_moments = line

for i in xrange(len(sample_moments)):
    sample_moments[i]=int(sample_moments[i])
sample_moments.sort()
print('length: ', len(sample_moments))
print(sample_moments)"""