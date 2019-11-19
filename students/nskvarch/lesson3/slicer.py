#A slicing exercise Created by Niels Skvarch

def exchange_first_last(seq):
    """Takes a sequence and swaps the first and last values"""
    new_seq = seq[-1:] + seq[1:-1] + seq[:1]
    return new_seq

def remove_every_other(seq):
    """Takes a sequence and removes every other item from that sequence"""
    new_seq = seq[::2]
    return new_seq

def first4_last4_and_every_other(seq):
    """Takes a sequence and removes the first and last four items then
    returns every other remaining item from that sequence"""
    new_seq = seq[4:-4:2]
    return new_seq

def reverse_the_sequence(seq):
    """Takes a sequence and reverses the order of the items in that sequence"""
    new_seq = seq[::-1]
    return new_seq


def thirds_switchero(seq):
    """Takes a sequence and switches the first third of the items to the middle
    the middle third of the items to the last, and the last third of items to the first"""
    new_seq = len(seq) // 3
    return seq[new_seq:] + seq[:new_seq]


if __name__ == "__main__":
    # run some tests and if successfull print an OK message

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_long_tuple = (2, 54, 13, 12, 5, 32, 48, 9, 15, 36, 1, 98)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert first4_last4_and_every_other(a_string) == " sas"
    assert first4_last4_and_every_other(a_tuple) == ()
    assert first4_last4_and_every_other(a_long_tuple) == (5, 48)
    assert reverse_the_sequence(a_string) == "gnirts a si siht"
    assert reverse_the_sequence(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert thirds_switchero(a_string) == "is a stringthis "
    assert thirds_switchero(a_tuple) == (13, 12, 5, 32, 2, 54)
    print("tests passed OK")


