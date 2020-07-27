# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 21:45:15 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    
    dictionary = {}
    
    for letter in s2:
        dictionary[letter] = True
    
    for letter in s1:
        if( dictionary.get(letter) != None ):
            return "YES"
        else:
            continue
    
    return "NO"

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    q = int(input())
    
    q = 1

    for q_itr in range(q):
        #s1 = input()
        s1 = "hello"

        #s2 = input()
        s2 = "world"

        result = twoStrings(s1, s2)
        
        print(result)

        #fptr.write(result + '\n')

    #fptr.close()