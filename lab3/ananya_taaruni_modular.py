import math
import random

radius = int(input('Please enter the radius of the sphere: '))

volume = float((4/3)*math.pi*math.pow(radius,3))

random_number = random.randint(1,10)

print('The volume of a sphere with radius of', radius, f'is {volume:.2f}')
print()
print('The factorial of', random_number, 'is', math.factorial(random_number))