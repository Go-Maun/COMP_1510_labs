import random


def roll_die(rolls, sides):
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


number_of_rolls = int(input("How many times, up to three, would you like to roll a die? "))
number_of_sides = int(input("How many sides should that die have? "))
roll_die(number_of_rolls, number_of_sides)

