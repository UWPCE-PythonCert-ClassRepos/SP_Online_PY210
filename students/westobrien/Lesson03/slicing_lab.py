def first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]


def every_other(seq):
    return seq[::2]

def first_four_last_four(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq
