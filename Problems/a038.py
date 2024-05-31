# 方法1
n = input()

b = n[-1::-1]
print(int(b))

# n [開始:結束:公差]
# n[-1::]

# 方法2
# n = input()
# for i in range(-1, -1 * (len(n) + 1), -1):
#     if n[i] != "0":
#         break
# print(n[i::-1])
