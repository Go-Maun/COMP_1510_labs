import doctest


def return_scenario(x_max: int, y_max: int) -> dict:
    """ returns a dictionary of the room to print

    :param x_max: the maximum room width
    :param y_max: the maximum room length
    :precondition: x and y max are positive integers
    :postcondition: creates a list
    :return: a dictionary for a function to print

    >>> return_scenario(5, 5)
    {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0, 1, 2, 3, 4], 4: [0, 1, 2, 3, 4]}

    >>> return_scenario(2, 2)
    {0: [0, 1], 1: [0, 1]}

    """
    room_dictionary = {y: [x for x in range(0, x_max)] for y in range(0, y_max)}
    return room_dictionary


def print_room(x_max: int, room_dictionary: dict, character_dictionary: dict):
    """ prints the room

    :param x_max: the maximum width
    :param room_dictionary: the rooms dictionary
    :param character_dictionary: the character dictionary
    :precondition: an int and 2 dictionaries are supplied
    :postcondition: prints the tiles and player
    :return: prints the room

    >>> print_room(5, {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0, 1, 2, 3, 4], 4: [0, 1, 2, 3, 4]}, {"position":[0,0]})
    You're currently at [0, 0]
    ◘ X X X X
    X X X X X
    X X X X X
    X X X X X
    X X X X X

    >>> print_room(3, {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2]}, {"position":[2,4]})
    You're currently at [2, 4]
    X X X
    X X X
    X X X
    X X X
    X X ◘

    """
    print("You\'re currently at", character_dictionary["position"])
    for y in room_dictionary:
        for x in room_dictionary[y]:
            x_y_position = [x, y]
            if x_y_position == character_dictionary["position"]:
                print_player(x_y_position, x_max, y)
            else:
                print_tile(x_y_position, x_max, y)


def print_tile(x_y_position: list, x_max: int, y: int):
    """ prints a tile depending on the x/y position

    :param x_y_position: the current x/y position
    :param x_max: the maximum width
    :param y: the current y value
    :precondition: a list and 2 ints are supplied
    :postcondition: prints the corresponding tile
    :return: prints a floor tile

    >>> print_tile([2,3], 3, 3)
    X
    """
    if x_y_position == [x_max - 1, y]:
        print("X")
    else:
        print("X", end=" ")


def print_player(x_y_position: list, x_max: int, y: int):
    """ prints the player depending on their x/y position

    :param x_y_position: the current x/y position
    :param x_max: the maximum width
    :param y: the current y value
    :precondition: a list and 2 ints are supplied
    :postcondition: prints the corresponding character
    :return: prints the player

    >>> print_player([2,3], 3, 3)
    ◘
    """
    if x_y_position == [x_max - 1, y]:
        print("◘")
    else:
        print("◘", end=" ")


def get_input() -> input:
    """ gets input from the user

    :return: the users input
    """
    print("")
    user_input = input("Type the dir. you would like to go ('up', 'down', 'left', 'right')")
    print("")
    return user_input


def test_input(user_input: str, x_max: int, y_max: int, character_dictionary: dict) -> dict:
    """ tests the users input

    :param user_input: the direction the user wants to go
    :param x_max: the maximum width
    :param y_max: the maximum length
    :param character_dictionary: the characters current position
    :precondition: direction is valid
    :postcondition: confirms the character movement
    :return: the changed character dictionary

    >>> test_input("up", 5, 5, {'position': [2, 4]})
    {'position': [2, 3]}

    >>> test_input("dog", 6, 17, {"position": [4, 15]})
    That is not a proper input
    {'position': [4, 15]}
    """
    if user_input.lower() in ("up", "down"):
        character_dictionary = move_player(user_input, y_max, 1, character_dictionary)
    elif user_input.lower() in ("left", "right"):
        character_dictionary = move_player(user_input, x_max, 0, character_dictionary)
    else:
        print("That is not a proper input")
    return character_dictionary


def move_player(user_input: input, position_max: int, position: int, character_dictionary: dict) -> dict:
    """ changes the character dictionary to match user input

    :param user_input: the user defined direction
    :param position_max: the maximum position
    :param position: the designated index of the values list
    :param character_dictionary: the characters dictionary
    :return: the changed character dictionary

    >>> move_player("up", 7, 0, {"position": [5, 6]})
    {'position': [4, 6]}

    >>> move_player("right", 8, 1, {"position": [1, 4]})
    {'position': [1, 5]}
    """
    if user_input.lower() in ("up", "left"):
        if character_dictionary["position"][position] != 0:
            character_dictionary["position"][position] -= 1
        else:
            print("You cant move", user_input.lower())
    elif user_input.lower() in ("down", "right"):
        if character_dictionary["position"][position] != position_max - 1:
            character_dictionary["position"][position] += 1
        else:
            print("You cant move", user_input.lower())
    return character_dictionary


def at_exit(character_dictionary: dict, x_max: int, y_max: int):
    """ tests whether the player has reached the exit

    :param character_dictionary:
    :param x_max: the maximum x value
    :param y_max: the maximum y value
    :return: true or false

    >>> at_exit({"position": [1,1]}, 2, 2)
    False

    >>> at_exit({"position": [5,8]}, 20, 20)
    True
    """
    if character_dictionary["position"] == [x_max - 1, y_max - 1]:
        return False
    else:
        return True


def game():
    character_dict = {"position": [0, 0]}
    board = return_scenario(5, 5)
    while at_exit(character_dict, 5, 5):
        print_room(5, board, character_dict)
        player_input = get_input()
        character_dict = test_input(player_input, 5, 5, character_dict)
    print("Congratulations, You escaped the maze!")


def main():
    game()


if __name__ == "__main__":
    doctest.testmod()
    main()
