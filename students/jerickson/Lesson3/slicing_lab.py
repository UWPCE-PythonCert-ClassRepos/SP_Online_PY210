def first_is_last(seq):
    first_is_last = seq[-1] + seq[1:-1] + seq[0]
    return first_is_last

def every_other(seq):
    every_other = seq[::2]
    return every_other


def missing_head_tail_every_other(seq):
    missing_head_tail = seq[4:-3]
    missing_head_tail_every_other = missing_head_tail[::2]
    return missing_head_tail_every_other

def reverse_seq(seq):
    reversed_seq = seq[::-1]
    return reversed_seq

def third_mixup(seq):
    len_third = int(len(seq) / 3)
    third_mixup = (
        seq[-len_third:] + seq[: len_third + 1] + seq[len_third + 1 : -len_third]
    )
    return third_mixup


if __name__ == "__main__":
    # sequence = "0123456789abcdef"
    sequence = "0123456789"
    assert first_is_last(sequence) == '9123456780'
