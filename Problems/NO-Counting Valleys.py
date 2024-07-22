import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# def countingValleys(steps, path):
path='DDDUUDDDUDUUDUUUDDUDUDUDDUDUDDDDDDUUUUUDDUUDDDUUDUDUDDUDUDUUUDUUUDUUUUDUUDUUUDDDUDUDUUUDUDUDUUDDDUUDUDDDUUDDUDDUDDDDUDDUUUUUUDUDUDUDUUDUDDUUUDUUDDUDDDDDDUDUDUUDUDDDUUUUUDDDDDUDDDDUUDDUDUDUDUDDUDUUDUDUDDDUDDUUUUDUDDUDUDDDDUUUDDUDDUUDDDUDUDDUDUUDUUUUDDUDDUUUDUUUUUDDUDUDUUUUUDDUDUDUDDUDUUDDDDDDUDUUDUDDUUDUUUUUDDUDDUDDUUDDDUDDUDDDUUDUDDDDDDUUDUDDDDDDDDDDUDDDDDUUDUUUDUUDDDUDDUDUDDUUUUDDDUUDUUDDUUDDUUUUUUUUDUUUUUDUUDUUDDUUUUDDDUDUUDUUDDDUUDDDUUDDDDDUDDDUDUUDDDUDDUUDDDUDDUUDDUUUDUDUUDDDUUUUDUUUDUDDUDDDDDDUDUUUUDDUDUDDDUUDUUDUDUDDUDUUUDDUDDUDDDUDDUUDUUUUUUDDDDDDDDUDUUDDDDDUUDDUDDDUDDDUDDDUDDUDUUDUDDDUUDUDUUDUDUDDUUDDUDUUDDDUDUDDUUDUUUDDUDDDUUDDUUUUUDDUUUUUUDUDUDDDUDDUUUUDDUUUDDDUDDDDDDUDDDUDUUDDUDUUUDDDUDDDDUDUUDDDDUDUDUDUDUUUDDUUUUDUUDUUUDDDUDUUUDUUUDUDUUUDDDUUDUUDUDDUUDUUUDDUDDUUUDDUDUDUDDDUUUDUUDUDDUUDUDUDUDUUDUDUUDDUUUDDUUDUDDUUUUUDUDDUDUDDDUUUDDUDUUDDUDUUDUUUUUDDUDUUDUDUDDDUUUDDDUDUUDUUUDUUDDUDUDDDDUUDUDUUDDDDUDUUUDDDDDUUUDUUDDUUUUUDDDUUUDDDDUDUUUDUUDDUDUDDUDUUUDDUDUDUUUDUUUUDUDUDDDDUUUUDDDDDDUUUUUUDDUDU'
step_list=[]
valley_list=[]
count=0
for i in range (len(path)):
    if path[i]=='U':
        step_list.append(1)
    if path[i]=='D':
        step_list.append(-1)
    # print (step_list)
for j in range (len(step_list)):
    # print(j)
    v=sum(step_list[0:j+1])
    valley_list.append(v)
# print(valley_list)
for a in range (len(valley_list)):
    if valley_list[a]==0 and valley_list[a-1]<0:
        count+=1
print(count)
#     for a in range(1,j+2):
#         v=sum(step_list[0:a])
#         valley_list.append(v)
# print(valley_list)
    # v=step_list[j]+step_list[j+1]
    # valley_list.append(v)
    # print(valley_list)

    

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     steps = int(input().strip())

#     path = input()

#     result = countingValleys(steps, path)

#     fptr.write(str(result) + '\n')

#     fptr.close()