from random import randint
import csv
from os import listdir, chdir, path
from random import sample

#Total number of machine lines: 12583
sample_moments = sample(xrange(1,12584),10)
print(sample_moments)