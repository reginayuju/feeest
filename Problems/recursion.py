# 1 1 2 3 5 8 13

# x = int(input())
# arr = [1, 1]
# for i in range(0, x - 2):
#     plus = arr[-1] + arr[-2]
#     arr.append(plus)
#     print(arr)


def f(x):
    if x == 1 or x == 2:
        return 1
    else:
        return f(x - 1) + f(x - 2)


print(f(9))
# for i in range(1, x+1):
#     print(f(i))
