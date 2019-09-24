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


base_conversion()