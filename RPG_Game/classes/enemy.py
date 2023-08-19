from classes.player import Player

p1 = Player()

class Enemy:
  def __init__(self):
    self.name = ""
    self.hp = 10
    self.hpmax = 10
    self.noise = "Roar"
    self.attack = 5
  
  def attack(self):
    print(f"{self.name} has dealt {self.attack} damage to !")
    #p1.hp -= self.attack
    print(f" 's health is now.")
    
  def get_health(self):
    print(f"{self.name}'s health is {self.hp}/{self.hpmax}.")


class NoisyMiner(Enemy):
  def __init__(self):
    self.name = "Noisy Miner"
    self.hp = 15
    self.hpmax = 15
    self.noise = "TWEET TWEET!"
  
  def attack(self):
    print(f"{self.name} screams {self.noise} and dealt {Enemy.attack} to {p1.name} !")
  
  
class Magpie(Enemy):
  def __init__(self):
    self.name = "Magpie"
    self.hp = 30
    self.hpmax = 30
    self.noise = "KRAAWWWW KRAAWWW!"
  
  def special_attack(self):
    self.spec_attack = 30
    print(f"{self.name} dives from the tree and screams {self.noise} with a special attack and dealt {self.spec_attack} to p1!")
  
  def attack(self):
    print(f"{self.name} has dealt {Enemy.attack} to {p1.name}!")