import numpy as np
import math
import sys

len = 5
disks = 25

count = np.zeros([len, disks], dtype = np.long) # count(m-3,n-1) = f(m,n)
R = np.zeros([len, disks], dtype=np.int)
step_true = np.zeros([len,disks],dtype=np.bool)
Step = {}
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

def step():
    for j in range(0, len):
        for i in range(0, disks):
            if j==0:
                if i > 10:
                    continue
                if i==0:
                    Step["0 0"] = [(1,65,67)]
                elif ~step_true[j][i]:
                    Step[str(j) + " " + str(i)] = []
                    change(i-1,j,i,j,0,67,False,False)
                    Step[str(j) + " " + str(i)].append((i+1,65,67))
                    change(i - 1, j, i, j, 0, 67, False, True)
                    step_true[j][i] = True
            else:
                if i==0:
                    Step[str(j)+" "+str(i)]=[(1,65,67+j)]
                elif ~step_true[j][i]:
                    Step[str(j) + " " + str(i)] = []
                    change(R[j][i],j,i,j,0,67+j,False,False)
                    change(i-R[j][i]-1,j-1,i,j,R[j][i]+1,67+j,True,False)
                    change(R[j][i], j, i, j, 0, 67+j, False, True)
                    step_true[j][i] = True

def change(i,j,i_tar,j_tar,index,tar,minus,start):
    for (a,b,c) in Step[str(j)+" "+str(i)]:
        a_tar = a+index
        if start:
            if b == 66:
                b_tar = 65
            elif b == 65:
                b_tar = 66
            else:
                b_tar = b
            if c == 66:
                c_tar = 65
            elif c == 65:
                c_tar = 66
            else:
                c_tar = c
        else:
            if minus:
                b_tar = b+1 if b !=65 else b
                c_tar = c+1 if c !=65 else c
            else:
                if b == 66:
                    b_tar = tar
                elif b == tar:
                    b_tar = 66
                else:
                    b_tar = b
                if c == 66:
                    c_tar = tar
                elif c == tar:
                    c_tar = 66
                else:
                    c_tar = c
        Step[str(j_tar)+" "+str(i_tar)].append((a_tar,b_tar,c_tar))

def printStep(i,j):
    total = 1
    for (i,j,k) in Step[str(i)+" "+str(j)]:
        print(str(total) + ":move disk "+str(i)+" from "+chr(j)+" to "+chr(k)+".f")
        total +=1


init3()
init4()
cal()
step()
while True:
    m = int(input("needls："))
    n = int(input("disks: "))
    printStep(m-3,n-1)
    5
    print(str(count[m-3][n-1]) +" steps in total.")