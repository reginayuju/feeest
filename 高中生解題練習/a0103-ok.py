'''
內容

各位在國小時都學過因數分解，都瞭解怎麼樣用紙筆計算出結果，現在由你來敎電腦做因數分解。

因數分解就是把一個數字，切分為數個質數的乘積，如 12=2^2 * 3

其中, 次方的符號以 ^ 來表示

輸入說明

輸入共一行。每行包含一個整數，符合 大於1 且 小於等於 100000000

輸出說明

針對每一行輸入整數輸出一個因數分解字串

標籤

╮(￣▽￣)╭
'''

number = input("請輸入一個數字:")
orgin_number = int(number)
number = int(number)
prime_number_list = []
ans_list = []
for _num in range(2, number + 1):
    isDivided = False
    for _p in prime_number_list:
        if (_num % _p == 0):
            isDivided = True
    if (isDivided == False):
        prime_number_list.append(_num)

for _p in prime_number_list:
    while (True):
        if (number % _p == 0):
            ans_list.append(_p)
            number = int(number / _p)
        else:
            break
print(ans_list)

ans_count = {}
count = 1
for i in range(0, len(ans_list)):
    ans_count[ans_list[i]] = ans_count[
        ans_list[i]] + 1 if ans_list[i] in ans_count else 1

print(ans_count)

ans_str = ""
for key, value in ans_count.items():

    if (value > 1):
        temp_str = str(key) + "^" + str(value)
    else:
        temp_str = str(key)

    ans_str = ans_str + temp_str + " * "

ans_str = ans_str[:-3]

print(ans_str)
