import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """

    rolls a certain amount of die a certain amount of times

    :param number_of_rolls: the number of die to roll
    :param number_of_sides: the number of sides those die have
    :precondition: number must be a positive integer
    :post-condition: generates a total
    :return: returns the total of all the rolled die
    """
    total = 0
    if (number_of_rolls > 0) and (number_of_sides > 1):
        for value in range(1, number_of_rolls + 1):
            total += random.randint(1, number_of_sides)
        return total
    else:
        return "That's impossible."


def shop():
    """

    the list of shop items

    :return: the shop's list
    """
    store = ["Broad Sword", "Iron Dagger", "War Axe", "Shield", "Chain-mail Armour", "Leather Armour", "Cloth Robes",
             "100 Ball Barrings", "2 Health Potion", "50ft of Rope", "An Adventurer's Kit", "One Week of Provisions"]
    return store


def choose_inventory(inventory, selection):
    """

    selects items from the shop's list based on how many items the user wants

    :param inventory: the shops inventory
    :param selection: the number of items the user wants
    :precondition: an int has been input
    :post-condition: chooses items for the user
    :return: the items selected for the user
    """
    player_inventory = []
    if len(inventory) - 12 < selection <= len(inventory) - 1:
        for value in range(1, selection + 1):
            player_inventory.append(inventory[random.randint(0, len(inventory) - 1)])
            player_inventory.sort()
        return player_inventory
    elif selection == len(inventory) - 12:
        return player_inventory
    elif selection < len(inventory):
        return player_inventory
    elif selection >= len(inventory):
        player_inventory = inventory
        player_inventory.sort()
        return player_inventory


def choose_inventory_messages(inventory, player_inventory, selection):
    """

    gives the user a message based on their requested amount

    :param inventory: the shops inventory
    :param player_inventory: the players inventory
    :param selection: the number of items the user wants
    :precondition: an int has been input
    :post-condition: generates message
    :return: a message to the user
    """
    if len(inventory) - 12 < selection <= len(inventory) - 1:
        print("You are satisfied with your purchase.")
        print(player_inventory)
    elif selection == len(inventory) - 12:
        print("You walk back out, confident that your abilities will carry you on your adventure.")
        print(player_inventory)
    elif selection < len(inventory):
        print('"I uh... I dont think I can muster a negative amount of my wares." replied a confused Orvish\n'
              ' "Get out you creep!"')
        print(player_inventory)
    elif selection >= len(inventory):
        print("You walk out of the store with a smug look as you purchased everything Orvish had.")
        print(player_inventory)


def generate_name(syllables):
    """

    creates a random name for the user

    :param syllables: the number of syllables the user wants
    :precondition: number must be a positive integer
    :post-condition: outputs name
    :return: the full name, made into title case

    >>> generate_name(0)
    That's incorrect, your name is now Dummy
    'Dummy'

    >>> generate_name(-7)
    That's incorrect, your name is now Dummy
    'Dummy'
    """
    completed_name = ""
    if syllables > 0:
        for value in range(1, 1 + syllables):
            completed_name += generate_syllable(generate_vowel(), generate_consonant())
        return completed_name.title()
    else:
        print("That's incorrect, your name is now Dummy")
        completed_name = "Dummy"
        return completed_name


def generate_vowel():
    """

    generates a random number and converts that to a vowel

    :return: a random vowel

    """
    vowel = str(random.randint(1, 5))
    vowel = vowel.replace('1', "a").replace('2', "e").replace('3', "i").replace('4', "o").replace('5', "u")
    return vowel


def generate_consonant():
    """

    generates a random number and converts that to a consonant

    :return: a random consonant

    """
    consonant = random.randint(1, 21)
    if consonant < 10:
        consonant = str(consonant)
        consonant = consonant.replace('1', "b").replace('2', "c").replace('3', "d").replace('4', "f").replace('5', "g")\
            .replace('6', "h").replace('7', "j").replace('8', "k").replace('9', "l")
    elif consonant >= 10:
        consonant = str(consonant)
        consonant = consonant.replace('10', "m").replace('11', "n").replace('12', "p").replace('13', "q") \
            .replace('14', "r").replace('15', "s").replace('16', "t").replace('17', "v").replace('18', "w") \
            .replace('19', "x").replace('20', "y").replace('21', "z")
    return consonant


def generate_syllable(vowel, consonant):
    """

    concatenates the randomly generated vowel and consonant

    :param vowel: the generated vowel
    :param consonant: the generated consonant
    :return: the completed syllable

    >>> generate_syllable("a", "s")
    'as'

    >>> generate_syllable("o", "n")
    'on'

    >>> generate_syllable("e", "t")
    'et'
    """
    syllable = vowel + consonant
    return syllable


def create_character(name_length, inventory, selection):
    """

    creates a list with the fully created character

    :param name_length: the number of syllables the user wants
    :param inventory: the shops inventory
    :param selection: the number of items the user wants
    :precondition: name length is a number above 0
    :post-condition: returns list
    :return: the characters list
    """
    character = ["Name", generate_name(name_length)]
    strength = generate_strength()
    dexterity = generate_dexterity()
    constitution = generate_constitution()
    intelligence = generate_intelligence()
    wisdom = generate_wisdom()
    charisma = generate_charisma()
    create_list(character, strength, dexterity, constitution, intelligence,
                wisdom, charisma, choose_inventory(inventory, selection))
    return character


def create_list(character, a, b, c, d, e, f, inventory):
    """

    appends the character list

    :param character:
    :param a: the strength
    :param b: the dexterity
    :param c: the constitution
    :param d: the intelligence
    :param e: the wisdom
    :param f: the charisma
    :param inventory: the shops inventory
    :return: the character list fully appended
    """
    for value in range(1, 3):
        character.append(a.pop(0))
    for value in range(1, 3):
        character.append(b.pop(0))
    for value in range(1, 3):
        character.append(c.pop(0))
    for value in range(1, 3):
        character.append(d.pop(0))
    for value in range(1, 3):
        character.append(e.pop(0))
    for value in range(1, 3):
        character.append(f.pop(0))
    for value in range(0, len(inventory)):
        character.append(inventory.pop(0))
    return character


def generate_strength():
    """

    generates a random strength stat

    :return: a number from 3-18
    """
    strength = ["Strength", roll_die(3, 6)]
    return strength


def generate_dexterity():
    """

    generates a random dexterity stat

    :return: a number from 3-18
    """
    dexterity = ["Dexterity", roll_die(3, 6)]
    return dexterity


def generate_constitution():
    """

    generates a random constitution stat

    :return: a number from 3-18
    """
    constitution = ["Constitution", roll_die(3, 6)]
    return constitution


def generate_intelligence():
    """

    generates a random intelligence stat

    :return: a number from 3-18
    """
    intelligence = ["Intelligence", roll_die(3, 6)]
    return intelligence


def generate_wisdom():
    """

    generates a random wisdom stat

    :return: a number from 3-18
    """
    wisdom = ["Wisdom", roll_die(3, 6)]
    return wisdom


def generate_charisma():
    """

    generates a random charisma stat

    :return: a number from 3-18
    """
    charisma = ["Charisma", roll_die(3, 6)]
    return charisma


def print_character(character, selection):
    """

    prints out the character stats and inventory

    :param character: the character list
    :param selection: the number of items the user wants
    :return: the finalized print out
    """
    items = character[1] + "'s items: "
    if selection < 0:
        selection = 0
    if selection > 12:
        selection = 12
    if 0 < selection <= 12:
        print_character_items(character, selection, items)
    elif selection == 0:
        print_character_no_items(character, items)


def print_character_items(character, selection, items):
    """

    prints out the character when the user requested items

    :param character: the generated character list
    :param selection: the number of items the user requested
    :param items: the players inventory
    :return: prints a list with items in them
    """
    x = 0
    for value in range(0, (len(character) - (selection - 1)) // 2):
        print(character[x], ":", character[x + 1])
        x += 2
    x = len(character) - selection
    for content in range(0, selection):
        items += character[x] + ", "
        x += 1
    print(items)


def print_character_no_items(character, items):
    """

    prints out the character when the user doesnt request items

    :param character: the generated character list
    :param items: the number of items the user requested
    :return: prints a list without items
    """
    x = 0
    for value in range(0, (len(character)) // 2):
        print(character[x], ":", character[x + 1])
        x += 2
    print(items, "None")


def main():
    bought = int(input("How many items would you like to buy? "))
    choose_inventory_messages(shop(), choose_inventory(shop(), bought), bought)
    name = int(input("How many syllables should your name have? "))
    print_character(create_character(name, shop(), bought), bought)


if __name__ == "__main__":
    doctest.testmod()
    main()
