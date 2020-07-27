#!/bin/python3

import math
import os
import random
import re
import sys

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low , high):

        # If current element is smaller than or
        # equal to pivot
        if   arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr,low,high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# Complete the maximumToys function below.
def maximumToys(prices, k):

    quickSort(prices, 0, len(prices)-1)

    toysBought = 0
    leftMoney = k
    for number in prices:
        if(number <= leftMoney):
            toysBought += 1
            leftMoney -= number
        if(leftMoney == 0):
            break

    return toysBought

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # nk = input().split()
    #
    # n = int(nk[0])
    #
    # k = int(nk[1])
    k = 50

    #prices = list(map(int, input().rstrip().split()))
    prices = [1,12,5,111,200,1000,10]

    result = maximumToys(prices, k)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
