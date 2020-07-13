# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = items

    def move(self, possible_room):
        if possible_room:
            self.current_room = possible_room
        else:
            raise Exception('Invalid Room')
