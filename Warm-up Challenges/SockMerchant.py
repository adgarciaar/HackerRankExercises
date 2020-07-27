# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:58:11 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    #actual = ar[0]
    parejas = 0
    vistos = []
    
    for i in range(0,n):
        
        actual = ar[i]        
        
        if(actual not in vistos):
            
            vistos.append(actual)
        
            coincidencias = 1
            
            for j in range(i+1,n):
                
                if( i != j and actual == ar[j] ):
                    coincidencias = coincidencias + 1
            
            #print("Para "+str(actual)+" es "+str(int(coincidencias/2)))
            if(coincidencias > 1):
                
                parejas = parejas + int(coincidencias/2)
     
    return parejas   
                
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 9

    ar = [10,20,20,10,10,30,50,10,20]

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

    #fptr.close()
