#!/bin/python3

import math
import os
import random
import re
import sys

def findMedian(arrayCount, d):

    if( d%2 != 0): #odd

        positionMedian = d//2 + 1

        tempCount = 0
        index = -1
        #keep while the position of median is reached
        while( tempCount < positionMedian):
            index += 1
            tempCount += arrayCount[index]
            #print('index:'+str(index)+' tempCount:'+str(tempCount)+' countMedian:'+str(positionMedian) )

        return index

    else: #even

        positionMedian1 = d/2
        positionMedian2 = d/2+1

        median1 = 0
        median2 = 0

        tempCount = 0
        index = -1
        while( tempCount < positionMedian1):
            index += 1
            tempCount += arrayCount[index]

        #if the two elements in the middle are the same
        if( tempCount > positionMedian1 ):
            return index
        else: #keep until the next element
            index2 = index
            while( tempCount < positionMedian2):
                index += 1
                tempCount += arrayCount[index]
            return (index+index2)/2

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):

    notificacions = 0

    arrayCount = [0 for i in range(201)]

    for i in range(0,d):
        arrayCount[ expenditure[i] ] += 1

    #median = findMedian(arrayCount, d)
    #print(median)

    for i in range( d, len(expenditure) ):

        #print("esto: "+str( expenditure[i] ))

        initialArray = expenditure[i-d:i]
        median = findMedian(arrayCount, d)
        #print('Median: '+str(median))
        #print(expenditure[i-d:i])
        if( expenditure[i] >= 2*median ):
            notificacions += 1

        arrayCount[ expenditure[i] ] += 1
        arrayCount[ expenditure[i-d] ] -= 1
        #print(i-d-1)

    return notificacions

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
