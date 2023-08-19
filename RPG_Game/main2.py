import os
import time
import random
from classes.enemy import NoisyMiner, Magpie
from classes.player import Player

p1 = Player()

run = True
play = False
menu = True
standing = True

x = 0 
y = 0 

        #  x = 0       x = 1     x = 3
map = [["plains",   "plains",   "plains"],    # y = 0
       ["forest",   "tower",    "plains"],     # y = 1
       ["forest",   "mountain", "forest"]]  # y = 2

#number of rows
y_len = len(map)-1
#number of columns
x_len = len(map[0])-1

biom = {
    "plains": {"title": "PLAINS", "e": True},
    "forest": {"title": "FOREST", "e": True},
    "tower": {"title": "TOWER", "e": True}, 
    "mountain": {"title": "MOUNTAINS", "e": True}
    }

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def draw():
  print("─┉┈┈┈┈┈┈┈┈┈┈┈┈◈◉◈┈┈┈┈┈┈┈┈┈┈┈┈┉")



def battle():

  enemy_pick = random.randint(0,2)
  if enemy_pick == 0:
    current_enemy = NoisyMiner()
  else:
    current_enemy = Magpie()

  print(f"You have stumbled upon an enemy...Its a {current_enemy.name}!")
  print("Choose your option:")
  print("1.Attack\n2.Heal\n3.Run")

  choice = input(">")
  
  if choice == "1":
    p1.attack()
    current_enemy.attack()
    input(">")
  elif choice == "2":
    p1.heal()
    input(">")
  elif choice == "3":
    lucky_draw = random.randint(0,2)
    if lucky_draw == 0:
      print(f"You can't escape from {current_enemy.name}")
    elif lucky_draw == 1:
      print(f"You've managed to escape from {current_enemy.name}")
      fight = False



while run:
  while menu:
    print("Welcome to Chum's world!")
    draw()
    print("1. New Game \n2. Rules\n3. Quit")
    draw()
    choice = input(">")
    
    if choice == "1":
      clear()
      name = input("What is your name, warrior? >")
      p1.name = name
      menu = False
      play= True
      
    elif choice == "2":
      clear()
      menu=False
      print("The rules are meant to be broken...\n 0--BACK")
      back = input(">")
      clear()
      menu = True
      
    elif choice == "3":
      system.exit()
    
  while play:
    clear()

    if not standing:
      if random.randint(0,100) < 30:
        fight = True
        battle()

      elif random.randint(0, 50) < 25:
        p1.potion += 1
        print("You have found a potion! YES!")
      
      elif biom[map[y][x]]["title"] == "MOUNTAINS":
        clear()
        print("You've reached the top of the mountain...")
        time.sleep(3)
        print("Your breath coming in ragged gasps as you gaze out at the world spread beneath you.")
        time.sleep(3)
        print("Before you lies a small, weathered treasure box, nestled amidst the rocks and snow.")
        time.sleep(3)
        print("What could this box possibly contain? Gold and jewels, perhaps?")
        time.sleep(2)
        last_level = input("1. Use key from inventory\n2. Go back\n>")
        if last_level == "1":
            print("You have unlocked the treasure box... You look inside and see something moving... something ALIVE...")
            time.sleep(3)
            clear()
            print(")/_ \n<' \ \n/)  ) \n---/'-""---")
            print(" I guess its just a little cockatoo hehe")
            time.sleep(3)
            draw()
            print("------------END GAME---------------")
            input("> Press 'ENTER' to go back to MENU.")
            play = False
            clear()
            menu = True
        elif last_level == "2":
            input("> ")

    if play:
      print("Location: " + biom[map[y][x]]["title"])
      draw()
      print(f"NAME: {p1.name}")
      p1.get_health()
      p1.get_inventory()
      p1.get_potion()
      print(f"COORD: {x}, {y}")
      draw()

      if y > 0:
        print("1 - NORTH")
      if x < x_len: #x_len is 1
        print("2 - EAST")
      if y < y_len:
        print("3 - SOUTH")
      if x > 0:
        print("4 - WEST")
      print("0 - QUIT")
      draw()

      dest = input("> ")

      if dest == "0":
        play = False
        clear()
        menu = True
      elif dest == "1":
        if y > 0:
          y -= 1
          standing = False
      elif dest == "2":
        if x < x_len:
          x += 1
          standing = False
      elif dest == "3":
                if y < y_len:
                    y += 1
                    standing = False
      elif dest == "4":
          if x > 0:
              x -= 1
              standing = False
      else:
          standing = True

