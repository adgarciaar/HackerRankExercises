# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 01:00:41 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    ocurrences_first = 0
    for i in range(0, len(s)):
        if(s[i] == "a"):
            ocurrences_first = ocurrences_first + 1       
    
    x = int(n / len(s))
    remainder = n % len(s)
        
    ocurrences = ocurrences_first*x
    substring = s[0:remainder]
        
    ocurrences_second = 0
    for i in range(0, len(substring)):
        if(substring[i] == "a"):
            ocurrences_second = ocurrences_second + 1     
                
    ocurrences = ocurrences + ocurrences_second
        
    return ocurrences     


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "aba"

    n = 10

    result = repeatedString(s, n)

    print(str(result) + '\n')

    #fptr.close()
