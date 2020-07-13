from room import Room
from player import Player
from item import Item, LightSource

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room['foyer'].items.append(
    Item('note', 'a strange note scrawled in hasty strokes, "Turn back!"')
)
room['overlook'].items.append(Item('sword', 'a rusting but sharp sword.'))
room['narrow'].items.extend([
    Item('bones', 'pile of bones. more than could come from a single beast.'),
    Item('armor', 'a leather cuirass in suprisingly good condition...')
])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Nick', room['outside'], [
    Item('chainmail', 'bronze chainmail. poorly woven'),
    Item('axe', 'battle axe. powerful weapon when wielded properly'),
    Item('map', 'poorly draw map of dubious provenance'),
    LightSource('torch', 'a crudely made torch offering barely adequate lighting')

])

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


while True:
    print('\n')
    current_room = player.current_room
    player_has_lightsource = any([isinstance(item, LightSource) for item in player.inventory])
    if current_room.is_light or player_has_lightsource:
        print(current_room.name + ':')
        print(current_room.description)
        if current_room.items:
            print('You see: ' + ', '.join([str(item) for item in current_room.items]))
        else:
            print('There is nothing in this room.')
    else:
        print("You can't see anything in the darkness!")

    user_command = input('''
What would you like to do?
    Move? (n, e, s, w)
    Action? (take, drop, examine, inventory)
>> ''').split(' ')
    command_verb = user_command[0]
    command_object = None
    if len(user_command) == 2:
        command_object = user_command[1]

    if command_object:
        if command_verb in ('get', 'take'):
            try:
                room_item = next(item for item in current_room.items if item.name == command_object)
                player.inventory.append(room_item)
                current_room.items.remove(room_item)
                room_item.on_take()
            except StopIteration:
                print(f'There is no {command_object} in the room.')
        elif command_verb == 'drop':
            try:
                player_item = next(item for item in player.inventory if item.name == command_object)
                current_room.items.append(player_item)
                player.inventory.remove(player_item)
                player_item.on_drop()
            except StopIteration:
                print(f"You aren't carrying a {command_object}.")
        elif command_verb == 'examine':
            try:
                room_item = next(item for item in current_room.items if item.name == command_object)
                print(room_item.description)
            except StopIteration:
                print(f'There is no {command_object} in the room.')
        else:
            print('You cant do that.')
    else:
        try:
            if command_verb in ('n', 'north'):
                player.move(current_room.n_to)
            elif command_verb in ('e', 'east'):
                player.move(current_room.e_to)
            elif command_verb in ('s', 'south'):
                player.move(current_room.s_to)
            elif command_verb in ('w', 'west'):
                player.move(current_room.w_to)
            elif command_verb in ('i', 'inventory'):
                print('You are carrying: ' + ', '.join([str(item) for item in player.inventory]))
            elif command_verb in ('q', 'quit'):
                break
            else:
                print("You can't do that.")
        except Exception:
            print('\nYou cannot go that way.\n')





























