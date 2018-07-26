# Yesterday:
# Practiced a bit with if statements and for loops
# got a bit of practice writing code

# if statements syntax/way of writing
  
# if <expression>:
#   statements...
# elif <expression>:
#   statements...
# else:
#   statements...

# remember: you need to tab/add spacing for each block of information (under an if statement)
# you need too add a colon :
# strings have " " or ' ' or """ """
# input("Enter a number: ")
# for loops syntax/way of writing using range
  
# for i in range(a, b):   # (not including b)
#   statements...

# for i in range(b): # a defaults to 0 (0, b)
#   statements...
# remember: the value of i increases with each loop
            # i is a variable and you could use a different name
  
# Today:

# Looking at the three problems left over from yesterday (first half-ish)
# Looking at the arithmetic operations we can do with numbers, and getting 
# comfortable using them (+ - / // * ** %)
  # /  float division
  # // integer division

  
# Average test score, take in 3 test scores, and add them then get average

# x = int(input("enter test score here: "))
# y = int(input("enter test score here: "))
# z = int(input("enter test score here: "))

# sum = (x+y+z) / 3 # operator precedence, order of operations PE MD AS
# print(sum)
  

Print the user's letter grade in a class, given their percentage
a lot of if statements and stuff 
90%+ = A, 80 <= B < 90 # 89.4%

# >= 
# score = float(input("enter your test score here: ")) # 90, 90.0
# if score >= 90.0:  
#  print('A')
# elif score >= 80.0:
#  print('B')
# elif score >= 70.0:
#  print('C')
# elif score > 60.0:
#  print('D')
# else:
#  print('F')


# Quadratic formula 
# a, b, c
# ((b**2) - (4*a*c))**(1/2) / (2*a)

# ^ 
# **
# x1 = -b + sqrt(b^2 - 4ac) / 2a
# x2 = -b - sqrt(b^2 - 4ac) / 2a


# input process output

# def function_name(all the variables it accepts)
def quadratic(a, b, c): # taking in a, b, and c
  discriminant = b**2 - 4*a*c # discriminant
  if discriminant >= 0: 
    x1 = (-b + discriminant**(1/2)) / (2*a)
    x2 = (-b - discriminant**(1/2)) / (2*a)
    print("You roots are ", x1, x2)
  else: # discriminant is negative
    print("Your roots are imaginary.")
        
a = int(input('enter value for a: '))
b = int(input('enter value for b: '))
c = int(input('enter value for c: '))
quadratic(a, b, c)
quadratic(2, 9, 1) # a = 2, b = 9, c = 1
quadratic(1, 5, 2) # a = 1, b = 5, c = 2
    
# f(x) = x + 1
# y = x + 1


# def f(x): # function, method
#   return x + 1

# f(2) # 3, if f(x) = x + 1
  
# same as if u wrote this (much uglier and harder to understand)
    
a = int(input('enter value for a: '))
b = int(input('enter value for b: '))
c = int(input('enter value for c: '))

discriminant = b**2 - 4*a*c # discriminant
if discriminant >= 0: 
  x1 = (-b + discriminant**(1/2)) / (2*a)
  x2 = (-b - discriminant**(1/2)) / (2*a)
  print("You roots are ", x1, x2)
else: # discriminant is negative
  print("Your roots are imaginary.")

  
a = 2
b = 9
c = 1

discriminant = b**2 - 4*a*c # discriminant
if discriminant >= 0: 
  x1 = (-b + discriminant**(1/2)) / (2*a)
  x2 = (-b - discriminant**(1/2)) / (2*a)
  print("You roots are ", x1, x2)
else: # discriminant is negative
  print("Your roots are imaginary.")

a = 1
b = 5
c = 2
  
discriminant = b**2 - 4*a*c # discriminant
if discriminant >= 0: 
  x1 = (-b + discriminant**(1/2)) / (2*a)
  x2 = (-b - discriminant**(1/2)) / (2*a)
  print("You roots are ", x1, x2)
else: # discriminant is negative
  print("Your roots are imaginary.")
  
quadratic(a, b, c)
     
    
#   x1 = -b + sqrt(b^2 - 4ac) / 2a
#   print(x1)
#   x2 = -b - sqrt(b^2 - 4ac) / 2a
#   print(x2)

#   if expression:
#     do this for that expression
  
# for expresson:
#   dadsa
  
# while expression
#   indent
# def sum(x, y) 
#   adada



Taking in 2 numbers (a and b, assume they are ints) from the user and 
printing their sum difference quotient product modulo and exponentiation ( + - / * % **) 

# print('sum = ', x + y) surprise

x = int(input('enter number here: '))
y = int(input('enter number here: '))
sum = x + y 
print('sum = ', sum)
difference = x - y
print('difference = ', difference)
quotient = x / y 
print('quotient = ', quotient)
product = x * y
print('product = ', product)
modulo = x % y
print('modulo = ', modulo)
print('exponentiation =', x**y)
  
  
  
# Even or odd integer? ---> super common problem in CS, best way to do this? 
# hint: use one of the arithmetic operators. - + * ** % / //
# # when would it be even?

# Let's write a program where you are given an integer
# and you output if it's even or odd


x = int(input('enter number here:'))
remainder = x % 2 
if remainder == 0:  
  print('x is even')
else:
  print('x is odd')




With for loops: given a number n, print all of the even numbers 1 to n
Hint: Can do this two ways. Using what we did right before, or by adjusting the for loop!

# all even num between 1 to n, if n was10, u would print 2 4 6 8 10

# With for loops: given a number n, print all of the odd numbers from 1 to n
  
# find range, find modulo of all numbers in range, print numbers that have a remainder of 0

# for i in range(a, b): # not including b, remem to indent

for i in range(1, n+1, 1):  # say n was 5
  
for i in range(1, 11, 2): 
  print(i)

n = int(input('enter number here: '))
for i in range(1, n + 1, 1): 
  x = i % 2  
  if x == 0:
    print(i)
# using for loop to print all odd
for i in range(1, n+1, 2):
  print(i)

# all even
for i in range(2, n+1, 2):
  print(i)
  
  
# Random fill-in-the-blank problems using the for loop step variable:
# Remember! The second value is not "included," for loops go UP TO but not including that value!
  
# Example
# for loop to print 1, 3, 5
# for i in range(1, 6, 2): # 6 is not included, starts at 1 then jumps to 3 (1+ 2 ), then 5 (3+ 2 )
#   print(i)
  
What would you put in the following for loop to print 10, 20, 30?
for i in range(__, __, __):
  print(i)
  
... to print 1, 7, 13?
for i in range(__, __, __):
  print(i)

  
... to print 0, -5, -10, -15, -20?
for i in range(__, __, __):
  print(i)
  
  
  
