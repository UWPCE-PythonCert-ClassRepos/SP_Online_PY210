# Tasks

# Write some functions that take a sequence as an argument
# and return a copy of that sequence:

# with the first and last items exchanged.

# with every other item removed.

# with the first 4 and the last 4 items removed,
# and then every other item in the remaining sequence.

# with the elements reversed (just with slicing).

# with the last third, then first third,
# then the middle third in the new order.

# NOTE: These should work with ANY sequence,
# but you can use strings to test, if you like.


def exchange_first_last(sequence):
    """Returns a passed sequence with its first and last items exchanged"""
    sequence_copy = sequence[:]
    first_item = sequence_copy[:1]
    last_item = sequence_copy[-1:]
    sequence_copy_sans_first_and_last = sequence_copy[1:len(sequence_copy)-1]
    a_new_sequence = last_item + sequence_copy_sans_first_and_last + first_item
    print(sequence)
    return a_new_sequence


def remove_every_other(sequence):
    """Returns a passed sequence with every other item removed"""
    sequence_copy = sequence[:]
    a_new_sequence = sequence_copy[::2]
    print(sequence)
    return a_new_sequence


def remove_first_last_four(sequence):
    """Returns a passed sequence with the first and last 4 items removed,"""
    """then every other element remaining"""
    sequence_copy = sequence[:]
    return


def reverse_sequence(sequence):
    """Returns a passed sequence with the elements reversed with slicing"""
    sequence_copy = sequence[:]
    pass


def return_last_first_middle_thirds(sequence):
    """Returns a passed sequence with its last third,"""
    """first third, then middle third in the new order"""
    sequence_copy = sequence[:]
    pass

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [
        'figs', 'apples', 'bananas', 'mangoes',
        'plums', 'coconuts', 'kiwis', 'raspberries'
        ]
