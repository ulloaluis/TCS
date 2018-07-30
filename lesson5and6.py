# ------- if statements ------
# if expression:
#   statements...
# elif expression:
#   statements...
# else:
#   statements...

# ------- for loops -------
# for i in range(a, b):
#   statements...

# array = [1, 2, 3]
# for number in array:
#   statements...
 
# ------- while loops -------
# while expression:
#   statements...

#  --------------------------
  
# Today's schedule
# Finish up yesterday's stuff 15-30 minutes
# New stuff - rest of lesson
#   functions 
  
# def sum(x, y):
#   return x+y
  
  
# From last lesson / review / going over it
# -------------------------------

# Take in two user inputs. The first is a string s and the second is an integer n.
# Print the string n amount of times, on separate lines.

# str = "dog"
# n = 5
# dog
# dog
# dog
# dog
# dog
str = input("enter a string pls: ") # variable
n = int(input("enter a number n: "))
for i in range(0, n + 1):
  print(str) 

print(str * n)  # dogdogdogdogdog



    
# Given a user input of an integer, if it is even, print it and allow them to
# enter another integer. If it's odd, stop allowing them to enter anything. 

# n = int(input('enter an integer here: ')) # n = 2
# while n % 2 == 0:           # x == 0 yeah, if n%2 == 1 then it's odd
#   print(n)                 # 4
#   print('play again')      # play again
#   n = int(input("enter a new integer: ")) # ask for another number

# print("done")
    
    
# x = 0 # x will be a variable that has the value 0
#   = 
# while x == 0: # test for equality 
  
    
  
# n = 0
# while n < 5:   # can think of as an if statement that keeps going until it's false
#   print(n)
#   n = n + 1
    
# n = int(input('enter an integer here: '))    



    
# The user enters a word and a number n. 
# You print their word concatenated n amount of times and then allow them to type 
# another word and number.

# This continues until they enter the word "stop", which is 
# --case insensitive, so they could enter "sToP" or "STOP" or "stop", etc.

# x = input(int('enter a value here: '))
# y = input('enter a word here: ') # "dog"      print(y) . # dog   print("y") # y

# while y != 'stop': # updating x doesn't affect this aprt, and we're only doing it bcuz the problem wants us to
#   print(y * x) 
#   x = input("enter another value: ")
#   y = input('enter another word: ')

# print('done')
  
  
# while expression:   # 1 . 4 . 7 11 15 19 ...
#   print("a")        # 2 . 5 . 8
#   print("b")        # 3 . 6 . 9
  
  
# CONCATENATION: "DOG"+"CAT" = "DOGCAT", "SPIDER"+"PIG"="SPIDERPIG" 
#           "dog"*2 --> "dog"+"dog" = "dogdog" 
#           "dog"*3 --> "dogdogdog"
#       Fancy word for adding strings together
      


    
    
# infinite loops --> the unseen killer bug
    
while expression-that-is-always-true:
  statements...
    
n = 0 # 0
while n >= 0: # True  1 >= 0 2>= 0
  print(n)   # 0 # 1
  n = n + 1 # 1 # 2
# doesn't stop outputting things because the expression is always true
    
    
    
# n = 0
# while n < 134014091304901934: 
#   n = n + 1 
# # takes like 5 seconds to do it (prob not)
    
    
    
# -------- new -------- functions
    
    
Sometimes you want to run code that does a specific thing multiple times 
in a single program, but you don't want to keep writing the code for it
over and over. However, unlike a loop you want to be able to run this 
code at specific times and not just over and over again. This is where functions are important.
    
# syntax
# def function_name(parameters):
#   statements...
    
    
# a simple example
  # add two numbers together
    
# we could do
x = 1
y = 1
sum = x + y

# but then if we wanted to add two numbers together later on you would have to keep writing
# variable_1 + variable_2
    
# could instead write a function that adds two numbers together, and then call that at certain times
def sum(x, y):
  return x + y 

# a =['a', 'b']
# b= ['a', 'c']
# z = sum(a, b)
    
x = 1
y = 1
z = sum(x, y)

a = 123
b = 51
c = sum(a, b)


print("adadd") 

int("11")


  
    
# Typically, you wouldn't write a sum() function since it's such a small piece of code,
# but functions are still also a way to clarify what's happening
  
# say you didnt want to take the sum of x and y but instead wanted to multiple them together
# and then divide by 1.073 and then raise that to power of 7, that's not something you'd want to keep 
# rewriting since chances are you'd get it wrong in one of those attempts. Also, it's best to write
# functions to avoid repeating code, but you could also use it to break apart the program flow.

  
  
# algorithmic thinking
# breaking apart the big problem into smaller problems
# pseudo code


# hangman game

def initialize_interface(word):
  draw_pot()
  add_lines(word)

  
  
word = get_random_word()
intialize_interface(word)   # . _ _ _ _ _ _        u
wrong_guesses = 0
while wrong_guesses < 7: 
  guess = prompt_user_for_guess()
  if correct_guess(guess, word):
    add_letter_to_screen(word, letter)
  else:
    wrong_guesses += 1
  
if wrong_guesses >= 7: 
  print("you lose")
else:
  print("you win")
  
  
  
# Example
initialize_game()
run_game()
while game_is_running:
  play_game()
display_game_over()
    
# let's pretend each of those functions are already written for us
# in this case, we didn't re-use some things very often (like initialize_game)
# but they were useful in clarifying the structure of the program
    
    
# ...


# Example problems 

def function_name(temp): # function
  print(temp) # R2D2

  
# name("R2D2")     # calling that function
  
  
Write a function that prints "Hello World" when you call it

def hello():
  print("Hello World")
hello()


def speech(line):
  print(line)

speech("R2D2") # R2D2
  
  
# Write a function that accepts a list from the user and then prints
# all of the elements in the list to the screen


def print_list(list):
  for x in list:
    print(x)

def element_list(list):
  print(list)
  
  



# Write a function that takes in a number (n) and a string (str) and then
# prints that string n amount of times.


def print_n_times(n, str): 
  asdadasd....as
  adsalkdmasdk
  
  
# Write a function that accepts two numbers and then returns the product of two numbers squared. 
# 5 and 5, (5*5)**2 (a and b)

def do_math(a, b):
  asdklaldksalkdmsad
  return sklamdklsamdalksd




  
