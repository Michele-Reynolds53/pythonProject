# ************************************************************* #
#  Michele Reynolds                                             #
#  IT-140 - J6840  	                                            #
#  6-4 Milestone: Moving Between Rooms#                         #
#  August 12, 2023                                              #
#  Revised Simplified version of the text-based game            #
# ************************************************************* #

# Empty inventory list to store weapons
inventory = []

# Starter Code from Sense
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# Weapons dictionary
weapons = {
    'Bedroom': 'Sword',
 }


DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Quit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " + \
                    str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You bumped into a wall."
GAME_OVER = "Thanks for playing."
EXIT_ROOM_SENTINEL = "Exit"
ERR_MSG = INVALID_DIRECTION

# Assigned starting room
current_room = 'Great Hall'


# Pauses game until player presses enter
def wait_to_continue():
    print('')
    input('Press enter to continue.')


# Function that introduces the game and the game's objective
def game_introduction():
    intro_text = '''
Moving Between Rooms
**********************************************************************************************
This is Simplified version of the text-based game  '''

    print(intro_text)
    wait_to_continue()
    print('*************************************************************************************************')


if __name__ == '__main__':
    game_introduction()

# Tell the player which room they are starting in
print('You are in the', current_room)

# Game Loop

# As long as the player is playing the game:
while DIRECTIONS != 'quit':
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
    if len(inventory) == 1:
        print("You have collected all the items.")
        if current_room == 'Cellar':
            print('You have defeated the Dragon!')
            print(GAME_OVER)


    # While the player is playing the game, tell them their move options
    possible_moves = rooms[current_room].keys()
    print('Your options are:', ', '.join(possible_moves))
    accessible_rooms = rooms[current_room].values()
    print(f'Accessible rooms from your current location are: {", ".join(accessible_rooms)}')
    print('----------------------------------------------------------------------------------------')

    # Prompt the player to input their move
    input_prompt = '''Enter your move. Your options are displayed above. Entry must be Title case. 
If you see a weapon, you may enter "get item" to retrieve it. If you wish to quit the game, you may enter "Quit". '''
    print(input_prompt)
    direction = input('Enter your move. ')
    # Tell the player what they just entered
    print('You entered:', direction)
    # If the player enters 'quit', print game_over message
    if direction == 'quit':
        print(GAME_OVER)

    # If the player entered a valid direction, move in that direction
    elif direction in DIRECTIONS:
        if direction in possible_moves:
            # Set the new room as the current room
            new_room = rooms[current_room][direction]
            current_room = new_room
            # Print the current room player is in
            print('You are in the', new_room)
        # If the player entered an invalid direction, print wrong_way statement and list their choices
        else:
            # Print wrong way message and give the player valid options
            print(CANNOT_GO_THAT_WAY)
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
        print(ERR_MSG)
