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
                player.name = input(">")
                self.menu = False
                self.play = True
            elif menu_choice == "2":
                clear()
                print("The goal is to reach the top of the mountain.")
                clear()
            elif menu_choice == "3":
                os.system.exit()
            else:
                print("Incorrect input, please try again:")
                input("> ")

    def play_game(self):
        while self.play is True:
            print(
                f"Name: {player.name} \nHP: {player.get_health()} \nPotions: {player.potion} \n{player.get_inventory()})"
            )
            draw()


player = Player()
game = Game(player)
game.open_menu()
game.play_game()


# class Battle:
#     mob = NoisyMiner()
#     clear()
#     print("You have stumbled upon an enemy...")
#     draw()
#     print(f"Defeat the {mob.name}!")
#     mob.get_health()
#     draw()
