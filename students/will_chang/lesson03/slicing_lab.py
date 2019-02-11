def exchange_first_last(seq):
    """Returns a copy of the given sequence with the first and last values swapped."""
    if(len(seq) == 1): #Prevents duplicates if sequence only has one value.
        seq_copy = seq[:]
    else:
        seq_copy = seq[-1:]+seq[1:-1]+seq[:1]
    return seq_copy
    
    
def exchange_every_other(seq):
    """Returns a copy of the given sequence with every other item removed."""
    seq_copy = seq[:0]
    for i in range(len(seq)):
        if i % 2 == 0: #Copy every other item of the original sequence into the new sequence.
            seq_copy += seq[i:i+1]
    return seq_copy
    

def first_last_four(seq):
    """Returns a copy of the given sequence with the first and last four items removed. Every other item is then removed from the remaining sequence."""
    first_last_seq = seq[4:-4] #Placeholder sequence to remove first and last four items
    return exchange_every_other(first_last_seq)


def reverse_elements(seq):
    """Returns a copy of the given sequence with the elements reversed."""
    seq_copy = seq[::-1]
    return seq_copy


def middle_last_first(seq):
    """Returns a copy of the given sequence with the following new order: middle third, last third, first third."""
    seq_copy =  seq[len(seq)//3:] + seq[:len(seq)//3]
    return seq_copy


# Test variables
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
a_list = [3, 7, 26, 5, 1, 13, 22, 75, 9]

# This block of code is used to test the exchange_first_last(seq) function.
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exchange_first_last(a_list) == [9, 7, 26, 5, 1, 13, 22, 75, 3]

# This block of code is used to test the exchange_every_other(seq) function.
assert exchange_every_other(a_string) == "ti sasrn"
assert exchange_every_other(a_tuple) == (2, 13, 5)
assert exchange_every_other(a_list) == [3, 26, 1, 22, 9]

# This block of code is used to test the first_last_four(seq) function.
assert first_last_four(a_string) == " sas"
assert first_last_four(a_tuple) == ()
assert first_last_four(a_list) == [1]

# This block of code is used to test reverse_elements(seq) function.
assert reverse_elements(a_string) == "gnirts a si siht"
assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)
assert reverse_elements(a_list) == [9, 75, 22, 13, 1, 5, 26, 7, 3]

# This block of code is used to test the middle_last_first(seq) function.
assert middle_last_first(a_string) == "is a stringthis "
assert middle_last_first(a_tuple) == (13, 12, 5, 32, 2, 54)
assert middle_last_first(a_list) == [5, 1, 13, 22, 75, 9, 3, 7, 26]