# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:58:54 2020

@author: adgar
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    
    #dictionaryMagazine = { i : 'Not used' for i in magazine }
    dictionaryMagazine = { }
    
    for word in magazine:
        if( word not in dictionaryMagazine.keys() ):
            dictionaryMagazine[word] = 1
        else:
            dictionaryMagazine[word] = dictionaryMagazine[word] + 1 

    #print(dictionaryMagazine)    
    
    #b = True
    for i in range(0, len(note)):
        word = note[i]
        if( word not in dictionaryMagazine.keys() ):
            #b = False
            print('No')
            return
        else: #word is in dictionary
            if (dictionaryMagazine[word] > 0 ):                
                dictionaryMagazine[word] = dictionaryMagazine[word] - 1              
            else: #word already used
                print('No')
                return
    
    print('Yes')            
    
if __name__ == '__main__':
#    mn = input().split()
#
#    m = int(mn[0])
#
#    n = int(mn[1])
#
#    magazine = input().rstrip().split()
#
#    note = input().rstrip().split()
    
    magazine = ['two','times','three','is','not','four']
    note = ['two','times','two','is','four']

    checkMagazine(magazine, note)