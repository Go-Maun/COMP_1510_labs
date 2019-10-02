import random


def get_input():
    user_input = input("Enter a number: ")
    return user_input


def print_number(number):
    print(number)


def number_generator():
    random_number = random.randint(1, 100)
    return random_number
