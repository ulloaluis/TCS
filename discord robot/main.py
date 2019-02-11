import discord
import asyncio
import requests
import os
import random
import time
import json
from random import randint

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('copy paste this in your browser to authorize bot https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(os.environ['CLIENTID']))
    print('------')

# https://discordpy.readthedocs.io/en/rewrite/api.html#

@client.event
async def on_message(message):
    increase_balance(message)

    if message.content.startswith("!sim"):
      await simulation_command(message)

    elif message.content.startswith("!inv"):
      await inventory_command(message)
      
    elif message.content.startswith("!give"):
      await give_command(message)

    elif message.content.startswith("!help"):
      await help_command(message)
  
@client.event
async def simulation_command(message):
  parts_of_message = message.content.split(' ')
  num_cases = int(parts_of_message[1])
  bank = json.load(open("bank.json", 'r'))
  balance = bank[message.author.id]

  if balance >= num_cases:
    # update their balance
    bank[message.author.id] = balance - num_cases
    with open('bank.json', 'w') as fp:
      json.dump(bank, fp) 

    colorguns = json.load(open("colorguns.json", 'r'))['colorguns']
    
    # use default values
    blue = 79.923
    purple = 15.985
    pink = 3.1969
    red = .6394
    knife = .2558

    num_blue, num_purple, num_pink, num_red, num_knife = 0, 0, 0, 0, 0
    you_got = ""
    prizes = []
    for _ in range(num_cases):
      number = random.randint(0, 100)
      color = None

      if number < blue:
        color = 'Blue'
        num_blue += 1
      elif number < blue + purple:
        color = 'Purple'
        num_purple += 1
      elif number < blue + purple + pink:
        color = 'Pink'
        num_pink += 1
      elif number < blue + purple + pink + red:
        color = 'Red'
        num_red += 1
      else:
        color = 'Knife'
        num_knife += 1

      options = colorguns[color]
      prize = random.choice(options)
      prizes.append(prize + " - " + color)
      you_got += "You got a %s weapon: %s\n" % (color, prize)
      
    stats = """
You got %d blues
You got %d purples
You got %d pinks
You got %d reds
You got %d knives
""" % (num_blue, num_purple, num_pink, num_red, num_knife)

    await client.send_message(message.channel, you_got)
    await client.send_message(message.channel, stats)
    user_id = message.author.id # the user's unique discord id
    store_user_data(user_id, prizes) # function, pass it the discord message object, and a list of the prizes they won
  else:
    await client.send_message(message.channel, "Not enough money.")



@client.event
async def inventory_command(message):
  # open the data file
  data = json.load(open("data.json", 'r'))

  # if they have any data!
  if message.author.id in data:
    their_data = data[message.author.id] # their_data !
    bank = json.load(open("bank.json", 'r'))
    inventory = "Balance: " + str(bank[message.author.id]) + "\n"

    inventory += message.author.display_name + "'s inventory:\n" # the thing we print! (their invetory)
    for skin, count in their_data.items(): # go thru all their stuff
      inventory += "%d - %s\n" % (count, skin)

    # show the world
    await client.send_message(message.channel, '`' + inventory + '`')




@client.event
async def help_command(message):
  help_message = ""
  help_message += "!inv\n"
  help_message += "!sim 10\n" 
  help_message += "!give @Gryph#8627 Desert Eagle Conspiracy - Pink" 
  help_message = "```" + help_message + "```"
  embed = discord.Embed(title="Bot commands", description=help_message, color=0x00ff00)
  embed.add_field(name="!inv", value="Displays your current inventory.", inline=False)
  embed.add_field(name="!sim <number_of_box_openining>", value="Simulate box openings, max of 40.", inline=False)
  embed.add_field(name="!give <@user> <exact_name_of_gun>", value="Give a user one of your items from inventory.", inline=False)
  await client.send_message(message.channel, embed=embed)




@client.event
async def give_command(message):
  # gonna need the discord id of the user initiating giving
  user_id = message.author.id 
  parts_of_message = message.content.split(' ')
  gun = ' '.join(parts_of_message[2:])

  # "!give @user Tec-9 Fubar"

  # ["!give", "@user", "Tec-9", "Fubar"]
  #     0 .      1 .       2 .      3

  # see if they actually have the gun they want to give (look at their inventory)
  if not userHasGun(user_id, gun):
    await client.send_message(message.channel, '`You don\'t have that gun`')   
  else:
    
    # gonna need the discord id of user they are giving to
    users_mentioned = message.raw_mentions
    user_to_give_to_id = users_mentioned[0]

    # store user data, but the gun being given to them is the "prize"
    store_user_data(user_to_give_to_id, [gun])

    await client.send_message(message.channel, '`Trade successful!`')





def increase_balance(message):
    user_id = message.author.id
    bank = json.load(open("bank.json", 'r'))
    
    if user_id not in bank:
      bank[user_id] = 0

    bank[user_id] = bank[user_id] + 1

    # open the json file, and let's (w)rite to it
    with open('bank.json', 'w') as fp:
      json.dump(bank, fp)   
  
      
# http://prntscr.com/m9s69h #
 
# !sim
# "message"

def store_user_data(user_id, guns):
  """Stores user data so we can sell it later wait what"""
  data = json.load(open("data.json", 'r')) # a dictionary with user data
  
  # go through all the guns passed in, which we will put in inventory for user
  for gun in guns:

    # if the user has no data, give them a little empty like dictionary
    # thing so we can then give them data
    if user_id not in data:
      data[user_id] = {}

    # update the amount of each gun that they have, make sure
    # to handle the case where they don't have a gun they just won
    # so we have to use a default value bcuz otherwise python
    # will throw an error/exception bcuz they couldnt find the gun
    data[user_id][gun] = data[user_id].get(gun, 0) + 1

  # open the json file, and let's (w)rite to it
  with open('data.json', 'w') as fp:
      json.dump(data, fp)





def userHasGun(user_id, gun):
  data = json.load(open("data.json", 'r'))

  if user_id in data: # the user has data in the json file (AKA THEYVE PLAYED BEFORE)
    user_data = data[user_id]

    if gun in user_data and user_data[gun] > 0:
      user_data[gun] = user_data[gun] - 1
      # open the json file, and let's (w)rite to it
      with open('data.json', 'w') as fp:
        json.dump(data, fp)
      return True
    else:
      return False
  
  else: # user has no data, aka NO GUNS
    return False


 
client.run(os.environ['TOKEN'])
