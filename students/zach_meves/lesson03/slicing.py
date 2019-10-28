"""
slicing.py

Zach Meves
Python 210
Lesson 03

Exercise : Slicing Lab
"""


def exchange_first_last(x):
    """Return a copy of a sequence with the first and last elements exchanged.

    Parameters
    ----------
    x : sequence
        Sequence to exchange first and last elements of

    Returns
    -------
    sequence
        Copy of input with first and last elements swapped"""

    if len(x) < 2:  # If sequence has 0 or 1 elements, return a copy
        return x[:]

    return x[-1] + x[1:-1] + x[0]


def every_other_removed(x):
    """Return copy of sequence with every other item removed.

    Parameters
    ----------
    x : sequence
        Sequence to operate on

    Returns
    -------
    sequence
        Copy of input with every other item removed"""

    return x[::2]


def chop_4_other(x):
    """Return copy of sequence with the first 4 and the last 4 items removed, and then every other item in
    the remaining sequence.

    Parameters
    ----------
    x : sequence
        Sequence to operate on

    Returns
    -------
    sequence
    """

    return x[4:-4:2]


def rev(x):
    """Return copy of sequence with elements reversed.

    Parameters
    ----------
    x : sequence
        Sequence to operate on

    Returns
    -------
    sequence
        Copy of input sequence with elements reversed"""

    return x[::-1]


def thirds(x):
    """Returns a copy of the input sequence with the last third, then first third,
    then the middle third in the new order.

    Parameters
    ----------
    x : sequence
        Sequence to operate on

    Returns
    -------
    sequence
        Copy of input after operation"""

    _third = 2 * len(x) // 3  # Cut the sequence at the 2/3 len index
    return x[_third:] + x[:_third]


if __name__ == '__main__':
    """Test functions."""

    # Test exchange_first_last
    assert exchange_first_last('') == ''
    assert exchange_first_last('a') == 'a'
    assert exchange_first_last('ab') == 'ba'
    assert exchange_first_last('abc') == 'cba'
    assert exchange_first_last('abcdefg') == 'gbcdefa'

    # Test every_other_removed
    assert every_other_removed('') == ''
    assert every_other_removed('a') == 'a'
    assert every_other_removed('ab') == 'a'
    assert every_other_removed('abc') == 'ac'
    assert every_other_removed('abcdef') == 'ace'

    # Test chop_4_other
    assert chop_4_other('abc') == ''
    assert chop_4_other('abcdefg') == ''
    assert chop_4_other('12345678912') == '57'
    assert chop_4_other('1234567891') == '5'
    assert chop_4_other('12345678') == ''

    # Test rev
    assert rev('') == ''
    assert rev('a') == 'a'
    assert rev('ab') == 'ba'
    assert rev('abcdefg') == 'gfedcba'

    # Test thirds
    assert thirds('') == ''
    assert thirds('a') == 'a'
    assert thirds('abc') == 'cab'
    assert thirds('abc123456') == '456abc123'
    assert thirds('ab') == 'ba'