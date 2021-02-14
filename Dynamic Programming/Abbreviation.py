#!/bin/python3

import math
import os
import random
import re
import sys

#------------------------------------------------------------------------------
# top-down approach 

def recursiveAux(a, b, i, j, remainingLowercaseCharactersA, equivalentCharacters):
    if(i == 0 or j == 0):
        if(equivalentCharacters == len(b) and i == remainingLowercaseCharactersA ):
            return True
        else:
            return False
    else:
        if( a[i-1].islower() ):
            remainingLowercaseCharactersA -= 1
            
        if( a[i-1] == b[j-1] ):            
            return recursiveAux(a, b, i-1, j-1, remainingLowercaseCharactersA, 
                              equivalentCharacters+1)
        else:
            ver = False
            if( a[i-1].lower() == b[j-1].lower() ):
                ver1 = recursiveAux(a, b, i-1, j-1,remainingLowercaseCharactersA, 
                                  equivalentCharacters+1)
                # handling repeated letters
                ver2 = recursiveAux(a, b, i-1, j, remainingLowercaseCharactersA, 
                                  equivalentCharacters)
                ver = ver1 or ver2
            else:
                if( a[i-1].islower() ):
                    ver = recursiveAux(a, b, i-1, j, remainingLowercaseCharactersA, 
                                      equivalentCharacters)
                else:
                    ver = False            
            return ver
        

def recursive(a, b):
    
    remainingLowercaseCharactersA = 0
    
    for i in range(0, len(a)):
        if( a[i].islower() ):        
            remainingLowercaseCharactersA += 1
    
    result = recursiveAux(a, b, len(a), len(b), remainingLowercaseCharactersA, 0)
    if(result):
        return 'YES'
    else:
        return 'NO'
    
    
#------------------------------------------------------------------------------
# top-down approach     
        
def memoizationAux(a, b, i, j, remainingLowercaseCharactersA, equivalentCharacters, M):
    
    if(M[i][j] == None):
        if(i == 0 or j == 0):
            if(equivalentCharacters == len(b) and i == remainingLowercaseCharactersA ):
                M[i][j] = True
            else:
                M[i][j] = False
        else:            
            if( a[i-1].islower() ):
                remainingLowercaseCharactersA -= 1
                
            if( a[i-1] == b[j-1] ):            
                M[i][j] = memoizationAux(a, b, i-1, j-1, remainingLowercaseCharactersA, 
                                  equivalentCharacters+1,M)
            else:
                ver = False
                if( a[i-1].lower() == b[j-1].lower() ):
                    ver1 = memoizationAux(a, b, i-1, j-1,remainingLowercaseCharactersA, 
                                      equivalentCharacters+1,M)
                    # handling repeated letters
                    ver2 = memoizationAux(a, b, i-1, j, remainingLowercaseCharactersA, 
                                      equivalentCharacters,M)
                    ver = ver1 or ver2
                else:
                    if( a[i-1].islower() ):
                        ver = memoizationAux(a, b, i-1, j, remainingLowercaseCharactersA, 
                                          equivalentCharacters,M)
                    else:
                        ver = False                          
                M[i][j] = ver
        
    return M[i][j]


def memoization(a, b):
    
    M = [[None]*( len(b) +1) for i in range( len(a) +1)]   
    
    remainingLowercaseCharactersA = 0
    
    for i in range(0, len(a)):
        if( a[i].islower() ):        
            remainingLowercaseCharactersA += 1
    
    result = memoizationAux(a, b, len(a), len(b), remainingLowercaseCharactersA, 0, M)
    #print(M)
    if(result):
        return 'YES'
    else:
        return 'NO'
    
#------------------------------------------------------------------------------
# bottom-up approach 
        
def bottomUpApproach(a, b):
    
    M = [[False]*( len(b)+1 ) for i in range( len(a)+1 )] 
    
    M[0][0] = True
    for i in range(1, len(a)+1):
        if( a[i-1].islower() ):
            M[i][0] = True
        else:
            M[i][0] = False
    
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):                
            if( a[i-1] == b[j-1] ):            
                M[i][j] = M[i-1][j-1]
            else:
                if( a[i-1].lower() == b[j-1].lower() ):
                    M[i][j] = M[i-1][j-1] or M[i-1][j] 
                else:
                    ver = False
                    if( a[i-1].islower() ):
                        ver = M[i-1][j]
                    else:
                        ver = False
                    M[i][j] = ver
    return M[len(a)][len(b)]
    
# Complete the abbreviation function below.
def abbreviation(a, b):   
    
    result = bottomUpApproach(a,b)
    
    if(result):
        return 'YES'
    else:
        return 'NO'
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        #result = recursive(a, b)
        #result = memoization(a, b)
        result = abbreviation(a, b)

        #fptr.write(result + '\n')
        print(result+'\n')

    #fptr.close()