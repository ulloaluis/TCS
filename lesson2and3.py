# Programs to write:

# Write a program that prints ‘Hello World’ to the screen.

print('Hello World')

# Write a program that asks the user for their name and greets them with their name.

user_name = input("user name: ")
print(user_name)


# Modify the previous program such that only the users Alice and Bob are greeted with their names.
# and: both are true, or: one is true
# want to check if user_name is 'Alice' or 'Bob'

# equality: ==
# 

if <expression>: 
  statement(s)
elif <other expression>: 
  statement(s) 
elif <other expression>:
  statement(s) 
else: # everything else
  statement(s)

username = input('enter your name: ')
if username == 'Alice' or username == 'Bob':
  print(username)
  
  
# modify the previous program so if the user's name is Luke, you print hello
# print("they all failed")


# in - "substring" - strings
# in - is this item in a list - list
username = input('enter your name: ') # variable = input(<prompt>)
username = 'Al'

if username == 'Alice' or username == 'Bob':
  print(username) #'Bob'
elif username == 'Luke':
  print('Hello')
elif username == 'Dog':
  print("it was a dog")
else: 
  if len(username) < 3:
    print('less than 3 characters')
  else:
    print('they all failed') # they all failed
  
# Write a program that asks the user for a number n and 
# prints the sum of the numbers 1 to n, 1 + 2 + 3+ 4 + ... + n
# for i in range(a, b): # doesn't include b
# "11" and 11
number_n = int(input('enter a number greater than one: '))
sum = 0
for i in range(1, number_n + 1):
  # 1 + 2 + 3 + .. + number_n
  sum = sum + i 
  
sum2 = (number_n+1)* number_n / 2
if sum == sum2:
  print("they were the same! yaymath")
  
# one / is float division (has decimals)
# two slash // is integer division (no decimals)

print( 5 / 4 ) # with decimal - float division
print( 7 // 4 ) # without decimal - integer division

#   sum = 1 + n 
#   sum = 2 + n
#   sum = .. + n
#   sum = n + n 
  
#   sum = 1 + 2 + 3 + ... + n
  
  
# for i in range(0, 3):
#   print(i)
  
# for i = 0: i <3
#   print(i)# 0
#   i = i + 1
  
# for i = 1: i < 3
#   print(i)# 1
#   i = i + 1
  
# for i = 2: i < 3
#   print(i) # 2
#   i = i+ 1
  
# for i = 3; 3< 3



# Homework/self practice/ and stuff

# Average test score, take in 3 test scores, and add them then get average




# Print the user's letter grade in a class, given their percentage
# a lot of if statements and stuff 
# 90%+ = A, 80 <= B < 90


score = int(input(enter your test score here))
if score > 89
  print('A')
elif score > 79
  print('B')
elif score > 69
  print('C')
elif score > 59
  print('D')
else
  print('F')


# Quadratic formula 
# a, b, c
((b**2) - (4*a*c))**(1/2)  / (2*a)

x1 = -b + sqrt(b^2 - 4ac) / 2a
x2 = -b - sqrt(b^2 - 4ac) / 2a
  
Atom text editor, file ends with filename.py
OR
https://glot.io/snippets/f37vy1t1a6
