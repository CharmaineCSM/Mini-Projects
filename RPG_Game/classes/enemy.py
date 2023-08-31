class Enemy:
    """
    A class used to represent the Enemy

    Attributes
    ----------
    name : str
        name of enemy depending on random choice
    hp : int
        the hp of enemy
    hpmax : int
        the maximum amount of health of enemy
    """

    def __init__(self):
        """
        initialize the enemy's attribute
        """
        self.name = ""
        self.hp = 10
        self.hpmax = 10
        self.noise = "Roar"
        self.attack = 5

    def attack_character(self):
        """
        print enemy attack statement
        """
        print(f"{self.name} has dealt {self.attack} damage to player!")
        # p1.hp -= self.attack

    def get_health(self):
        """
        get HP/HPMAX stats for enemy
        """
        print(f"HP: {self.hp}/{self.hpmax}")


class NoisyMiner(Enemy):
    def __init__(self):
        Enemy.__init__(self)
        self.name = "Noisy Miner"
        self.hp = 15
        self.hpmax = 15

    def attack_character(self):
        print(f"{self.name} has dealt {self.attack} to player!")


class Magpie(Enemy):
    def __init__(self):
        Enemy.__init__(self)  # initialise parent class to inherite parent attributes
        self.name = "Magpie"
        self.hp = 30
        self.hpmax = 30
        self.attack = 30

    def attack_character(self):
        """
        Print higher attack statement for Magpie
        """
        print(f"{self.name} has dealt {self.attack} to player!")
