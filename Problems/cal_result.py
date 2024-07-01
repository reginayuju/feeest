import numpy as np


def func_button_RESULT(input_text):
    answer = 0
    bracket_list = []

    for i in range(len(input_text)):
        if input_text[i] == "+":
            print(int(input_text[i - 1]) + int(input_text[i + 1]))
        if input_text[i] == "(" or input_text[i] == ")":
            bracket_list.append(i)
            # print(bracket_list)
        if input_text[i] == "+":
            print(
                int(input_text[bracket_list[i - 1]]) +
                int(input_text[bracket_list[i + 1]]))

    return answer


if __name__ == '__main__':
    # input_text = "((1+5)/(2+1))*(5+5)"
    # input_text = "(1+5)/2"

    input_text = "12+31"
    input_text = "13+144+144+111+233+443"
    input_text = "122-244+31-433"
    input_text = "155+331*231/3"

    answer = func_button_RESULT(input_text)
    # print(answer)
