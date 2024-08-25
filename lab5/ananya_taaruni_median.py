# This program takes in three integers and outputs the median value (not the largest or smallest value).

#user input of numbers 
first_number = int(input('Please enter the first number: '))
second_number = int(input('Please enter the second number: '))
third_number = int(input('Please enter the third number: '))
print()
if first_number < second_number < third_number:
    print(f'The median number is {second_number}')
elif first_number < third_number < second_number:
    print(f'The median number is {third_number}')
elif second_number < first_number < third_number:
    print(f'The median number is {first_number}')
elif second_number < third_number < first_number:
    print(f'The median number is {third_number}')
elif third_number < first_number < second_number:
    print(f'The median number is {first_number}')
elif third_number < second_number < first_number:
    print(f'The median number is {second_number}')