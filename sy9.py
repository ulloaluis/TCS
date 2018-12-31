import random

# simple 9lives program

## https://www.codementor.io/garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz

# constants
HEART = '❤  '
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane', 'dog', 'cat']

# code
num_lives = int(input("How many lives do you want? "))
secret_word = random.choice(words)
word_to_print = ['?']*len(secret_word)


word_not_guessed = True
while num_lives > 0 and word_not_guessed:
  guess = input('Guess a letter or the whole word: ')

  if len(guess) == 1:  # entered a letter
    guessed_at_least_one = False
    for i, letter in enumerate(secret_word):
      # guess = 'X'
      if letter == guess: # they guessed one of the letters!
        guessed_at_least_one = True
        word_to_print[i] = letter 

    if not guessed_at_least_one:
      num_lives -= 1
      print(guess, 'is not in the secret word.')


  elif guess == secret_word: # entered correct word
      word_not_guessed = False
      word_to_print = secret_word
  else:              # entered wrong word
    num_lives -= 1      # num_lives = num_lives - 1
    print(guess, 'is not the secret word.')
  
  print(word_to_print) # C A T
  print(HEART*num_lives)
  print()
  


if not word_not_guessed:
  print('You won! The secret word was', secret_word)
else:
  print('You lost! The secret word was', secret_word)




