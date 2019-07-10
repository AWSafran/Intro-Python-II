from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Methods

def parse_command(command, player):
    # make sure it's a valid command
    if command[0] == "get" or command[0] == "take":
        pickup_item = [item for item in player.room.items if item.name == command[1]]
        if len(pickup_item) == 0:
            print(f"There is no {command[1]} in this room")
        else:
            player.take_item(pickup_item[0])
            player.room.take_item(pickup_item[0])
    elif command[0] == "drop":
        drop_item = [item for item in player.inventory if item.name == command[1]]
        if len(drop_item) == 0:
            print(f"There is no {command[1]} in your inventory")
        else:
            player.drop_item(pickup_item[0])
            player.room.add_item(pickup_item[0])
        




# Declare Items

item = {
    'sword': Item("sword", "An old sword that doesn't look very strong"),
    'key': Item("key", "A shiny gold Key"),
    'book': Item("book", "A dusty book written in another language. You can't read any of it")
}

room['foyer'].add_item(item['book'])
room['narrow'].add_item(item['key'])
room['narrow'].add_item(item['sword'])


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
 
name = input("Please enter your name to begin: ")

player = Player(name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



print(f"You arrive at the {player.room.name}")
print(player.room.description)

while True:
    
    
    cmd = input("\nPlease enter a command: \n")

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
        parse_command(split_command, player)
    # See if they want inventory
    elif cmd == "i" or cmd == "inventory":
        player.print_items()
    # see if they even put in a real direction
    elif not cmd in next_room.keys():
        print("Not a valid Input")
    # checking to see if it's a room you can go to
    elif next_room[cmd] != None:
        player.room = next_room[cmd]
        print(f"\nYou arrive at the {player.room.name}\n")
        print(player.room.description)
        player.room.print_items()
    elif next_room[cmd] == None:
        print("You can not move that direction from here")

print("Thanks for playing!")

