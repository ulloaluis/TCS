#!/usr/bin/env python3

import random


class Gun:
  def __init__(self, name, damage):
    self.name = name
    self.damage = damage

  def __repr__(self):
    return "%s (%d damage)" % (self.name, self.damage)
    # example: prints "AWP (100 damage)"

class CSGOPlayer:

  # class variables
  num_players = 0

  def __init__(self, name, gun):
    self.name = name

    self.hp = 100
    self.gun = gun # Gun class object

    self.alive = True

    CSGOPlayer.num_players += 1


  def shoots(self, other): # other is going to another CSGOPlayer
    # we shoot the other player
    # and they lose hp equal to our gun's damage

    if other.alive:
      other.hp = other.hp - self.gun.damage
      if other.hp <= 0:
        other.alive = False

      if not other.alive:
        print('%s shot %s dead for %d damage' % (self.name, other.name, self.gun.damage))
      else:
        print('%s shot %s for %d damage' % (self.name, other.name, self.gun.damage))
      # CSGOPlayer>Gun>shoot>damage

  def __repr__(self):
    return self.name


guns = [['AWP', 100], ['AK47', 36], ['P90', 26]]

# only 6 people in a game
a = CSGOPlayer('Player1', Gun(*random.choice(guns)))


# ['AWP', 100]
# *['AWP', 100]
# * "unpacks the elements" ----> so 'AWP', 100

# Gun(*random.choice(guns)) # step 1
# Gun(*['AWP', 100])       # step 2
# Gun('AWP', 100)


b = CSGOPlayer('Player2', Gun(*random.choice(guns)))
c = CSGOPlayer('Player3', Gun(*random.choice(guns)))
d = CSGOPlayer('Player4', Gun(*random.choice(guns)))
e = CSGOPlayer('Player5', Gun(*random.choice(guns)))
f = CSGOPlayer('Player6', Gun(*random.choice(guns)))

teamT = [a, b, c]
teamCT = [d, e, f]
in_game = teamT+teamCT

print(*in_game) # prints everyone in the game


for person in in_game:
  print("%s has %d hp with a(n) %s" % (person.name, person.hp, person.gun))
  # print("{} has {} hp".format(person.name, person.hp))


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


while True:
  T_player = choose_alive_player(teamT)
  CT_player = choose_alive_player(teamCT)

  if random.choice([True, False]):
    T_player.shoots(CT_player)
  else:
    CT_player.shoots(T_player)

  if team_alive(teamT) and not team_alive(teamCT):
    print('T wins')
    t_wins += 1
    break
  elif team_alive(teamCT) and not team_alive(teamT):
    print('CT wins')
    ct_wins += 1
    break
  elif not team_alive(teamCT) and not team_alive(teamT):
    print('draw')
    break

print('Round over.')


# how would we simulate several thousand games? (next time)


t_wins = 0
ct_wins = 0

# <Start of next lesson or after we develop our classes a bit more>

# print('probability of T winning: %f' % (t_wins / (t_wins + ct_wins)))
# print('probability of CT winning: %f' % (ct_wins / (t_wins + ct_wins)))

