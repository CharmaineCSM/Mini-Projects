import time
import random
import os

run = True
play = False
menu = True
standing = True

HP = 100
HPMAX = 100
inventory =['key']
ATK = 5 
potion = 1
x = 0
y = 0


        #  x = 0       x = 1     x = 3
map = [["plains",   "plains",   "plains"],    # y = 0
       ["forest",   "tower",    "plains"],     # y = 1
       ["forest",   "mountain", "forest"]]  # y = 2

    

#         #  x = 0       x = 1       x = 2       x = 3       x = 4       x = 5         x = 6
# map = [["plains",   "plains",   "plains",   "plains",   "forest", "mountain",       "cave"],    # y = 0
#        ["forest",   "forest",   "forest",   "forest",   "forest",    "hills",   "mountain"],    # y = 1
#        ["forest",   "fields",   "bridge",   "plains",    "hills",   "forest",      "hills"],    # y = 2
#        ["plains",     "shop",     "town",    "mayor",   "plains",    "hills",   "mountain"],    # y = 3
#        ["plains",   "fields",   "fields",   "plains",    "hills", "mountain",   "mountain"]]    # y = 4


y_len = len(map)-1 #number of row
#print(y_len)
x_len = len(map[0])-1 #number of column
#print(x_len)

biom = {
    "plains": {"title": "PLAINS", "e": True},
    "forest": {"title": "FOREST", "e": True},
    "tower": {"title": "TOWER", "e": True}, 
    "mountain": {"title": "MOUNTAINS", "e": True}
    }

#print(biom[map[2][1]]["title"])

e_list = ["Noisy Miner", "Magpie"]

mobs = {
    "Noisy Miner":{
        "hp": 15,
        "atk": 5},
    "Magpie":{
        "hp" : 50,
        "atk" : 15}
    }


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw():
    print("─┉┈┈┈┈┈┈┈┈┈┈┈┈◈◉◈┈┈┈┈┈┈┈┈┈┈┈┈┉")


def heal(amount):
    global HP
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    print(f"{name}'s HP refilled to {HP}!")

def battle():
    global fight, play, potion, HP, HPMAX
    enemy = random.choice(e_list)

    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["atk"]

    while fight:
        clear()
        draw()
        print(f"You have stumbled upon an enemy... \nDefeat the {enemy}!")
        print(f"{enemy}'s HP: {hp}/{hpmax}")
        draw()
        print(f"{name}'s HP: {HP}/{HPMAX}")
        print(f"HEALING POTIONS: {potion}")
        draw()
        print("Choose your option: \n 1 - ATTACK \n 2 - USE HEALING POTION (+30HP) \n 3 - RUN")
        draw()

        choice = input("> ")

        if choice == "1":
            hp -= ATK
            print(f"{name} has dealt {ATK} damage on {enemy}.")
            if hp > 0:
                HP -= atk #enemy attack back
                print(f"{enemy} has dealt {atk} damage to {name}.")
            input("> 'ENTER' to continue ")
        
        elif choice == "2":
            if potion >= 1:
                heal(30)
                HP -= atk
                potion -= 1
                print(f"{enemy} has dealt {atk} damage to {name}.")
            else:
                print("No potions!")
            input("> 'ENTER' to continue ")
        
        elif choice == "3":
            lucky_draw = random.randint(0,2)
            if lucky_draw == 0:
                print(f"You have escaped from {enemy}. PHEW! \n Now you are back to where you were before...")
                fight = False
            elif lucky_draw == 1:
                print(f"{enemy} screams: 'YOU CAN'T RUN FROM ME, CHILD!' ")
            input("> 'ENTER' to continue fighting")
            
        
        if HP <= 0:
            clear()
            print(f"{enemy} has deafeated {name}...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            clear()
            print(f"{name} has defeated the {enemy}!")
            draw()
            fight = False
            if random.randint(0, 50) < 20:
                potion += 1
                print("You have found a potion! YES!")
            input("> Press 'ENTER' to go back ")
            clear()




while run:
    while menu:

        print("Welcome to Chum's world!")
        draw()
        print("1. NEW GAME")
        print("2. RULES")
        print("3. QUIT")
        draw()
        
        choice = input("Pick your input> ")    
        
        if choice == "1":
            clear()
            print("What is your name, warrior")
            name = input("> ")
            menu = False
            play = True

        elif choice == "2":
            clear()
            menu = False
            print("This game .....")
            print("0--BACK")
            back = input()
            if back == "0":
                clear()
                menu = True
            else:
                print("Please type 0 to go back.")
                back = input()
                clear()
                menu=True
    
        elif choice == "3":
            sys.exit()

    while play:
        clear()

        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) < 30:
                    fight = True
                    battle()
            
            if random.randint(0, 50) < 25:
                potion += 1
                print("You have found a potion! YES!")
            
            if biom[map[y][x]]["title"] == "MOUNTAINS":
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
            print(f"NAME: {name}")
            print(f"HP: {HP}/{HPMAX}")
            print(f"Inventory Bag: {inventory}")
            print(f"Potions: {potion}")
            print(f"COORD: {x}, {y}")
            draw()
        

            if y > 0:
                print("1 - NORTH")
            if x < x_len:  #x_len is 1
                print("2 - EAST")
            if y < y_len: #y_len is 2
                print("3 - SOUTH")
            if x > 0:
                print("4 - WEST")
            print("0 -- QUIT")
            draw()

            dest = input("# ")

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


