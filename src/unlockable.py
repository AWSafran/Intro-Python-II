from room import Room

class Unlockable(Room):
    def __init__(self, name, description, dark, item, activation_description, direction):
        super().__init__(name, description, dark)
        self.item = item
        self.activation_description = activation_description
        self.direction = direction
        self.secret_room = None
        self.activated = False

    def activate(self, item):
        if item == self.item and not self.activated:
            setattr(self, f"{self.direction}_to", self.secret_room)
            print(self.activation_description)
        else:
            print("Nothing happened")