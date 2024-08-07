cents = int(input('Please enter a number of cents: '))

quarters = int(cents//25)
cents %= 25

dimes = int(cents//10)
cents %= 10

nickels = int(cents//5)
cents %= 5

pennies = int(cents//1)
cents %= 1

print('Coins:', quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels,', pennies, 'pennies')