"""
Map generation
"""

import random
import sys

import world
import beginning
import namegen
import commands

r_descrip1 = ""
r_descrip2 = ""
r_descrip3 = ""
name_choice = ""

area1 = []
area2 = []
area3 = []
area4 = []
area5 = []

exits = []
player_area = 1

# format: choose one from each list; read top to bottom
descrip1 = ['desolate', 'ghostly', 'relaxing', 'cheerful', 'vast', 'abandoned',
        'ancient', 'beautiful', 'boring', 'charming', 'picturesque', 'creepy',
        'deserted', 'mysterious', 'calm', 'tranquil', 'unusual']
descrip2 = ['valley', 'town', 'citadel', 'farmland', 'grassland', 'trash can']
descrip3 = ['full of bugs', 'with scorch marks lying about',
        'covered in trash', 'that is eerily quiet', 'shrouded in fog']

def area_gen():
    global area1
    global r_descrip1
    global r_descrip2
    global r_descrip3
    global name_choice

    r_descrip1 = random.choice(descrip1)
    r_descrip2 = random.choice(descrip2)
    r_descrip3 = random.choice(descrip3)

    if r_descrip2 == "valley":
        name_choice = "Valley"
    elif r_descrip2 == "town":
        name_choice = "Town"
    elif r_descrip2 == "citadel":
        name_choice = "Castle"
    elif r_descrip2 == "farmland" or r_descrip2 == "grassland":
        name_choice = "Hamlet"
    elif r_descrip2 == "trash can":
        name_choice = "Waste Bin"

    namevary = random.randint(1, 2)
"""
    if namevary == 1:
        print("%s %s" % (name_choice, namegen.randomName()))
    else:
        print("%s %s" % (namegen.randomName(), name_choice))
    
    print("You have arrived in a %s %s %s." % (r_descrip1, r_descrip2,
        r_descrip3))

    area1 = [r_descrip1, r_descrip2, r_descrip3, name_choice,
            namegen.randomName()]
"""

def mapgen():
    global area1
    global area2
    global area3
    global area4
    global area5
    
    area_gen()
    area1 = [r_descrip1, r_descrip2, r_descrip3, name_choice,
            namegen.randomName(), 3, 5]
    area_gen()
    area2 = [r_descrip1, r_descrip2, r_descrip3, name_choice,
            namegen.randomName(), 3, 4]
    area_gen()
    area3 = [r_descrip1, r_descrip2, r_descrip3, name_choice,
            namegen.randomName(), 1, 2]
    area_gen()
    area4 = [r_descrip1, r_descrip2, r_descrip3, name_choice,
            namegen.randomName(), 2, 5]
    area_gen()
    area5 = [r_descrip1, r_descrip2, r_descrip3, name_choice,
            namegen.randomName(), 1, 4]

def callmaps():
    global player_area
    global exits

    #player_area = area1
    #exits = []

    if player_area == 1:
        exits = [area3[4], area5[4]]
    elif player_area == 2:
        exits = [area3[4], area4[4]]
    elif player_area == 3:
        exits = [area1[4], area2[4]]
    elif player_area == 4:
        exits = [area2[4], area5[4]]
    elif player_area == 5:
        exits = [area1[4], area4[4]]

    while True:
        print()
        print("Where do you want to go?")
        print("""[1] - %s
[2] - %s""" % (exits[0], exits[1]))
        '''
        print("%s    %s    %s    %s    %s" % (area1[4], area2[4], area3[4],
                                          area4[4], area5[4]))
        '''

        movechoice = input(world.hpbar())
        move = ""

        if movechoice == "1" or movechoice == "2":
            movechoice = int(movechoice) 

            if movechoice == 1:
                move = exits[0]
            elif movechoice == 2:
                move = exits[1]

        elif movechoice == "s" or movechoice == "status":
            commands.status_bar()
        elif movechoice == "h" or movechoice == "help":
            commands.commandlist()
        elif movechoice == "v" or movechoice == "version":
            commands.version()
        elif movechoice == "q" or movechoice == "quit":
            commands.quitting()
        elif movechoice == "a" or movechoice == "attack":
            print("You kick the ground in anger.")
        elif movechoice == "t" or movechoice == "trick":
            print("You try to trick yourself. It works half the time!")
        elif movechoice == "d" or movechoice == "dance":
            print("You are not in the mood for dancing.")

        else:
            pass

        if move == exits[0] or move == exits[1]:
            if move == area1[4]:
                print("%s %s" % (area1[3], area1[4]))
                print("You have arrived in a %s %s %s." % (area1[0], area1[1],
                    area1[2]))
                player_area = 1
                break
            elif move == area2[4]:
                print("%s %s" % (area2[3], area2[4]))
                print("You have arrived in a %s %s %s." % (area2[0], area2[1],
                    area2[2]))
                player_area = 2
                break
            elif move == area3[4]:
                print("%s %s" % (area3[3], area3[4]))
                print("You have arrived in a %s %s %s." % (area3[0], area3[1],
                    area3[2]))
                player_area = 3
                break
            elif move == area4[4]:
                print("%s %s" % (area4[3], area4[4]))
                print("You have arrived in a %s %s %s." % (area4[0], area4[1],
                    area4[2]))
                player_area = 4
                break
            elif move == area5[4]:
                print("%s %s" % (area5[3], area5[4]))
                print("You have arrived in a %s %s %s." % (area5[0], area5[1],
                    area5[2]))
                player_area = 5
                break
