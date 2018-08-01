Today
  Review yesterday's lesson on strings/finish it (half or >)
  Review all the material we've learned so far by doing random questions/anything you want help on
    Maybe: Introduce project we'll do for last two days
      
# Yesterday

#                      ------ Defaults ------
# array[a:] second value always defaults to length of array if excluded
# array[:b] first value always defaults to 0 if excluded
# array[::c] third argument defaults to 1 (step, like third argument of for loop)
              # if negative, then defaults for a and b switch around
#----------------------------------------------------------------------

Practice Problems

# We have the following word:
word = "DOGSPELLEDBACKWARDISGOD"
# we want to extract "SPELLEDBACKWARDIS", how would you do that? 
  
  
# What about getting rid of "SPELLEDBACKWARD" so we just have
# "DOGISGOD"? We will have to make a new string, there will be two slicing
# parts that we concatenate together.
  
  
# We have the following *sorted* list 
# Assume the list is t least 3 numbers large
biggest_numbers = [1, 213, 1213, 3301, 9991, 99999, 1032103021]
# We want to get and print a list of the 3 greatest values. How to? 
  
def biggest_numbers(list): 
  return list[-3:]
   
  list = [1, 213, 1213, 3301, 9991, 99999, 1032103021]

print(biggest_numbers(list))

new_list = list[-3:]
print(new_list)
  
# From the previous problem, how would we get the 3 smallest values?
  
  
list = [1, 213, 1213, 3301, 9991, 99999, 1032103021]
new_list = list[:3] 
print(new_list)
  
# How would we get the middle number (3301)? 
# hint: easiest without negative numbers 
# another hint: start at middle, but you can't "hardcode" the value u need, use len()
# another hint: / or // ???   3 / 2 = 1.5  3 // 2 = 1 
# yes you can assume the list is odd and has a middle number, 

# list[len(list) // 2] 7 // 2 = 3
list = [1, 213, 1213, 3301, 9991, 99999, 1032103021]

list[  len(list) // 2 : len(list)//2 + 1 ] # --> 3301
list[len(list)//2]

# [start at the index of middle number : 1 greater than that] 

list = [1, 213, 1213, 3301, 9991, 99999, 1032103021]
new_list = list[len(list) // 2]
print(new_list)
  
  


# Write a function/method that returns the average of a list

def average(list): 
  return sum(list) / len(list)
x = [3, 3, 3]
print(average(x)) # 3

# Given a sorted list
# Return the average of the 2 greatest numbers

# Sorted List
# Average of greatest 2 numbers

def average_of_greatest(list):
  return sum(list[-2:]) / 2          # list[-2:] creates list  /2 divides by 2

  
list1 = [1, 2, 3, 4, 5] # average of greatest 2 = 4+5 / 2 = 4.5
list2 = [13, 19, 24, 40] # avg of greatest 2 = 24+40  / 2 = 32
  
# Random string problem

Write a program that takes in a user input string and then 
prints the string reversed to the screen (can do with slicing)
  
# I'll write this part
  
word = input("Enter a string to reverse: ")
print(word[::-1]) # reverses word and then goes through it normally is a way to think of this



# Let's say you wanted to exchange secret messages with your friends
# Let's write a program that converts your message into a special format
# that your friend can undo using string slicing

x = "gxoad" # 

print(x[::-2])  # x = [1, 2, 3]   x[::-1]  x[3:0:-1] 3-1 2-1 1-1 x[0:3:1] [1, 2, 3]


# ----------- small encryption program ------------- #

import string
import random

def encrypt_message(msg):
  # Add in random characters in every other location
  # we want to reverse the string
  letters = string.letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  new_str = ""
  
  for letter in msg:  # "dog" -> "dAopgI" -> "IgpoAd"
    new_str = new_str + letter + random.choice(letters)
    
  return new_str[::-1]
  
def decrypt_message(msg): 
  return msg[::-2]
  
# Today - Open Stage for questions/anything you've seen in the past week that you want more info on
  
  
import random


def encrypt_message(msg):
    # Add in random characters in every other location
    # we want to reverse the string
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#!@,\"\\:;/}][{-_=+`~$"
    new_str = ""

    for letter in msg:  # "dog" -> "dAopgI" -> "IgpoAd"
        new_str = new_str + letter + random.choice(letters)

    return new_str[::-1]


def decrypt_message(msg):
    return msg[::-2]


# Ask user for message to encrypt

# Allow user to decrypt a message


msg = input("Enter a message and I'll encrypt it for you: ")
encrypt_level = int(input("Layers of security: "))

for i in range(encrypt_level):
    msg = encrypt_message(msg)
print("Here's your encrypted message: ", msg)


x = input("Enter an encrypted message and I'll decrypt it for you: ")
decrypt_level = int(input("What was the encryption level? "))
for i in range(decrypt_level):
    x = decrypt_message(x)
print("Here's your decrypted message: ", x)

  
# ----------- small encryption program ------------- #
  
  
  
# Project

# class Pikachu(pokemon):
#   def __init__(self):
#     self.name = "Pikachu"
#     self.hp = 547
#     self.dmg = 175
    
#   def basic_attack(self, other):
#     other.hp -= self.dmg # subtract 175 health from metapod.
#     print(self.name, "hit", other.name, "for", self.dmg, "damage!") # Pikachu hit metapod for 175 damage!


# look into encryption program


  # Let's choose: Hangman? Guess the dice roll game? etc. 
  # graphics are a bit harder, so we might just stick to a text-based game
