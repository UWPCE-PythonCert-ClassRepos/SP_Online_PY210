def exchange_first_last(seq):
    """ Take a sequence and return a new sequence with
     the first and last items exchanged """
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_sequence

def every_other_removed(seq):
    """ Take a sequence and return a new sequence with
     every other item removed """
    a_new_sequence = seq[0::2]
    return a_new_sequence

def first_last_four(seq):
    """ Take a sequence and return a new sequence with
    the first 4 and the last 4 items removed, and then every 
    other item in the remaining sequence. """
    if len(seq) < 9:
        return "Sequence is too small"
    else:
        a_new_sequence = seq[4:-4:2]
        return a_new_sequence

def reverse_seq(seq):
    """ Take a sequence and return a new sequence with
    with the elements reversed. """
    a_new_sequence = seq[::-1]
    return a_new_sequence

def seq_thirds(seq):
    """ Take a sequence and return a new sequence with
    the last third, then first third, then the middle 
    third in the new order. """
    one_third = len(seq) // 3
    a_new_sequence = seq[-1 * one_third:] + seq[:one_third] + seq[one_third:one_third * 2]
    return a_new_sequence

# Test Functions
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32, 20, 23, 15, 29)

assert exchange_first_last(a_string) == 'ghis is a strint'
assert exchange_first_last(a_tuple) == (29, 54, 13, 12, 5, 32, 20, 23, 15, 2)
assert every_other_removed(a_string) == 'ti sasrn'
assert every_other_removed(a_tuple) == (2, 13, 5, 20, 15)
assert first_last_four(a_string) == ' sas'
assert first_last_four(a_tuple) == (5,)
assert reverse_seq(a_string) == 'gnirts a si siht'
assert reverse_seq(a_tuple) == (29, 15, 23, 20, 32, 5, 12, 13, 54, 2)
assert seq_thirds(a_string) == 'tringthis is a '
assert seq_thirds(a_tuple) == (23, 15, 29, 2, 54, 13, 12, 5, 32)