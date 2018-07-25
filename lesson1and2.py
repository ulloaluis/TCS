# Last lesson we looked at print statements and touched on
# a lot of other things that we will be covering over the next
# few days
print("Output this text to screen.")
  
  
# Now we will be looking at Computer Science Philosophy 
# and then maybe more in-depth about variables
  
# Key Points
  # everything is typically executed in order, unless we specify otherwise, 
  # like we saw with 
    # def sum(x, y)
print("prints first") 
print("second")
print("third")
    
  # Python code files end with .py, example: MyProgram.py
    
  # Computer Science is computational and algorithmic, we solve problems
  # with computers by breaking them into smaller problems.
  # "study of solving problems computationally" --> formal CS definition
    
    
    
# PSEUDOCODE - writing out the program flow without actually coding it yet
 #   if the user input is greater than 5
 #       print hello
 #   else
 #      print goodbye
    
if int(input('Enter a number: ')) > 5: # note: input() doesn't work on this website :/
  print("hello")
else:
  print("goodbye")
  
    
# Format of most programs we will be writing:
  # Input - Process - Output (IPO)
    
# Example (Input-Process-Output):
celsius = input("Enter a temperature in celsius: ") # all inputs are read as strings, even if they enter a number
fahrenheit = 9/5 * int(celsius) + 32   # we convert celsius to a number so that we can do proper math
print("The temperature is", fahrenheit, "degrees Fahrenheit.") # we output result to screen
  
# Comments (like these) are used to explain a program, so we and others can 
# easily and quickly understand what the program does

# (following is from handout, word for word)
#   For example, let’s consider the problem we presented earlier in this lesson; writing a program which translates celsius temperatures to fahrenheit. Although this is a fairly simple problem, we can break the original problem of: “Write a program which translates celsius temperatures to fahrenheit” into sub-problems. These might be: 
# 1) Get a temperature input in degrees celsius from the user. 
# 2) Use our formula to calculate fahrenheit temperature.
# 3) Tell the user the temperature in degrees fahrenheit.

# This breaks our original problem into 3 smaller problems. We could further break each of these into even more simple problems.
# 1a) Get input from user
# 1b) Evaluate input as number
# 1c) Save number into a variable
# 2a) Calculate fahrenheit temperature with given formula
# 2b) Save fahrenheit temperature into a variable
# 3a) Print message explaining our calculation
# 3b) Print value of fahrenheit variable
  
# Our original problem has now been split into 7 much smaller subproblems, each of can be solved with a single line of code or less. In the case of this problem, we only require 3 lines of code.

  
  
 # ------------ following is on variables and stuff ---------------- #
  
# Understand what types are
# Know the difference between a Float and an Int and when to use them
# Understand the Strings
# Learn what a Boolean is
  
# Variables are nothing but names for reserved memory locations that store values.
  # Used to keep track of info in a program (like user input!)
  # Can be updated throughout the program
  # You have to declare a variable before you can use it (can't use it if it doesn't exist)
  
# Each of these is a variable being assigned, each has a different type  
counter = 100          # An integer assignment (non decimal) (ex. -1, 4, -1231, 0, 15315)
miles   = 1000.0       # A floating point (decimal) (ex. -31.5, 12.0, 0.0, 15.35)
name    = "Luke"       # A string (ex. always written with '' or "" or even """ """)
    
print(counter, miles, name) # when we print them, we get the value we gave them
  
# Can use normal arithmetics like + / - * and also ** for powers

  
# Adding an int to an int = an int!
a = 3 + 3
print(a) # 6
# Adding an int to a float = a float!
a = 3 + 1.0
print(a) # 4.0
  
  
# Yes you can reassign a variable
x = 10
print(x) # 10
x = 7
print(x) # 7
  
# Yes you can assign a variable to another variable
y = 50 # y is 50
x = y  # x is also 50
print(x, y)
  
# You can assign multiple variables to one value on one line
a=b=c=1
print(a, b, c)
  
# You can assign multiple variables to different values on one line
m, n, o = 1, 2, 'word' 
print(m, n, o) # 1 2 word
  
# Naming rules
# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that the names are lowercase.
# 5. Variable names should not be Python reserved words like with or not.
  
  
# None Object
  # empty placeholder commonly used to initialize names and objects. 
  # None is a real piece of memory that is created and given a built in name by Python
x = None # None placeholder
print(x) # None
  
# Can use int(x), float(x), and long(x) to convert strings to numbers (like input strings)
a = "5"
b = int(a)
print(b) # 5 not "5"
  
  
# Strings - used to store text, behaves like an "array of characters"
name = "Luke"
  # can access each character, remember, 0 1 2 3... indexing
name[0] # "L"
name[3] # "e"
  
# backslash \ is used to "escape" characters, also special things
  # bcuz of this, if you want to put \ in a string, you need to "escape" it
  # with another backslash, so
print('\\') # is only one \
print('a \n a') # \n is a special expression, it prints a new line
print('\'') # prints a single apostrophe ', we had to escape it with backslash
  
# Boolean - True or False , useful for controlling program flow
# bool(some_value) can cast things to boolean if they can be interpreted as a truth value (0 false, not 0 true)
size = 1
print(size < 0) # False

  
# Core data types
  # Numbers, strings, lists, dictionaries, tuples, files, and sets
  # numbers 0 1 2..., strings "word", lists [1, 2, 3]
  # dictionaries {'food': 'spam', 'taste': 'yum'} uses key-value pairs
  # tuples a_tuple = ('physics', 'chemistry', 1997, 2000)  --> "sequence of immutable Python objects"
  # files open('eggs.txt') will open the file, typically written as "with open('file.txt') as fileVariable:"
  # sets set('abc') --> {'a', 'b', 'c'} Contains only unique elements, no repeats
  
# Immutable types: strings, numbers, tuples
# Types that cannot be "changed in place", so they get a different 
# location in memory when you change their value


# *Homework/Challenge*: If you wanted to take in 3 test grades from a user and then tell them
# their average score, how would you do that? Write in pseudo code and then attempt a working program.
  
  
  
