import math
#This program will take the user's input of driving speed in miles per hour (mph) and speed limit, then it will output the traffic ticket amount.

speed_limit = int(input('Please enter the speed limit for the road: '))
vehicle_speed = int(input("Please enter the vehicle's recorded speed: "))

speed_difference = abs(vehicle_speed - speed_limit)

if 5 < speed_difference <= 10:
    print('The speeding fine is $50.')
elif 6 <= speed_difference <= 20:
    print('The speeding fine is $75.')
elif 21 <= speed_difference <= 40:
    print('The speeding fine is $150.')
elif speed_difference > 40:
    print('The speeding fine is $300.')
else:
    print('There is no fine.')