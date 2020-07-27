#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#from itertools import combinations     #slower

#combinatory
def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def countTriplets(arr, r):
    triplets = 0
    dictionary1 = {} #save the count for every number in first position (all)
    dictionary2 = {} #save the count for every number in second position

    for number in arr:
        if number in dictionary2:
            triplets += dictionary2[number]

        if number in dictionary1:
            if number*r in dictionary2:
                dictionary2[number*r] += dictionary1[number]
            else:
                dictionary2[number*r] = dictionary1[number]

        if number*r in dictionary1:
            dictionary1[number*r] += 1
        else:
            dictionary1[number*r] = 1

    return triplets
    

# Complete the countTriplets function below.
def countTripletsNaive(arr, r):

    dictionary = {}

    for number in arr:
        if( dictionary.get(number) == None ):
            dictionary[number] = 1
        else:
            dictionary[number] = dictionary[number] + 1

    #print(dictionary)

    triplets = 0
    temp = []
    for i in range(0, len(arr)):
        temp = []
        number = arr[i]
        temp.append(number)
        for j in range(i+1, len(arr)):
            number2 = arr[j]
            if( number2 == number*r ):
                temp.append(number2)
                number = number2
            if( len(temp)==3 ):
                print(temp)
                if( dictionary[temp[1]] == 1 and dictionary[temp[2]] == 1 ):
                    triplets += 1
                else:
                    if( dictionary[temp[1]] > 1):
                        triplets += dictionary[temp[1]]
                    if( dictionary[temp[2]] > 1):
                        triplets += dictionary[temp[2]]
                break

    return triplets

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fptr = open("input06.txt", 'r')
    #
    # nr = input().rstrip().split()

    nr = fptr.readline().rstrip().split(' ')
    #print(nr)

    n = int(nr[0])
    #n = 5dictionary[secondNextNumber]

    r = int(nr[1])
    #r = 2

    #arr = list(map(int, input().rstrip().split()))f( dictionaryPairs.get(i) == None ):
    #arr = [1,2,2,4]
    #arr = [1237]*100000
    arrS = fptr.readline().rstrip().split(' ')
    #
    arr = []
    for element in arrS:
        arr.append( int(element) )
    #print(len(arr))

    #arr = [1,2,1,2,4]

    ans = countTriplets(arr, r)

    print(ans)

    # fptr.write(str(ans) + '\n')
    #
    # fptr.close()
