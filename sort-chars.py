def main():
    vowels = []
    consonants = []
    integers = []
    others = []
    spaces = 0

    all_vowels = 'AEIOUaeiou'
    all_consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnopqrstvwxyz'
    all_ints = '0123456789'

    string = input('> ')

    for char in string:
        if char in all_vowels:
            vowels.append(char)
        elif char in all_consonants:
            consonants.append(char)
        elif char in all_ints:
            integers.append(char)
        elif char == ' ':
            spaces += 1
        else:
            others.append(char)

    print(f'Vowels:      {vowels}')
    print(f'Consonants:  {consonants}')
    print(f'Integers:    {integers}')
    print(f'Other Chars: {others}')
    print(f'{spaces} spaces')

if __name__ == "__main__":
    main()
