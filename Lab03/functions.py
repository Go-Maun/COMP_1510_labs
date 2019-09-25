import random


def roll_die(rolls, sides):
    """
    takes inputs of the amount of roles and how many sides and randomly chooses number(s) to give to the user
    :param rolls: the amount of times the user requests the dice to be rolled
    :param sides: the number od sides the requested dice have
    :return: returns the value of the different rolls to the system
    """
    total = ""
    if rolls == 3:
        roll01 = random.randint(1, sides)
        rolls = rolls - 1
        total = total + str(roll01) + " "
    if rolls == 2:
        roll02 = random.randint(1, sides)
        rolls = rolls - 1
        total = total + str(roll02) + " "
    if rolls == 1:
        roll03 = random.randint(1, sides)
        rolls = rolls - 1
        total = total + str(roll03) + " "
    if rolls == 0:
        value = print("Your rolls are:", total)
        return value


def create_name(length):
    """
    generates upto 5 random numbers and outputs a 'name'
    :param length: the length of the word the user requests
    :return: returns the 'name' to the program
    """
    name = ""
    if length == 5:
        letter = random.randint(1, 26)
        final_letter = convert_letter(letter)
        name = name + final_letter
        length = length - 1
    if length == 4:
        letter = random.randint(1, 26)
        final_letter = convert_letter(letter)
        name = name + final_letter
        length = length - 1
    if length == 3:
        letter = random.randint(1, 26)
        final_letter = convert_letter(letter)
        name = name + final_letter
        length = length - 1
    if length == 2:
        letter = random.randint(1, 26)
        final_letter = convert_letter(letter)
        name = name + final_letter
        length = length - 1
    if length == 1:
        letter = random.randint(1, 26)
        final_letter = convert_letter(letter)
        name = name + final_letter
        length = length - 1
    if length == 0:
        return name.title()


def convert_letter(x):
    """
    converts each randomly generated number into a letter
    :param x: each individual generated number
    :return: the letter corresponding with the number
    """
    if x < 10:
        x = str(x)
        letter = x.replace("1", "A").replace("2", "B").replace("3", "C").replace("4", "D") \
            .replace("5", "E").replace("6", "F").replace("7", "G").replace("8", "H").replace("9", "I")
        return letter
    if 10 <= x <= 19:
        x = str(x)
        letter = x.replace("10", "J").replace("11", "K").replace("12", "L").replace("13", "M").replace("14", "N")   \
            .replace("15", "O").replace("16", "P").replace("17", "Q").replace("18", "R").replace("19", "S")
        return letter
    if 20 <= x <= 26:
        x = str(x)
        letter = x.replace("20", "T").replace("21", "U").replace("22", "V").replace("23", "W").replace("24", "X")     \
            .replace("25", "Y").replace("26", "Z")
        return letter


number_of_rolls = int(input("How many times, up to three, would you like to roll a die? "))
number_of_sides = int(input("How many sides should that die have? "))
roll_die(number_of_rolls, number_of_sides)
length = int(input("Between 1 and 5, how many letters would you like?: "))
complete = create_name(length)
print(complete)
