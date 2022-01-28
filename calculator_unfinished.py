# constants
all_letters = 'abcdefghijklmnopqrstuvwxyz'
all_digits = '0123456789'
all_operators = '+-*/'
whitespace = ' \t\n'

digits = []
operators = []

def help():
    print(
        """
        COMMANDS        DESCRIPTION

        done            exits the program
        help            displays this menu
        clearall        clears the calculator's history
        showhistory     shows the calculator's history
        """
    )

def do_math(num1, num2, op):
    match op:
        case "+":
            print(int(num1) + int(num2))
        case "-":
            print(int(num1) - int(num2))
        case "*":
            print(int(num1) * int(num2))
        case "/":
            print(int(num1) / int(num2))

# run function
def run(text):
    # sort the tokens by type
    for token in text:
        if token in all_digits:
            digits.append(token)

        elif token in all_operators:
            operators.append(token)

        elif token in whitespace:
            pass

        elif token in all_letters:
            print("You can't use letters")

        else:
            print(f"Unexpected token: {token}")

    num1 = digits[len(digits) - 2]
    num2 = digits[len(digits) - 1]
    op = operators[len(operators) - 1]

    do_math(num1, num2, op)

# main function
def main():
    print("Type 'done' when finished or 'help' if you get stuck")

    while True:
        text = input("\n> ")

        # make sure these are served first
        match text:
            case "done":
                break

            case "help":
                help()

            case "clearall":
                digits.clear()
                operators.clear()
                print("History successfully cleared")

            case "showhistory":
                print(f"Digits:    {digits}")
                print(f"Operators: {operators}")

            case _:
                run(text)

if __name__ == "__main__":
    main()
