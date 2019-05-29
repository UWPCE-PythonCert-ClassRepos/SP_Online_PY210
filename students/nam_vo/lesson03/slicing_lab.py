def exchange_first_last(seq):
    """Return a copy of seq with the first and last items exchanged"""
    return (seq[-1:] + seq[1:-1] + seq[:1])

def remove_every_other(seq):
    """Return a copy of seq with every other item removed"""
    return seq[1::2]

def remove_first_last_4(seq):
    """Return a copy of seq with the first 4 and the last 4 items removed, and then every other item in the remaining sequence"""
    first_4_removed_seq = seq[4:]
    last_4_removed_seq = first_4_removed_seq[:-4]
    every_other_seq = last_4_removed_seq[::2]
    return every_other_seq

def reverse_element(seq):
    """Return a copy of seq with the elements reversed (just with slicing)"""
    return seq[::-1]

def slice_third(seq):
    """Return a copy of seq with the last third, then first third, then the middle third in the new order"""
    return (seq[-3:-2] + seq[2:3] + seq[5:6])

if __name__ == "__main__":
    # Sequences to be tested
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    b_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

    # Test exchange_first_last()
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    # Test remove_every_other()
    assert remove_every_other(a_string) == "hsi  tig"
    assert remove_every_other(a_tuple) == (54, 12, 32)

    # Test remove_first_last_4()
    assert remove_first_last_4(a_string) == " sas"
    assert remove_first_last_4(b_tuple) == (5, 7, 9, 11)

    # Test slice_third()
    assert slice_third(a_string) == "iii"
    assert slice_third(b_tuple) == (13, 3, 6)
