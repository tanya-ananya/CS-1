class Number:
  def __init__(self, number):
    self.number = number

  def __str__(self):
    return str(self.number)

  def __add__(self, other):
    return Number(self.number + other.number)

  def __sub__(self, other):
    return Number(self.number - other.number)

  def __mul__(self, other):
    return Number(self.number * other.number)

  def __truediv__(self, other):
    return Number(self.number / other.number)

num1 = Number(25)
num2 = Number(5)
num3 = Number(11)

string = num1.__str__()
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
all = ((num1 + num2) - num3) * num2 / num3

print(string)
print(f'{num1} + {num2} = {add}')
print(f'{num1} - {num2} = {sub}')
print(f'{num1} * {num2} = {mul}')
print(f'{num1} / {num2} = {div}')
print(f'({num1} + {num2} - {num3}) * {num2} / {num3} = {all}')