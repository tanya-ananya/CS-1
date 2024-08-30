import random

random_number = random.randrange(1,100)

print()
print('I have generated random number between 1 and 100. You will have 10 attempts to guess that number.')
print()

for x in range(1,11):
    guess = int(input(f'Guess {x}: '))
    if guess < random_number:
        print('Your guess is less than my random  number.')
    elif guess > random_number: 
        print('Your guess is larger than my random number')
    elif guess == random_number:
        print('You correctly guessed my random number.')
        break
else: 
    print()  
    print("You've run out of guesses")
