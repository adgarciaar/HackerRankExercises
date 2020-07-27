# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:27:41 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    valleys = 0    
    level = 0
    started = False
    
    for i in range(0,n):
        level_before = level
        if(s[i] == "U"):
            level = level + 1
        else:
            level = level - 1
            
        #print(level_before)
        #print(level)
        
        if(level < 0 and level_before == 0):
            started = True
        if(level == 0 and level_before < 0 and started == True):
            valleys = valleys + 1
            started = False
            
    return valleys

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 8

    s = "UDDDUDUU"

    result = countingValleys(n, s)

    print(str(result) + '\n')

    #fptr.close()