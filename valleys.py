"""
Code for entering the Valley of Doom and the Valley of Happiness
"""

import time
import random
import sys

import world
import combat
import death
import commands

# placeholder variables in order to work-around the local variable problem
flyenemy = ""
trickenemy = ""
weakenemy = ""
strongenemy = ""
undeadenemy = ""

trickchance = 0

def item_pickup():
    print("You found a %s!"
            % world.inv_names[world.itemfound - 1])
    if world.inventory == 0:
        world.inventory = world.itemfound
    elif world.inventory == world.itemfound:
        print("You toss your old %s aside."
                % world.inv_names[world.inventory -1])
        if world.inventory == 3:
            world.ammo = 10
        world.textbreak()
    elif world.inventory == 4:
        print("You laugh scornfully at the pathetic %s."
                % world.inv_names[world.itemfound - 1])
        world.textbreak()
        pass
    else:
        while True:
            try:
                print()
                print("Exchange your %s for the %s? (y/n)" %
                        (world.inv_names[world.inventory - 1],
                            world.inv_names[world.itemfound - 1]))
                take_choice = input(world.hpbar())
                if take_choice == 'y' or take_choice == 'yes':
                    print("You discard your previous item.")
                    world.inventory = world.itemfound
                    if world.inventory == 3:
                        world.ammo = 10
                    break
                elif take_choice == 'n' or take_choice == 'no':
                    print("You ignore the %s."
                            % world.inv_names[world.itemfound - 1])
                    break
                else:
                    print("Please enter 'yes' or 'no'.")

            except KeyboardInterrupt:
                print()

            except EOFError:
                print()
                print("Not staying? That's too bad. See you soon!")
                sys.exit()

def happy():
    '''    
    if world.happy_visited == False:
        print("""
You find yourself in a lush, green valley full of life. A gurgling stream lies
nearby, and the aroma of freshly bloomed flowers wafts towards you. Looking at
the clear blue sky, you relax, for you have arrived at the Valley of Happiness!
""")
        world.happy_visited = True
        world.textbreak()
    else:
        print()
        print("You have arrived again at the Valley of Happiness!")
    '''
    goodluck = random.randint(1, 8)

    # finding items
    if goodluck == 1:
        world.itemfound = 1
        item_pickup()
    elif goodluck == 2:
        world.itemfound = 2
        item_pickup()
    elif goodluck == 3:
        world.itemfound = 3
        item_pickup()
    
    # increasing wisdom
    elif goodluck == 4:
        print("You feel wise!")
        world.wisdom = world.wisdom + 1

    # rest of the time refills HP
    else:
        print("\033[0;34mYou are surrounded by a light blue aura.\033[0;m")
        world.hp = world.maxhp

def options():
    world.opchoice = 1
    options_firsttime = False

    while world.opchoice == 1:
        try:
            if options_firsttime == False:

                options_firsttime = True

            option_choice = input(world.hpbar())

            if option_choice == "a" or option_choice == "attack":
                combat.combat()
            elif option_choice == "h" or option_choice == "help":
                commands.commandlist()
            elif option_choice == "s" or option_choice == "status":
                commands.status_bar()
            elif option_choice == "q" or option_choice == "quit":
                commands.quitting()
            elif option_choice == "v" or option_choice == "version":
                commands.version()
                print()
            elif option_choice == "t" or option_choice == "trick":
                global trickchance

                if world.wisdom == 0:
                    print("The %s is not impressed by your puny magic tricks."
                            % world.char_enemy)
                    print("The %s attempts to eat you!" % world.char_enemy)
                    world.textbreak()
                    retreat()
                    break

                elif world.wisdom == 1:
                    trickchance = random.randint(1, 4)
                    trick_option()
                    break
                elif world.wisdom == 2:
                    trickchance = random.randint(1, 3)
                    trick_option()
                    break
                elif world.wisdom > 2:
                    trickchance = random.randint(1, 2)
                    trick_option()
                    break
                                    
            elif option_choice == "d" or option_choice == "dance":
                dance = random.choice(world.dancename)
                print("You dance the %s!" % dance)
                print("The %s attempts to eat you!" % world.char_enemy)
                world.textbreak()
                retreat()
                break
            else:
                pass

        except KeyboardInterrupt:
            print() 

        except EOFError:
            print()
            print("Not staying? That's too bad. See you soon!")
            sys.exit()

def trick_option():
    global trickchance

    if trickchance == 1:
        print(random.choice(world.trickflav))
        world.survive_num = world.survive_num + 1
    else:
        print(random.choice(world.trickfail))
        retreat()

def doom():
    global weakenemy
    global trickenemy
    global flyenemy
    global strongenemy
    global undeadenemy
    '''
    if world.doom_visited == False:
        print("""
You arrive at a desolate bleak valley, one eerily quiet. Tumbleweeds blow in
the harsh gust, and skeletal remains of massive creatures lie bleached under
the eternal red sun. A thin fog covers the area, and you begin to wonder what
might hide behind. This is indeed the Valley of Doom.
""")
        world.doom_visited = True
        world.textbreak()
    else:
        print()
        print("You have arrived again at the Valley of Doom!")
    '''
    # monster generation
    weakgen = random.choice(world.weak_mons)
    strong_gen = random.choice(world.strong_mons)
    flygen = random.choice(world.flying_mons)
    trickgen = random.choice(world.tricky_mons)
    undeadgen = random.choice(world.undead_mons)

    weakenemy = weakgen
    strongenemy = strong_gen
    flyenemy = flygen
    trickenemy = trickgen
    undeadenemy = undeadgen

    enemyclass = [flyenemy, trickenemy, weakenemy, strongenemy, undeadenemy]

    world.char_enemy = random.choice(enemyclass)
    print("A %s appears out of nowhere!" % world.char_enemy)
    world.undead = 0
    world.flying = 0

    if world.char_enemy == trickenemy:
        print()
        print("What magnificent beauty! You reach out to the %s..."
                % world.char_enemy)
        time.sleep(0.3)

        if world.wisdom < 2:
            print("...and the %s bursts into flames." % world.char_enemy)
            world.textbreak()
            retreat()
        else:
            print("...but you notice the trap and step back.")
            world.survive_num = world.survive_num + 1
            world.textbreak()
    else:
        if world.char_enemy == strongenemy:
            world.monsterhp = 15
        elif world.char_enemy == undeadenemy:
            world.undead = 1
        elif world.char_enemy == flyenemy:
            world.flying = 1
        options()

def retreat():
    rundamage = random.randint(5, 15)
    world.hp = world.hp - rundamage

    if world.hp < 1:
        death.death()
    else:
        print("You barely escape, suffering %d damage."
                % rundamage)
        world.survive_num = world.survive_num + 1
    pass
