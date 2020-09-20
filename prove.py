import numpy as np
import math
import sys

len = 5
disks = 25

count = np.zeros([len, disks], dtype = np.long) # count(m-3,n-1) = f(m,n)
_count = np.zeros([len, disks], dtype = np.long) # count(m-3,n-1) = f(m,n)
R = np.zeros([len, disks], dtype=np.int)
def init3():
    for i in range(0, disks):
        count[0, i] = 2 ** (i+1) - 1

def init4():
    for i in range(0, disks):
        _r = (math.sqrt(8*(i+1)+1)-1)/2
        _r = math.floor(_r)
        count[1, i] = math.floor((i+1-(_r**2 -_r +2)/2)*2**_r +1)

def cal():
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

def C(n,m):
    p = 100000007
    def power(x,y):     #求x的y次方
        p = 100000007
        res = 1
        while y:
            if y % 2 != 0:
                res *= (x%p)
            y >>= 1
            x *= (x%p)
        return res
    a = (math.factorial(n))%p
    b = (power(math.factorial(m),(p-2)))%p
    c = (power(math.factorial(n-m),(p-2)))%p
    return(a*b*c%p)

def cal_ger():
    for k in range(1,len):
        for n in range(k+2,disks):
            t = 0
            for r in range(1,100):
                print(C(k+r,k+1),n+1,C(k+r+1, k+1))
                if (n+1 >= C(k+r,k+1)) and (n+1 <= C(k+r+1, k+1)):
                    t = r
                    break
            print(t)
            sumj = math.floor((k+1)/2)
            sumt = 0
            for j in range(0,sumj+1):
                print(sumj)
                print(k-2*j+t-1,t-2)
                sumt += C(k-2*j+t-1,t-2)
            _count[k][n] = 2**t*(n+1-sumt)-(-1)**k
            assert(_count[k][n] == count[k][n])


init3()
init4()
cal()
cal_ger()
print(count)
print(_count)