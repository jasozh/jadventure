"""
Boss fight and all its dependencies
"""

import time
import random
import sys

import world
import death
import commands

npc_dead = False
npc_hp = 20
boss_hp = 200

def npc_help():
    global npc_dead
    global npc_hp
    global boss_hp

    npc_dead = False
    npc_hp = 20
    boss_hp = 200

    bready = False
    print("""
A man appears from the trees, a man clad in steel. Another foe? \"Salutations
my friend. I am %s of al'Baham, Knight of the Cross and Warden of
Bak'al-Thur. I see you also seek to destroy %s. Let me be
of assistance to you.\"
""" % (world.npc_name, world.boss_name))
    while bready == False:
        try:
            print("Listen to him? (y/n)")
            npc_listen = input(world.hpbar())

            if npc_listen == 'y' or npc_listen == 'yes':
                print('''
\"Very well, %s. With me I have brought a legendary artifact from
Katobr, the dragonslayer spear used by Melbrith during the Dark Wars. It is to
be given only to the most able, and you have survived seven journeys into the
Blasted Lands. This I gift to thee.\"''' % world.role)
                world.inventory = 4
                world.textbreak()
                if world.hp != 20:
                    world.hp = 20
                    print("\"You are wounded. Hold on...\"")
                    world.textbreak()
                    print("%s casts a spell!" % world.npc_name)
                    time.sleep(0.3)
                    print("\033[0;34mYou are surrounded by a light blue aura.\033[0;m")
                    print()
                    time.sleep(0.3)

                print("\"Let us make haste, then. %s will be in his cave.\""
                        % world.boss_name)
                print()

                while True:
                    try:
                        print("Enter 'ready' to proceed.")
                        bossready = input(world.hpbar())

                        if bossready == 'ready':
                            bready = True
                            bossoptions()
                            break

                    except KeyboardInterrupt:
                        print()
                        pass

                    except EOFError:
                        print()
                        print("Not staying? That's too bad. See you soon!")
                        sys.exit()

            elif npc_listen == 'n' or npc_listen == 'no':
                # hint that maybe the NPC isn't so nice after all...
                print("""\"So be it then.\" Without even a glance, %s raised a hand, and at his
signal a storm of arrows fell down on you. Now that's just unfair!"""
% world.npc_name)
                world.textbreak()
                death.death()
                break

            else:
                print("Please enter 'yes' or 'no'.")

        except KeyboardInterrupt:
            print()
            pass

        except EOFError:
            print()
            print("Not staying? That's too bad. See you soon!")
            sys.exit()

def bossoptions():
    print("""
A monstrous creature slithers out of the cave, its scales glistening in the
black sun. A serpent, no a lizard, no... a dragon. You ready your spear and
prepare for battle. This is %s himself. The great dragon.

This will be his end."""
% world.boss_name)
    world.opchoice = 1
    while world.opchoice == 1:
        try:
            bo_choice = input(world.hpbar())

            if bo_choice == "s" or bo_choice == "status":
                commands.status_bar()
            elif bo_choice == "h" or bo_choice == "help":
                commands.commandlist()
            elif bo_choice == "v" or bo_choice == "version":
                commands.version()
            elif bo_choice == "q" or bo_choice == "quit":
                commands.quitting()
            elif bo_choice == "a" or bo_choice == "attack":
                bossfight()
            elif bo_choice == "t" or bo_choice == "trick":
                if npc_dead == False:
                    print("\"You can't fool %s!\" %s shouts."
                            % (world.boss_name, world.npc_name))
                else:
                    print("\"You can't fool me with your puny magic tricks,\" %s says." % world.boss_name)
            elif bo_choice == "d" or bo_choice == "dance":
                if npc_dead == False:
                    print("\"No, how could this be?\" cries %s. \"No. No! NOOOOO!\"" % world.boss_name)
                    world.textbreak()

                    print("""Your dance becomes more vibrant, and you jump gracefully as
%s screams in pain. %s's mouth drops open.
\"This was his weakness?\" """ % (world.boss_name, world.npc_name))
                    world.textbreak()

                    print("""%s's scales begin to blister, and pus flows out of his
once paralyzing eyes. Your feet move like a tornado, arms moving with
dexterous calm. With a final throat wrenching scream, %s
collapses. %s plunges his sword into the beast."""
    % (world.boss_name, world.boss_name, world.npc_name))
                    world.textbreak()
                    victory()
                    break
                else:
                    print("\"No, how could this be?\" cries %s. \"No. No! NOOOOO!\"" % world.boss_name)
                    world.textbreak()
                    print("""Your dance becomes more vibrant, and you jump gracefully as
%s screams in pain.""" % world.boss_name)
                    world.textbreak()
                    print("""%s's scales begin to blister, and pus flows out of his
once paralyzing eyes. Your feet move like a tornado, arms moving with
dexterous calm. With a final throat wrenching scream, %s
collapses. You plunge your spear into the beast."""
    % (world.boss_name, world.boss_name))
                    world.textbreak()
                    victory()
                    break

        except KeyboardInterrupt:
            print()
            pass

        except EOFError:
            print()
            print("Not staying? That's too bad. See you soon!")
            sys.exit()

def bossfight():
    global npc_dead
    global boss_hp
    global npc_hp

    # NPC stats
    npc_damage = random.randint(4, 16)
    npc_heal = random.randint(2, 10) # area heal

    # boss stats
    boss_damage = random.randint(9, 19)
    boss_breath = random.randint(4, 11) # area damage

    dragonspearhit = random.choice(world.dragonspearflav)
    npchit = random.choice(world.npcflav)
    bosshit = random.choice(world.bossflav)

    # here in case I decide in the future to add more weapons
    if world.inventory == 4:
        pldamage = random.randint(7, 12)

    pl_hitchance = random.randint(1, 5)
    npc_hitchance = random.randint(1, 7)
    boss_hitchance = random.randint(1, 4)

    # player hits first
    if pl_hitchance == 1:
        print("Your swing wildly misses %s." % world.boss_name)
        time.sleep(0.3)
    else:
        if world.inventory == 4:
            print("You %s %s, dealing %d damage!"
                    % (dragonspearhit, world.boss_name, pldamage))
            boss_hp = boss_hp - pldamage
            time.sleep(0.3)

            if boss_hp < 1:
                # if this ever runs, you are ultra-lucky
                time.sleep(0.3)
                victory()
                world.opchoice = 0

    # followed by the NPC
    if world.opchoice == 1:
        if npc_dead == False:
            if npc_hitchance == 1:
                print("%s's swing misses %s!"
                        % (world.npc_name, world.boss_name))
                time.sleep(0.3)
            
            elif npc_hitchance > 5:
                print("%s casts a spell!" % world.npc_name)
                time.sleep(0.3)
                print("\033[0;34m%s is surrounded by a light blue aura.\033[0;m"
                        % world.npc_name)
                print("\033[0;34mYou are surrounded by a light blue aura.\033[0;m")

                if (world.hp + npc_heal) > world.maxhp:
                    world.hp = world.maxhp
                else:
                    world.hp = world.hp + npc_heal

                if (npc_hp + npc_heal) > world.maxhp:
                    npc_hp = world.maxhp
                else:
                    npc_hp = npc_hp + npc_heal
                time.sleep(0.3)

            else:
                print("%s %s %s, dealing %d damage!"
                        % (world.npc_name, npchit, world.boss_name,
                            npc_damage))
                boss_hp = boss_hp - npc_damage
                time.sleep(0.3)

                if boss_hp < 1:
                    # if this ever runs, you are ultra-lucky
                    time.sleep(1)
                    victory()
                    world.opchoice = 0
        else:
            pass

    # and finally the boss
    if world.opchoice == 1:
        if boss_hitchance == 1:
            print("%s snaps wildly." % world.boss_name)
            time.sleep(0.3)

        elif boss_hitchance == 2:
            print("%s breathes fire, causing %d area damage!"
                    % (world.boss_name, boss_breath))
            world.hp = world.hp - boss_breath
            npc_hp = npc_hp - boss_breath
            time.sleep(0.3)

            if world.hp < 1:
                time.sleep(0.3)
                death.death()
                world.opchoice = 0
            elif npc_hp < 1 and npc_dead == False:
                time.sleep(0.3)
                npc_death()

        else:
            hitchoice = random.randint(1, 2)
            if hitchoice == 1:
                print("%s %s you, dealing %d damage!"
                        % (world.boss_name, bosshit, boss_damage))
                world.hp = world.hp - boss_damage
                time.sleep(0.3)

                if world.hp < 1:
                    time.sleep(0.3)
                    death.death()
                    world.opchoice = 0

            elif hitchoice == 2:
                if npc_dead == False:
                    print("%s %s %s, dealing %d damage!"
                            % (world.boss_name, bosshit, world.npc_name,
                                boss_damage))
                    npc_hp = npc_hp - boss_damage
                    time.sleep(0.3)

                    if npc_hp < 1 and npc_dead == False:
                        time.sleep(0.3)
                        npc_death()

                else:
                    print("%s %s you, dealing %d damage!"
                            % (world.boss_name, bosshit, boss_damage))
                    world.hp = world.hp - boss_damage
                    time.sleep(0.3)

                    if world.hp < 1:
                        time.sleep(0.3)
                        death.death()
                        world.opchoice = 0

def npc_death():
    global npc_dead
    print("""
\"Far from home I fall, but in vain 'tis not! Avenge me!\"
And with that, %s collapses in a pool of blood.""" % world.npc_name)
    npc_dead = True
    world.textbreak()

def victory():
    if npc_dead == False:
        print("""%s slumps to the ground, eyes blazing. "This is not the
end!" %s sputters, tail thrashing angrily. %s
steps back from the beast, blood-covered sword lowered. "It is done," he says.
"%s will trouble nor man nor creature any further."
And with that, %s collapses, dying in his own blood."""
% (world.boss_name, world.boss_name, world.npc_name,
    world.boss_name, world.boss_name))
    elif npc_dead == True:
        print("""%s slumps to the ground, eyes blazing. "This is not the
end!" %s sputters, tail thrashing angrily. And with that,
%s collapses, dying in his own blood."""
% (world.boss_name, world.boss_name, world.boss_name))

    world.boss_death = True
    world.textbreak()

    print("""Congratulations! You have reached the end of JAdventure.
Would you like to continue playing, retire, or replay the boss fight?""")

    while True:
        try:
            continue_choice = input("HP: %s(%s)> "
                    % (world.hp, world.maxhp))
            if continue_choice == 'continue':
                world.continueplay = True
                break
            elif continue_choice == 'retire':
                death.retire()
                break
            elif continue_choice == 'replay':
                death.replayboss()
                break
            else:
                print("Please enter 'continue', 'retire', or 'replay'.")

        except KeyboardInterrupt:
            print()
            pass

        except EOFError:
            print()
            print("Not staying? That's too bad. See you soon!")
            sys.exit()
