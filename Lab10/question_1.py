import math
import doctest


def eratosthenes(upper_bound: int) -> list:
    """ gets all prime numbers between 0 and upper_bound

    :param upper_bound: non inclusive integer upperbound
    :precondition: upper_bound must be positive
    :postcondition: calculates all prime numbers
    :return: a list of sorted prime numbers

    >>> eratosthenes(10)
    [2, 3, 5, 7]

    >>> eratosthenes(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    numbers = [x for x in range(0, upper_bound)]
    max_multiple = int(math.sqrt(upper_bound))
    prime_numbers_list = []
    non_prime_list = [0, 1]
    for num in range(2, max_multiple + 1):
        if num not in non_prime_list:
            prime_numbers_list.append(num)
        non_prime_list += [x for x in range(num + num, upper_bound, num)]
    numbers_set = set(numbers)
    non_prime_set = set(sorted(non_prime_list))
    prime_numbers_list = sorted(list(numbers_set.difference(non_prime_set)))
    return prime_numbers_list


def main():
    answer = int(input("please choose a non inclusive positive upper bound: "))
    try:
        print(eratosthenes(answer))
    except ValueError:
        print("That number is invalid")


if __name__ == "__main__":
    doctest.testmod()
    main()
