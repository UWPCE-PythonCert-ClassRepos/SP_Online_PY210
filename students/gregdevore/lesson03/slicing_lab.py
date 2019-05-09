# Various functions to practice sequence slicing

def exchange_first_last(seq):
    """ Return sequence with first and last items swapped. """
    if len(seq) <= 1: # Edge case for empty or single sequence -> return sequence
        return seq
    else:
        # Use slicing even on single items to ensure all are sequences
        return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    """ Return sequence with every other item removed. First item will be kept. """
    return seq[::2]

def return_every_other_between_first_last_4(seq):
    """ Return sequence with every other item between first four and last four. """
    return seq[4:-4:2]

def reverse_sequence(seq):
    """ Return sequence with items reversed. """
    return seq[::-1]

def swap_thirds(seq):
    """ Return sequence with last third, first third, middle third, in that order. """
    # Be aware that for sequences whose length is not evenly divisible by three,
    # abs(-len(seq)//3) != len(seq)//3, so results may be different than expected.
    return seq[-len(seq)//3:] + seq[:-len(seq)//3]

if __name__ == '__main__':
    # Test edge cases (empty or single item) and normal cases
    empty_str = ''
    really_short_str = 'a'
    short_str = 'ab'
    normal_str = 'There is nothing permanent except change'
    empty_list = []
    really_short_list = [1]
    short_list = [1,2]
    normal_list = [1,2,3,4,5,6]
    long_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    assert exchange_first_last(empty_str) == ''
    assert exchange_first_last(really_short_str) == 'a'
    assert exchange_first_last(short_str) == 'ba'
    assert exchange_first_last(normal_str) == 'ehere is nothing permanent except changT'
    assert exchange_first_last(empty_list) == []
    assert exchange_first_last(really_short_list) == [1]
    assert exchange_first_last(short_list) == [2,1]
    assert exchange_first_last(normal_list) == [6,2,3,4,5,1]

    assert remove_every_other(empty_str) == ''
    assert remove_every_other(really_short_str) == 'a'
    assert remove_every_other(short_str) == 'a'
    assert remove_every_other(normal_str) == 'Teei ohn emnn xetcag'
    assert remove_every_other(empty_list) == []
    assert remove_every_other(really_short_list) == [1]
    assert remove_every_other(short_list) == [1]
    assert remove_every_other(normal_list) == [1,3,5]

    assert return_every_other_between_first_last_4(empty_str) == ''
    assert return_every_other_between_first_last_4(really_short_str) == ''
    assert return_every_other_between_first_last_4(short_str) == ''
    assert return_every_other_between_first_last_4(normal_str) == 'ei ohn emnn xetc'
    assert return_every_other_between_first_last_4(empty_list) == []
    assert return_every_other_between_first_last_4(really_short_list) == []
    assert return_every_other_between_first_last_4(short_list) == []
    assert return_every_other_between_first_last_4(normal_list) == []
    assert return_every_other_between_first_last_4(long_list) == [4, 6, 8, 10, 12, 14]

    assert reverse_sequence(empty_str) == ''
    assert reverse_sequence(really_short_str) == 'a'
    assert reverse_sequence(short_str) == 'ba'
    assert reverse_sequence(normal_str) == 'egnahc tpecxe tnenamrep gnihton si erehT'
    assert reverse_sequence(empty_list) == []
    assert reverse_sequence(really_short_list) == [1]
    assert reverse_sequence(short_list) == [2,1]
    assert reverse_sequence(normal_list) == [6,5,4,3,2,1]

    assert swap_thirds(empty_str) == ''
    assert swap_thirds(really_short_str) == 'a'
    assert swap_thirds(short_str) == 'ba'
    assert swap_thirds(normal_str) == ' except changeThere is nothing permanent'
    assert swap_thirds(empty_list) == []
    assert swap_thirds(really_short_list) == [1]
    assert swap_thirds(short_list) == [2,1]
    assert swap_thirds(normal_list) == [5,6,1,2,3,4]
    assert swap_thirds(long_list) == [13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    print('All tests passed.')
