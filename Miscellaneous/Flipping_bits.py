#!/bin/python3

import math
import os
import random
import re
import sys

maxDigits = 32

def decimalToBinary(n):
    
    accumulated = 0
    binaryS = ''
    for i in range( maxDigits-1, -1, -1 ):
        if( accumulated + 2**i <= n ):
            binaryS = binaryS + '1'
            accumulated += 2**i
        else:
            binaryS = binaryS + '0'
    
    return binaryS

def decimalToBinaryRecursive(n, binaryS):
    
    if( n == 1):
        return '1'    
    if(n > 1):        
        binaryS = binaryS + decimalToBinaryRecursive(n//2, binaryS) + str( n%2 )
        return binaryS

# Complete the flippingBits function below.
def flippingBits(n):
    
    initialBinary = None
    
    if( n == 0 ):
        initialBinary = '0'
    elif( n == 1 ):
        initialBinary = '1'
    else:
        #initialBinary = decimalToBinaryRecursive(n, '')
        initialBinary = decimalToBinary(n)
        
    if( len(initialBinary) < maxDigits ):
        for i in range( maxDigits - len(initialBinary) ):
            initialBinary = '0' + initialBinary
    
    newInteger = 0
    counter = 0
    for element in reversed(initialBinary):
        
        number = int(element)
        if(number == 0):
            newInteger += 2**counter
        counter += 1
        
    return newInteger

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)
        
        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
