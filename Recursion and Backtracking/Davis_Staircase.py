#!/bin/python3

import math
import os
import random
import re
import sys

def recursiveAux(n, i):
    if( i == n ):
        return 1
    elif( i > n ):
        return 0
    else:
        ways = 0
        ways += recursiveAux(n, i+3)
        ways += recursiveAux(n, i+2)
        ways += recursiveAux(n, i+1)
        return ways

def recursive(n):
    ways = 0
    ways += recursiveAux(n, 1)
    if( n>=2 ):
        ways += recursiveAux(n, 2)
    if( n>=3 ):
        ways += recursiveAux(n, 3)
    return ways%10000000007

# Complete the stepPerms function below.
def stepPerms(n):
    if(n == 1):
        return 1
    arr = [ None for i in range(n) ]
    arr[0] = 1
    if(n >= 2):
        if( n == 2 ):
            return 2
        arr[1] = 2
    if(n >= 3):
        if( n == 3 ):
            return 4
        arr[2] = 4
    for i in range( 3, n ):
        arr[i] = arr[i-3]+arr[i-2]+arr[i-1]
    return arr[n-1]%10000000007

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        #fptr.write(str(res) + '\n')
        print(str(res) + '\n')

    #fptr.close()
