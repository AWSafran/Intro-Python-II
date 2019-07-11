# Write a class to hold player information, e.g. what room they are in
# currently.
from unlockable import Unlockable

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
        self.has_torch = False
        self.has_treasure = False
        self.escaped = False

    def take_item(self, item):
        item.on_take()
        self.inventory.append(item)
        self.room.take_item(item)
        if item.name == "torch":
            self.has_torch = True
        

    def drop_item(self, item):
        print(f"You dropped your {item.name}")
        self.inventory.remove(item)
        self.room.add_item(item)
        if item.name == "torch":
            self.has_torch = False

    def enter_room(self, room):
        self.room = room
        if room.name == "Outside Cave Entrance" and self.has_treasure:
            print("You Made it to safety!")
            self.escaped = True
        else:
            print(f"You arrive in the {room.name}")
            if not self.can_see() or self.has_treasure:
                print(f"It's too dark to see in here")
            else:
                print(room.description)
                room.print_items()

    def can_see(self):
        if self.room.is_dark and not self.has_torch:
            return False
        else:
            return True

    def print_items(self):
        if len(self.inventory) == 0:
            print("Your inventory is currently empty")
        else:
            for item in self.inventory:
                print(item)
    
    def take_treasure(self):
        self.has_treasure = True
        print("A darkness descends over the land. 100 torches couldn't illuminate your surroundings. \n It's time to go")

    def parse_command(self, command):
        # make sure it's a valid command
        if command[0] == "get" or command[0] == "take":
            pickup_item = None
            for item in self.room.items:
                if item.name == command[1]:
                    pickup_item = item
                    break
            if not self.can_see():
                print("It's way too dark to do that")
            elif pickup_item is None:
                print("That item is not in this room")
            else:
                self.take_item(pickup_item)
                if pickup_item.name == "treasure":
                    self.take_treasure()

        elif command[0] == "drop":
            drop_item = None
            for item in self.inventory:
                if item.name == command[1]:
                    drop_item = item
                    break
            if drop_item is None:
                print("You do not have that item in your inventory")
            else:
                self.drop_item(drop_item)
        elif command[0] == "use":
            use_item = False
            for item in self.inventory:
                if item.name == command[1]:
                    use_item = True
            
            if use_item:
                if isinstance(self.room, Unlockable):
                    self.room.activate(command[1])
                else:
                    print("Nothing happened")
            else:
                print("You do not have that item in your inventory")
    
