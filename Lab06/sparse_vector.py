import doctest
"""
The reason we cannot get the length of a sparse vector is because they can have a
large amount of 0's padding the size by a large amount. I need to ask them if storing those sparse vectors
in dictionaries will work for the way they are implementing their code.
"""


def sparse_add(dictionary_one, dictionary_two):
    """creates new dictionary

    :param dictionary_one: the first dictionary
    :param dictionary_two: the second dictionary
    :return: the sorted list

    >>> sparse_add({1:8, 3:1, 4:2}, {1:1, 4:1, 6:4})
    {1: 9, 3: 1, 4: 3, 6: 4}

    >>> sparse_add({1:2, 4:3, 9:6}, {1:-2, 5:2, 8:10})
    {4: 3, 5: 2, 8: 10, 9: 6}

    >>> sparse_add({}, {1:5, 4:1, 5:8})
    {1: 5, 4: 1, 5: 8}
    """
    dict_output = {}
    for key in dictionary_one:
        if key in dictionary_two:
            dict_output[key] = dictionary_one[key] + dictionary_two[key]
        elif key not in dictionary_two:
            dict_output[key] = dictionary_one[key]
    for key in dictionary_two:
        if key not in dictionary_one:
            dict_output[key] = dictionary_two[key]
    sort = sorted(dict_output)
    sorted_dictionary = {}
    for item in sort:
        if dict_output[item] == 0:
            continue
        sorted_dictionary[item] = dict_output[item]
    return sorted_dictionary


def main():
    dict_one = {2: -2, 4: 4, 15: 5}
    dict_two = {2: 2, 5: 1, 7: 6, 13: 2}
    completed_dictionary = sparse_add(dict_one, dict_two)
    print(completed_dictionary)


if __name__ == "__main__":
    doctest.testmod()
    main()
