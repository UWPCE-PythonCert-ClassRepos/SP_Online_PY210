# PY210 Lesson 03 Slicing Lab Exercise - Chase Dullinger

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    return seq[::2]

def remove_outside_four(seq):
    return seq[4:-4]

def reverse_sequence(seq):
    return seq[::-1]

def reorder_thirds(seq):
    seq_length=len(seq)
    first_third = seq[:seq_length // 3]
    last_third = seq[-seq_length // 3:]
    middle_third = seq[seq_length // 3 : -seq_length //3]
    return last_third+first_third+middle_third


if __name__=="__main__":
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    # Test exchange_first_last
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    # Test remove_every_other
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    # Test remove_outside_four
    assert remove_outside_four(a_string) == " is a st"
    # on a_tuple this should return an empty tuple because it's less than 8 items
    assert remove_outside_four(a_tuple) == ()

    # Test reverse_sequence
    assert reverse_sequence(a_string) == "gnirts a si siht"
    assert reverse_sequence(a_tuple) == (32, 5, 12, 13, 54, 2)

    # Test reordering_thirds
    assert reorder_thirds(a_string) == "stringthis is a "
    assert reorder_thirds(a_tuple)  == (5, 32, 2, 54, 13, 12)

    print("Tests completed successfully!")
