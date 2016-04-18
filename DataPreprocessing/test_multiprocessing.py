__author__ = 'Minh'

from multiprocessing import Process, Manager

def f(d,i,amount):
    d[i] += amount

"""def f(d):
    d[1] += '1'
    d['2'] += 2"""

if __name__ == '__main__':
    manager = Manager()

    d = manager.list([0]*10)

    p1 = Process(target=f, args=(d,2,100))
    p2 = Process(target=f, args=(d,3,10))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print d