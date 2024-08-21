#This program will take the quantity of inputed items by the user and print the sum using a dictinary 

#the dictionry storing the values
food_dict = {'Hot Dog':1.50, 'Slice of Pizza':1.99, 'Whole Pizza':9.95, 'Soft Drink':0.59}

#input items
hot_dog = int(input('Please enter the number of Hot Dogs: '))
pizza_slices = int(input('Please enter the number of Pizza Slices: '))
whole_pizza = int(input('Please enter the number of Whole Pizzas: '))
soft_drinks = int(input('Please enter the number of Soft Drinks: '))

#calculating the total cost
total_cost = (hot_dog * food_dict['Hot Dog']) + (pizza_slices * food_dict['Slice of Pizza']) + (whole_pizza * food_dict['Whole Pizza']) + (soft_drinks * food_dict['Soft Drink'])
print()
print(f'The total cost is {total_cost:.2f}')
print()