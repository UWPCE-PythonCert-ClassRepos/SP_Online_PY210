def exchange_first_last(seq):
    '''This function switches the first and last letters of a string'''
    x = seq[-1:]
    y = seq[0:1]

    a_new_sequence = x + seq[1:-1] + y
    print(a_new_sequence)
    return a_new_sequence

def every_other_item_removed(seq):
    '''This function removes every other item'''
    a_new_sequence = seq[::2]
    print(a_new_sequence)
    return a_new_sequence

def first_and_last_four_removed(seq):
    '''This function removes the first and last four items of a sequence'''
    a_new_sequence = seq[4:-4:2]
    print(a_new_sequence)
    return a_new_sequence

def elements_reversed(seq):
    '''This function prints all items in reverse order'''
    a_new_sequence = seq[::-1]
    print(a_new_sequence)
    return a_new_sequence

def thirds(seq):
    '''This function prints the last third, first third, then middle third'''
    first_third = seq[0:int(len(seq)/3)]
    middle_third = seq[int(len(seq)/3):int(2*len(seq)/3)]
    last_third = seq[int(2*len(seq)/3):]
    a_new_sequence = last_third + first_third + middle_third
    print(a_new_sequence)
    return a_new_sequence

if __name__ == "__main__":
    '''These are tests written to test the functions above'''
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert every_other_item_removed(a_string) == "ti sasrn"
    assert every_other_item_removed(a_tuple) == (2, 13, 5)
    assert first_and_last_four_removed(a_string) == " sas"
    assert first_and_last_four_removed(a_tuple) == ()
    assert elements_reversed(a_string) == "gnirts a si siht"
    assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert thirds(a_string) == "stringthis is a "
    assert thirds(a_tuple) == (5, 32, 2, 54, 13, 12)