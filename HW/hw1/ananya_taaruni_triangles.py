import math
"""
This program will take the user's input of three sides of a triangle and calculate:
the perimeter, area, and type

Author: Taaruni Ananya
CRN: 20388
"""

# User input for the sides of the triangle
side_A = int(input('Please enter the length of side A of the triangle (in meters): '))
side_B = int(input('Please enter the length of side B of the triangle (in meters): '))
side_C = int(input('Please enter the length of side C of the triangle (in meters): '))

# Calculations
perimeter = side_A + side_B + side_C
semi_perimeter = (perimeter)/2
area = math.sqrt(semi_perimeter*(semi_perimeter-side_A)*(semi_perimeter-side_B)*(semi_perimeter-side_C))

# Calculating and determining the type of triangle presented
left_side = math.pow(side_A, 2) + math.pow(side_B, 2)
right_side = math.pow(side_C, 2)

if left_side == right_side:
    triangle_type = 'Right Triangle'
elif left_side > right_side:
    triangle_type = 'Acute Triangle'
elif left_side < right_side:
    triangle_type = 'Obtuse Triangle'

print()
print(f'The perimeter of the triangle is {perimeter}m')
print(f'The area of the triangle is {area:.2f}m^2')
print(f'It is a {triangle_type}.')
print()