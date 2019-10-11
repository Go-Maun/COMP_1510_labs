import random
import doctest


def roll_die(number_of_rolls, number_of_sides):
    """roll die

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
    """creates list

    the list of shop items

    :return: the shop's list
    """
    store = ["Broad Sword", "Iron Dagger", "War Axe", "Shield", "Chain-mail Armour", "Leather Armour", "Cloth Robes",
             "100 Ball Barrings", "2 Health Potion", "50ft of Rope", "An Adventurer's Kit", "One Week of Provisions"]
    return store


def choose_inventory(inventory, selection):
    """generates inventory

    selects items from the shop's list based on how many items the user wants

    :param inventory: the shops inventory
    :param selection: the number of items the user wants
    :precondition: an int has been input
    :post-condition: chooses items for the user
    :return: the items selected for the user

    >>> choose_inventory(["apples", "bananas", "soft pears", "crunchy pears"], 0)
    []

    >>> choose_inventory(["apples", "bananas", "soft pears", "crunchy pears"], -5)
    []

    >>> choose_inventory(["apples", "bananas", "soft pears", "crunchy pears"], 4)
    ['apples', 'bananas', 'crunchy pears', 'soft pears']
    """
    shop_stock = len(inventory)
    player_inventory = []
    if shop_stock - shop_stock < selection <= shop_stock - 1:
        for value in range(1, selection + 1):
            player_inventory.append(inventory[random.randint(0, shop_stock - 1)])
            player_inventory.sort()
        return player_inventory
    elif selection == shop_stock - shop_stock:
        return player_inventory
    elif selection < shop_stock:
        return player_inventory
    elif selection >= shop_stock:
        player_inventory = inventory[:]
        player_inventory.sort()
        return player_inventory


def choose_inventory_messages(inventory, player_inventory, selection):
    """generates a message

    gives the user a message based on their requested amount

    :param inventory: the shops inventory
    :param player_inventory: the players inventory
    :param selection: the number of items the user wants
    :precondition: an int has been input
    :post-condition: generates message
    :return: a message to the user

    >>> choose_inventory_messages(["apples", "bananas", "soft pears", "crunchy pears"], ["crunchy pears"], 1)
    <BLANKLINE>
    You are satisfied with your purchase.
    ['crunchy pears']

    >>> choose_inventory_messages(["crunchy pears"], ["crunchy pears"], 1)
    <BLANKLINE>
    You walk out of the store with a smug look as you purchased everything Orvish had.
    ['crunchy pears']

    >>> choose_inventory_messages(["apples", "bananas", "soft pears", "crunchy pears"], [], 0)
    <BLANKLINE>
    You walk back out, confident that your abilities will carry you on your adventure.
    []

    >>> choose_inventory_messages(["apples", "bananas", "soft pears", "crunchy pears"], [], -2)
    <BLANKLINE>
    "I uh... I dont think I can muster a negative amount of my wares." replied a confused Orvish
     "Get out you creep!"
    []
    """
    shop_stock = len(inventory)
    if shop_stock - shop_stock < selection <= shop_stock - 1:
        print("\nYou are satisfied with your purchase.")
        print(player_inventory)
    elif selection == shop_stock - shop_stock:
        print("\nYou walk back out, confident that your abilities will carry you on your adventure.")
        print(player_inventory)
    elif selection < shop_stock:
        print('\n"I uh... I dont think I can muster a negative amount of my wares." replied a confused Orvish\n'
              ' "Get out you creep!"')
        print(player_inventory)
    elif selection >= shop_stock:
        print("\nYou walk out of the store with a smug look as you purchased everything Orvish had.")
        print(player_inventory)


def generate_name(syllables):
    """generates a name

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
    """generates a vowel

    generates a random number and converts that to a vowel

    :return: a random vowel

    """
    vowel = str(random.randint(1, 6))
    vowel = vowel.replace('1', "a").replace('2', "e").replace('3', "i").replace('4', "o").replace('5', "u")\
        .replace("6", "y")
    return vowel


def generate_consonant():
    """generates a consonant

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
    """generates a syllable

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


def create_character(name_length):
    """generates a list

    creates a list with the fully created character

    :param name_length: the number of syllables the user wants
    :precondition: name length is a number above 0
    :post-condition: returns list
    :return: the characters list
    """
    character = ["Name", generate_name(name_length)]
    strength = generate_attribute("Strength", 3, 6)
    dexterity = generate_attribute("Dexterity", 3, 6)
    constitution = generate_attribute("Constitution", 3, 6)
    intelligence = generate_attribute("Intelligence", 3, 6)
    wisdom = generate_attribute("Wisdom", 3, 6)
    charisma = generate_attribute("Charisma", 3, 6)
    create_list(character, strength, dexterity, constitution, intelligence,
                wisdom, charisma)
    return character


def add_items_to_character(character, player_inventory):
    """adds items to character list

    adds the inventory to the characters list

    :param character: the character list
    :param player_inventory: the players inventory
    :return: returns a modified character list with the inventory added

    >>> add_items_to_character(["apple"], ["banana"])
    ['apple', ['banana']]

    >>> add_items_to_character(["sword", "shield"], ["57 gnoll ears"])
    ['sword', 'shield', ['57 gnoll ears']]
    """
    character.append(player_inventory[:])
    return character


def generate_attribute(name_of_attribute, number_of_dice, number_of_sides):
    """generates a stat

    generates a number for each dnd attribute

    :param name_of_attribute: the name of the stat being generated
    :param number_of_dice: the number of die to roll
    :param number_of_sides: the number of sides those dice have
    :return: a random number between 3 and 18 inclusive
    """
    return [name_of_attribute, roll_die(number_of_dice, number_of_sides)]


def create_list(character, strength, dexterity, constitution, intelligence, wisdom, charisma):
    """appends the character list

    puts every required value into a list

    :param character: the character list
    :param strength: the strength
    :param dexterity: the dexterity
    :param constitution: the constitution
    :param intelligence: the intelligence
    :param wisdom: the wisdom
    :param charisma: the charisma
    :return: the character list fully appended

    >>> create_list([1], [2], [3], [4], [5], [6], [7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    for value in range(0, len(strength)):
        character.append(strength.pop(0))
    for value in range(0, len(dexterity)):
        character.append(dexterity.pop(0))
    for value in range(0, len(constitution)):
        character.append(constitution.pop(0))
    for value in range(0, len(intelligence)):
        character.append(intelligence.pop(0))
    for value in range(0, len(wisdom)):
        character.append(wisdom.pop(0))
    for value in range(0, len(charisma)):
        character.append(charisma.pop(0))

    return character


def print_character(character):
    """prints the character

    prints out the character stats and inventory

    :param character: the character list
    :return: the finalized print out

    >>> print_character(["bananas?", "yes", "soft pears?", "no", "cats and dogs?", "cute"])
    bananas? : yes
    soft pears? : no
    cats and dogs? : cute
    """
    x = 0
    for value in range(0, (len(character)) // 2):
        print(character[x], ":", character[x + 1])
        x += 2


def print_items(player, inventory, selection):
    """prints the characters items

    prints out the inventory when the user requested items

    :param player: the generated character list
    :param inventory: the shops inventory
    :param selection: the number of items the user requested
    :return: prints a list with items in them

    >>> print_items(["name", "tim", ["c", "a"]], ["a", "b", "c", "d"], 2)
    tim's items: c, a,

    >>> print_items(["name", "tim", []], ["a", "b", "c", "d"], 0)
    tim's items:  None
    """
    x = 0
    items = player[1]+"'s items: "
    if selection < 0:
        selection = 0
    if selection > len(inventory) - 1:
        selection = len(inventory)
    if selection > 0:
        for content in range(0, selection):
            items += player[-1][x] + ", "
            x += 1
        print(items)
    elif selection <= 0:
        print(items, "None")


def main():
    bought = int(input("How many items would you like to buy? "))
    inventory_chosen = choose_inventory(shop(), bought)
    choose_inventory_messages(shop(), inventory_chosen, bought)
    name = int(input("How many syllables should your name have? "))
    character = create_character(name)
    print_character(character)
    add_items_to_character(character, inventory_chosen)
    print_items(character, shop(), bought)


if __name__ == "__main__":
    doctest.testmod()
    main()
