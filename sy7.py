## REFERENCE: https://qualitymemes.xyz/cases/ <--

# + more work on csgo simulator

import random


# have a case
#   case with guns
# randomly choose color blue/pink/red/knife
# randomly choose item inside color (actual gun name + skin)


python = {
  "Blue": [
    "Tec-9 Fubar",
    "Five SeveN Violet Dynamo",
    "Glock-18 Off World",
    "Desert Eagle Meteorite",
    "R8-Revlover Grip"
  ],

  "Purple": [
    "CZ-75 Auto Tacticat",
    "USP-S Cyrex",
    "R8 Revolver Reboot",
    "MP5-SD Lab Rats",
    "AWP Worm God",
    "AK47 Blue Laminate"
  ],

  "Pink": [
    "Desert Eagle Conspiracy",
    "SCAR-20 Cyrex",
    "P250 Asiimov",
    "USP-S Orion",
    "M4A1-S Decimator",
    "AK47 Cartel"
  ],

  "Red": [
    "AK47 Fire Serpent", 
    "AWP Neo-Noir", 
    "AWP Asiimov", 
    "M4A1-S Cyrex"
  ],

  "Knife": [
    "M9 Bayonet - Tiger Tooth", 
    "M9 Bayonet - Autotronic"
  ]
}


# ask user if they want default or custom
blue, purple, pink, red, knife = 0, 0, 0, 0, 0
while True:
  mode = input("Default chances or customized chances (d or c)? ")
  if mode == 'd':
    blue = 0.79923
    purple = .15985
    pink = 0.031969
    red = 0.006394
    knife = 0.002558
    break

  elif mode == 'c':
    tot = 0
    blue = float(input("Blue chances (0 to 100)? "))
    tot += blue
    purple = float(input("Purple chances (0 to %.2f) " % (100 - tot)))
    tot += purple
    pink = float(input("Pink chances (0 to %.2f) " % (100 - tot)))
    tot += pink
    red = float(input("Red chances (0 to %.2f) " % (100 - tot)))
    tot += red
    print("Knife chances are %.2f" % (100 - tot))
    knife = 100 - tot
    break

  else:
    print("%s is an invalid input, please enter d for default or c for custom." % mode)
    # ask the question again


num_cases = int(input("How many cases to open? "))
for _ in range(num_cases):
  number = random.random()
  color = None

  if number < blue:
    color = 'Blue'
  elif number < blue + purple:
    color = 'Purple'
  elif number < blue + purple + pink:
    color = 'Pink'
  elif number < blue + purple + pink + red:
    color = 'Red'
  else:
    color = 'Knife'

  options = python[color]
  prize = random.choice(options)
  print("You got a %s weapon: %s" % (color, prize))







    # Blue Expected			79.923%
    # Purple Expected			15.985%
    # Pink Expected			3.1969%
    # Red Expected			0.6394%
    # Knife Expected			0.2558%



