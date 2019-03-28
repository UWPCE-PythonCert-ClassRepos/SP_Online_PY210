# Russell Felts
# Assignment 3 - Slicing Lab Exercise
# Write some functions that take a sequence as an argument, and return a modified copy of that sequence.


def exchange_first_last(seq):
    """
    Return a copy of the sequence with the first and last items exchanged
    :param seq - The sequence to copy
    :return seq - A new sequence
    """

    # print(seq[-1:] + seq[1:-1] + seq[:1])
    return seq[-1:] + seq[1:-1] + seq[:1]


def remove_every_other(seq):
    """
    Return a copy of the sequence with every other item removed.
    :param seq - The sequence to copy
    :return seq - A new sequence
    """

    # print(seq[::2])
    return seq[::2]


def remove_first_last_every_other_middle(seq):
    """
    Return a copy of the sequence with the first 4 and the last 4 items removed, and then every other item in between.
    :param seq - The sequence to copy
    :return seq - A new sequence
    """

    # print(seq[4:-4:2])
    return seq[4:-4:2]


def reverse_sequence(seq):
    """
    Return a copy of the sequence with the elements reversed (just with slicing).
    :param seq - The sequence to copy
    :return seq - A new sequence
    """

    # print(seq[::-1])
    return seq[::-1]


def mid_last_first(seq):
    """
    Return a copy of the sequence with the middle third, then last third, then the first third in the new order.
    :param seq - The sequence to copy
    :return seq - A new sequence
    """

    # Get the sequence size then divide it into thirds
    size = len(seq)
    third = int(round(size / 3))

    # print(third, size)
    # print(seq[third:third*2] + seq[third*2:size] + seq[:third])

    # Use the third plus multiples of a third along with the total size to rearrange the sequence. Using the total
    # length accommodates lengths that aren't evenly divisible by 3.

    return seq[third:third*2] + seq[third*2:size] + seq[:third]


# Values used for testing the functions.
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
tuple_2 = ("one", "two", "three", "four", 1, 2, 3, 4, 5, 6, "seven", "eight", "nine", "ten")

# Function tests.
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(tuple_2) == ('ten', 'two', 'three', 'four', 1, 2, 3, 4, 5, 6, 'seven', 'eight', 'nine',
                                        'one')
assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)
assert remove_first_last_every_other_middle(a_string) == " sas"
assert remove_first_last_every_other_middle(a_tuple) == ()
assert remove_first_last_every_other_middle(tuple_2) == (1, 3, 5)
assert reverse_sequence(a_string) == "gnirts a si siht"
assert reverse_sequence(a_tuple) == (32, 5, 12, 13, 54, 2)
assert mid_last_first(a_string) == "is a stringthis "
assert mid_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)

print("Test completed")
