import random
import doctest


def list_tagger(batch):
    batch.insert(0, len(batch))
    return batch


def cutoff(integer_list, integer_multiple):
    count = 0
    for number in range(len(integer_list)):
        if number % integer_multiple == 0:
            count += 1
    return count


def prepender(string_list, new_string):  # function should modify the list without returning anything
    for value in range(len(string_list)):
        string_list[value] = new_string + string_list[value]
    print(string_list)  # dont know if this should be here


def name_list():
    loop = True
    name_dict = {}
    while loop:
        name = input("Please type an name. Type \'quit\' to stop: ")
        if name.title() in "Quit":
            break
        name_length = len(name)
        if name_length not in name_dict:
            name_dict[name_length] = list()
            name_dict[name_length].append((name.title()))
        else:
            name_dict[name_length].append(name.title())
    return name_dict


def multiples_of_3(upper_bound):
    added = 0
    for number in range(1, upper_bound):
        if number % 3 == 0:
            added += number
    return added


def tally_die():
    rolls = int(input("How many die would you like to roll: "))
    sides = int(input("How many sides do those die have: "))
    tally_total = {}
    for number in range(1, sides + 1):
        tally_total[number] = 0
    while rolls:
        value = random.randint(1, sides)
        tally_total[value] += 1
        rolls -= 1
    for key in tally_total:
        print(key, ":", tally_total[key])


def main():
    print(list_tagger(['cat', 'dog', 'mouse', 'rabbit']))
    print(cutoff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
    prepender(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], 'twenty-')
    print(name_list())
    print(multiples_of_3(40))
    tally_die()


if __name__ == "__main__":
    doctest.testmod()
    main()
