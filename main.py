import random
import os
import time
import sys

#stats:
player_max_health = 10
player_health = 10
player_gold = 0
player_max_damage = 5
player_min_damage = 1

#Clear the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

#c
def get_user_choice(prompt, choices):
    user_choice = input(prompt).strip()
    while user_choice not in choices:
        cls()
        print("Please enter a valid input:", "/".join(choices))
        user_choice = input(prompt).strip()
    return user_choice

def slowType(str, delay):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)

monster_list = ["Goblin", "Slime", "Ogre", "Hilicurl"]
cls()
#Generic ahh rpg
if 1 == 1:
    print("$$$$$$\  $$$$$$$$\ $$\   $$\ $$$$$$$$\ $$$$$$$\  $$$$$$\  $$$$$$\         $$$$$$\  $$\   $$\ $$\   $$\       $$$$$$$\  $$$$$$$\   $$$$$$\ ")
    print("$$  __$$\ $$  _____|$$$\  $$ |$$  _____|$$  __$$\ \_$$  _|$$  __$$\       $$  __$$\ $$ |  $$ |$$ |  $$ |      $$  __$$\ $$  __$$\ $$  __$$\ ")
    print("$$ /  \__|$$ |      $$$$\ $$ |$$ |      $$ |  $$ |  $$ |  $$ /  \__|      $$ /  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ /  \__| ") #NOQA
    print("$$ |$$$$\ $$$$$\    $$ $$\$$ |$$$$$\    $$$$$$$  |  $$ |  $$ |            $$$$$$$$ |$$$$$$$$ |$$$$$$$$ |      $$$$$$$  |$$$$$$$  |$$ |$$$$\ ")
    print("$$ |\_$$ |$$  __|   $$ \$$$$ |$$  __|   $$  __$$<   $$ |  $$ |            $$  __$$ |$$  __$$ |$$  __$$ |      $$  __$$< $$  ____/ $$ |\_$$ /")
    print("$$ |  $$ |$$ |      $$ |\$$$ |$$ |      $$ |  $$ |  $$ |  $$ |  $$\       $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |      $$ |  $$ |")
    print("\$$$$$$  |$$$$$$$$\ $$ | \$$ |$$$$$$$$\ $$ |  $$ |$$$$$$\ \$$$$$$  |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |      \$$$$$$  |")
    print(" \______/ \________|\__|  \__|\________|\__|  \__|\______| \______/       \__|  \__|\__|  \__|\__|  \__|      \__|  \__|\__|       \______/ ")

#Introduce and names and shit
slowType("Made by BlastedMeteor44", 0.1)
print('\n \n \n')
slowType('Press enter to begin: ', 0.1)
input()
print("Welcome to the world!!")
world_name = input("Name the world: ")
print("Welcome to", world_name, "!")
player_name = input("Name the human: ")
player_name_lowered = player_name.lower()

if len(player_name_lowered) > 6:
    print("Your player name is greater than six characters. Please try again.")
elif player_name_lowered == "michae":
    print("Why didn't you include the L?")
elif player_name_lowered == "aaaaaa":
    print("Not very creative...")
elif player_name_lowered == "frisk":
    print("You do have to kill in this game, Frisk.")
else:
    print("Nice name!")

#Game loop
while True:
    cls()
    #at the top of the main menu
    print(f"The story of {player_name} in {world_name}")
    print(f"You have {player_gold} gold.")
    user_choice = get_user_choice("Options: \n1. Explore\n2. Shop\n3. Quit game\nWhat would you like to do? : ", ["1", "2", "3"])

    if user_choice == "1":
        cls()
        print("Exploring...")
        # choosing if you find a monster or not
        if random.choices([True, False], weights=[40, 60])[0]:
            monster = random.choice(monster_list)
            monster_health = random.randint(10,15)
            print("You found something!")
            print(f"It was a {monster} with {monster_health} health!")
            time.sleep(1)
            while monster_health > 0:
                cls()
                print(f"Your health: {player_health}")
                print(f"Opponent: {monster}. Opponent health: {monster_health}")
                
                action = get_user_choice("Options: \n1. Fight\n2. Flee\n3. Heal\nWhat would you like to do? : ", ["1", "2", "3"])
                if action == "1":
                    damage = random.randint(player_min_damage, player_max_damage)
                    monster_damage = random.randint(1,3)
                    monster_health -= damage
                    player_health -= monster_damage
                    if monster_health < 0:
                        monster_health = 0
                    if player_health < 0:
                        player_health = 0
                        cls()
                        print("You died")
                        exit()
                    if damage == 5:
                        print("Critical hit!")
                    print(f"You hit the {monster} for {damage} damage. The {monster} is now on {monster_health} health!")
                    print(f"The {monster} hit you for {monster_damage} damage. You are now on {player_health} health!")
                    time.sleep(1)
                    if monster_health <= 0:
                        print(f"The {monster} has been defeated!")
                        gold_earned = random.randint(4,10)
                        player_gold += gold_earned
                        player_health = player_max_health
                        print(f"You got {gold_earned} gold from the {monster}!")
                        time.sleep(1)
                        break
                elif action == "2":
                    print("Fleeing...")
                    player_health = player_max_health
                    time.sleep(1)
                    break
                elif action == "3":
                    print("Healing...")
                    player_health += 3
                    print(f"You healed 3 health! You are now on {player_health} health!")
                    time.sleep(1)
        else:
            print("You looked, but you found nothing.")
            time.sleep(1)
    elif user_choice == "2":
        print("Shopping...")
        while True:
            cls()
            print(f"Welcome, {player_name} to the generic ahh shop!\nYou have {player_gold} gold")
            print("\nItems for sale: \n Increase max health (5g): enter 1\n Increase damage (8g): enter 2\nEnter 3 to exit the shop.")
            user_choice = get_user_choice("What would you like to buy? :", ["1", "2", "3"])
            if user_choice == "1":
                if player_gold > 4:
                    player_max_health += 1
                    print(f"Your max health is now {player_max_health}!")
                    player_gold -= 5
                    time.sleep(1)
                else:
                    print("You don't have enough gold!")
                    time.sleep(1)
            elif user_choice == "2":
                if player_gold > 7:
                    player_max_damage += 1
                    player_min_damage += 1
                    print(f"Your max damage is now {player_max_damage} and your minimum damage is now {player_min_damage}!")
                    player_gold -= 8
                    time.sleep(1)
                else:
                    print("You don't have enough gold!")
                    time.sleep(1)
            elif user_choice == "3":
                print("Exiting the shop...")
                time.sleep(1)
                break
            else:
                print("Please enter a valid input (1/2/3)")
    elif user_choice == "3":
        slowType("Quitting game...", 0.2)
        exit()
