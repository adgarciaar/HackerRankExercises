#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    numbers = sorted(arr)
    #print(numbers)

    minimumDiff = math.inf
    for i in range(0, len(numbers)-1):
        difference = abs( numbers[i] - numbers[i+1] )
        if( difference < minimumDiff ):
            minimumDiff = difference
    return minimumDiff

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())
    #
    # arr = list(map(int, input().rstrip().split()))

    arr = [-59,-36,-13,1,-53,-92,-2,-96,-54,75]

    result = minimumAbsoluteDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
