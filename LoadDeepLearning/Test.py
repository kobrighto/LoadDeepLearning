__author__ = 'Minh'

import platform
from os import listdir, chdir, path
import csv
import sys
import math

if (platform.platform()=="Linux-3.19.0-25-generic-x86_64-with-Ubuntu-14.04-trusty"):
    dirPath = '/home/minh/Desktop/Google_Data/processed'

chdir(dirPath)

with open('justfortest.csv','w') as f:
    writer = csv.writer(f)
    str = [("abcdy"),("exyz")]
    writer.writerow(str)