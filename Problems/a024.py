# 內容
# 給定兩個整數，請求出它們的最大公因數

# 輸入說明
# 輸入包含兩個整數，以空白鍵隔開，兩個整數均 大於 0, 小於 

# 輸出說明
# 輸出兩個整數的最大公因數

# 範例輸入 #1
# 12 15
# 範例輸出 #1
# 3
# 範例輸入 #2
# 1 100
# 範例輸出 #2
# 1

a, b = map(int, input().split())
factor_a_list=[]
ans_list_a=[]
for a_num in range (2,(a+1)):
    isDivided=False
    for f_a in factor_a_list:
        if (a_num % f_a==0):
            isDivided=True
        if (isDivided=False):
            factor_a_list.append(a_num)
    for f in range (factor_a_list):
        while(True)
    if (a%f==0):
        ans_list_a.append(f)
        print(ans_list_a)
    


