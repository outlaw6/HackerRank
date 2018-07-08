#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here


num_of_swaps = 0
for num in range(len(a)):
    
    for nmbr in range(n-1):
        if a[nmbr] > a[nmbr+1]:
            temp = a[nmbr]
            a[nmbr] = a[nmbr+1]
            a[nmbr+1] = temp
            num_of_swaps += 1
    if num_of_swaps == 0:
        break
if num_of_swaps == 0:
    print("Array is sorted in 0 swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
else:
    print("Array is sorted in {0} swaps.".format(num_of_swaps))
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
         