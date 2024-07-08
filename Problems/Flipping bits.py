import math
import os
import random
import re
import sys
from sys import stdin

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

# def flippingBits(n):
# n=894832
# for read in stdin:
#     n=int(read)
#     print(bin(n)[2:])


a_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


x = 13
temp = format(x, "b")
list_2 = []
ans_list = []
for i in range(len(temp)):
    a_list[-1 - i] = temp[-1 - i]

for i in range(len(a_list)):
    if a_list[i] == '1':
        b = 0
        list_2.append(b)
    if a_list[i] == '0':
        b = 1
        list_2.append(b)
    if a_list[i] == 0:
        b = 1
        list_2.append(b)
for e in range(len(list_2)):
    if list_2[-1-e] == 1:
        ans = 2**e
        ans_list.append(ans)
    if list_2[-1-e] == 0:
        ans = 0
        ans_list.append(ans)
print(sum(ans_list))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

# q = int(input().strip())

# for q_itr in range(q):
#     n = int(input().strip())

#         result = flippingBits(n)

#         fptr.write(str(result) + '\n')

#     fptr.close()
