# Isabella Kemp
# 1/12/2020
# Slicing Lab

# Exchanges first and last character in a string
def exchange_first_last(seq):
    first = seq[0:1]
    mid = seq[1:-1]
    last = seq[-1:]
    exchanged = last + mid + first
    return exchanged


# Removes every other character in a string
def every_other_removed(seq):
    return seq[::2]


# Removes the first and last 4 elements, then every other
def first_last_four_every_other(seq):
    return seq[4:-4:2]


# This reverses the sequence
def elements_reversed(seq):
    return seq[::-1]


# Rearranges sequence to return last third, then first third, then middle third.
def new_seq(seq):
    first_third = seq[0:int(len(seq) // 3)]
    last_third = seq[int(2 * len(seq) // 3):]
    middle_third = seq[int(len(seq) // 3):int(2 * len(seq) // 3)]
    new_sequence = last_third + first_third + middle_third
    return new_sequence


# If__name == __main__ function allows us to execute the tests below
if __name__ == "__main__":
    # Assertion tests written to test the code functions above.
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last((a_tuple)) == (32, 54, 13, 12, 5, 2)
    print("Exchanging first and last works")
    assert every_other_removed(a_string) == "ti sasrn"
    assert every_other_removed((a_tuple)) == (2, 13, 5)
    print("Removing every other works")
    assert first_last_four_every_other(a_string) == " sas"
    assert first_last_four_every_other(
        (2, 54, 13, 12, 5, 32, 43, 65, 13, 42, 54, 12)) == (5, 43)
    print("Replacing the last four and first four then every other works")
    assert elements_reversed(a_string) == "gnirts a si siht"
    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    print("Reversing the elements works")
    assert new_seq(a_string) == "stringthis is a "
    assert new_seq(a_tuple) == (5, 32, 2, 54, 13, 12)
