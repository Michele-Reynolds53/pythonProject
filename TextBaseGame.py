# ************************************************************* #
#  Michele Reynolds                                             #
#  IT-140 - J6840  	                                            #
#  7-3 Project Two                                              #
#  August 12, 2023                                               #
#  Text-based adventure game                                    #
# ************************************************************  #
# Empty inventory list to store weapons
inventory = []

# Rooms dictionary
rooms = {
    # Grand Ballroom, directions to other rooms and weapon
    'Grand Ballroom': {
        'north': 'Hall',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Library',
    },
    # Kitchen, directions to other rooms and weapon
    'Kitchen': {
        'north': 'Grand Ballroom',
        'east': 'Conservatory',
    },
    # Library, directions to other rooms and weapon
    'Library': {
        'north': 'Study',
        'east': 'Grand Ballroom',
    },
    # Study, directions to other rooms and weapon
    'Study': {
        'south': 'Library',
        'east': 'Hall',
    },
    # Hall, directions to other rooms and weapon
    'Hall': {
        'south': 'Grand Ballroom',
        'east': 'Lounge',
        'west': 'Study',
    },
    # Lounge, directions to other rooms and weapon
    'Lounge': {
        'south': 'Dining Room',
        'west': 'Hall',
    },
    # Dining room, directions to other rooms and weapon
    'Dining Room': {
        'north': 'Lounge',
        'west': 'Grand Ballroom',
    },
}

# Weapons dictionary
weapons = {
    'Kitchen': 'Dagger',
    'Library': 'Lead Pipe',
    'Study': 'Monkey Wrench',
    'Hall': 'Revolver',
    'Lounge': 'Rope',
    'Dining Room': 'Candlestick',
}

# Assigned starting room
current_room = 'Grand Ballroom'

# Room killer is hiding
killer_room = 'Conservatory'

# Empty string to store directions
direction = ''

# list of valid directions
directions = ['north', 'south', 'east', 'west']

# Command player enters to exit the game
exit_command = "quit"

# Valid input is equal to the list of valid directions
valid_inputs = directions

# Message output when the player loses or quits the game
game_over = "The game is over. Thank you for playing."

# Output if player enters an invalid command
invalid_directions = "That is not a valid entry. Try again."

# Output if player heads the wrong way#
wrong_way = "You bumped into a wall."

err_msg = invalid_directions

win_game = 'Congratulations! You solved the murder!'

lose_game = 'Oh no! You ran into the killer and lost the game!!'


# Pauses game until player presses enter
def wait_to_continue():
    print('')
    input('Press enter to continue.')


# Function that introduces the game and the game's objective
def game_introduction():
    intro_text = '''
Murder Mystery Text Adventure Game
**********************************************************************************************

An event coordinator has planned a grand ball in a stunning mansion.
However, the celebrations turn dark when a murder occurs in the manor.
You have been called, as an investigator, to solve the murder.
'''

    print(intro_text)
    wait_to_continue()
    print('*************************************************************************************************')

    rooms_text = '''
There are eight rooms in the mansion, each room holds a crucial piece of evidence --
A weapon linked to the murder.

However, you must be cautious, because the killer is lurking in one of these rooms.
'''

    print(rooms_text)
    wait_to_continue()
    print('****************************************************************************************************')

    task_text = '''
Your task is to swiftly search and gather all the scattered weapons before encountering the killer.
You must collect all six weapons before you encounter the killer or you lose the game.
Are you up to the challenge?
'''

    print(task_text)
    wait_to_continue()
    print('*****************************************************************************************************')

    evidence_text = '''
You hold an evidence bag to collect the weapons. It is currently empty.
As you navigate from room to room, you will collect and add the evidence to your inventory.
'''
    print(evidence_text)
    wait_to_continue()
    print('*****************************************************************************************************')


if __name__ == '__main__':
    game_introduction()

# Tell the player which room they are starting in
print('You are in the', current_room)

# Game Loop

# As long as the player is playing the game:
while direction != 'quit':
    # Show what is in the player's inventory
    print(f'Inventory: {inventory}')

    # Show weapon information if available in the current room
    weapon_info = weapons.get(current_room)
    if weapon_info is not None and weapon_info not in inventory:
        print(f'You see a {weapon_info}')
        print("-------------------------------------------------------------------------------")
    else:
        print('There is no weapon in this room.')

    # Win/lose condition
    # If the player has six weapons in their inventory, they win the game
    if len(inventory) == 6:
        print("You have retrieved all six weapons!")
        print(win_game)
        print(game_over)
        break
    # If the player has less than six items in their inventory and enter the Conservatory, they lose
    elif len(inventory) < 6 and current_room == killer_room:
        print(lose_game)
        print(game_over)
        break

    # While the player is playing the game, tell them their move options
    possible_moves = rooms[current_room].keys()
    print('Your options are:', ', '.join(possible_moves))
    accessible_rooms = rooms[current_room].values()
    print(f'Accessible rooms from your current location are: {", ".join(accessible_rooms)}')
    print('----------------------------------------------------------------------------------------')

    # Prompt the player to input their move
    input_prompt = '''Enter your move. Your options are displayed above. Entry is not case sensitive. 
If you see a weapon, you may enter "get item" to retrieve it. If you wish to quit the game, you may enter "quit". '''
    print(input_prompt)
    direction = input('Enter your move. ').strip().lower()
    # Tell the player what they just entered
    print('You entered:', direction)
    # If the player enters 'quit', print game_over message
    if direction == 'quit':
        print(game_over)

    # If the player entered a valid direction, move in that direction
    elif direction in directions:
        if direction in possible_moves:
            # Set the new room as the current room
            new_room = rooms[current_room][direction]
            current_room = new_room
            # Print the current room player is in
            print('You are in the', new_room)
        # If the player entered an invalid direction, print wrong_way statement and list their choices
        else:
            # Print wrong way message and give the player valid options
            print(wrong_way)
            print('Your only choices are:', *possible_moves)

    # If the player enters 'get item'
    elif direction == 'get item':
        # If a weapon is in the current room
        if current_room in weapons:
            # If the weapon is already in your inventory print Item is already collected
            if weapons[current_room] in inventory:  # Corrected condition
                print('Item is already collected.')
            else:
                # Add weapon to player's inventory
                inventory.append(weapons[current_room])
                # Print you picked up and name of the weapon player just picked up
                print(f'You picked up the {weapons[current_room]}')
        else:
            # Otherwise, print if there is no weapon in the room
            print('There is no weapon in this room.')
    # Otherwise, print an error message if player did not make a valid move
    else:
        print(err_msg)
