# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:20:00 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#better complexity
def minimumBribes(q):
    
    bribes = 0
    
    #less, medium, higher
    minimumValues = [math.inf, math.inf, math.inf]    
    
    for i in range(len(q)-1,-1,-1):
        
        if( q[i] - (i+1) > 2):
            print("Too chaotic")
            return
        else:
            if(q[i] > minimumValues[2]):
                print("Too chaotic")
                return
            elif(q[i] > minimumValues[1]):
                bribes = bribes + 2
            elif(q[i] > minimumValues[0]):
                bribes = bribes + 1
        
        #update minimumValues
        
        if(q[i] < minimumValues[0]):
            minimumValues[2] = minimumValues[1]
            minimumValues[1] = minimumValues[0]
            minimumValues[0] = q[i]
        elif(q[i] < minimumValues[1]):
            minimumValues[2] = minimumValues[1]
            minimumValues[1] = q[i]
        elif(q[i] < minimumValues[2]):
            minimumValues[2] = q[i]    
    
    print(bribes)

#No best solution because of complexity but it works
def minimumBribesTwoCycles(q):
    
    counter = 0    
    
    for i in range(len(q)):
        
        if(q[i] - (i+1) > 2): 
            print("Too chaotic")     
            return
        else:        
           for j in range(i+1, len(q)):
               if(q[j] < q[i]):
                   counter = counter + 1                          
    
    print(counter)

if __name__ == '__main__':
    #t = int(input())
    
    t = [[2,1,5,3,4],[2,5,1,3,4],[1,2,5,3,7,8,6,4]]

    for t_itr in range(len(t)):
        #n = int(input())

        #q = list(map(int, input().rstrip().split()))
        q = t[t_itr]

        minimumBribes(q)