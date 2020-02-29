def exchange_first_last(seq):
    """
    Switch the position of the first and last character in the given sequence.
    The sequence must have more than 1 item
    """
    if len(seq) > 1:
        return seq[-1:] + seq[1:-1] + seq[0:1]


def every_other(seq):
    """
    Remove every other item from the sequence
    """
    return seq[::2]


def fours(seq):
    """
    Removes the first 4 and the last 4 items and then every other item
    in the remaining sequence.
    """
    if len(seq) > 8:
        return seq[4:-4:2]


def reverse(seq):
    """
    Reverses the elements in the sequennce
    """
    return seq[::-1]


def thirds(seq):
    """
    Reorders the sequence by the last third, then first third,
    then the middle third."
    """
    length = len(seq)
    if length >= 3:
        return seq[(length // 3) * -1:] + seq[0: (length // 3) * -1]


if __name__ == "__main__":
    # test first last exchange
    string_a = "vancouver"
    string_b = "Moon is a good dog"
    string_c = "JavaRod"
    string_d = "xy"
    string_e = "x"
    tuple_a = (1, 2, 3, 4, 5)
    tuple_b = (44, 88)
    list_a = [1, 2, 3, 4, 5]

    fours_a = "xxxxSyeycyryeytyCyoydyezzzz"
    fours_b = "NotLong"
    fours_c = (1, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5)
    fours_d = [1, 1, 1, 1, 1, 2, 3, 4, 5, 5, 5, 5]

    assert exchange_first_last(string_a) == "rancouvev"
    assert exchange_first_last(string_b) == "goon is a good doM"
    assert exchange_first_last(string_c) == "davaRoJ"
    assert exchange_first_last(string_d) == "yx"
    assert exchange_first_last(string_e) == None
    assert exchange_first_last(tuple_a) == (5, 2, 3, 4, 1)
    assert exchange_first_last(tuple_b) == (88, 44)
    assert exchange_first_last(list_a) == [5, 2, 3, 4, 1]

    assert every_other(string_a) == "vnovr"
    assert every_other(string_b) == "Mo sago o"
    assert every_other(string_c) == "JvRd"
    assert every_other(string_d) == "x"
    assert every_other(string_e) == "x"
    assert every_other(tuple_a) == (1, 3, 5)
    assert every_other(tuple_b) == (44, )
    assert every_other(list_a) == [1, 3, 5]

    assert fours(fours_a) == "SecretCode"
    assert fours(fours_b) == None
    assert fours(fours_c) == (1, 3)
    assert fours(fours_d) == [1, 3]

    assert reverse(string_a) == "revuocnav"
    assert reverse(string_b) == "god doog a si nooM"
    assert reverse(string_c) == "doRavaJ"
    assert reverse(string_d) == "yx"
    assert reverse(string_e) == "x"
    assert reverse(tuple_a) == (5, 4, 3, 2, 1)
    assert reverse(tuple_b) == (88, 44)
    assert reverse(list_a) == [5, 4, 3, 2, 1]

    assert thirds(tuple_a) == (5, 1, 2, 3, 4)
    assert thirds(string_a) == "vervancou"
    assert thirds(fours_c) == (5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 3, 4)
    assert thirds(fours_d) == [5, 5, 5, 5, 1, 1, 1, 1, 1, 2, 3, 4]

    print('Tests Passed')

