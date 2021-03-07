#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
# for i,j in range(len(ranks)-1,-1,-1),range(len(player)):
#         print(f'{ranks[i]} is at {i}')
#         print(f'{player[j]} is at {j}')
def climbingLeaderboard(ranked, player):
    # ranked=list(Counter(ranked).keys())
    # arr=[0]*(len(ranked)+len(player))
    # m=max(max(ranked),max(player))
    # arr=[0]*(m+1)
    ranks=list(Counter(ranked).keys())
    pos=len(ranks)
    rl=[0]*len(player)
    c=1
    if len(ranks)==1:
        for i,v in enumerate(player):
            if v>=ranks[0]:
                rl[i]=1
            else:
                rl[i]=2
        return rl
    
    for i in range(len(player)):
        f=0
        for j in range(len(ranks)-c,0,-1):
            if player[i]<ranks[j]:
                rl[i]=j+2
                break
            elif player[i]==ranks[j]:
                rl[i]=j+1
                break
            elif player[i]>=ranks[0]:
                rl[i]=1
                break
            else:
                f=1
        if f:
            c+=1

    return rl
    

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
    print(result)