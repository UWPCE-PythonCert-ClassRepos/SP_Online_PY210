def firstlast_exchange(seq):
    """Returns copy of sequence with the first and last items exchanged."""
    new_seq = seq[-1] + seq[1:-1] + seq[0]
    return new_seq


def every_other_rem(seq):
    """Returns copy of sequence with every other item removed."""
    new_seq = seq[::2]
    return new_seq


def first4_last4_every_other_rem(seq):
    """Returns copy of sequence with the first 4 and last 4 items removed, and
    then every other item in the remaining sequence."""
    new_seq = seq[4:-4:2]
    return new_seq


def elements_reversed(seq):
    """Returns copy of sequence with the elements reversed (just with slicing)."""
    new_seq = seq[::-1]
    return new_seq


def thirds_order(seq):
    """Returns copy of sequence with the last third,
    then first third, then the middle third in the new order."""
    thirds = int(len(seq) / 3)
    new_seq = seq[-thirds:] + seq[:thirds] + seq[thirds:-thirds]
    return new_seq


# Tests
a_string = 'you never fail until you stop trying'
a_tuple = (1, 5, 9, 13, 19, 22, 27, 65, 79, 82, 93, 101, 200, 404, 500)

if __name__ == "__main__":
    assert firstlast_exchange(a_string) == 'gou never fail until you stop tryiny'
    assert every_other_rem(a_tuple) == (1, 9, 19, 27, 79, 93, 200, 500)
    assert first4_last4_every_other_rem(a_tuple) == (19, 27, 79, 93)
    assert elements_reversed(a_string) == 'gniyrt pots uoy litnu liaf reven uoy'
    assert thirds_order(a_tuple) == (93, 101, 200, 404, 500, 1, 5, 9, 13, 19, 22, 27, 65, 79, 82)

    print("tests passed")
