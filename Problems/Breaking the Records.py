#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    Min = scores[0]
    Max = scores[0]
    lo = 0
    hi = 0
    for i in range(1, len(scores)):
        print("Game", i)
        print("Score", scores[i])

        if scores[i] < Min:
            lo += 1
            Min = scores[i]
        if scores[i] > Max:
            hi += 1
            Max = scores[i]
        print(Max, Min)
        print(hi, lo)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()