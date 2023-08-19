class Player:
  def __init__(self):
    self.name = ''
    self.hp = 100
    self.hpmax = 100
    self.potion =1 
    self.inventory = ['key']
  
  def attack(self):
    self.attack = 10
    #enemy.health = enemy.health - self.attack
    print(f"{self.name} has dealt {self.attack} to enemy.")
  
  def get_health(self):
    print(f"HP: {self.hp}/{self.hpmax}")
    
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
 
