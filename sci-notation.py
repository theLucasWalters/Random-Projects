# python program to convert numbers into scientific notation

# conversion function
def convert(num: float):
    conversion_count = 0

    if num >= 10:
        while num >= 10:
            num /= 10
            conversion_count += 1

    elif num < 1:
        while num < 1:
            num *= 10
            conversion_count -= 1

    else:
        return "The number doesn't need to be converted.", f"{num} * 10^{conversion_count}"

    return f'{num} * 10^{conversion_count}'

# main function
def main():
    number = float(input('Enter a number to convert > '))

    assert type(number) == float, "Must be a number, cannot include letters or symbols."

    print(convert(number))

if __name__ == "__main__":
    main()
