# 內容
# 輸入任意數字，並將其數字全部倒轉

 

# 輸入說明
# 輸入一行包含一個整數，且不超過 

# 輸出說明
# 輸出翻轉過後的數字

# 範例輸入 #1
# 12345
# 範例輸出 #1
# 54321
# 範例輸入 #2
# 5050
# 範例輸出 #2
# 505


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
