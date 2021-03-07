lis=[97, 96, 94, 94, 94, 94, 89, 87, 87, 86, 83, 83, 83, 83, 83, 81, 81, 81, 80, 80, 80, 80, 76, 76, 76, 76, 
75, 74, 73, 73, 73, 72, 72, 72, 72, 72, 72, 71, 70, 70, 70, 70, 69, 69, 69, 67, 67,
 66, 63, 63, 63, 63, 63, 63, 63, 63, 61, 59, 59, 57, 57, 57, 54, 52, 52, 51, 50, 49, 
 48, 47, 47, 47, 47, 47, 47, 47, 47, 47, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 45, 45, 
 45, 45, 45, 44, 44, 44, 43, 43, 41, 39, 38, 38, 38, 37, 37, 37, 34, 34, 34, 34, 34, 34, 34, 34, 
 34, 34, 34, 34, 34, 34, 34, 34, 32, 32, 32, 32, 32, 32, 31, 31, 31, 30, 30, 30, 30, 30, 30, 29, 29, 
 29, 28, 27, 27, 27, 25, 24, 24, 24, 24, 24, 24, 24, 21, 19, 19, 19, 19, 18, 17, 17, 16, 16, 16, 16, 16,
 16, 15, 15, 15, 14, 14, 13, 13, 12, 12, 11, 10, 10, 10, 10, 10, 9, 9, 8, 8, 6, 6, 6, 5, 4, 4, 4, 3, 3, 3, 0, 0, 0, 0] 
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
        for j in range(len(ranks)-c,-1,-1):
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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
