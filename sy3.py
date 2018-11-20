# x = 'dog'
# for letter in x:
#   print(letter)
#   # d o g

# for i in range(0, 5):
#   print(i)
  # prints 0 1 2 3 4

# while something_true:
#   do_something

# def im_a_function(im_an_argument):
#   do_something_with_argument
#   return can_return_stuff_with_stuff

# if expression:
#   do_this
# elif expression:
#   do_this
# else:
#   do_this


# name = input()


# if name == 'griffin':
#   print('that\'s my name too!')
# elif name == 'luis':
#   print('hi')
# else:
#   print('eww')


# farenheit and celsius
# Celsius = (5/9)(Farenheit-32)
# Farenheit = (9/5)Celsius +32


# Have a user input either farenheit or celsius temperature
# if they give u farenheit, return celsius.... if they gave u celsius, return farenheit


# def sum(x, y):
#   return x + y

# variable = sum(1, 2)  # 3

# def celsius(farenheit):
#   # takes in farenheit, and gives back celsius
#   return (5/9)*(farenheit-32) 


# def farenheit(celsius):
#   # takes in celsius, and gives back farenheit
#   return (9/5)*celsius+32


# # if they say farenheit, then return temperature they give you in celsius
# while True:
#   unit = input("Enter a unit of temperature (Celsius and Farenheit)! ") 
#   print()

#   if unit == 'farenheit' or unit == 'f' or unit == 'F' or unit == 'Farenheit':
#     number = float(input("Enter a unit of temperature (Degrees)! "))
#     print()
#     print('You entered', number, 'in', unit, 'here it is in celsius:', celsius(number))
#     #print(celsius(number)) 

#   elif unit == 'celsius' or unit == 'c' or unit == 'C' or unit == 'Celsius':
#     number = float(input("Enter a unit of temperature (Degrees)! "))
#     print('You entered', number, 'in', unit, 'here it is in farenheit:', farenheit(number))
#     print()
#     #print(farenheit(number))
#   # if they say celsius, then return temperature they give you in farenheit

#   else:
#     break

# print('PROGRAM HAS ENDED')


# ------------------------------------------------------------------------

# HackerRank
# https://github.com/karan/Projects



# import random


# def flip(n):
#   # return number of heads that show up in N coin flips
#   sides = ['Heads', 'Tails'] # random.choice(sides)
#   numHeads = 0
#   numTails = 0
#   for i in range(n): 
#     side = random.choice(sides)
#     if side == 'Heads':
#       numHeads += 1
#     else:
#       numTails += 1

#   print('Number of heads:', numHeads)
#   print('Number of tails:', numTails)


  
# # Let user say how many times we flip the coin
# timesFlipped = int(input("Enter an amount of times to flip: "))
# print()

# flip(timesFlipped)


  
# We report the number of heads and tails flipped

# Prompt them to see if they want to continue
# T U P L E


# --------------------------------------------------------



# arr = []
# for i in range(0, 101):
#   arr.append(i)


# arr = [(i,j) for i in range(0, 10) for j in range(0, 10)]

# print(type((1, 2)))



class Cat:
  def __init__(self, name):
    self.name = name

  def meow(self):
     print('meow')

  

cat = Cat('kitty')


cat.meow()


