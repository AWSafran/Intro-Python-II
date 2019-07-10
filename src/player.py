# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def take_item(self, item):
        item.on_take()
        self.inventory.append(item)

    def drop_item(self, item):
        print(f"You dropped your {item.name}")
        self.inventory.remove(item)

    def print_items(self):
        if len(self.inventory) == 0:
            print("Your inventory is currently empty")
        else:
            for item in self.inventory:
                print(item)
    
