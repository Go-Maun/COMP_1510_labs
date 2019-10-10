import random


def roll_die(number_of_rolls, number_of_sides):
    total = 0
    if (number_of_rolls > 0) and (number_of_sides > 1):
        for value in range(1, number_of_rolls + 1):
            total += random.randint(1, number_of_sides)
        return total
    else:
        return "That's impossible."


def shop():
    store = ["Broad Sword", "Iron Dagger", "War Axe", "Shield", "Chain-mail Armour", "Leather Armour", "Cloth Robes",
             "100 Ball Barrings", "2 Health Potion", "50ft of Rope", "An Adventurer's Kit", "One Week of Provisions"]
    return store


def choose_inventory(inventory, selection):
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


def choose_inventory_messages(inventory, selection):
    if len(inventory) - 12 < selection <= len(inventory) - 1:
        print("You are satisfied with your purchase.")
    elif selection == len(inventory) - 12:
        print("You walk away, confident in your own items to carry you on your adventure.")
    elif selection < len(inventory):
        print("The shop owner is confused when you request negative amounts of stock.")
    elif selection >= len(inventory):
        print("You walk out of the store with a smug look as you purchased everything the shop keeper had.")


def generate_name(syllables):
    completed_name = ""
    for value in range(1, 1 + syllables):
        completed_name += generate_syllable(generate_vowel(), generate_consonant())
    return completed_name.title()


def generate_vowel():
    vowel = str(random.randint(1, 5))
    vowel = vowel.replace('1', "a").replace('2', "e").replace('3', "i").replace('4', "o").replace('5', "u")
    return vowel


def generate_consonant():
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
    syllable = vowel + consonant
    return syllable


def create_character(name_length, inventory, selection):
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


def generate_strength():
    strength = ["Strength", roll_die(3, 6)]
    return strength


def generate_dexterity():
    dexterity = ["Dexterity", roll_die(3, 6)]
    return dexterity


def generate_constitution():
    constitution = ["Constitution", roll_die(3, 6)]
    return constitution


def generate_intelligence():
    intelligence = ["Intelligence", roll_die(3, 6)]
    return intelligence


def generate_wisdom():
    wisdom = ["Wisdom", roll_die(3, 6)]
    return wisdom


def generate_charisma():
    charisma = ["Charisma", roll_die(3, 6)]
    return charisma


def print_character(character, selection):
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
    x = 0
    for value in range(0, (len(character)) // 2):
        print(character[x], ":", character[x + 1])
        x += 2
    print(items, "None")


def main():
    bought = int(input("How many items would you like to buy? "))
    choose_inventory_messages(shop(), bought)
    name = int(input("How many syllables should your name have? "))
    print_character(create_character(name, shop(), bought), bought)


if __name__ == "__main__":
    main()
