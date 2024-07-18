# Python- lambda 函式
# 練習
# 求某數的平方
# def square(x):
# 	return x ** 2

square = lambda x:x**2
ANS = square(3)

# # 求兩數相加
# # def add_number(x,y):
# #     return x+ y

add_number = lambda x,y: x+y
ANS = add_number(3,5)

ANS = (lambda x,y : x+y)(3,5)

# if條件判斷
# def abs_number(x):
#     if x > 0:
#         return x
#     else:
#         return -x
    
ANS = lambda x: x if x >= 0 else -x

