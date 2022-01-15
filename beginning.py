"""
Covers everything before main()
Includes welcome messges and choosing roles
"""

import sys

import world

def welcome():
    while True:
        try:
            print("What is your name?")
            world.name = input("> ")

            if len(world.name) > 15:
                print("Your name must be 15 characters or under.")
                print()

            elif len(world.name) == 0:
                pass
            else:
                break
        
        except KeyboardInterrupt:
            print()

        except EOFError:
            print()
            print("Not staying? That's too bad. See you soon!")
            sys.exit()

    choosing_roles()
    choosing_gender()
    if world.name != "Don Quixote" and world.name != "Don Quijote":
        print("Welcome to JAdventure, %s the %s %s!"
                % (world.name, world.gender, world.role))
    else:
        print("Welcome to JAdventure, %s the %s!"
                % (world.name, world.role))
    print("Enter 'help' for help!")

def choosing_roles():
    while True:
        try:
            print("""Choose your role:
[a] - Arbalist
[b] - Bandit
[k] - Knight
[s] - Sage
[t] - Tourist""")

            if world.cheat_help > 4:
                print("[v] - Vicar of Katobr")

            role_choice = input("> ")

            if role_choice == "a":
                world.inventory = 3
                world.ammo = 10
                world.role = "Arbalist"
                break
            elif role_choice == "b":
                world.inventory = 1
                world.role = "Bandit"
                break
            elif role_choice == "k":
                world.inventory = 2
                if world.name == "Don Quixote" or world.name == "Don Quijote":
                    world.role = "Ingenious Gentleman of La Mancha"
                    world.gender = "male"
                else:
                    world.role = "Knight"
                break
            elif role_choice == "s":
                world.wisdom = 2
                world.role = "Sage"
                break
            elif role_choice == "t":
                world.wisdom = 1
                world.role = "Tourist"
                break

            elif world.cheat_help > 4 and role_choice == "v":
                world.wisdom = 2
                world.inventory = 2
                world.role = "Vicar of Katobr"
                break

            else:
                print("Please choose from the following options.")
                print()

        except KeyboardInterrupt:
            print()

        except EOFError:
            print()
            print("Not staying? That's too bad. See you soon!")
            sys.exit()

def choosing_gender():
    while world.name != "Don Quixote" and world.name != "Don Quijote":
        try:
            print("""Choose your gender:
[f] - Female
[m] - Male""")
            gender_choice = input("> ")
            if gender_choice == "f":
                world.gender = "female"
                break
            elif gender_choice == "m":
                world.gender = "male"
                break
            else:
                print("Please choose from the following options.")
                print()

        except KeyboardInterrupt:
            print()

        except EOFError:
            print()
            print("Not staying? That's too bad. See you soon!")
            sys.exit()

