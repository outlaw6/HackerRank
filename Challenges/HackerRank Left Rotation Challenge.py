#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    def RotateLeft(arr, d, n):
        for x in range(d):
            RotateLeftTimes(arr,n)
            
    def RotateLeftTimes(arr, n):
        temp = arr[0]
        
        for x in range(n - 1):
            arr[x] = arr[x+1]
        arr[n - 1] = temp
        
    RotateLeft(a, d, n)
    
    for i in range(len(a)):
        print(a[i], end=' ')
        
    
        
        
