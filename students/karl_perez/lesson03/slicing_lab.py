def exchange_first_last(seq):
    """Write some functions that take a sequence as an argument, and return a copy of that sequence: with the first and last items exchanged."""
    return seq[-1:] + seq[1:-1] +seq[0:1]

def every_other_letter(seq):
    """Write some functions that take a sequence as an argument, and return a copy of that sequence: with every other item removed."""
    every_other = seq[::2]
    return every_other

def every_4_then_2(seq):
    """Write some functions that take a sequence as an argument, and return a copy of that sequence: with the first 4 and the last 4 items removed, and then every other item in the remaining sequence."""
    every_4 = seq[4:-4:]
    then_2 = every_4[::2]
    return then_2

def reverse(seq):
    """Write some functions that take a sequence as an argument, and return a copy of that sequence: with the elements reversed (just with slicing)."""
    reverse = seq[::-1]
    return reverse

def replace_thirds(seq):
    """take seq as an argument and return a copy of with the middle third, then last third, then the first third in the new order"""
    third = int(len(seq)/3)
    middle_third = seq[third:-third]
    last_third = seq[-third:]
    first_third = seq[0:third]
    seq_copy = middle_third + last_third + first_third
    return seq_copy

#Assert Test Function
if __name__ == "__main__":

    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert every_other_letter(a_string) == "ti sasrn"
    assert every_other_letter(a_tuple) == (2, 13, 5)
    assert every_4_then_2(a_string) == " sas"
    assert every_4_then_2(a_tuple) == ()
    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert replace_thirds(a_string) =="is a stringthis "
    assert replace_thirds(a_tuple) == (13, 12, 5, 32, 2, 54)
    print("test passed")