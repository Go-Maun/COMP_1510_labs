import random
import doctest


def list_tagger(batch):
    """ tags the lists length at the beginning of the list

    :param batch: the given list
    :precondition batch is a list:
    :postcondition tags the lists length:
    :return: the tagged list

    >>> list_tagger(['strength', 12, 'dexterity', 15, 'constitution', 4])
    [6, 'strength', 12, 'dexterity', 15, 'constitution', 4]

    >>> list_tagger(['one', 'two', 'three'])
    [3, 'one', 'two', 'three']
    """
    batch.insert(0, len(batch))
    return batch


def cutoff(integer_list, integer_multiple):
    """ counts the multiples of integer_multiple

    :param integer_list:
    :param integer_multiple:
    :precondition the list only has integers:
    :postcondidtion returns the multiples of integer_multiple:
    :return: the count variable

    >>> cutoff([1,3,5,7,9,11,13,15,17,19,21], 3)
    4

    >>> cutoff([5,10,15,20,25,30,35,40,45,50,55,60], 4)
    3
    """
    count = 0
    for number in integer_list:
        if number % integer_multiple == 0:
            count += 1
    return count


def prepender(string_list, new_string):  # function should modify the list without returning anything
    """ adds a word or phrase to each string in a list

    :param string_list: the list of strings
    :param new_string: the word to concatenate
    :precondition the list contains only strings:
    :postcondition the list gets modified:
    :return: the changed list

    >>> prepender(['got time for that'], 'aint nobody ')
    ['aint nobody got time for that']

    >>> prepender(['yo kids', 'yo wife'], 'hide ')
    ['hide yo kids', 'hide yo wife']
    """
    for value in range(len(string_list)):
        string_list[value] = new_string + string_list[value]
    print(string_list)  # dont know if this should be here


def name_list():
    """ sorts names by the number of letters

    :precondition the function is called:
    :postcondition creates a dictionary:
    :return: creates a dictionary with the length of names as the key
    """
    loop = True
    name_dict = {}
    while loop:
        name = input("Please type an name. Type \'quit\' to stop: ")
        if name.title() in "Quit":
            break
        name_length = len(name)
        if name_length not in name_dict:
            name_dict[name_length] = [name.title()]
        else:
            name_dict[name_length].append(name.title())
    return name_dict


def multiples_of_3(upper_bound):
    """ adds all multiples of 3 under the upper bound

    :param upper_bound: the requested upper bound
    :precondition the upper bound is a positive int above 1:
    :postcondition adds all multiples of 3:
    :return: the sum of all multiples of 3

    >>> multiples_of_3(10)
    18

    >>> multiples_of_3(100)
    1683
    """
    added = 0
    for number in range(1, upper_bound):
        if number % 3 == 0:
            added += number
    return added


def tally_die():
    """ rolls a die and tallies the result

    :precondition and int is input for sides and rolls:
    :postcondition prints the results:
    :return: prints how many times the die was rolled for each number
    """
    rolls = int(input("How many die would you like to roll: "))
    sides = int(input("How many sides do those die have: "))
    tally_total = {num: 0 for num in range(1, sides + 1)}
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
