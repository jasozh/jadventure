### Version 2.1, January 2016
- Replaced manual textwrap with automatic textwrap

### Version 2.0, December 2016
- Bug fixes:
	- Fixed: Boss fight used non-existent status code
	- Fixed: Trickery failure descriptions don't match actual results
	- Fixed: Boss and NPC health magically regenerates after combat
	- Fixed: NPC continues to fight even after death
	- Fixed: Text overlap in retirement message
	- Fixed: Dance & trickery in boss fight "revives" NPC if previously killed
	- Fixed: Players respawn when killed after defeating the boss
	- Fixed: Boss remains killed even after player restarts game
	- Fixed: Game crashes when finding weapons while holding Dragonslayer Spear
	- Fixed: Surviving by failed trickery or dance does not register in game

- Combat:
	- Added bare-handed combat
	- Added ammunition system for crossbow
	- Added undead monster type (increased dodge rate)
	- Added damage penalty when attacking airborne monsters without crossbow

- Flavor:
	- Added more attack flavor messages
	- Improved random map generator
	- Added more monster names
	- New easter eggs
	- Boss names are now consistent for the entire game

- Graphics:
	- Healing spell effects now are shown in light blue font
	- HP bar now changes color depending on current HP
	- JAdventure title now written in ASCII art
	- Makeshift copyright symbol replaced with the actual symbol

- User interface:
	- Replaced some text breaks with terminal pager
	- Reintroduction of text delays (0.3 seconds)
	- Added basic commands
	- Removed prompt if player recieves a weapon that is currently held
	- Removed version informatin until recalled with command
	- Added prompts to yes or no questions
	- Minor text rewording
	- Increased  name limit from 9 to 15 characters
	- Added gender selection at game start

- Miscellaneous:
	- Reduced Vicar of Katobr role requirement to five deaths (was ten)
	- Vicar of Katobr inventory changed to sword and wisdom lowered to High
	- Updated boss combat system to latest features
	- Major code cleanup
	- ChangeLog and README cleanup

### Version 1.4, July 2016
- Fixed: Space after prompt was missing
- Minor text rewording
- Removed more text delays
- Added random maps
- Added increased monster variety

### Version 1.3, July 2016
- Minor text rewording
- Improved combat system
- Added constant HP status bar
- Added structure for basic commands
- Updated README and split ChangeLog

### Version 1.2, June 2016
- Fixed: Restarting after combat death leaves player still in combat
- Text delays replaced with NetHack-style terminal pager
- Insta-deaths replaced with a retreat and some HP loss

### Version 1.1, June 2016
- Fixed: Replaying boss fight does not revive the boss
- Fixed: Replaying boss fight leaves NPC dead if previously killed
- Boss attacks can no longer insta-kill
- Max HP properly added; healing will no longer go over max HP

### Version 1.0, June 2016
- Initial release