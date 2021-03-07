#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
def countingValleys(steps, path):
    s_l=0
    val=-1
    mt=1
    tot=0
    ct=0
    i=0
    while i<len(path)-1:
        j=i
        print('for at : ',i)
        if path[i]=='U':
            tot+=mt
        else:
            tot+=val
        if tot<0:
            print('gg')
            while True:
                print('.')
                if tot==0:
                    ct+=1
                    break
                j+=1
                if path[j]=='U':
                    tot+=mt
                else:
                    tot+=val
        i=j
        i+=1
    return ct        

if __name__ == '__main__':
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    print(result)