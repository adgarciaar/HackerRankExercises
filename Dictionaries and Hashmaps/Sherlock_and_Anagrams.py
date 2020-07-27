# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:07:18 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations

def areAnagramsBetter(s1, s2):
    
    string1_list = sorted(s1)
    string2_list = sorted(s2)
    
    string1 = ''
    for ch in string1_list:
        string1 = string1+ch
        
    #print(string1)
    
    string2 = ''
    for ch in string2_list:
        string2 = string2+ch
        
    #print(string2)
    
    if( string1 == string2 ):
        return True
    else:
        return False

#not the best but works
def areAnagrams(s1, s2):
    
    dictionary = {}
    
    for letter in s2:
        if( dictionary.get(letter) == None ):
            dictionary[letter] = 1
        else:
            dictionary[letter] = dictionary[letter] + 1
            
    #print(dictionary)
    
    for letter in s1:
        if(dictionary.get(letter) == None):
            return False
        else:
            if(dictionary[letter] > 0):
                dictionary[letter] = dictionary[letter] - 1
            else:
                return False
    
    return True

def findSubstrings(s):
    
    substrings = []
    
    anagram = ""
    for i in range(0, len(s)):
        anagram = anagram + s[i]
        
        substrings.append(anagram)
            
        for j in range(i+1, len(s)):
            anagram = anagram + s[j]
            
            substrings.append(anagram)
            
        anagram = ""
            
    #print(substrings)
    return substrings

#organize alphabetically a string
def orderString(s):
    
    string_list = sorted(s)
    
    string = ''
    for ch in string_list:
        string = string+ch
        
    return string

def sherlockAndAnagrams(s):   
    
    counter1 = 0
    counter2 = len(s)-1
    
    substrings = findSubstrings(s)
    #print(substrings)
    
    pairs = 0
    
    dictionary = {}
    
    for subs in substrings:
        #if string is organized alphabetically then is easy see the anagrams
        orderS = orderString(subs)
        if( dictionary.get(orderS) == None ):
            dictionary[orderS] = 1
        else:
            dictionary[orderS] = dictionary[orderS] + 1
            
    keys = list( dictionary.keys() )
    for element in keys:
        reps = dictionary[element]
        #create array of the same element to use combinations of python
        elements = [element]*reps
        if( reps > 1 ):
            #number of ways to organize m elements in n positions
            #through combination
            #in this case organize reps elements (the same) in 2 positions
            comb = list(combinations(elements, 2) )
            pairs = pairs + len(comb)
            
    #print(dictionary)
    
    return int(pairs)

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagramsNaive(s):   
    
    counter1 = 0
    counter2 = len(s)-1
    
    substrings = findSubstrings(s)
    #print(substrings)
    
    pairs = 0
    
    for i in range(0, len(substrings)):
        for j in range(i+1, len(substrings)):
            s1 = substrings[i]
            s2 = substrings[j]
            if( len(s1) == len(s2) and areAnagrams(s1, s2) ):
                pairs += 1
    
    return pairs

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(input())
    q = 1

    for q_itr in range(q):
        #s = input()
        s = "kkkk"

        result = sherlockAndAnagrams(s)

        print(result)
        #fptr.write(str(result) + '\n')

    #fptr.close()