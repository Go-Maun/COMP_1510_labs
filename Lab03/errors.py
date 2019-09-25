def zero_divide():
    """will create a divide by zero error"""
    zero = 0
    number = int(input("What number would you like to divide ny zero?: "))
    div_zero = number/zero
    return div_zero


def index_error():
    """will output multiple index error messages"""
    list_error01 = [0, 1, 2]
    list_error01[3]
    list_error02 = ["cat", "dog", "fish"]
    print(list_error02[4])


def type_error():
    """will output multiple type error messages"""
    len(42)
    error = "dog" + 2


def main():
    zero_divide()
    index_error()
    type_error()


main()
