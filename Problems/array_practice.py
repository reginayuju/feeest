import numpy as np

a_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 印出反向

print(a_array[-1::-1])

# 印出 正向 每2個數字印一次

print(a_array[0:9:2])

# 印出 反向 每兩個數字印一次

print(a_array[-1:-10:-2])

b_array = [[1, 2, 3], [1, 2, 3]]
print(np.array(b_array).shape)
# shape [2][3]
# 1 2 3
# 1 2 3

c_array = [b_array, b_array, b_array, b_array]

print(np.array(c_array).shape)
print(c_array[2][1][1])

d_array = [c_array, c_array, c_array, c_array, c_array]
print(np.array(d_array).shape)


shape (row , col, channel)


class 


function
