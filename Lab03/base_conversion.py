def base_conversion():
    """asks the user for a base and a number"""
    base = int(input("Choose your desired base between 2 and 9: "))
    destination = (base**4)-1
    number = int(input("What number between 0 and " + str(destination) + " would you like to convert?: "))
    if 0 <= number <= destination:
        calculations(base, number)
    else:
        wrong_input(destination)


def calculations(x, y):
    """calculates and prints the converted number"""
    original_number = y
    place_1 = remainder(x, y)
    y = new_divisor(x, y)
    place_2 = remainder(x, y)
    y = new_divisor(x, y)
    place_3 = remainder(x, y)
    y = new_divisor(x, y)
    place_4 = remainder(x, y)
    y = new_divisor(x, y)
    end_result(x, original_number, place_4, place_3, place_2, place_1)


def remainder(x, y):
    """finds the remainder number/base"""
    place = y % x
    return place


def new_divisor(x, y):
    """calculates a new value for the number variable"""
    number = y//x
    return number


def string_concatenation(a, b, c, d):
    """concatenates the new numbers together"""
    final = str(a) + str(b) + str(c) + str(d)
    return final


def end_result(x, y, a, b, c, d):
    """prints the end result"""
    print("Your number", y, "in base", x, "is", int(string_concatenation(a, b, c, d)))


def wrong_input(max):
    """tells the user that they input an invalid number"""
    print("I said between 0 and " + str(max) + ", you clearly cant follow instructions, goodbye!")


base_conversion()