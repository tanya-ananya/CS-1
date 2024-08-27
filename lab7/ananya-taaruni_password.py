print()
initial_password = input('Please Enter Your Password: ')

new_password = ''
for letter in initial_password:
    if letter == 'o':
        new_password += '0'
    elif letter == 'i':
        new_password += '1'
    elif letter == 'a':
        new_password += '@'
    elif letter == 'e':
        new_password += '3'
    elif letter == 'A':
        new_password += '4'
    elif letter == 'B':
        new_password += '8'
    elif letter == 's':
        new_password += '$'
    else:
        new_password += letter

print(f'{new_password}!')
print()