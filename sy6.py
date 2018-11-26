#!/usr/bin/env python3

import random
import time
# import wait
################ IDEA LIST ################

##  

## Headshot Rate

## waiting between each message



class Gun:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage

  def __repr__(self):
    return "%s (%d damage)" % (self.name, self.damage)
    # example: prints "AWP (100 damage)"


class Skill:
  def __init__(self, rank):
    self.rank = rank # Global Elite
    self.miss_rate = None
    self.hs_rate = None

    if rank == 'Silver':
      self.miss_rate = 80
      self.hs_rate = 10
    elif rank == 'Gold Nova':
      self.miss_rate = 50
      self.hs_rate = 30
    elif rank == 'Master Eagle':
      self.miss_rate = 20
      self.hs_rate = 50
    elif rank == 'Global Elite':
      self.miss_rate = 5
      self.hs_rate = 90


class CSGOPlayer:

  # class variables
  num_players = 0

  def __init__(self, name, gun, skill):
    # instance variables
    self.name = name
    self.hp = 100
    self.gun = gun      # Gun class object
    self.skill = skill # Skill class object

    self.alive = True

    CSGOPlayer.num_players += 1


  def shoots(self, other): # other is going to another CSGOPlayer
    # we shoot the other player
    # and they lose hp equal to our gun's damage
 
    if other.alive:
      if self.skill.miss_rate < random.randint(1, 100): # X, (1, X) - don't shoot, (X, 100) shoot
        dmg_multiplier = 1

        if self.skill.hs_rate > random.randint(1, 100): # X, (1, X) - get a hs, (X, 100) don't get a hs
          dmg_multiplier *= 2

        other.hp = other.hp - (self.gun.damage * dmg_multiplier)
        if other.hp <= 0:
          other.alive = False

        if not other.alive:
          print_str = '%s (%s) shot %s (%s) dead for %d damage using a %s' % (self.name, self.skill.rank, other.name, other.skill.rank, self.gun.damage*dmg_multiplier, self.gun.name)

          if dmg_multiplier > 1:
            print_str += ' (HEADSHOT)'
          print(print_str, flush=True)

        else:
          print_str = '%s (%s) shot %s (%s) for %d damage using a %s' % (self.name, self.skill.rank, other.name, other.skill.rank, self.gun.damage*dmg_multiplier, self.gun.name)
        # CSGOPlayer>Gun>shoot>damage

          if dmg_multiplier > 1:
            print_str += ' (HEADSHOT)'
          print(print_str, flush=True)

      else: # miss case
        print('%s (%s) missed %s (%s) with %s' % (self.name, self.skill.rank, other.name, other.skill.rank, self.gun.name), flush=True)
 

  def __repr__(self):
    return self.name


def team_alive(team):
  for player in team:
    if player.alive:
      return True
  return False


def choose_alive_player(team):
  while True:
    player = random.choice(team)
    if player.alive:
      return player



guns = {"AWP":100, "AK47":36, "P90":26, "M4A4":36}

teamT = []
teamCT = []

print("Answer Various Questions:")
while True:
  name = input("Enter your CSGO name: ")
  team = input("What team are you on (CT or T)? ")
  gun = input("What gun are you using? ")
  skill = input("What rank are you? ")

  player = CSGOPlayer(name, Gun(gun, guns[gun]), Skill(skill))

  if team == "CT":
    teamCT.append(player)
  elif team == "T":
    teamT.append(player)

  answer = input("Any other players (y or n)? ")

  if answer == "n":
    break


while True:
  T_player = choose_alive_player(teamT)
  CT_player = choose_alive_player(teamCT)
  
  if random.choice([True, False]):
    T_player.shoots(CT_player)
  else:
    CT_player.shoots(T_player)

  time.sleep(0.5)

  if team_alive(teamT) and not team_alive(teamCT):
    print('T wins')
    break
  elif team_alive(teamCT) and not team_alive(teamT):
    print('CT wins')
    break
  elif not team_alive(teamCT) and not team_alive(teamT):
    print('draw')
    break

print('Round over.')
