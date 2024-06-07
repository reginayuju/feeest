#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(n, arr):
    p_count = 0
    n_count = 0
    z_count = 0
    for x in (arr):
        # print("ZZZ",x)
    
        if x > 0:
            p_count = p_count + 1
    
        if x < 0:
            n_count = n_count + 1
            # print("NN", n_count)
    
        if x == 0:
            z_count = z_count + 1
    # print("AAA", p_count, p_count/n)
    # print("BBB", n_count, n_count/n)
    # print("CCC", z_count, z_count/n)
    print('%.6f' %(p_count/n))
    print('%.6f' %(n_count/n))
    print('%.6f' %(z_count/n))
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)