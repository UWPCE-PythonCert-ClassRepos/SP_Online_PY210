#!/usr/bin/env python3

# Write some functions that take a sequence as an argument, and return a copy of that sequence:
# (1) with the first and last items exchanged.
# (2) with every other item removed.
# (3) with the first 4 and the last 4 items removed, and then every other item in between.
# (4) with the elements reversed (just with slicing).
# (5) with the middle third, then last third, then the first third in the new order.


def main():
    # exchange_first_last tests
    assert exchange_first_last((1, 2, 5, 7, 0)) == (0, 2, 5, 7, 1)
    assert exchange_first_last(['ball', 0, 2.5, 'glove', (1, 2, 3)]) == [(1, 2, 3), 0, 2.5, 'glove', 'ball']
    assert exchange_first_last('this is a string') == "ghis is a strint"

    # remove_every_other tests
    assert remove_every_other((1, 2, 5, 7, 0)) == (1, 5, 0)
    assert remove_every_other(['ball', 0, 2.5, 'glove', (1, 2, 3)]) == ['ball', 2.5, (1, 2, 3)]
    assert remove_every_other('this is a string') == 'ti sasrn'

    # first_four_last_four tests
    assert first_four_last_four((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) == (5,)
    assert first_four_last_four(['ball', 0, 2.5, 'glove', (1, 2, 3)]) == []
    assert first_four_last_four("this is a string") == ' sas'

    # reverse tests
    assert reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reverse((2.5, 'ball', 'glove', 0, (1, 2, 3))) == ((1, 2, 3), 0, 'glove', 'ball', 2.5)
    assert reverse("this is a string") == 'gnirts a si siht'

    # middle_last_first_third tests
    assert middle_last_first_third((1, 2, 3, 4, 5, 6, 7, 8, 9)) == (4, 5, 6, 7, 8, 9, 1, 2, 3)
    assert middle_last_first_third("this is a string") == "is a stringthis "
    assert middle_last_first_third((2, 54, 13, 12, 5, 32)) == (13, 12, 5, 32, 2, 54)


def exchange_first_last(seq):
    '''
    :param seq: a sequence
    :return: sequence w/ first and last items swapped
    '''
    seq_list = seq[1:-1]
    return seq[-1:] + seq_list + seq[:1]


def remove_every_other(seq):
    '''
    :param seq: a sequence
    :return: sequence w/ every other item removed
    '''
    return seq[::2]


def first_four_last_four(seq):
    '''
    :param seq: a sequence
    :return: sequence w/ first four and last four elements removed and every other item thereafter
    '''
    return seq[4:-4:2]


def reverse(seq):
    '''
    :param seq: a sequence
    :return: sequence w/ elements reversed
    '''
    return seq[::-1]


def middle_last_first_third(seq):
    '''
    :param seq: a sequence
    :return: sequence w/ middle third, last third, first third
    '''
    return seq[len(seq) // 3:] + seq[0:len(seq) // 3]


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)