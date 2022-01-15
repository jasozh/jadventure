"""
All global variables for reference in other modules
"""

import getpass
import random

"""
Weak monsters needs items to kill
Strong monsters are the same, but have more HP
Flying monsters needs crossbow to kill
Tricky monsters needs wisdom to avoid
Boss monsters are... the boss
"""
weak_mons = ['goblin', 'kobold', 'pixie', 'dark elf', 'skeleton', 'newt',
        'gnoll']
strong_mons = ['golem', 'giant scorpion', 'beholder', 'daemon', 'cuttlefish',
        'behemoth', 'giant', 'giant rat', 'demon', 'troll',
        'genetically modified kobold', 'titan']
flying_mons = ['bat', 'vulture', 'gryphon', 'dragon hatchling', 'killer bee']
tricky_mons = ['chair', 'butterfly', 'striped ball', 'golden crown', 'windmill']
undead_mons = ['grimreaper', 'ghast', 'ghost', 'lich', 'spectre', 'banshee']
boss_mons = ['Jason the fire dragon', 'Vashik, Dragon of Baman']

# 0 = none; 1 = club; 2 = sword; 3 = crossbow; 4 = dragonslayer spear
inventory = 0
inv_names = ['club', 'sword', 'crossbow']
itemfound = 0
ammo = 0

# 0 = low; 1 = medium; 2 = high
wisdom = 0

"""
class Creature:
    def self:
        name = None
        hp = None
        maxhp = None
        role = None
        inv_stat = None
        wis_stat = None

    def describe:
        return "Hitpoints: %d(%d) \t Inventory: %s \t Wisdom: %s" % (hp, maxhp,
                inv_stat, wis_stat)

class Player:
    def self:
        maxhp = 20
        killcount = 0
        survive_num = 0
        cheat_help = 0

"""

# all player information is here
name = ""
role = ""
gender = ""
hp = 20
maxhp = 20
killcount = 0
survive_num = 0
cheat_help = 0
boss_death = False

# NPC information
npc_name = "Sir Edouard"

# allow first-time description
happy_visited = False
doom_visited = False

boss_visited = False

continueplay = False

# placeholder for options choice
opchoice = 1

# monster the player is going to face
char_enemy = ""
boss_name = random.choice(boss_mons)

# flavor texts
dancename = ['cha-cha', 'tango', 'ballet', 'Irish jig']

trickflav = ['You vanished in a puff of smoke. Now *that* was a good trick.',
        'You turned your pathetic foe into an ant. Squish.',
        'From your sleeve you pulled out a duelling pistol. Bam!',
        'You created a bunch of smoke and ran away in the confusion.']

trickfail = ['You artfully acted out your death. You forgot about vultures.',
        'You pulled a carnivorous rabbit out of your hat. You look tasty.',
        'You turned into a newt. Newts die very easily.',
        'While performing, you tripped and fell into a spiked pit.']

fistflav = ['punch', 'kick', 'bite', 'slap']
clubflav = ['beat', 'smack', 'bash', 'crush', 'grind', 'beat', 'smash']
swordflav = ['slash', 'cut', 'stab', 'gash', 'mince', 'lacerate']
bowflav = ['pierces', 'punctures', 'penetrates', 'perforates', 'drills into']

monsterhp = 9
undead = 0
flying = 0
monsflav = ['claws', 'bites', 'rakes', 'shreds', 'tears', 'bashes']

dragonspearflav = ['send twisting shockwaves into', 'brutally jab',
        'viciously stab']
npcflav = ['deeply gashes', 'plunges his sword into', 'viciously thrusts']
bossflav = ['eviscerates', 'tears deeply into', 'plunges his claws into']

# the NetHack solution: text breaks are now more flexible to the player
def textbreak():
    moveon = getpass.getpass(prompt = "--More--")
    if moveon == moveon:
        pass

# HP bar
def hpbar():
    hpstatus = ""

    if hp > 14: # 20-15 is first threshold
        hpstatus = "HP: \033[0;32m%d(%d)\033[0;m> " % (hp, maxhp)
    elif hp > 9 and hp < 15: # 15-10 is second threshold
        hpstatus = "HP: \033[0;33m%d(%d)\033[0;m> " % (hp, maxhp)
    elif hp > 4 and hp < 10: # 10-5 is third threshold
        hpstatus = "HP: \033[0;31m%d(%d)\033[0;m> " % (hp, maxhp)
    elif hp < 5: # 5-0 is fourth threshold
        hpstatus = "HP: \033[0;41m%d(%d)\033[0;m> " % (hp, maxhp)
    
    return hpstatus
