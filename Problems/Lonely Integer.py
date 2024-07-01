import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# def lonelyinteger(a):
arr= 1, 2, 3, 4, 3, 2, 1

# var cText = allText.indexOf('c');
# if(cText > -1){
#     allText.splice(cText, 1);
# }

# my_array = array('i', [1,2,3,3,5])
# my_array.count(3)
# # 2

for i in range(len(arr)):
    # print(arr.count(arr[i]))
    a = arr.count(arr[i])
    print (a)
    if a==1:
        print(arr[i])
    
    # if arr.count(arr[i]) == 1:
    #     print(arr.count[i])


# arr2=set(arr)

# ans=arr.index(arr2)
# print(ans)

# print(arr2)


    

# if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     a = list(map(int, input().rstrip().split()))

    

#     result = lonelyinteger(a)

#     fptr.write(str(result) + '\n')

#     fptr.close()
