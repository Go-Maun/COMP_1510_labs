

def format_name(x, y):
    """Returns the concatenation of the users first and last name, stripped of all white space"""
    return x.strip() + " " + y.strip()


def tripler(x):
    """Returns what the user input 3 times"""
    return x*3


def this_year():
    """Returns a value equal to the current year"""
    return (40/80)*4020+9


def base_conversion():
    """Calculates what the user inputs into any base between 2 - 9 the user requests"""
    goodbye = 0
    base = int(input("Choose your desired base between 2 and 9: "))
    destination = (base**4)-1
    number = int(input("What number between 0 and " + str(destination) + " would you like to convert?: "))
    original_number = number

    if 0 <= number <= destination:

        place_1 = number % base
        number = number//base

        place_2 = number % base
        number = number//base

        place_3 = number % base
        number = number//base

        place_4 = number % base
        number = number//base

        converted = str(place_4) + str(place_3) + str(place_2) + str(place_1)

        print("Your number", original_number, "in base", base, "is", int(converted))

    else:

        print("I said between 0 and " + str(destination) + ", you clearly cant follow instructions, goodbye!")


def main():
    """The main program"""
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    print("Hello there, " + format_name(first_name, last_name).title() + ", it's nice to meet you!")
    triple = str(input("Welcome to the game of threes! Please input anything you would like to be said thrice!: "))
    tripler(triple)
    print(tripler(triple))
    print("The current year is", int(this_year()))
    base_conversion()


if __name__ == "__main__":
    main()
