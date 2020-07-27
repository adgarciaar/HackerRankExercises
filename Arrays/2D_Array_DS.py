# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:52:22 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    
    suma_mayor = -math.inf
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if( i+2 <= len(arr)-1 and j+2 <= len(arr)-1 ):
                suma = 0
                suma = suma + arr[i][j]+arr[i][j+1]+arr[i][j+2]
                suma = suma + arr[i+1][j+1]
                suma = suma + arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                if(suma > suma_mayor):
                    suma_mayor = suma                
    
    return suma_mayor

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    arr.append([-1,-1,0,-9,-2,-2])
    arr.append([-2,-1,-6,-8,-2,-5])
    arr.append([-1,-1,-1,-2,-3,-4])
    arr.append([-1,-9,-2,-4,-4,-5])
    arr.append([-7,-3,-3,-2,-9,-9])
    arr.append([-1,-3,-1,-2,-4,-5])

    result = hourglassSum(arr)

    print(str(result) + '\n')

    #fptr.close()
