__author__ = 'Minh'

def swap(a,b):
    a,b = b,a
    print('Inside swap:')
    print(a,b)

x,y = 123,456
swap(x,y)
print('Outside swap:')
print(x,y)