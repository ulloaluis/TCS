------- if statements ------
if expression:
  statements...
elif expression:
  statements...
else:
  statements...

------- for loops -------
for i in range(a, b):
  statements...

array = [1, 2, 3]
for number in array:
  statements...
 
------- while loops -------
while expression:
  statements...

 -------- functions ------------
def function_name(arguments):
  statements...
  return something # this part is optional, functions without this are called void functions
  
  
# Today's schedule
# Finish up yesterday's stuff 15-30 minutes
# New stuff - rest of lesson
  # string manipulation stuff (yay) 
  
  
# From last lesson / review / going over it
# -------------------------------


Write a function that prints "Hello World" when you call it

def hello():
  print("Hello World")
hello()


def speech(line):
  print(line)

speech("R2D2") # R2D2
  
  
# Write a function that accepts a list from the user and then prints
# all of the elements in the list to the screen


def print_list(list):  # 
  for x in list:    #  
    print(x)        #  do something with element in list
  
  
  function(arguments)
  
  for i in range(0, 3): # [0, 1, 2]
    

#   x = [ 1, 2, 3]
#   x[0] # get first element  
    
  # parentheses -> functions, separating math/algebra
  # brackets -> accessing an index, or slicing (see later)
    
def element_list(list):
  print(list)
  
  


# Write a function that takes in a number (n) and a string (str) and then
# prints that string n amount of times.

# n = 2, str - "word"
word
word

def print_n_times(n, str): 
  # code goes under here
  
  for _ in range(n):
    print(str)
  
  
  for str in n: # use in for lists and stuff like that, but not for numbers
    print(str)
  
# Write a function that accepts two numbers and then returns the product of two numbers squared. 
# 5 and 5, (5*5)**2 (a and b)

def do_math(a, b):
  return (a * b) ** 2 

  
val = do_math(5, 5) 
  
  

we have a list, we want to print even numbers greater than or equal to 10

 # expression  and    expression .     true if both parts are true
  

def even_and_double_digit(list):
  for item in list:
    if item >= 10 and item % 2 == 0:
      print(item)


#print those here
  

x = [1, 30, 17, 18, 9, 20, 10]        # 30, 18, 20, 10




# given a string, return that string but with no vowels

def no_vowels(word):    # a e i o u
  # in here, build up a new string, not including the vowels
  new_word = ""
  for letter in word:
    if letter != 'a' and letter!= 'e' and letter!= 'i' and letter!= 'o' and letter!= 'u': 
      new_word += letter # new_word = new_word + letter
  return new_word
dog = "dog"

print(no_vowels(dog)) # dg
  
  
    
    " adsakldmlask mdaslkdm aksl"
#---------- new ------------ string stuff ----------
# string manipulation is sort of like what I mentioned yesterday 
# with a string being like a "list/array of characters" "dog" --> ['d', 'o', 'g'] --> word[0] --> "d"
# a lot of things we are gonna do with strings today you can do with lists!
    
    
            -         slicing stuff        -
# getting parts of a string
 string[a:b] # start at index a and go up to index b (dont include b)
# example: 

word = "dog"      # "dog"
# .    0 1 2

#        ^ (b-a or 2-1 or 1 characters)
#   word[1:2]



new_word = word[1:2] # "o" we start at "o" and end at "g", not including "g"
print(new_word)
  
  
# better to think of it here as it starts at "o" and gets total of 3 - 1 characters

word = "dog"
new_word = word[1:3] # "og"  
print(new_word)
  
  
word = "cat"
        #  ^ 3-2 or 1 characters
new_word = word[2:3] # t 
  
  
  
# what if we just use left side of the colon?
  
word = "dogssssZs"
new_word = word[1:] 
print(new_word) # ogssssZs
  
# by default, [a:] starts at character in index a and goes until end of word
# shorthand for [a:len(word)]
  

# using just the right side
word = "dogssssZs"
new_word = word[:3]   
print(new_word) # dog
  
# by default, it makes the left side 0, so you get characters at indexes 0 1 2, or first 3
  
  
  
                      ------ Defaults ------
array[a:] second value always defaults to length of array if excluded
array[:b] first value always defaults to 0 if excluded
----------------------------------------------------------------------
  
  
  
# cool, but now let's make life unnecessarily hard for a minute cuz why not
# what about negative numbers in all of the above cases?

# negative numbers just mean "start from the end and move backwards"
  
  
  
dog = "dog " 
print(dog[-2]) # neg numbe to access from end of list
  
  
word = "IMAFANOFDOGS"
new_word = word[-3:] # OGS
print(new_word)
# this moved back by 3 characters and then read from there to end
  
  
  
  
word = "|IMAFANO|FDOGS"
new_word = word[:-5] # IMAFANO
print(new_word)
# this starts at beginning of word by default, then moves forward until 5 characters before word ends
  
  
  

word = "IMA|FANOF|DOGS"
new_word = word[3: -5] # FANO
print(new_word)
# this starts word at 3rd index (4th character) and reads until 5 characters before word ends
# could also say     word[3:7]

word = "IMAFANOFDOGS"
  
  

# Can do all of this with lists (a.k.a. arrays) too
  
array = [1, 2, 3, 4, 5]
new_array = array[1:-1] # this starts at index 1 character and goes until 1 character before word ends
print(new_array) # [2, 3, 4]
    
    
  
# SURPRISE: optional 3rd arguments (like a for loop!), used as a "step"
  
name[a:b:c] # start at index a and move towards index b but don't include. 
            # normally c defaults to 1, but can specify different numbers 
            # to get it to go through it differently
# Example


array = [1, 2, 3, 4, 5]
new_array = [1::2] # start at index 1 (has value 2) and go till end of array, but skipping one (1+2-->3, skips index 2)
print(new_array) # 2 4
  
array = [3, 4, 5, 6, 7]
new_array = array[::2] # [a:b:c] a and b default to a = 0, b = list length
print(new_array) # 3 5 7
  
# you can even make c negative, this would make it go backwards!
# it's a bit funky in a way though. 
# You can think of it as negative c CHANGES the default values and then goes through it normally
    # so if c is negative,  a defaults to len(list) and b defaults to 0 (opposite)

  if c is negative --> a now behaves like b, and b now behaves like a
  
array = [1, 2, 3, 4, 5, 6]
new_array = array[end of list:start of list:-2] # [5, 3, 1] 
# equivalent to instead making array = [5, 4, 3, 2, 1] and then doing array[::2]
  

Practice Problems
  
  
# We have the following word:
word = "DOGSPELLEDBACKWARDISGOD"
# we want to extract "SPELLEDBACKWARDIS", how would you do that? 
  
  
# What about getting rid of "SPELLEDBACKWARD" so we just have
# "DOGISGOD"? We will have to make a new string, there will be two slicing
# parts that we concatenate together.
  
  
# We have the following sorted list 
biggest_numbers = [1, 213, 1213, 3301, 9991, 99999, 1032103021]
# We want to get and print a list of the 3 greatest values. How to? 
  
  
  
# From the previous problem, how would we get the 3 smallest values?
  
  
# How would we get the middle number (3301)? 
# hint: easiest without negative numbers 
# another hint: start at middle, but you can't "hardcode" the value u need, use len()
# another hint: / or // ???
# yes you can assume the list is odd and has a middle number
  
  

# Random string problem
  
# Write a program that takes in a user input string and then 
# prints the string reversed to the screen (can do with slicing)
  
# I'll write this part
  
word = input("Enter a string to reverse: ")
print(word[::-1]) # reverses word and then goes through it normally is a way to think of this


  
