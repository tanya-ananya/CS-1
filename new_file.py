'''
This program will implement a calculator in the terminal 
by accepting inputs and operators from the user and returning
the solution.

Author: Taaruni Ananya
'''
print()
#First, the prompt:
print("Please enter an Expression:\n")

while True:
    expression = input()

    if expression.lower() == 'q' or expression.lower() == 'quit':
        break
    else:
        expression = expression.split()

        if len(expression) != 3:
            print(f'Error: Invalid Expression - ({expression})')
            continue
        else:
            left_hand = int(expression[0])
            operator = expression[1]
            right_hand = int(expression[2])

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