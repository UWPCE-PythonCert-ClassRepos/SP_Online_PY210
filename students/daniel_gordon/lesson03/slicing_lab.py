def exchange_first_last(seq):
    return seq[-1] + seq[1:-1] + seq[0]

def delete_every_other(seq):
    return seq[::2]

def delete_every_other_from_middle(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def course_shuffle(seq):
    third = len(seq)/3
    return 