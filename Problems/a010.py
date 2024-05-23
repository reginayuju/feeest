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

number = input()
number = int(number)
prime_number_list = []
for _num in range(2, number + 1):
    # p = list(>=number, number[n]/number[n-1])

    print(_num)

    isDivided = False

    for _p in prime_number_list:
        print(_p)
        if (_num % _p == 0):
            isDivided = True
        print(isDivided)

    if (isDivided == False):
        prime_number_list.append(_num)

    print(prime_number_list)

    # a =_num[n]/num[n+1]
    # if a!=0:
    # print(a)
