def convert_to_roman_numeral(number):
    """
    converts a number up to 10000 to roman numerals
    :param number: the number to convert
    :return: the converted number
    """
    number = str(number)
    length = len(number)
    roman_number = ""
    if length == 5:
        roman_number = "MMMMMMMMMM"
        length = 0
    if length == 4:
        roman_number = thousands(number, roman_number)
        number = int(number) % 1000
        length -= 1
    if length == 3:
        roman_number = hundreds(number, roman_number)
        number = int(number) % 100
        length -= 1
    if length == 2:
        roman_number = tens(number, roman_number)
        number = int(number) % 10
        length -= 1
    if length == 1:
        roman_number = ones(number, roman_number)
        length -= 1
    if length == 0:
        return roman_number


def thousands(number, roman_number):
    """
    converts any number in the thousands placement
    :param number: the number the user input
    :param roman_number: where the converted number
    :return: the converted roman numeral
    """
    number_to_convert = str(int(number) // 1000)
    roman_number = roman_number + number_to_convert[0].replace("1", "M").replace("2", "MM").replace("3", "MMM") \
        .replace("4", "MMMM").replace("5", "MMMMM").replace("6", "MMMMMM").replace("7", "MMMMMMM") \
        .replace("8", "MMMMMMMM").replace("9", "MMMMMMMMM").replace("0", "")
    return roman_number


def hundreds(number, roman_number):
    """
    converts any number in the hundreds placement
    :param number: the number the user input
    :param roman_number: where the converted number
    :return: the converted roman numeral
    """
    number_to_convert = str(int(number) // 100)
    roman_number = roman_number + number_to_convert[0].replace("1", "C").replace("2", "CC").replace("3", "CCC") \
        .replace("4", "CD").replace("5", "D").replace("6", "DC").replace("7", "DCC").replace("8", "DCCC") \
        .replace("9", "CM").replace("0", "")
    return roman_number


def tens(number, roman_number):
    """
    converts any number in the tens placement
    :param number: the number the user input
    :param roman_number: where the converted number
    :return: the converted roman numeral
    """
    number_to_convert = str(int(number) // 10)
    roman_number = roman_number + number_to_convert[0].replace("1", "X").replace("2", "XX").replace("3", "XXX") \
        .replace("4", "XL").replace("5", "L").replace("6", "LX").replace("7", "LXX").replace("8", "LXXX") \
        .replace("9", "XC").replace("0", "")
    return roman_number


def ones(number, roman_number):
    """
    converts any number in the ones placement
    :param number: the number the user input
    :param roman_number: where the converted number
    :return: the converted roman numeral
    """
    number_to_convert = str(int(number) // 1)
    roman_number = roman_number + number_to_convert[0].replace("1", "I").replace("2", "II").replace("3", "III") \
        .replace("4", "IV").replace("5", "V").replace("6", "VI").replace("7", "VII").replace("8", "VIII") \
        .replace("9", "IX").replace("0", "")
    return roman_number


def main():
    positive_int = int(input("What number form 1 to 10,000 would you like converted to roman numerals?: "))
    print(convert_to_roman_numeral(positive_int))


if __name__ == "__main__":
    main()
