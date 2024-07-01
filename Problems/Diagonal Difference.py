import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# def diagonalDifference(arr):

n=3
arr=[[11, 2, 4],[4, 5, 6],[10, 8, -12]]
list1=[]
list2=[]
for i in range (len(arr)):
    for j in range (len(arr)):
        if i==j:
            list1.append(arr[i][j])
print(list1)

arr.reverse()
for i in range (len(arr)):
    for j in range (len(arr)):
        if i==j:
            list2.append(arr[i][j])
print(list2)
ans=sum(list1)-sum(list2)
print(ans)
if ans>=0:
    ans=ans
if ans<0:
    ans=-(ans)
print(ans)
# for i in reversed(len(arr)):
#     for j in range (len(arr)):
#         print(i,j)
# #         if i==j:
# #             list2.append(arr[i][j])
# print(list2)





# if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    
    # n = int(input().strip())
    



    # for _ in range(n):
        # arr.append(list(map(int, input().rstrip().split())))

    # result = diagonalDifference(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
