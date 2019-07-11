# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, dark):
        self.name = name
        self.description = description
        self.is_dark = dark
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def print_items(self):
        if len(self.items) == 0:
            print("The room is empty")
        else:
            print("The room contains the following items: ")
            for item in self.items:
                print(item)
    
    def add_item(self, item):
        self.items.append(item)
    
    def take_item(self, item):
        self.items.remove(item)