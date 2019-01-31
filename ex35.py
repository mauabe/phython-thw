from sys import exit

def gold_room():
  print ('This room is full of gold bars. Help yourself. How many do you take?');

  next = input('?: ')
  if '0' in next or '1' in next:
      how_much = int(next)
  else:
      dead('Man, learn to type a number.')

  if how_much < 50:
    print ('Nice, you\'re not greedy, you win!')
    exit(0)

  else:
    dead('You greedy bastard! Too heavy to carry. The bear ate you.')

def bear_room():
  print('There is a bear here.')
  print('The bear has a bunch of honey.')
  print('The fat bear is in front of another door.')
  print('How are you going to move the bear? "take the honey", "taunt the bear" or "poke it" ')
  bear_moved = False

  while True:
    next = input('?: ')

    if next == 'take the honey':
      dead('The bear looks at you then slaps your face off.')
    elif next == 'taunt the bear' and not bear_moved:
      print('The bear has moved from the door. You can go through it now. "open door"')
      bear_moved = True
    elif next == 'poke it' and not bear_moved:
      dead('The bear gets pissed off and chews your leg off.')
    elif next == 'open door' and bear_moved:
      gold_room()
    else:
      print('I got no idea what that means.')
      bear_room()

def cthulhu_room():
  print('Here you see the great evil Cthulhu.')
  print('He, it, whatever stares at you and you go insane.')
  print('Do you "flee" for your life or "eat" your head?')

  next = input('?: ')

  if 'flee' in next:
    start()
  elif 'eat' in next:
    dead('Well, that was tasty!')
  else:
    cthulhu_room()

def dead(why):
  print(why, 'Good job! Bye!')
  exit (0)

def start():
  print('You are in a dark room.')
  print('There is one door to your right and and one to your left.')
  print('Which one do you take? "right or "left" ')

  next = input('?: ')

  if next == 'left':
    bear_room()
  elif next == 'right':
    cthulhu_room()
  else:
    dead('You stumble around the room until you starve.')


start()



