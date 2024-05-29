# 內容
# 還記得計算機概論嗎？還記得二進位嗎？

# 現在我們來計算一下將一個10進位的數字換成二進位數字

 

# 輸入說明
# 輸入若干行直到 EOF 為止。每一行包含一個十進位的整數

 

# 輸出說明
# 針對每一行的整數輸出其二進位制的結果

# 範例輸入 #1
# 3
# 6
# 範例輸出 #1
# 11
# 110

# X=int(input())
# Y=X/2
# Z=X%2
# while(Z==0):
#     print(0)
# Y=Y/2

from sys import stdin

for read in stdin:
    n=int(read)
    print(bin(n)[2:]) 

# data=input()
# for read in data:
#     n=int(data)
#     print(bin(n)[2:])