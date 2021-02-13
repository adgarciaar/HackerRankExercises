#!/bin/python3

import math
import os
import random
import re
import sys

def findSubstringsNaive(s):

    substrings = []
    sub = ''
    differentLetters = {}
    for i in range( 0, len(s) ):
        sub = sub + s[i]
        differentLetters[ s[i] ] = True
        substrings.append( sub )
        for j in range( i+1, len(s) ):
            if( differentLetters.get(s[j]) == None ):
                differentLetters[ s[j] ] = True
            if( len(differentLetters) <= 2 ):
                sub = sub + s[j]
                substrings.append( sub )
        sub = ''
        differentLetters = {}

    return substrings

def isSpecialSubstring(s):

    histogram = {}

    for letter in s:
        histogram[letter] = histogram.get(letter, 0) + 1
        if( len(histogram) > 2 ):
            return False

    #print( histogram )
    #print( len(histogram) )

    letters = list( histogram.keys() )
    if( len(letters) == 1 ):
        return True
    elif( len(letters) == 2 and len(s)%2 != 0 ):
        mediumLetter = s[ len(s)//2 ]
        if( histogram[mediumLetter] == 1 ):
            return True
        else:
            return False
    else:
        return False

# Complete the substrCount function below.
def substrCountNaive(n, s):

    substrings = findSubstrings(s)

    print( "subs: "+str(len(substrings)) )

    #print(substrings)
    numberSpecials = 0
    for sub in substrings:
        if( isSpecialSubstring(sub) == True ):
            numberSpecials += 1

    return numberSpecials

# Complete the substrCount function below.
def substrCount(n, s):

    newString = []
    counter = -1
    lastLetter = s[0]
    reps = 0
    for letter in s:
        if( letter != lastLetter):
            newString.append( [lastLetter, reps] )
            lastLetter = letter
            counter += 1
            reps = 0
        reps += 1

    newString.append( [lastLetter, reps] )

    #print(newString)

    counter = 0

    for i in range( 0, len(newString) ):

        element = newString[i]

        if( element[1]>1 ):
            counter += ( element[1] * (element[1]+1) )/2
            # [n(n+1)]/2 = #substrings no vacíos en un string
        elif( element[1] == 1 ):
            counter += 1

        if( i+1 < len(newString) and i+2 < len(newString) ):

            element2 = newString[i+1]
            element3 = newString[i+2]

            if( element3[0] == element[0] and element2[1] == 1 ):
                leastReps = min( element[1], element3[1] )
                counter += leastReps

    return int(counter)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
