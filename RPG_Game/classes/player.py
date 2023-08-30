class Player:
    """
    A class used to represent the Player

    Attributes
    ----------
    name : str
        name of player following input of user
    hp : int
        the hp of player
    hpmax : int
        the maximum amount of health of player
    potion : int
        the number of potions the player has
    inventory: list
        the items player has in inventory
    """

    def __init__(self):
        """
        initialize the players attribute
        """
        self.name = ""
        self.hp = 100
        self.hpmax = 100
        self.potion = 1
        self.inventory = ["key"]
        self.atk = 10

    def attack(self):
        """
        return player atk damage and print attack statement
        """
        # enemy.health = enemy.health - self.attack
        print(f"{self.name} has dealt {self.atk} to enemy.")

    def get_health(self):
        """
        to get HP/HPMAX stats for player
        """
        print(f"HP: {self.hp}/{self.hpmax}")

    def get_inventory(self):
        """
        to get player inventory
        """
        print(f"Inventory Bag: {self.inventory}")

    def get_potion(self):
        """
        get potion numbers of player
        """
        print(f"Healing Potions: {self.potion}")

    def heal(self):
        """
        when player chooses healing potion
        """
        if self.hp == 100:
            print("Your health is full!")
        elif self.hp < 100 and self.potion >= 1:
            self.hp == 100
            self.potion -= 1
            print(f"{self.name}'s HP has been refilled to {self.hp}.")
