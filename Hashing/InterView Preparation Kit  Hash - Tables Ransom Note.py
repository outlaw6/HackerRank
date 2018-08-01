#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    t = True
    temp = []
    for word in note:
        if word in magazine and magazine.count(word) == note.count(word):
            continue
        else:
            return "No"
    return "Yes"
    
'''def ransom_note(magazine, ransom):
    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] += 1
    print(d)
    for word in ransom:
        if word in d:
            d[word] -= 1
        else:
            return False
    print(d)
    
    return all( [x >= 0 for x in d.values()] )'''

from collections import Counter

def ransom_note(magazine, rasom):
    print(Counter(magazine))
    print(Counter(rasom))
    print(Counter(rasom) - Counter(magazine))
    return (Counter(rasom) - Counter(magazine)) == {}
if __name__ == '__main__':
    #mn = input().split()

    #m = int(mn[0])

    #n = int(mn[1])
    
    
    magazine = ["give","me","one","grand","today","night"] #input().rstrip().split()

    note = ["give","one","grand","today"]#input().rstrip().split()

    print(ransom_note(magazine, note))