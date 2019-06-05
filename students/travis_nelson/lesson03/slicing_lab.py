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
    return a_new_sequence


def remove_every_other(sequence):
    """Returns a passed sequence with every other item removed"""
    sequence_copy = sequence[:]
    a_new_sequence = sequence_copy[::2]
    return a_new_sequence


def remove_first_last_four(sequence):
    """Returns a passed sequence with the first and last 4 items removed,"""
    """then every other element remaining"""
    sequence_copy = sequence[:]
    a_new_sequence = sequence_copy[4:-4]
    return a_new_sequence


def reverse_sequence(sequence):
    """Returns a passed sequence with the elements reversed with slicing"""
    sequence_copy = sequence[:]
    a_new_sequence = sequence_copy[::-1]
    return a_new_sequence


def last_first_middle_thirds(sequence):
    """Returns a passed sequence with its last third,"""
    """first third, then middle third in the new order"""
    sequence_copy = sequence[:]
    length_of_third = int(len(sequence_copy) / 3)
    first_third = sequence_copy[:length_of_third]
    middle_third = sequence_copy[length_of_third: length_of_third * 2]
    last_third = sequence_copy[(length_of_third * 2):]
    return last_third + middle_third + first_third

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [
        'figs', 'apples', 'bananas', 'mangoes',
        'plums', 'coconuts', 'kiwis', 'raspberries', 'guavas'
        ]

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_list) == [
        'guavas', 'apples', 'bananas', 'mangoes',
        'plums', 'coconuts', 'kiwis', 'raspberries', 'figs']

assert remove_every_other(a_string) == "ti sasrn"
assert remove_every_other(a_tuple) == (2, 13, 5)
assert remove_every_other(a_list) == [
        'figs', 'bananas', 'plums', 'kiwis', 'guavas']

assert remove_first_last_four(a_string) == " is a st"
assert remove_first_last_four(a_tuple) == ()
assert remove_first_last_four(a_list) == ['plums']


assert reverse_sequence(a_string) == "gnirts a si siht"
assert reverse_sequence(a_tuple) == (32, 5, 12, 13, 54, 2)
assert reverse_sequence(a_list) == [
        'guavas', 'raspberries', 'kiwis', 'coconuts',
        'plums', 'mangoes', 'bananas', 'apples', 'figs']

assert last_first_middle_thirds(a_string) == "stringis a this "
assert last_first_middle_thirds(a_tuple) == (5, 32, 13, 12, 2, 54)
assert last_first_middle_thirds(a_list) == [
        'kiwis', 'raspberries', 'guavas', 'mangoes',
        'plums', 'coconuts', 'figs', 'apples', 'bananas']

print("Tests Passed")
