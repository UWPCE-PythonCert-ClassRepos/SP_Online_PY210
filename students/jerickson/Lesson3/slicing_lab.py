def first_is_last(seq):
    """Returns the sequence with the first and last elements swapped"""
    first_is_last = seq[-1:] + seq[1:-1] + seq[0:1]
    return first_is_last


def every_other(seq):
    """Returns after removing every other element"""
    every_other = seq[::2]
    return every_other


def missing_head_tail_every_other(seq):
    """Returns after; removing the head-4 and tail-4 elements, then cutting every other element"""
    missing_head_tail = seq[4:-3]
    missing_head_tail_every_other = missing_head_tail[::2]
    return missing_head_tail_every_other


def reverse_seq(seq):
    """Reverses a sequence"""
    reversed_seq = seq[::-1]
    return reversed_seq


def third_mixup(seq):
    """Mixes up sequence in thirds; last->first->middle"""
    len_third = int(len(seq) / 3)
    third_mixup = seq[-len_third:] + seq[:-len_third]
    return third_mixup


if __name__ == "__main__":
    seq_string = "0123456789"
    seq_tuple = tuple(seq_string)

    assert first_is_last(seq_string) == "9123456780"
    # fmt: off
    assert first_is_last(seq_tuple) == ('9', '1', '2', '3', '4', '5', '6', '7', '8', '0')
    # fmt: on

    assert every_other(seq_string) == "02468"
    assert every_other(seq_tuple) == ("0", "2", "4", "6", "8")

    assert missing_head_tail_every_other(seq_string) == "46"
    assert missing_head_tail_every_other(seq_tuple) == ("4", "6")

    assert reverse_seq(seq_string) == "9876543210"
    assert reverse_seq(seq_tuple) == ("9", "8", "7", "6", "5", "4", "3", "2", "1", "0")

    assert third_mixup(seq_string) == "7890123456"
    assert third_mixup(seq_tuple) == ("7", "8", "9", "0", "1", "2", "3", "4", "5", "6")

    print("All Tests Passed")

