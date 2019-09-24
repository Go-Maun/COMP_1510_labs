def zero_divide():
    zero = 0
    number = int(input("What number would you like to divide ny zero?: "))
    div_zero = number/zero
    return div_zero


def index_error():
    list_error01 = [0,1,2]
    list_error01[3]
    list_error02 = [7,16,5,8,7]
    print(list_error02[5])


def type_error():
    len(42)
    error = "dog" + 2


def main():
    zero_divide()
    index_error()
    type_error()


main()