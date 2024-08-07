age = int(input('Please enter your age: '))
weight = int(input('Please enter your weight in pounds: '))
heart_rate = int(input('Please enter your heart rate in beats per minute: '))
time = int(input('Please enter the length of your workout in minutes: '))

calories = float((((age*0.2757+weight*0.03295+heart_rate*1.0781-75.4991)*time)/8.368))

print()
print(f'Calories burned: {calories:.2f} calories')