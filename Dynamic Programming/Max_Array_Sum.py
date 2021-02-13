#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    
    maxSum = 0
    maxSumArray = [0 for i in range(0, len(arr))]
    if(arr[0] > 0):
        maxSumArray[0] = arr[0]
    if(arr[1] > 0):
        maxSumArray[1] = arr[1]
    if(arr[2] > 0):
        maxSumArray[2] = arr[2]
    maxSumArray[2] = max(maxSumArray[2], maxSumArray[0]+maxSumArray[2])
    
    for i in range(3, len(arr)):
        if(arr[i] > 0):
            maxSumArray[i] = arr[i]
        maxSumAux1 = maxSumArray[i] + maxSumArray[i-2]
        maxSumAux2 = maxSumArray[i] + maxSumArray[i-3]
        maxSumAux = max(maxSumAux1, maxSumAux2)
        maxSumAux = max(maxSumAux, maxSumArray[i])
        maxSumArray[i] = maxSumAux
        maxSum = max(maxSum, maxSumArray[i])
    
    return maxSum

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    #fptr.write(str(res) + '\n')
    
    print(str(res) + '\n')

    #fptr.close()
