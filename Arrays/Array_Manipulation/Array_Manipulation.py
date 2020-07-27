#!/bin/python3

import math
import os
import random
import re
import sys

#la idea es guardar el número a sumar en la posición donde se debe empezar a 
#sumar, y guardar el mismo número pero negativo donde se debe empezar a restar
#Luego hay que recorrer el array sumando todo lo que se encuentre hasta esa
#posición. Con los negativos automáticamente se deja de restar los que no 
#aplican para determinada posición.
def arrayManipulation(n, queries):
    
    array = [0 for i in range(n)]
    
    #for every operation
    for i in range(0, len(queries)):
        
        pMin = queries[i][0]
        pMax = queries[i][1]
        number = queries[i][2]
        
        array[pMin-1] = array[pMin-1] + number
        #position where the number is not added anymore
        if(pMax <  len(array) ):
            array[pMax] = array[pMax] - number
            
        #print(array)
        
    #print(array)
    
    maxElement = -math.inf
    acumulativeSum = 0
    
    for i in range(0, len(array)):
        
        acumulativeSum = acumulativeSum + array[i]
        #array[i] = acumulativeSum #problem with this
        
        #if( array[i] > maxElement ): #problem with this
        if( acumulativeSum > maxElement ):
            #maxElement = array[i] #problem with this
            maxElement = acumulativeSum
            
    #print(array)

    return maxElement

# Complete the arrayManipulation function below.
def arrayManipulationNaive(n, queries):

    array = [0 for i in range(n)]

    #for every operation
    for i in range(0, len(queries)):
        pMin = queries[i][0]
        pMax = queries[i][1]
        number = queries[i][2]
        for j in range(pMin, pMax+1):
            array[j-1] = array[j-1] + number

    print(array)

    maxElement = -math.inf
    for i in range(0, len(array)):
        if( array[i] > maxElement ):
            maxElement = array[i]

    return maxElement

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # nm = input().split()
    #
    # n = int(nm[0])
    #
    # m = int(nm[1])
    #
    # queries = []
    #
    # for _ in range(m):
    #     queries.append(list(map(int, input().rstrip().split())))
    
    file = open("testLarge.txt", "r")
    linesFile = file.readlines()
    #print(linesFile[0])    
    arrayFirstLine = linesFile[0].strip().rsplit(' ')
    n = int(arrayFirstLine[0])
    m = int(arrayFirstLine[1])
    
    print('n = '+str(n)+', m = '+str(m))
    
    queries = [] 
    for i in range(1, m+1):
        operationString = linesFile[i].strip().rsplit(' ')
        operation = [ int(operationString[0]), int(operationString[1]), int(operationString[2]) ]
        queries.append(operation)

#    n = 10
#    queries = []
#    queries.append([1,2,75755])
#    queries.append([2,5,75755])
#    queries.append([3,4,75755])

    result = arrayManipulation(n, queries)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
