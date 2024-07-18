import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# def pangrams(s):

string = "The quick brown ox jumps over the lazy dog"
lowerstring=string.lower()
# pattern = '[a-zA-Z]'  # 匹配大小写字母
# result = re.findall(pattern, s)
# if result:
#     print ('True')
# else:
#     print ('False')

alpha_arr=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ans=[]
for i in range (len(alpha_arr)):
    while alpha_arr[i] in string:
        ans.append("program")
        if alpha_arr[i] not in string:
            ans.append("not program")
print(ans)
# if "not program" in ans:
#     print("not program")
# else:
#     print("program")
    # if alpha_arr[i] not in string:
    #     print(True)
    # else:
    #     print(False)


# print(programs(text))




# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = pangrams(s)

#     fptr.write(result + '\n')

#     fptr.close()
