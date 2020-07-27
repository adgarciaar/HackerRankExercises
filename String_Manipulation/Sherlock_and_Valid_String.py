#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):

    dictionary = {}

    for letter in s:
        dictionary[letter] = dictionary.get(letter,0) + 1

    print(dictionary)

    histogram = {}

    count = 0
    keys = list( dictionary.keys() )
    number = dictionary[keys[0]]
    for element in keys:
        frequency = dictionary[element]
        histogram[frequency] = histogram.get(frequency,0) + 1

    print(histogram)

    keys = list( histogram.keys() )

    differentFrequencies = len(keys)

    if(differentFrequencies > 2):
        return 'NO'
    elif(differentFrequencies == 1):
        return 'YES'
    elif(differentFrequencies == 2):
        #if( abs(keys[0]-keys[1]) == 1 ):
        n1 = histogram[ keys[0] ]
        n2 = histogram[ keys[1] ]
        if( n1 > 1 and n2 == 1):
            if( keys[1]-1 == keys[0] or keys[1]-1 == 0 ):
                return 'YES'
            else:
                return 'NO'
        elif( n1 == 1 and n2 > 1 ):
            if( keys[0]-1 == keys[1] or keys[0]-1 == 0 ):
                return 'YES'
            else:
                return 'NO'
        elif( n1 == 1 and n2 == 1 ):
            return 'YES'
        else:
            return 'NO'
        #else:
        #    return 'NO'

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
