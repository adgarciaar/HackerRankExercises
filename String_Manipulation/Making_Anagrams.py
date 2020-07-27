#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    originalA = a
    originalB = b

    dictionaryA = {}
    for letter in a:
        dictionaryA[letter] = dictionaryA.get(letter, 0) + 1

    changes = 0
    array = []

    dictionaryB = {}
    for letter in b:
        dictionaryB[letter] = dictionaryB.get(letter, 0) + 1

    keysDictA = list( dictionaryA.keys() )

    for letter in keysDictA:
        if( dictionaryB.get(letter) == None ):
            changes += 1
            array.append( [letter, 1] )
            a = a.replace(letter, '')
        else:
            if( dictionaryA.get(letter) != dictionaryB.get(letter) ):
                changes += abs( dictionaryA.get(letter)- dictionaryB.get(letter) )
                array.append( [letter, abs( dictionaryA.get(letter)- dictionaryB.get(letter) )] )

                if( dictionaryA.get(letter) > dictionaryB.get(letter) ):

                    for i in range(0, abs( dictionaryA.get(letter)- dictionaryB.get(letter) )):
                        a = a.replace(letter, '', 1)
                else:
                    for i in range(0, abs( dictionaryA.get(letter)- dictionaryB.get(letter) )):
                        b = b.replace(letter, '', 1)


    keysDictB = list( dictionaryB.keys() )

    for letter in keysDictB:
        if( dictionaryA.get(letter) == None ):
            changes += 1
            array.append( [letter, 1] )
            b = b.replace(letter, '')

    print(array)

    #print(sorted(a))
    #print(sorted(b))

    #return changes
    return ( abs(len(originalA)-len(a)) + abs(len(originalB)-len(b)) )

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = input()

    #b = input()

    a = 'fcrxzwscanmligyxyvym'
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    res = makeAnagram(a, b)

    print(res)

    #fptr.write(str(res) + '\n')

    #fptr.close()
