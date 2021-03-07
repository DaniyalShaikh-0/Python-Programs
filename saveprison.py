import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    if n>m:
        x=m
        if x+s-1>n:
            ans=x+s-n-1
            if ans!=0:
                return ans
            else:
                return n
        else:
            ans=x+s-1
            if ans!=0:
                return ans
            else:
                return n
    elif n==m:
        if s-1!=0:
            return s-1
        else:
            return s
    else:
        x=m%n
        if x+s-1>n:
            ans=x+s-n-1
            if ans!=0:
                return ans
            else:
                return n
        else:
            ans=x+s-1
            if ans!=0:
                return ans
            else:
                return n

if __name__ == '__main__':
    fptr = open('OUt.txt', 'w')
    rf = open('read.txt','r')

    t = int(rf.readline())

    for t_itr in range(t):
        nms = rf.readline().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
