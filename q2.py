import numpy as np
import math
import sys

len = 5
disks = 25

count = np.zeros([len, disks], dtype = np.long) # count(m-3,n-1) = f(m,n)
R = np.zeros([len, disks], dtype=np.int)
optimum = np.zeros([len,disks],dtype=np.bool)
Step = {}
def init3():
    for i in range(0, disks):
        count[0, i] = 2 ** (i+1) - 1

def init4():
    for i in range(0, disks):
        _r = (math.sqrt(8*(i+1)+1)-1)/2
        _r = math.floor(_r)
        count[1, i] = math.floor((i+1-(_r**2 -_r +2)/2)*2**_r +1)

def cal1():
    for j in range(1,len):
        for i in range(0,disks):
            min_true = sys.maxsize
            if i == 0:
                count[j][i] = 1
                continue
            for r in range(i-1, -1, -1):
            #for r in range(0,i):
                if 2*count[j][r] + count[j-1][i-r-1] < min_true:
                    min_true = 2*count[j][r] + count[j-1][i-r-1]
                    count[j][i] = min_true
                    R[j][i] = r

def cal2():
    for j in range(1,len):
        for i in range(0,disks):
            for r in range(i-1, -1, -1):
                if 2 * count[j][r] + count[j - 1][i - r - 1] == count[j][i] + 1:
                    optimum[j][r] = True;
                    break;
                elif optimum[j][r] | optimum[j - 1][i - r - 1]:
                    optimum[j][r] = True;
                    break;


init3()
init4()
cal1()
cal2()
print(optimum)
