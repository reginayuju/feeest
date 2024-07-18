import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# def marsExploration(s):
count = 0
s = "SOSSPSSQSSOR"
s = list(s)
# print(s)
# print(int(len(s)/3))
for i in range (1,int(len(s)/3)+1):
    print(i, s[i])
    print(i+1, s[i+1])
    print(2*i+1, s[2*i+1])
    # if s[(i-1)] != 'S':
    #     print(i-1,s[i-1])
    #     # count +=1
#     if s[3(i+1)+1] != 'S':
#         count +=1
#     if s[3(i+1)-1] != 'O':
#         count +=1
# print(count)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = marsExploration(s)

#     fptr.write(str(result) + '\n')

#     fptr.close()
