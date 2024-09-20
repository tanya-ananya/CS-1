class NegativeValueError(Exception):
  pass

def steps_to_miles(steps):
  try:
      steps = int(steps)
  except ValueError:
      raise ValueError("Exception: Non-Numeric Value Entered.")

  if steps < 0:
    raise NegativeValueError('Exception: Non-Numeric Value Entered.')

  miles = steps / 2000
  return miles

while True:
    try:
      steps = input("Enter # of steps: ")
      if steps.lower() == 'quit':
        break
      miles = steps_to_miles(steps)
      print(f'{miles:.2f} miles.')
    except (ValueError, NegativeValueError) as excpt:
      print(excpt)

