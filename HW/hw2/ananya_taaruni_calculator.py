'''
This program will implement a calculator in the terminal by accepting inputs and operators from the user and returning
the solution.

Author: Taaruni Ananya
'''

# First, the prompt:
print("Please enter an Expression:\n")

# A while loop is used to allow the user to enter as many expressions as needed until they quit
while True:
    expression = input()

    # Checks to see if the user wants to quit the program
    if expression.lower() == 'q' or expression.lower() == 'quit':
        break

    # Splits the expression for better assignment of values and identification of operators
    expression = expression.split()

    # Checks to see if the entered input fits expression requirements
    if len(expression) != 3:
        print(f'Error: Invalid Expression - ({expression})')
        print()
        continue
    else:
        # Assignment of values for cleaner and easier code to identify the operator and perform calculations
        left_hand = int(expression[0])
        operator = expression[1]
        right_hand = int(expression[2])

        # if statements are used to identify the type of operator, perform the corresponding calculations, and output the result
        if operator == '+':
            result = left_hand + right_hand
            print(f'Result: {left_hand} + {right_hand} = {result}')
        elif operator == '-':
            result = left_hand - right_hand
            print(f'Result: {left_hand} - {right_hand} = {result}')
        elif operator == '*':
            result = left_hand * right_hand
            print(f'Result: {left_hand} * {right_hand} = {result}')
        elif operator == '/':
            result = left_hand / right_hand
            print(f'Result: {left_hand} / {right_hand} = {result}')
        elif operator == '%':
            result = left_hand % right_hand
            print(f'Result: {left_hand} % {right_hand} = {result}')
        elif operator == '**':
            result = left_hand ** right_hand
            print(f'Result: {left_hand} ** {right_hand} = {result}')
        elif operator == '//':
            result = left_hand // right_hand
            print(f'Result: {left_hand} // {right_hand} = {result}')
    print()
