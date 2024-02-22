def export_input_number(string: str, operator):
    # ['55', '-558']
    return string.split(operator)


def check_is_numeric(string: str) -> bool:
    return string.isnumeric()


def check_is_calculator_input(a: str, b: str) -> bool:
    return check_is_numeric(a) and check_is_numeric(b)


user_input = input()  # 55/-558
if '+' in user_input:
    a, b = export_input_number(user_input, '+')  # a = '5' , b = '5'
    if check_is_calculator_input(a, b):
        a, b = list(map(int, [a, b]))
        print(a + b)

elif '*' in user_input:
    a, b = export_input_number(user_input, '*')

    if check_is_calculator_input(a, b):
        print('test')
        a, b = list(map(int, [a, b]))
        print(a * b)
elif '/' in user_input:
    a, b = export_input_number(user_input, '/')
    if check_is_calculator_input(a, b):
        a, b = list(map(int, [a, b]))
        print(a / b)
elif '-' in user_input:
    a, b = export_input_number(user_input, '-')
    if check_is_calculator_input(a, b):
        a, b = list(map(int, [a, b]))
        print(a - b)
else:
    print('Unsupported operator')
