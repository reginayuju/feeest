def camelcase(s):
    str = s.split(';')
    A = str[0]
    B = str[1]
    C = str[2]
    upper_index_list = [0]
    word_list = []
    if A == "S":
        if B == "M" or B == "V":
            ans = C[:-2]
            for i in range(len(ans)):
                if ans[i].isupper():
                    upper_index_list.append(i)
            upper_index_list.append(len(ans))
            for i in range(len(upper_index_list) - 1):
                word_list.append(
                    ans[upper_index_list[i]:upper_index_list[i + 1]].lower())
            print(' '.join(word_list))
        if B == "C":
            upper_index_list = []
            word_list = []
            for i in range(len(ans)):
                if ans[i].isupper():
                    upper_index_list.append(i)
            upper_index_list.append(len(ans))
            for i in range(len(upper_index_list) - 1):
                word_list.append(
                    ans[upper_index_list[i]:upper_index_list[i +1]].lower())
            print(' '.join(word_list))

    if A=="C":
        if B == 'V':
            content = content.split(' ')
            word_list = []
            word_list.append(content[0])
            for i in range(1, len(content)):
                word_list.append(content[i].capitalize())
            print(''.join(word_list))
        if B == 'C':
            content = content.split(' ')
            word_list = []
            for i in range(len(content)):
                word_list.append(content[i].capitalize())
            print(''.join(word_list))
        if B == 'M':
            content = content.split(' ')
            word_list = []
            word_list.append(content[0])
            for i in range(1, len(content)):
                word_list.append(content[i].capitalize())
            print(''.join(word_list) + '()')


if __name__ == '__main__':
    while True:
        try:
            s = input()
            camelcase(s)
        except EOFError:
            break

# plasticCup()
# plastic cup
