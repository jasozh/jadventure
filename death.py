"""
What happens if player dies
"""

import time
import sys

import beginning
import world
import mapgen
import world

def death():
    print("You die...")
    time.sleep(0.3)
    stats()

def retire():
    print("You retire to a happy sunny farmhouse in Lenniqun...")
    world.survive_num = 0
    time.sleep(0.3)
    stats()

def run():
    print("Disgraced by all, you ran away, away, away...")
    time.sleep(0.3)
    stats()

def replayboss():
    world.hp = 20
    world.inventory = 0
    world.boss_death = False
    pass

def stats():
    if world.boss_death == True:
        points = (9 * world.survive_num) + (4 * world.killcount) + 250
    else:
        points = (9 * world.survive_num) + (4 * world.killcount)

    if world.boss_death == True:
        print("""
Farewell %s the %s! You have survived %d hostile encounter(s), killed
%d monster(s), and defeated %s. You have accumulated %d
points.
""" % (world.name, world.role, world.survive_num,
    world.killcount, world.boss_name, points))

    else:
        print("""
Farewell %s the %s! You have survived %d hostile encounter(s) and
killed %d monster(s). You have accumulated %d points.
""" % (world.name, world.role, world.survive_num,
    world.killcount, points))
    
    while True:
        try:
            if world.survive_num == 10 and world.boss_death == False:
                print("Would you like to respawn? (y/n)")
            else:
                print("Would you like to play again? (y/n)")
            playagain = input("> ")

            if playagain == 'y' or playagain == 'yes':
                if world.survive_num == 10 and world.boss_death == False:
                    world.hp = 20
                    world.inventory = 0
                    break
                else:
                    world.boss_death = False
                    world.hp = 20
                    world.wisdom = 0
                    world.inventory = 0
                    world.survive_num = 0
                    world.killcount = 0
                    world.ammo = 0
                    world.cheat_help = world.cheat_help + 1
                    beginning.welcome()
                    mapgen.mapgen()
                    break
            elif playagain == 'n' or playagain == 'no':
                print("That's too bad. See you soon!")
                sys.exit()
            else:
                print("Please enter 'yes' or 'no'.")
                print()

        except KeyboardInterrupt:
            print()

        except EOFError:
            print()
            print("Not staying? That's too bad. See you soon!")
            sys.exit()
