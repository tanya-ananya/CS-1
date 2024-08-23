# Given a highway number, this program will indicate whether it is a primary, auxiliary highway or an invalid highway number

# User prompt for the number 
interstate_number = int(input('Please enter an interstate number: '))
even_or_odd = interstate_number % 2
print()
# if statements to indicate the type of highway 
if 1 <= interstate_number <= 99 and even_or_odd == 1:
    print(f'I-{interstate_number} is primary, going north/south.')
elif 1 <= interstate_number <= 99 and even_or_odd == 0:
    print(f'I-{interstate_number} is primary, going east/west.')
elif 100 <= interstate_number <= 999:
    if interstate_number % 100 == 0 :
        print(f'{interstate_number} is not a valid interstate highway number')
    else:
        if even_or_odd == 1:
            print(f'I-{interstate_number} is auxiliary, serving I-{interstate_number%100} going north/south.')
        elif even_or_odd == 0:
            print(f'I-{interstate_number} is auxiliary, serving I-{interstate_number%100} going east/west.')
print()