all_letters = 'abcdefghijklmnopqrstuvwxyz'
all_digits = '0123456789'
all_operators = '+-*/^'
whitespace = ' \t\n'

digits = []
operators = []

while True:
    expression = input('> ')

    if expression == 'done':
        break

    for token in expression:
        if token in all_digits:
            digits.append(token)
        elif token in all_operators:
            operators.append(token)
        elif token in whitespace:
            pass
        elif token in all_letters:
            raise Exception('This is a calculator...?')
        else:
            raise Exception(f"Unknown token: '{token}'")

print(digits)
print(operators)
