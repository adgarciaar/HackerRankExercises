#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):

    array = []
    dictionary = {}
    dictFrequencies = {}

    for pair in queries:
        operation = pair[0]
        number = pair[1]
        if(operation == 1):
            dictionary[ number ] = dictionary.get( number, 0 ) + 1
            frequency = dictionary[ number ]
            dictFrequencies[ frequency ] = dictFrequencies.get( frequency, 0 ) + 1
            if( dictFrequencies.get(frequency-1) != None ):
                dictFrequencies[ frequency-1 ] = dictFrequencies[ frequency-1 ] - 1
        elif(operation == 2):
            if( dictionary.get(number) != None and dictionary[number] > 0 ):
                dictionary[ number ] -= 1
                frequency = dictionary[ number ]
                if( dictFrequencies.get(frequency) != None ):
                    dictFrequencies[ frequency ] = dictFrequencies[frequency] + 1
                if( dictFrequencies.get(frequency+1) != None ):
                    dictFrequencies[ frequency+1 ] = dictFrequencies[ frequency+1 ] - 1
        elif(operation == 3):
            keys = list( dictionary.keys() )
            if( len(keys)==0 ):
                array.append(0)
            else:
                if( dictFrequencies.get(number) != None  and dictFrequencies[number] > 0):
                    array.append(1)
                else:
                    array.append(0)
                # b = False
                # for element in keys:
                #     if( dictionary[element] == number ):
                #         b = True
                # if(b==True):
                #     array.append(1)
                # else:
                #     array.append(0)
        # print(dictionary)
        # print(dictFrequencies)
        # print(array)

    return array

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print(ans)

    # fle = open('nana.txt','w')
    # for element in ans:
    #     fle.write(str(element)+"\n")
    # fle.close()

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')
    #
    # fptr.close()
