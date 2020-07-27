#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    
    print(a)
    newArray = [ None for i in range(0, len(a)) ]

    #a is array of integers
    #d is #rotations
    for i in range(len(a)-1,-1,-1):
        newIndex = (i-d) % len(a)
        newArray[newIndex] = a[i]        
        #print(newArray)
    
    return newArray

if __name__ == '__main__':
    
    a = [1,2,3,4,5]
    d = 4

    result = rotLeft(a, d)

    print(result)
