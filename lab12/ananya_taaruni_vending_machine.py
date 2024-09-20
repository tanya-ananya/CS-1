class VendingMachine:
  def __init__(self, soda, water, coffee):
    self.soda = soda
    self.water = water
    self.coffee = coffee
  
  def vending(self, drink):
    if drink == 1:
      if self.soda > 0:
          self.soda -= 1
      else:
          return "Soda out of stock."
    elif drink == '2':
      if self.water > 0:
          self.water -= 1
      else:
          return "Water out of stock."
    elif drink == '3':
      if self.coffee > 0:
          self.coffee -= 1
      else:
          return "Coffee out of stock."
    else:
      return "Invalid drink type."
  
  def restock(self, drink, num_restocked):
    if drink == 1:
        self.soda += num_restocked
    elif drink == 2:
        self.water += num_restocked
    elif drink == 3:
        self.coffee += num_restocked
  
  def inventory_print(self):
    print('Inventory')
    print(f'Soda: {self.soda} bottles')
    print(f'Water: {self.water} bottles')
    print(f'Coffee: {self.coffee} bottles')

machine = VendingMachine(10, 10, 10)

while True:
  command = input().lower()
  if command == 'q' or command == 'quit':
    break
  elif command == 'buy':
    print('Please select an option:')
    print('1 - Soda')
    print('2 - Water')
    print('3 - Coffee')
    drink = int(input())
    machine.vending(drink)
  elif command.lower() == 'restock':
    print('Please select an option:')
    print('1 - Soda')
    print('2 - Water')
    print('3 - Coffee')
    drink = int(input())
    number = int(input('Please enter an amount:\n'))
    machine.restock(drink, number)
  elif command == 'inventory':
    machine.inventory_print()
    