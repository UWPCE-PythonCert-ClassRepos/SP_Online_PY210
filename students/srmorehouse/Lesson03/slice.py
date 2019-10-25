#!/usr/bin/env python3

"""
swap the first and last chars of a sequence
"""


def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


"""
every other item removed
"""


def every_other_removed(seq):
    return seq[::2]


"""
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence
"""


def first_last_four(seq):
    return seq[4:-4:2]


"""
with the elements reversed (just with slicing).
"""


def reversed(seq):
    return seq[::-1]


"""
with the last third, then first third, then the middle third in the new order.
"""


def thirds(seq):
    slice = int(len(seq) / 3)
    return seq[-slice:] + seq[:-slice]


if __name__ == '__main__':
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    # exchange_first_last
    print('exchange_first_last tests')

    print('a_string is \'' + a_string + '\'')
    print('a_string exchanged is \'' + exchange_first_last(a_string) + '\'')
    assert exchange_first_last(a_string) == "ghis is a strint"
    print('a_tuple is ' + str(a_tuple))
    print('a_tuple exchanged is ' + str(exchange_first_last(a_tuple)))
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    # every_other_removed
    print('\n' + 'every_other_removed tests')

    print('a_string is \'' + a_string + '\'')
    print('a_string ever_othered is \'' + every_other_removed(a_string) + '\'')
    assert every_other_removed(a_string) == 'ti sasrn'
    print('a_tuple is ' + str(a_tuple))
    print('a_tuple ever_othered is ' + str(every_other_removed(a_tuple)))
    assert every_other_removed(a_tuple) == (2, 13, 5)

    # first_last_four
    print('\n' + 'first_last_four tests')

    print('a_string is \'' + a_string + '\'')
    print('a_string first_last_four\'d is \'' + first_last_four(a_string) + '\'')
    assert first_last_four(a_string) == ' sas'
    print('a_tuple is ' + str(a_tuple))
    print('a_tuple first_last_four\'d is ' + str(first_last_four(a_tuple)))
    assert first_last_four(a_tuple) == ()

    # reversed
    print('\n' + 'reversed tests')

    print('a_string is \'' + a_string + '\'')
    print('a_string reversed\'d is \'' + reversed(a_string) + '\'')
    assert reversed(a_string) == 'gnirts a si siht'
    print('a_tuple is ' + str(a_tuple))
    print('a_tuple reversed is ' + str(reversed(a_tuple)))
    assert reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

    # thirds
    print('\n' + 'thirds tests')

    print('a_string is \'' + a_string + '\'')
    print('a_string thirds is \'' + thirds(a_string) + '\'')
    assert thirds(a_string) == 'tringthis is a s'
    print('a_tuple is ' + str(a_tuple))
    print('a_tuple thirds is ' + str(thirds(a_tuple)))
    assert thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
