import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# def gradingStudents(grades):
grades = [
    64, 24, 68, 14, 53, 49, 45, 99, 55, 24, 59, 67, 8, 76, 37, 24, 24, 73, 81,
    37, 47, 63, 99, 63, 40, 54, 82, 9, 80, 84, 15, 32, 51, 18, 70, 4, 86, 59,
    32, 68, 22, 1, 71, 51, 81, 22, 35, 65, 9, 17, 94, 69, 40, 39, 52, 94, 84,
    13, 68, 95
]
list1 = list(range(35, 101, 5))
result = []
for i in range(len(grades)):
    if grades[i] <= 35:
        ans = grades[i]
        result.append(ans)
    if grades[i] > 35:
        for j in range(len(list1)):
            if list1[j] < grades[i] <= list1[j + 1]:
                if 0 < list1[j + 1] - grades[i] < 3:
                    ans = list1[j + 1]
                    result.append(ans)
                if list1[j + 1] - grades[i] >= 3:
                    ans = grades[i]
                    result.append(ans)
                if list1[j + 1] == grades[i]:
                    ans = grades[i]
                    result.append(ans)

for i in result:
    print(i)

# print(result)

# for i in range(len(grades)):
#     if grades[i]<40:
#         ans=grades[i]
#         result.append(ans)
#     for j in range (len(list)):
#         if list[j]<grades[i]:
#             if list[j]- grades[i]<3:
#                 ans = grades[i]+1
#                 result.append(ans)
#             if list[j] >= grades[i]:
#                 ans = grades[i]
#                 result.append(ans)
#     print(result)

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     grades_count = int(input().strip())

#     grades = []

#     for _ in range(grades_count):
#         grades_item = int(input().strip())
#         grades.append(grades_item)

#     result = gradingStudents(grades)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
