import math
import doctest


def eratosthenes(upper_bound: int) -> list:
    numbers = [x for x in range(0, upper_bound)]
    max_multiple = int(math.sqrt(upper_bound))
    prime_numbers_list = []
    non_prime_list = []
    for num in range(2, max_multiple + 1):
        if num not in non_prime_list:
            prime_numbers_list.append(num)
        non_prime_list += [x for x in range(num+num, upper_bound, num)]
    numbers_set = set(numbers)
    non_prime_set = set(sorted(non_prime_list))
    prime_numbers_list = sorted(list(numbers_set.difference(non_prime_set)))
    return prime_numbers_list


def main():
    answer = int(input("please choose a non inclusive positive upper bound: "))
    try:
        print(eratosthenes(answer))
    except:
        print("That number is invalid")


if __name__ == "__main__":
    main()
