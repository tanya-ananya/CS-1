print()
phone = int(input('Please enter your phone number: '))
print()

last_digits = phone % 10000
area_code = phone // 10000000
middle_digits = (phone // 10000) % 10000
print(f'({area_code}){middle_digits}-{last_digits}')
print()