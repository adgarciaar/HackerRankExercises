# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:45:28 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    actual = 0
    path_jumps = 0
    
    while( actual < len(c)-1  ):
        
        if( actual+2 <= len(c)-1 and c[actual + 2] == 0  ):
            actual = actual + 2
            path_jumps = path_jumps+1
            
        elif( actual+1 <= len(c)-1 and c[actual + 1] == 0):
            actual = actual + 1
            path_jumps = path_jumps+1
            
    return path_jumps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 7
    
    c = [0,0,1,0,0,1,0]

    result = jumpingOnClouds(c)

    print(str(result) + '\n')

    #fptr.close()
