#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):

    maximumLuck = 0
    importants = []
    for pair in contests:
        if( pair[1] == 0 ):
            maximumLuck += pair[0]
        if( pair[1] == 1 ):
            importants.append( pair[0] )

    if( len(importants) > 0 ):

        importants = sorted( importants )
        importants.reverse()
        #print(importants)

        for i in range(0, k):
            if(len(importants)>0):
                maximumLuck += importants[0]
                importants.pop(0)

        for element in importants:
            maximumLuck -= element

    return maximumLuck

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    nk = input().split()
    #
    n = int(nk[0])
    #
    k = int(nk[1])
    #
    contests = []
    #
    for _ in range(n):
         contests.append(list(map(int, input().rstrip().split())))

    #k = 3
    #contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]

    result = luckBalance(k, contests)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
