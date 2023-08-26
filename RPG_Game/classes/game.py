import os
import time
import random
from enemy import NoisyMiner
from player import Player


def clear():
    """
    Function to clear console
    """
    os.system("cls" if os.name == "nt" else "clear")


def draw():
    """
    prints line/banner
    """
    print("─┉┈┈┈┈┈┈┈┈┈┈┈┈◈◉◈┈┈┈┈┈┈┈┈┈┈┈┈┉")


class Game:
    def __init__(self, player):
        self.menu = True
        self.play = False
        self.fight = False

    def open_menu(self):
        while self.menu is True:
            draw()
            print("WELCOME TO CHUM'S WORLD")
            draw()
            print("1.NEW GAME\n2.RULES\n3.EXIT")
            menu_choice = input("> ")
            if menu_choice == "1":
                clear()
                print("What is your name, warrior?")
                player.name = input("> ")
                self.menu = False
                self.play = True
                self.play_game()
            elif menu_choice == "2":
                clear()
                print("The goal is to reach the top of the mountain.")
                time.sleep(3)
                clear()
            elif menu_choice == "3":
                os.system.exit()
            else:
                print("Incorrect input, please try again:")
                input("> ")

    def battle(self):
        self.fight = True

        while self.standing is False:
            clear()
            print(f"You encountered an enemy...Defeat the {enemy.name}!")
            enemy.get_health()
            draw()
            print(f"Name: {player.name}")
            player.get_health()
            player.get_potion()
            draw()
            print("1. Attack \n2. Heal \n3. Run")

            battle_choice = input("> ")

            if battle_choice == "1":
                player.attack()
                enemy.attack_character()
                player.hp -= enemy.attack
                enemy.hp -= player.atk
                input("> ")
            elif battle_choice == "2":
                player.heal()
                enemy.attack_character()
                input("> ")
            elif battle_choice == "3":
                print("You can't run away...")
                input("> ")

    def play_game(self):
        x = 0
        y = 0
        x_max = 4
        y_max = 4
        self.standing = True

        while self.play is True:
            clear()
            print(f"Name: {player.name}")
            player.get_health()
            print(f"Potions: {player.potion}")
            player.get_inventory()
            print(f"COORD: {x}, {y}")
            draw()

            if x < x_max:
                print("1. EAST")
            if y < y_max or y == 0:
                print("2. SOUTH")
            if x > 0:
                print("3. WEST")
            if y > 0:
                print("4. NORTH")
            print("0. QUIT")
            draw()

            dest = input("> ")

            if dest == "0":
                self.play = False
                clear()
                self.menu = True
            elif dest == "1":
                if x < x_max:
                    x += 1
                    self.standing = False
            elif dest == "3":
                if x > 0:
                    x -= 1
                    self.standing = False
            elif dest == "2":
                if y < y_max:
                    y += 1
                    self.standing = False
            elif dest == "4":
                if y > 0:
                    y -= 1
                    self.standing = False

            battle_draw = random.randint(0, 100)

            if battle_draw < 80:
                self.battle()


player = Player()
enemy = NoisyMiner()

game = Game(player)
game.open_menu()
game.play_game()
