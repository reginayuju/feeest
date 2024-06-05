# 內容
# 考慮以下的演算法：

# 1.         輸入 n
# 2.         印出 n
# 3.         如果 n = 1 結束
# 4.         如果 n 是奇數 那麼 n=3*n+1
# 5.         否則 n=n/2
# 6.         GOTO 2

# 例如輸入 22, 得到的數列： 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

# 據推測此演算法對任何整數而言會終止 (當列印出 1 的時候)。雖然此演算法很簡單，但以上的推測是否真實卻無法知道。然而對所有的n ( 0 < n < 1,000,000 )來說，以上的推測已經被驗證是正確的。

# 給一個輸入 n ,透過以上的演算法我們可以得到一個數列（1作為結尾）。此數列的長度稱為n的cycle-length。上面提到的例子, 22 的 cycle length為 16.

# 問題來了：對任2個整數i，j我們想要知道介於i，j（包含i，j）之間的數所產生的數列中最大的 cycle length 是多少。
# 輸入說明
# 輸入可能包含了好幾列測試資料，每一列有一對整數資料 i，j 。 0< i，j < 1,000,000
# 輸出說明
# 對每一對輸入 i , j 你應該要輸出 i, j 和介於 i, j 之間的數所產生的數列中最大的 cycle length。
# 範例輸入 #1
# 1 10
# 10 1
# 100 200
# 201 210
# 900 1000
# 範例輸出 #1
# 1 10 20
# 10 1 20
# 100 200 125
# 201 210 89
# 900 1000 174

i, j = map(int, input().split())
list = []
if i <= j:
    for n in range(i, j + 1):
        # print("RRRRRR",n)

        count = 1
        while (n > 1):
            # print("ZZZZ", n)
            if (n % 2 != 0):
                n = n * 3 + 1
                # print("AAA",n)
            else:
                n = n / 2
                # print("BBB", n)
            count = count + 1
        list.append(count)
    # print("WWW",count)
# print(list)
# print(max(list))
    print(i, j, max(list))
    # print(n)
    # max = max(int(count))
    # print(max)
if i > j:
    for n in range(j, i + 1):
        # print("RRRRRR",n)

        count = 1
        while (n > 1):
            # print("ZZZZ", n)
            if (n % 2 != 0):
                n = n * 3 + 1
                # print("AAA",n)
            else:
                n = n / 2
                # print("BBB", n)
            count = count + 1
        list.append(count)
    # print("WWW",count)
# print(list)
# print(max(list))
    print(i, j, max(list))
    # print(n)
    # max = max(int(count))
    # print(max)
