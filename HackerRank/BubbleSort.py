#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0;
    for i in range(1, len(a)):
        for j in range(len(a) - i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swaps += 1 
                            
    print("Array is sorted in {0} swaps.".format(swaps))
    print("First Element: {0}".format(a[0]))
    print("Last Element: {0}".format(a[len(a)-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
