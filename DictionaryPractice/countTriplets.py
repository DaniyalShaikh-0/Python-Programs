#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    f=0
    fg=0
    count=0
    i=0
    j=1
    k=2
    while i < len(arr)-2:
        #print(f"({i},{j},{k})",end=' ')
        if j<len(arr)-1:
            if k<len(arr):
                if arr[i]*r==arr[j]:
                    if arr[j]*r==arr[k]:
                        count+=1
                        #print('Yes',end=' ')
                k+=1
            else:
                j+=1
                k=j+1
        else:
            i+=1
            j=i+1
            k=j+1
        #print()
        # if fg==1:
        #     if arr[f]*r==arr[i+1]:
        #         count+=1
        #     if i==len(arr)-2:
        #         fg=0
        #         i=f-1
        # elif arr[i]*r==arr[i+1]:
        #     f=i+1
        #     fg=1
    return count
        # if i==3 and f==0:
        #     i=0
        #     f+=1
        # else:
        #     print(i)
        #     i+=1

if __name__ == '__main__':

    f1 = open('input01.txt','r')
    st = f1.read().rstrip().split()
    n = int(st[0])
    r = int(st[1])
    st = [int(i) for i in st]
    print(n,r,st)
    ans=countTriplets(st[2:], r)
    print(ans)
