'''
Andrew Garcia
Slicing Lab
6/12/19
'''


def first_and_last(sequence):
    """ Exchanges the first and last item in a sequence """
    first = sequence[0:1]
    last = sequence[-1:]
    middle = sequence[1:-1]
    new_sequence = last + middle + first
    return new_sequence


def remove_other(sequence):
    """ Removes every other item in the sequence """
    removed = sequence[0:len(sequence):2]
    return removed


def remove_four_other(sequence):
    """ Removes the first and last four items in a sequence, and then every other item """
    remove_four = sequence[4:-4]
    remove_other = remove_four[0:len(remove_four):2]
    return remove_other


def reverse(sequence):
    return sequence[::-1]


def third_first_middle(sequence):
    """ Reorganizes the sequence, taking the last third, first third, and then middle third of sequence"""
    one_third = (len(sequence) // 3)
    two_third = (one_third *2)
    first_second = sequence[0:two_third]
    third = sequence[two_third:]
    mixed_sequence = third + first_second
    return mixed_sequence


# testing functions
if __name__ == '__main__':
    assert first_and_last('mumbojumbo') == 'oumbojumbm'
    assert first_and_last((1, 2, 3, 4, 5, 6)) == (6, 2, 3, 4, 5, 1)
    print('Exchange Working')

    assert remove_other('mumbojumbo') == 'mmoub'
    assert remove_other((1, 2, 3, 4, 5, 6)) == (1, 3, 5)
    print('Removing Others Working')

    assert remove_four_other((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)) == (5, 7)
    assert remove_four_other('supercalifragilisticexpialidocious') == 'rairglsiepaio'
    print('Remove First/Last Four and Every Other Working')

    assert reverse('mumbojumbo') == 'obmujobmum'
    assert reverse((1, 2, 3, 4, 5, 6)) == (6, 5, 4, 3, 2, 1)
    print('Reverse Working')

    assert third_first_middle('mumbojumbo') == 'umbomumboj'
    assert third_first_middle((1, 2, 3, 4, 5, 6)) == (5, 6, 1, 2, 3, 4)
    print("Thirds Working")