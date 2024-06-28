def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return str(e)


# 範例使用
expression = "((1+5)/(2+1))*(5+5)"
result = calculate_expression(expression)
print(f"Result: {result}")
