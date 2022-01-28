all_letters = 'abcdefghijklmnopqrstuvwxyz'
all_digits = '0123456789'
all_operators = '+-*/^'
whitespace = ' \t\n'

digits = []
operators = []

while True:
    print("Type 'done' when you're finished.")
    text = input('> ')

    if text == 'done':
        break
    elif text == 'help':
        print("Help")

    for token in text:
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
