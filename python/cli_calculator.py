print("Welcome to the CLI Calculator")
print("Hint: input 'help' to get list of commands or 'start' to start the calculator.")

while True:
    start = input('Enter a command (help / start): ').lower()

    if start == 'help':
        print("""
            input any of these in the operator section [+, -, /, *, %]
            '+' = addition,
            '-' = subtraction,
            '/' = division,
            '*' = multiplication,
            '%' = modulus.
        """)
    elif start != 'help' and start != 'start':
        print("Invalid command, Use 'help' command to check the command list")
        break

    try:
        first_number = float(input("Enter first number: "))
        operator = input("Operator: ")
        second_number = float(input("Enter second number: "))
    except ValueError:
        print('This is a calculator, use numbers not letters')
        break

    if operator == '+':
        print(f'{first_number} {operator} {second_number} =', first_number + second_number)
    elif operator == '-':
        print(f'{first_number} {operator} {second_number} =', first_number - second_number)
    elif operator == '/':
        print(f'{first_number} {operator} {second_number} =', first_number / second_number)
    elif operator == '*':
        print(f'{first_number} {operator} {second_number} =', first_number * second_number)
    elif operator == '%':
        print(f'{first_number} {operator} {second_number} =', first_number % second_number)
    else:
        print('Invalid command, Try again\n')
    break
