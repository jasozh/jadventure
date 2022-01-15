"""
Code for the combat mechanism
"""

import time
import random

import world
import death

def combat():
    # monster variables
    monsdamage = random.randint(1, 5)

    fisthit = random.choice(world.fistflav)
    clubhit = random.choice(world.clubflav)
    swordhit = random.choice(world.swordflav)
    bowhit = random.choice(world.bowflav)
    dspearhit = random.choice(world.dragonspearflav)

    monshit = random.choice(world.monsflav)

    if world.inventory == 0:
        # fist deserves to be the weakest
        char_damage = random.randint(1, 2)
    elif world.inventory == 2:
        # sword does the most damage, as usual
        char_damage = random.randint(4, 8)
    elif world.inventory == 4:
        # ultra weapons deserve to be ultra
        char_damage = random.randint(7, 12)
    elif world.inventory == 3 and world.ammo == 0:
        print("Out of quarrels, you discard your empty crossbow.")
        world.textbreak()
        world.inventory = 0
        char_damage = random.randint(1, 2)
    else:
        # crossbow and club do the same damage
        char_damage = random.randint(2, 5)

    char_hitchance = random.randint(1, 5)
    if world.undead == 1:
        mons_hitchance = random.randint(1, 2)
        char_damage = char_damage - 2
        if char_damage < 1:
            char_damage = 1
    elif world.flying == 1 and world.inventory != 3 and world.inventory != 4:
        mons_hitchance = random.randint(1, 2)
        char_damage = char_damage - 3
        if char_damage < 1:
            char_damage = 1
    else:
        mons_hitchance = random.randint(1, 6)

    if char_hitchance == 1:
        if world.flying == 1 and world.inventory != 3 and world.inventory != 4:
            print("The %s nimbly dodges your effort to reach it."
                    % world.char_enemy)

        elif world.undead == 0:
            if world.inventory == 3:
                print("Your quarrel misses the %s!" % world.char_enemy)
                world.ammo = world.ammo - 1
            else:
                print("You miss the %s!" % world.char_enemy)
        
        elif world.undead == 1:
            if world.inventory == 3:
                print("Your quarrel flies straight through the %s!"
                        % world.char_enemy)
                world.ammo = world.ammo - 1
            elif world.inventory == 2:
                print("Your swing cuts harmlessly through the %s!"
                        % world.char_enemy)
            elif world.inventory == 1:
                print("Your club harmlessly passed through the %s!"
                        % world.char_enemy)
            elif world.inventory == 0:
                print("Your clumsy kick did no damage.")

    else:
        if world.inventory == 0:
            print("You %s the %s, dealing %d damage!"
                    % (fisthit, world.char_enemy, char_damage))
        if world.inventory == 1:
            print("You %s the %s, dealing %d damage!"
                    % (clubhit, world.char_enemy, char_damage))
        elif world.inventory == 2:
            print("You %s the %s, dealing %d damage!"
                    % (swordhit, world.char_enemy, char_damage))
        elif world.inventory == 3:
            print("Your quarrel %s the %s, dealing %d damage!"
                    % (bowhit, world.char_enemy, char_damage))
            world.ammo = world.ammo - 1
        elif world.inventory == 4:
            print("You %s the %s, dealing %d damage!"
                    % (dspearhit, world.char_enemy, char_damage))
        world.monsterhp = world.monsterhp - char_damage

        if world.monsterhp < 1:
            time.sleep(0.3)
            print("You have slain the %s!" % world.char_enemy)
            world.survive_num = world.survive_num + 1
            world.killcount = world.killcount + 1
            world.monsterhp = 9
            world.opchoice = 0
            world.textbreak()

    if world.opchoice == 1:
        if mons_hitchance == 1:
            time.sleep(0.3)
            print("The %s misses!" % world.char_enemy)
        else:
            time.sleep(0.3)
            print("The %s %s you, dealing %d damage!"
                    % (world.char_enemy, monshit, monsdamage))
            world.hp = world.hp - monsdamage

        if world.hp < 1:
            world.textbreak()
            death.death()
            world.monsterhp = 9
            world.opchoice = 0
