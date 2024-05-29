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
# print(a,b)
a_list = []
b_list = []
factor_a_list = []
factor_b_list = []
ans_list = []
for a_num in range(2, (a + 1)):
    isDivided = False
    for _a in a_list:
        if (a_num % _a == 0):
            isDivided = True
    if (isDivided == False):
        a_list.append(a_num)
# print("AAAAA", a_list)

for ia in a_list:
    while (True):
        if (a % ia == 0):
            ans_list.append(ia)
            a = int(a / ia)
            # print("EEEE",a)
        else:
            break
        # print(ans_list)
for d in range (len(ans_list)):
    # print(d)
    # print(int(len(ans_list)))
    result=1
    # if (d + 1) < len(ans_list):
    result=result*ans_list[d]
    print(result)
    # else:
    #     break
# for ia in a_list:
#     if (a % ia == 0):
#         factor_a_list.append(ia)
#         a = int(a/ia)
#         print("FFFF",a)
#     else:
#         break

#     print(factor_a_list)

# print("BBBBB", factor_a_list)
# for b_num in range(2, (b + 1)):
#     isDivided = False
#     for _b in b_list:
#         if (b_num % _b == 0):
#             isDivided = True
#     if (isDivided == False):
#         b_list.append(b_num)
#         # print("CCCCC", b_list)
# for ib in b_list:
#     if (b % ib == 0):
#         factor_b_list.append(ib)
# print("DDDDD", factor_b_list)
# for fa in factor_a_list:
#     # print("C",fa)
#     for fb in factor_b_list:
#         # print("D",fb)
#         if (fa==fb):
#             ans_list.append(fa)
#             print(ans_list)
#     factor_b_list.remove(fa)
#     print(factor_b_list)
#     print(ans_list)

#     # print(a_num)
#     if (a%a_num==0):
#         factor_a_list.append(a_num)
#         # print("A",factor_a_list)
# for b_num in range(2,(b+1)):
#     # print(a_num)
#     if (b%b_num==0):
#         factor_b_list.append(b_num)
#         # print("B",factor_b_list)
# for ia in factor_a_list:
#     # print("C",ia)
#     for ib in factor_b_list:
#         # print("D",ib)
#         if (ia==ib):
#             ans_list.append(ia)
#             # print(ans_list)
#             factor_b_list.remove(ia)
#             # print(factor_b_list)
#             # print(ans_list)

# for ib in factor_b_list:

#     isDivided=True
#     for f_a in (factor_a_list):
# #         if (a_num % f_a==0):
# #             isDivided=True
# #             factor_a_list.append(a_num)
# #         if (isDivided==False):
# #             break
# print(factor_a_list)
# for b_num in range (2,(b+1)):
#     isDivided=True
#     for f_b in (factor_b_list):
#         if (a_num % f_b==0):
#             isDivided=True
#             factor_b_list.append(b_num)
#         if (isDivided==False):
#             break

# for ia in factor_a_list:
#     print(ia)

# if factor_a_list[ia]==factor_b_list[]:
#     ans_list.append()
