#!/bin/python3

import math
import os
import random
import re
import sys

def simplifyString(s):

    newS = []
    lastLetter = None
    counter = 0
    for i in range(0, len(s)):

        letter = s[i]

        if( lastLetter == None ):
            lastLetter = letter

        if( letter != lastLetter ):
            newS.append( [lastLetter, counter] )
            lastLetter = letter
            counter = 0
        counter += 1

        if( i == len(s)-1 ):
            newS.append( [lastLetter, counter] )

    print( newS )
    return newS

#This problem is LCS
def commonChildRecursive(X, Y, a, b):

    if a == 0 or b == 0:
       return 0
    elif X[a-1] == Y[b-1]:
       return 1 + commonChildRecursive(X, Y, a-1, b-1)
    else:
       return max( commonChildRecursive(X, Y, a, b-1), commonChildRecursive(X, Y, a-1, b) )

def commonChildMemoization(X, Y, a, b, M):

    if a == 0 or b == 0:
       M[a-1][b-1] = 0
    elif X[a-1] == Y[b-1]:
       M[a-1][b-1] =  1 + commonChildMemoization(X, Y, a-1, b-1, M);
    else:
       M[a-1][b-1] = max( commonChildMemoization(X, Y, a, b-1, M), commonChildMemoization(X, Y, a-1, b, M) )

    return M[a-1][b-1]

def LCS_llenado_matriz(X , Y): #so much fast but not enough, obviously
    a = len(X)
    b = len(Y)
    M = [[-math.inf]*(b+1) for i in range(a+1)]
    for i in range(a+1):
        for j in range(b+1):
            if i == 0 or j == 0 :
                M[i][j] = 0
            elif X[i-1] == Y[j-1]:
                M[i][j] = M[i-1][j-1]+1
            else:
                M[i][j] = max( M[i-1][j] , M[i][j-1])

    return M[a][b]

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    M = [ [-math.inf]*( len(s2) +1) for i in range( len(s1) +1)]
    #print(M)
    #result = commonChild(s1, s2)
    #result = commonChildRecursive(s1, s2, len(s1), len(s2))
    #esult = commonChildMemoization(s1, s2, len(s1), len(s2), M)
    result = LCS_llenado_matriz(s1, s2)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
