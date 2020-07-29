# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 00:40:32 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    
    c = sorted(c)
    
    dictionary1 = {}
    dictionary2 = {}
    
    purchase = 0    
    counter = 0
    for element in reversed( c ):
        cost = (dictionary1.get(counter,0) + 1)*element
        dictionary1[counter] = dictionary1.get(counter,0)+1
        dictionary2[counter] = dictionary2.get(counter,0)+cost        
        counter += 1
        if(counter == k):
            counter = 0
        purchase += cost
            
    #print(dictionary1)
    #print(dictionary2)
    return purchase

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    
    print(minimumCost)

    #fptr.write(str(minimumCost) + '\n')

    #fptr.close()
