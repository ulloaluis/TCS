# yesterday we reviewed if statements, operators and their precedence/order of operations
# and we did stuff with for loops
  
# Today we will be looking at while loops, similarity to for loops, 
# and when to use each one. Also, infinite loops.
  
# Review: 10-25 min, might do some interesting for loops
# Today: Rest of time

# where we left off
    
# Random fill-in-the-blank problems using the for loop step variable:
# Remember! The second value is not "included," for loops go UP TO but not including that value!
  
# Example
# for loop to print 1, 3, 5
# for i in range(1, 6, 2): # 6 is not included, starts at 1 then jumps to 3 (1+ 2 ), then 5 (3+ 2 )
#   print(i)
  
# What would you put in the following for loop to print 10, 20, 30?
# for i in range( 10 , 31 , 10 ):
#   print(i)
  
# ... to print 1, 7, 13?
# for i in range(1,14,6):
#   print(i)

  
# ... to print 0, -5, -10, -15, -20?
# for i in range(0,-21,-5):
#   print(i)
  

# # called nested for loops
# # used a lot in graphics
# # photoshop software uses double for loops a.k.a. 
# # nested for loops to change photos. i and j represent
# # locations on a screen and you change the value in each iteration
# # (i think)
# for i in range(a, b):
#   for j in range(c, d):
#     print(i, j)
  
      
      
# TODAY
      
# while loop
# --> Do something until an expression is no longer true
      
# Syntax
while expression:
  statements
    
    
#Take in a user input. Input is a string. While the string is not 
# the phrase "ok done", print "dogs > cats" to screen

#  exclamation point, !, means NOT    != is NOT EQUAL

s = input("Enter anything to start: ")
while s != "ok done":
  print("dogs > cats")
  s = input("done?: ")
print("ok cool")

arr = [2, 4322, 54534, 543255]
for num in arr: # wouldn't need quotation marks for num
  print(num) # num --> arr[0 1 2.. length of array]
  
#   # 2
#   # 4322
#   # 54534
#   # 543255

# target_word = "dog"
# num_fails = 0
# letters_guessed = [False]*len(target_word) # [False, False, False]
# while num_fails < 7:
#     if is_all_true(letters_guessed): # they guessed all the letters
#         print("You win!")
#         end_program()
#     their_letter = input("enter a letter: ") # g
#     for i in range(0, len(target_word)): # (0, 3) # 0 1 2
#         if target_word[i] == their_letter:
#             letters_guessed[i] = True
            
            
    
#     -# d nope did nothing they weren't the same letter
#     -# o nope
#     -# g 3rd time through the loop, we do something
#     # g
#     # g
#     # g
#     ..
    
# print("You lose!")
  

  
# #        0  1  2
# array = [3, 5, 123132] # a list of something(s)

# for num in array:
#     print(num) # 3 5 123132


# print(array[1]) # 2
#     #   01
# word = "someword" # array of characters
# word = ['s', 'o', 'm', 'e', 'w' ...]
# print(word[1]) # o

# word[] 
# # access an index
# for i in range(0, len(word)):  
#     if word[i] 


# word = "someword" # array of characters
# for letter in word: # word[0] --> word[1] --> word[2] .. word[last letter]
#     if letter








# For loop OR while loop problems ???!!!
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
    
n = int(input('enter an integer here: '))    
x = n % 2  
if x = 0
  print(n)
  print('play again')





# The user enters a word and a number n. You print their word 
# concatenated n amount of times and then allow them to type 
# another word and number.
# This continues until they enter the word "stop", which is 
# --case insensitive, so they could enter "sToP" or "STOP" or "stop", etc.
    
# CONCATENATION: "DOG"+"CAT" = "DOGCAT", "SPIDER"+"PIG"="SPIDERPIG" 
#           "dog"*2 --> "dog"+"dog" = "dogdog" 
#           "dog"*3 --> "dogdogdog"
      # Fancy word for adding strings together

    
    
# infinite loops --> the unseen killer bug
    
while expression-that-is-always-true:
  statements...
    
n = 0
while n < 0:
  print(n) 
  n = n + 1
# doesn't stop outputting things because the expression is always true
      
      
      
