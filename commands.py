"""
All commands in JAdventure
"""

import sys

import world

def status_bar():
    inv_stat = ""
    wis_stat = ""

    if world.inventory == 0:
        inv_stat = "None"
    elif world.inventory == 1:
        inv_stat = "Club"
    elif world.inventory == 2:
        inv_stat = "Sword"
    elif world.inventory == 3:
        inv_stat = "Crossbow"
    elif world.inventory == 4:
        inv_stat = "Dragonslayer Spear"

    if world.wisdom == 0:
        wis_stat = "Low"
    elif world.wisdom == 1:
        wis_stat = "Medium"
    elif world.wisdom == 2:
        wis_stat = "High"
    elif world.wisdom > 2:
        wis_stat = "Very High"

    if world.ammo == 0:
        print("""Inventory: %s
Wisdom: %s""" % (inv_stat, wis_stat))
    else:
        print("""Inventory: %s, %d quarrel(s)
Wisdom: %s""" % (inv_stat, world.ammo, wis_stat))

def commandlist():
    print("""
Available Commands:
(s)tatus - Displays current inventory and wisdom level
(h)elp - Shows help
(v)ersion - Shows game version
(a)ttack - Attacks enemy
(t)rick - Attempt to trick enemy
(d)ance - Dance!
(q)uit - Quit the game""")

def version():
    print("""    _  _      _             _                
 _ | |/_\  __| |_ _____ _ _| |_ _  _ _ _ ___ 
| || / _ \/ _` \ V / -_) ' \  _| || | '_/ -_)
 \__/_/ \_\__,_|\_/\___|_||_\__|\_,_|_| \___|

Copyright © Jason Zheng 2016
Version 2.0""")

def quitting():
    while True:
        print("Are you sure you want to quit? (y/n)")
        quit = input(world.hpbar()) # <-- THIS DOESN'T WORK!!!
        if quit == "y" or quit == "yes":
            print("Are you really sure? (n/n)")
            quit2 = input(world.hpbar())
            if quit2 == "y" or quit2 == "yes":
                print("Are you really really not not not sure? (N/A)")
                quit3 = input(world.hpbar())
                if quit3 == "n" or quit3 == "no":
                    print("That's too bad. See you soon!")
                    sys.exit()
                elif quit3 == "y" or quit3 == "yes":
                    print("Great!")
                    break
                else:
                    pass
            elif quit2 == "n" or quit2 == "no":
                print("Great!")
                break
            else:
                pass
        elif quit == "n" or quit == "no":
            print("Great!")
            break
        else:
            pass
