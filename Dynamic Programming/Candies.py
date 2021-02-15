#!/bin/python3

import math
import os
import random
import re
import sys

def candiesAux(n, arr, i, direction, previousInAuxArray):
    numberCandies = None
    if(direction == 0): # left to right
        if( arr[i-1] < arr[i] ):
            numberCandies = previousInAuxArray + 1
        else:
            if( i+1 < n ):
                if( arr[i+1] < arr[i] ):
                    numberCandies = 2
                else:
                    numberCandies = 1
            else:
                numberCandies = 1
    else: # right to left
        if( arr[i+1] < arr[i] ):
            numberCandies = previousInAuxArray + 1
        else:
            if( i-1 >= 0 ):
                if( arr[i-1] < arr[i] ):
                    numberCandies = 2
                else:
                    numberCandies = 1
            else:
                numberCandies = 1
    return numberCandies

# Complete the candies function below.
def candies(n, arr):

    i = 1
    auxArrayLR = [ 1 for i in range( len(arr) ) ]
    while( i < len(arr) ):
        auxArrayLR[i] = candiesAux(n, arr, i, 0, auxArrayLR[i-1])
        i += 1

    j = len(arr)-2
    auxArrayRL = [ 1 for i in range( len(arr) ) ]
    while( j >= 0 ):
        auxArrayRL[j] = candiesAux(n, arr, j, 1, auxArrayRL[j+1])
        j -= 1

    i = 0
    numberCandies = 0
    while( i < len(arr) ):
        numberCandies += max( auxArrayLR[i], auxArrayRL[i] )
        i += 1

    #print(auxArray)
    return numberCandies

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    #fptr.write(str(result) + '\n')
    print(str(result) + '\n')

    #fptr.close()
