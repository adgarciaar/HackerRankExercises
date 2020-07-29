#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):

    sortedArray = sorted(arr)
    minimum = math.inf
    for i in range(0, (len(arr)-k) + 1):
        subarr = sortedArray[i:i+k]
        #print(subarr)
        if( subarr[ k-1 ] - subarr[0] < minimum ):
            minimum = subarr[ k-1 ] - subarr[0]
    return minimum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
