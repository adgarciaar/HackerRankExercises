# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:48:35 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import copy

def minimumSwaps(arr):
    
    swaps = 0
    
    dictionary = { arr[i] : i for i in range(0, len(arr)) }
    #print(dictionary)
    
    for i in range(0, len(arr)):
        
        #si no está donde debería
        if( arr[i] != i+1 ):            
            
            #tomar posición de dónde estaba el que toca poner
            position = dictionary[i+1]
            
            #el que está en posición equivocada
            numberBefore = arr[i]
            
            #poner el correcto en posición
            arr[i] = i+1            
            
            #el que estaba en pos equivocada se intercambia
            arr[position] = numberBefore   
            
            #actualizar dictionary
            dictionary[i+1] = i
            dictionary[numberBefore] = position            
            
            swaps = swaps + 1
    
    return swaps

#----------------------------------------------------

def findHigher(arr, i, f):
    higher = -math.inf
    pos = None
    for i in range(i,f):
        if(arr[i] > higher):
            higher = arr[i]
            pos = i
    return pos

def findLess(arr, i, f):
    less = math.inf
    pos = None
    for i in range(i,f):
        if(arr[i] < less):
            less = arr[i]
            pos = i
    return pos

# Complete the minimumSwaps function below.
#def minimumSwapsFirstTry(arr):
def minimumSwapsNaive(arr):
    
    swaps = 0
    
    firstIndex = 0
    lastIndex = len(arr)-1
    
    while(lastIndex - firstIndex > 0):
        
        #print(arr[firstIndex:lastIndex+1])        
        
        posH = findHigher(arr, firstIndex, lastIndex+1)
        #print(posH)
        
        if(lastIndex != posH):     
            #print("cambia "+str(arr[lastIndex])+" por "+str(arr[posH]))
            temp = arr[lastIndex]
            arr[lastIndex] = arr[posH]
            arr[posH] = temp            
            swaps = swaps + 1
        
        posL = findLess(arr, firstIndex, lastIndex+1)
        #print(posL)
        
        if(firstIndex != posL):   
            #print("cambia "+str(arr[firstIndex])+" por "+str(arr[posL]))
            temp = arr[firstIndex]
            arr[firstIndex] = arr[posL]
            arr[posL] = temp
            swaps = swaps + 1
        
        #arr = exchange[arr[firstIndex:lastIndex+1], posH, lastIndex]        
        #arr = exchange[arr[firstIndex:lastIndex+1], posL, firstIndex]
            
        #print(arr[firstIndex:lastIndex+1])   
        
        firstIndex = firstIndex + 1
        lastIndex = lastIndex - 1       
        
    return swaps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #arr = list(map(int, input().rstrip().split()))
    arr = [7,1,3,2,4,5,6]
    #arr = [4,3,1,2]

    res = minimumSwaps(arr)
    
    print(res)

    #fptr.write(str(res) + '\n')

    #fptr.close()