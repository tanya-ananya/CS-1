print()
values = int(input('Please enter the number of floating-point values: '))

list_values = []
for x in range(values):
    list_append = float(input('Please enter a floating-point value: '))
    list_values.append(list_append)

print()
print('Normalized Floating-Point Values: ')
for list_append in list_values:
    list_append = list_append / max(list_values)
    print(f'{list_append:.2f}')
