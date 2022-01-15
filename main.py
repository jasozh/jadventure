"""
Main program
"""

import time
import random
import sys

import world
import mapgen
import beginning
import valleys
import boss
import death
import commands

def main():
    try:
        if world.survive_num == 10 and world.continueplay == False:
            if world.boss_visited == False:
                print("""
Ahead of you is a single narrow path made up of red gravel. Bordering it is a
thick line of trees, but scraggly trees who are but mere skeletons of what they
once were. A dry gust strongly blows westward, and a black sun (a black sun?)
stands in the red sky, blacker than black yet more blinding than a star.""")

            else:
                print("Ahead of you is a narrow path made up of red gravel.")

            while True:
                print()
                print("""Where do you want to go?
[1] - Onwards to glory!
[2] - Run away""")
                ready = input(world.hpbar())

                if ready == '1':
                    boss.npc_help()
                    break
                elif ready == '2':
                    if world.gender == "male" and world.name != "Don Quixote" and world.name != "Don Quijote":
                        print("""Brave Sir %s ran away,
Bravely ran away away.

When danger reared its ugly head,
He bravely turned his tail and fled.

Yes, brave Sir %s turned about,
And gallantly he chickened out.

Bravely taking to his feet,
He beat a very brave retreat.""" % (world.name, world.name))
                        world.textbreak()
                        print("Bravest of the brave, Sir %s!" % world.name)
                        print()
                        death.run()
                        break
                    elif world.name == "Don Quixote" or world.name == "Don Quijote":
                        print("""Brave %s ran away,
Bravely ran away away.

When danger reared its ugly head,
He bravely turned his tail and fled.

Yes, brave %s turned about,
And gallantly he chickened out.

Bravely taking to his feet,
He beat a very brave retreat.""" % (world.name, world.name))
                        world.textbreak()
                        print("Bravest of the brave, %s!" % world.name)
                        print()
                        death.run()
                        break
                    else:
                        print("""Brave Dame %s ran away,
Bravely ran away away.

When danger reared its ugly head,
She bravely turned her tail and fled.

Yes, brave Dame %s turned about,
And gallantly she chickened out.

Bravely taking to her feet,
She beat a very brave retreat.""" % (world.name, world.name))
                        world.textbreak()
                        print("Bravest of the brave, Dame %s!" % world.name)
                        print()
                        death.run()
                        break
                elif ready == "s" or ready == "status":
                    commands.status_bar()
                elif ready == "h" or ready == "help":
                    commands.commandlist()
                elif ready == "v" or ready == "version":
                    commands.version()
                elif ready == "q" or ready == "quit":
                    commands.quitting()
                elif ready == "a" or ready == "attack":
                    print("You kick the ground in anger.")
                elif ready == "t" or ready == "trick":
                    print("You try to trick yourself. It works half the time!")
                elif ready == "d" or ready == "dance":
                    print("You are not in the mood for dancing.")

        else:
            '''
            print()
            print("You have come across two paths. Take which one? (1 or 2)")
            status_bar()

            pathluck = random.randint(1, 2)
            pathchoice = input(world.hpbar())

            if pathchoice == "1" or pathchoice == "2":
                pathchoice = int(pathchoice)

                if pathchoice == pathluck:
                    valleys.happy()
                else:
                    valleys.doom()
            else:
                print("Please enter '1' or '2'.")
            '''
            mapgen.callmaps()
            pathluck = random.randint(1, 2)
            if pathluck == 1:
                valleys.doom()
            elif pathluck == 2:
                valleys.happy()

    except KeyboardInterrupt:
        print()
        pass

    except EOFError:
        print()
        print("Not staying? That's too bad. See you soon!")
        sys.exit()

beginning.welcome()
mapgen.mapgen()
while True:
    main()
