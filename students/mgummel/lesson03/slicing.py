def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    return seq[0::2]
#with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.

def remove_ends(seq):
    ends_removed = seq[4:-4:2]
    return ends_removed

def reverse_it_up(seq):
    return seq[::-1]

def mixed_thirds(seq):
    one_third = int(len(seq) / 3)
    print("this is the index: "  + str(index))
    print("this is the index: "  + str(int(average)))
    return None

if __name__=='__main__':
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32, 34, 4, 23, 512, 3, 17)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (17, 54, 13, 12, 5, 32, 34, 4, 23, 512, 3, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5, 34, 23, 3)

    assert remove_ends(a_tuple) == (5, 34)

    assert reverse_it_up(a_tuple) == (17, 3, 512, 23, 4, 34, 32, 5, 12, 13, 54, 2)

    mixed_thirds(a_string)

    print("All tests completed successfully!")