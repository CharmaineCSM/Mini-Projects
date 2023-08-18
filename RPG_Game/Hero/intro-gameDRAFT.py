import os

play = False
battle = False
menu = True
rules = False
run = True

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def draw():
  print("xx--------------------------------------------------xx")
  

  
class Player:
  def __init__(self):
    self.name = ""
    self.hp = 100
    self.hpmax = 100
    self.potion =1 
    self.inventory = ['key']
  
  def attack(self):
    self.attack = 10
    #enemy.health = enemy.health - self.attack
    print(f"{self.name} has dealt {self.attack} to enemy.")
  
  def get_health(self):
    print(f"{self.name}'s health is {self.hp}/{self.hpmax}.")
    
  def get_inventory(self):
    print(f"Inventory Bag: {self.inventory}")
    
  def get_potion(self):
    print(f"Healing Potions: {self.potion}")
    
  def heal(self):
    amount = 30
    if self.hp == 100:
      print("Your health is full!")
    elif self.hp + amount < 100:
      return self.hp == self.hp + amount
      print(f"{self.name}'s HP has been refilled to {self.hp}.")

p1 = Player()

while run:
  while menu:
    print("Welcome to Chum's world!")
    draw()
    print("1. New Game \n2. Rules\n3. Quit")
    draw()
    choice = input(">")
    
    if choice == "1":
      clear()
      print("What is your name, warrior?")
      p1.name = input(">")
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
    draw()
    p1.get_health()
    p1.get_potion()
    p1.get_inventory()
    draw()
    print("LOCATION: ")
    draw()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
