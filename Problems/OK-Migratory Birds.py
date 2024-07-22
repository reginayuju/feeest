import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def migratoryBirds(arr):
arr = [1, 1, 2, 2, 3]
c_list =[]
s_list = []
type_list= list(range(1, 6))
# print(type_list)
for i in range (len(type_list)):
    x = arr.count(type_list[i])
    c_list.append(x)
# print(c_list)
for j in range (len(c_list)):
    if c_list[j] == max(c_list):
        s_list.append(j)
print(min(s_list)+1)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     arr_count = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = migratoryBirds(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()
