def infix_to_postfix(expression):
    # 定義運算符的優先級
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit() or expression[i] == '.':  # 處理數字和小數點
            num = []
            while i < len(expression) and (expression[i].isdigit()
                                           or expression[i] == '.'):
                num.append(expression[i])
                i += 1
            output.append(''.join(num))
        elif expression[i] == '(':  # 左括號直接入堆疊
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':  # 遇到右括號，將堆疊中的運算符彈出直到遇到左括號
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # 彈出左括號
            i += 1
        else:  # 處理運算符
            while (operators and operators[-1] in precedence
                   and precedence[operators[-1]] >= precedence[expression[i]]):
                output.append(operators.pop())
            operators.append(expression[i])
            i += 1

    while operators:  # 將剩餘的運算符彈出
        output.append(operators.pop())

    return output


def evaluate_postfix(postfix_expression):
    stack = []

    for token in postfix_expression:
        if token.isdigit() or '.' in token:  # 處理數字
            stack.append(float(token))
        else:  # 處理運算符
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack[0]


def calculate_expression(expression):
    postfix_expression = infix_to_postfix(expression)
    return evaluate_postfix(postfix_expression)


# 範例使用
# expression = "((1+5)/(2+1))*(5+5)"
expression = "((1.999+4.001)/(2+1))*(5+5)"
result = calculate_expression(expression)
print(f"Result: {result}")


# 1+5+6+7

# stack  [1, +, 5, +, 6, +, 7]

# stack  [1, +, 5, +, 13]

# stack  [1, +, 18]

# stack  [19]