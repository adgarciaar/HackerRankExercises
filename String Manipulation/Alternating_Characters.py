#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.

#se crea nueva cadena con el primer caracter. Cada vez que cambia el character
#se añade a esa cadena. Si se repite no se añade. Al final, se retorna la
#diferencia de longitudes de la cadena inicial y la generada.

def alternatingCharacters(s):

    new = ''
    change = s[0]
    new = new + change
    for i in range(0, len(s)):
        if( s[i] == change ):
            pass
        else: #change of character
            new = new + s[i]
            change = s[i]

    #print(new)

    return len(s)-len(new)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #q = int(input())
    q = 1

    for q_itr in range(q):
        #s = input()
        s = 'AABAAB'
        #s = 'AAAAAAA'

        result = alternatingCharacters(s)

        print(result)

        #fptr.write(str(result) + '\n')

    #fptr.close()
