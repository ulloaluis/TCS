#repl.it discord bot

import discord
import asyncio
import requests
import os
import random
import time
from random import randint

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('copy paste this in your browser to authorize bot https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(os.environ['CLIENTID']))
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith("!sim"):
      parts_of_message = message.content.split(' ')
      num_cases = int(parts_of_message[1])
      colorguns = {
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
          "M9 Bayonet - Autotronic",
          "Ursus Knife - Fade",
          "Talon Knife - Crimson Web"
        ]
      }

      # use default values
      blue = 79.923
      purple = 15.985
      pink = 3.1969
      red = .6394
      knife = .2558

      num_blue, num_purple, num_pink, num_red, num_knife = 0, 0, 0, 0, 0
      you_got = ""
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


client.run(os.environ['TOKEN'])
