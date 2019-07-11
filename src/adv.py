from room import Room
from unlockable import Unlockable
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", False),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Unlockable("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", False, "book", "From the rocks below, a bridge rises to traverse the canyon to the north", "n"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", True),
    'lighthouse': Room("Lighthouse", """The light at the top is out, but the embers of a recent fire stil burn. Someone has just been here. A dark path leads east""", False),
    'shed': Room("Shed", """Two skeletons lay side by side, mouths agape in agony. 
Fresh footprints lead to where they lay. Something dark is afoot""", False)
}

# Declare Items

item = {
    'sword': Item("sword", "An old sword that doesn't look very strong"),
    'key': Item("key", "A shiny gold Key"),
    'book': Item("book", "A dusty book written in another language. You can't read any of it"),
    'torch': Item("torch", "A burning torch hanging on the wall"),
    'treasure': Item("treasure", "A heavy bag of gold and diamonds, must be worth a lot!")
}

room['foyer'].add_item(item['book'])
room['narrow'].add_item(item['key'])
room['narrow'].add_item(item['sword'])
room['overlook'].add_item(item['torch'])
room['shed'].add_item(item['treasure'])


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['lighthouse'].s_to = room['overlook']
room['lighthouse'].e_to = room['shed']
room['shed'].w_to = room['lighthouse']
room['overlook'].secret_room = room['lighthouse']

 
name = input("Please enter your name to begin: ")

player = Player(name, room['outside'])



print(f"You arrive at the {player.room.name}")
print(player.room.description)

while True:
    
    
    cmd = input("\nPlease enter a command: \n")
    cmd = cmd.lower()

    if cmd == 'q':
        break

    next_room = {
        'n': player.room.n_to,
        'e': player.room.e_to,
        's': player.room.s_to,
        'w': player.room.w_to
    }

    split_command = cmd.split()

    # See if they did a pick up or drop command
    if len(split_command) == 2:
        player.parse_command(split_command)
    # See if they want inventory
    elif cmd == "i" or cmd == "inventory":
        player.print_items()
    # see if they even put in a real direction
    elif not cmd in next_room.keys():
        print("Not a valid Input")
    # checking to see if it's a room you can go to
    elif next_room[cmd] is not None:
        player.enter_room(next_room[cmd])
    elif next_room[cmd] is None:
        print("You can not move that direction from here")

    if player.escaped:
        break

print(f"Thanks for playing, {player.name}!")

