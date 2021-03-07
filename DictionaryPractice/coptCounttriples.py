#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
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
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    fptr.write(str(countTriplets(arr, r)) + '\n')

    fptr.close()
