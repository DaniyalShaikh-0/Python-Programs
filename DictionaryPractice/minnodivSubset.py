#!/bin/python3

import math
import os
import random
import re
import sys
# def nonDivisibleSubset(k, s):
#     arr=[]
#     for i in range(1,len(s)):
#         fg=0
#         fg2=0
#         for j in range(i+1,len(s)):
#             if (s[i]+s[j])%k !=0:
#                 for p in arr:
#                     if (not (s[i]+p)%k) or s[i]==p :
#                         fg=1
#                     if (not (p+s[j])%k) or s[j]==p:
#                         fg2=1
#                     if fg and fg2:
#                         break
#                 if not fg:
#                     arr.append(s[i])
#                 if not fg2:
#                     arr.append(s[j])
#         # if len(arr[i])>mxlen:
#         #      mxlen=i
#     print(arr)
#     return len(arr)
# def nonDivisibleSubset(k, s):
#     arr=[[] for i in range(len(s))]
#     mxlen=0
#     for i in range(len(s)):
#         # fg2=0
#         arr[i].append(s[i])
#         for j in range(i+1,len(s)):
#             fg=0
#             #print(f' j value is : {j} with s : {s[j]}')
#             if ((s[i]+s[j])%k) !=0:
#                 for p in arr[i]:
#                     # if (not (s[i]+p)%k) or s[i]==p :
#                     #     fg=1
#                     if ((p+s[j])%k)==0 or s[j]==p:
#                         # if s[i]==576:
#                         #     print(f'value at which f is 1 is {p} + {s[j]}')
#                         fg=1
#                     if fg:
#                         break
#                 if not fg:
#                     arr[i].append(s[j])
#             # else:
#                 # print(f'\n---\nnum is divisible by {k} and num is {s[j]} and j is {j}\n---')
#         if len(arr[i])>mxlen:
#              mxlen=len(arr[i])
#         if (len(s)-i)<mxlen:
#             # print(f'this is working at {i} on {s[i]}')
#             break
        # print(arr[i],end=' ')
        # print(f' with lenth = {len(arr[i])}')
    # return mxlen
from collections import Counter
def nonDivisibleSubset(k,a):
    c = Counter((i%k for i in a))
    count = 0
    blacklist = set()
    print(list(c.elements()))
    # for x,y in c.most_common():
    #     if x == k/2 or x==0:
    #         count+=1
    #     elif k-x not in blacklist:
    #         count+=y
    #         blacklist.add(x)
    return count
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print (result)
