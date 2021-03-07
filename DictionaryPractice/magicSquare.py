#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
     #x = list(range(1,10))
    tot=tot1=tot2=tot3=0
    tot4=tot5=tot6=tot7=tot8=0
    flg=0
    ifg=0
    #checking mid val
    tot+=abs(s[1][1]-5)
    print(f'tot at 5 form is : {tot}')
    #checking where 9 1 belongs
    a1=abs(s[0][1]-9)
    a2=abs(s[2][1]-1)
    tot1=a1+a2+tot
    tot2=tot1

    print('tot1 is : ',tot1)
    print('tot2 is : ',tot2)

    a11=abs(s[0][1]-1)
    a22=abs(s[2][1]-9)

    tot3=a11+a22+tot
    tot4=tot3

    print('tot3 is : ',tot3)
    print('tot4 is : ',tot4)
    
    a3=abs(s[1][2]-9)
    a4=abs(s[1][0]-1)
    
    tot5=a3+a4+tot
    tot6=tot5
    
    print('tot5 is : ',tot5)
    print('tot6 is : ',tot6)

    a33=abs(s[1][2]-1)
    a44=abs(s[1][0]-9)

    #print(s[1][2],' and  ',s[1][0] ,'  and these : ',a33,' : ',a44)
    
    tot7=a33+a44+tot
    tot8=tot7

    print('tot7 is : ',tot7)
    print('tot8 is : ',tot8)
    
    a5=abs(s[1][0]-7)
    a6=abs(s[1][2]-3)
    a55=abs(s[1][0]-3)
    a66=abs(s[1][2]-7)
    
    tot1+=a5+a6
    tot1+=abs(s[0][0]-2)
    tot1+=abs(s[0][2]-4)
    tot1+=abs(s[2][0]-6)
    tot1+=abs(s[2][2]-8)
    
    tot2+=a55+a66
    tot2+=abs(s[0][0]-4)
    tot2+=abs(s[0][2]-2)
    tot2+=abs(s[2][0]-8)
    tot2+=abs(s[2][2]-6)
    
    tot3+=a5+a6
    tot3+=abs(s[0][0]-6)
    tot3+=abs(s[0][2]-8)
    tot3+=abs(s[2][0]-2)
    tot3+=abs(s[2][2]-4)
    
    tot4+=a55+a66
    tot4+=abs(s[0][0]-8)
    tot4+=abs(s[0][2]-6)
    tot4+=abs(s[2][0]-4)
    tot4+=abs(s[2][2]-2)
           
    a5=abs(s[0][1]-7)
    a6=abs(s[2][1]-3)
    a55=abs(s[0][1]-3)
    a66=abs(s[2][1]-7)
    
    tot5+=a5+a6
    tot5+=abs(s[0][0]-6)
    tot5+=abs(s[0][2]-2)
    tot5+=abs(s[2][0]-8)
    tot5+=abs(s[2][2]-4)
    
    tot6+=a55+a66
    tot6+=abs(s[0][0]-8)
    tot6+=abs(s[0][2]-4)
    tot6+=abs(s[2][0]-6)
    tot6+=abs(s[2][2]-2)
    
    tot7+=a5+a6
    tot7+=abs(s[0][0]-2)
    tot7+=abs(s[0][2]-6)
    tot7+=abs(s[2][0]-4)
    tot7+=abs(s[2][2]-8)

    tot8+=a55+a66
    tot8+=abs(s[0][0]-4)
    tot8+=abs(s[0][2]-8)
    tot8+=abs(s[2][0]-2)
    tot8+=abs(s[2][2]-6)
    
    x=min(tot1,min(tot2,min(tot3,tot4)))
    y=min(tot5,min(tot6,min(tot7,tot8)))
    tot=min(x,y)
    return tot
if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    print(formingMagicSquare(s))
