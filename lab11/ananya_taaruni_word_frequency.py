'''This program will create a bag of words from the user's input
Author: Taaruni Ananya'''

def build_dictionary(word_list):
  word_number = {}
  for word in word_list:
      word = word.lower()
      if word in word_number:
          word_number[word] += 1
      else:
          word_number[word] = 1
  return word_number

sentence = input('')
words = sentence.split()
word_number_dict = build_dictionary(words)

print()
print('Word list:\n', words)
print()
print('Bag of Words: ')
for key in sorted(word_number_dict.keys()):
  print(f'{key} - {word_number_dict[key]}')