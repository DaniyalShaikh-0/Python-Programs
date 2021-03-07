#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def rot(a):
    f=a[-1]
    for i in range(len(a)-1,0,-1):
        a[i]=a[i-1]
    a[0]=f
    return a
def circularArrayRotation(a, k, queries):
    print(rot(a))
    return a
    

if __name__ == '__main__':
    # fptr = open('OUt.txt', 'w')

    # nkq = input().split()

    # n = int(nkq[0])

    # k = int(nkq[1])

    # q = int(nkq[2])

    # a = list(map(int, input().rstrip().split()))

    # queries = []

    # for _ in range(q):
    #     queries_item = int(input())
    #     queries.append(queries_item)

    # result = circularArrayRotation(a, k, queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
