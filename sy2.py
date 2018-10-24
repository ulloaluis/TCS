
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

def celsius(farenheit):
  # takes in farenheit, and gives back celsius
  return (5/9)*(farenheit-32) 


def farenheit(celsius):
  # takes in celsius, and gives back farenheit
  return (9/5)*celsius+32


# if they say farenheit, then return temperature they give you in celsius
while True:
  # if they dont enter farenheit or celsius, we end program (break)
  # BUT if they enter the wrong unit, it still asks them for number, and program doesn't end until they enter one
  unit = input("Enter a unit of temperature (Celsius or Farenheit)! ") 
  print()
  number = float(input("Enter a unit of temperature (Degrees)! "))
  print()

  if unit == 'farenheit' or unit == 'f' or unit == 'F' or unit == 'Farenheit':
    print('You entered', number, 'in', unit, 'here it is in celsius:', celsius(number))
    #print(celsius(number)) 

  elif unit == 'celsius' or unit == 'c' or unit == 'C' or unit == 'Celsius':
    print('You entered', number, 'in', unit, 'here it is in farenheit:', farenheit(number))
    #print(farenheit(number))
  # if they say celsius, then return temperature they give you in farenheit

  else:
    break


# hw: fix buggy program








