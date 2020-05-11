# Exercise 3.1, Slicing lab

# Exchange first and last items
def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

# Remove every other item
def remove_every_other(seq):
    return seq[::2]

# Remove first 4 and last 4 items, and then every other items
def remove_firstFour_lastFour_everyOther(seq):
    return seq[4:-4:2]

# Elements reversed
def elements_reversed(seq):
    return seq[::-1]

# Last third, then first third, then middle third
def thirds_initial_last_mid(seq):
    l = len(seq)
    aThird = int(l/3)
    first  = seq[:aThird]
    mid = seq[aThird:-aThird]
    last = seq[-aThird:]
    return last + first + mid

# test functions
if __name__ == "__main__":

    # test variables
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other(a_string) == 'ti sasrn'
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert remove_firstFour_lastFour_everyOther(a_string) == ' sas'
    assert remove_firstFour_lastFour_everyOther(a_tuple) == ()

    assert elements_reversed(a_string) == 'gnirts a si siht'
    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert thirds_initial_last_mid(a_string) == 'tringthis is a s'
    assert thirds_initial_last_mid(a_tuple) == (5, 32, 2, 54, 13, 12)

    print('All tests pass!')
