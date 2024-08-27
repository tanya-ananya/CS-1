print()
string = input('Please Enter Your String: ')


while string != 'Quit' or 'quit' or 'q':
    reversed = ''
    for x in range(len(string) -1, -1, -1):
        reversed += string[x]
    print(f'Reversed: {reversed}')
    break

print()