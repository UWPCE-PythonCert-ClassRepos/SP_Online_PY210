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
    return last_item + sequence_copy_sans_first_and_last + first_item


def remove_every_other(sequence):
    sequence_copy = list(sequence[:])
    every_other_sequence_copy = sequence_copy[0::2]
    return every_other_sequence_copy


def remove_first_last_four(sequence):
    pass


def reverse_sequence(sequence):
    pass


def return_last_first_middle_thirds(sequence):
    pass

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [
        'figs', 'apples', 'bananas', 'mangoes',
        'plums', 'coconuts', 'kiwis', 'raspberries'
        ]
