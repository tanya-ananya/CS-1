scrabble_dict = {
  'A': 1,
  'B': 3,
  'C': 3,
  'D': 2,
  'E': 1,
  'F': 4,
  'G': 2,
  'H': 4,
  'I': 1,
  'J': 8,
  'K': 5,
  'L': 1,
  'M': 3,
  'N': 1,
  'O': 1,
  'P': 3,
  'Q': 10,
  'R': 1,
  'S': 1,
  'T': 1,
  'U': 1,
  'V': 4,
  'W': 4,
  'X': 8,
  'Y': 4,
  'Z': 10
}

def word_points(user_input, scrabble_dict):
    points = 0
    for x in user_input.upper():
        if x in scrabble_dict:
            points += scrabble_dict[x]
    return points
    
while True:
  user_input = input()
  if user_input.lower() == 'q' or user_input.lower() == 'quit':
      break
  total_points = word_points(user_input, scrabble_dict)
  print(f'{user_input.upper()} is worth {total_points} points.')