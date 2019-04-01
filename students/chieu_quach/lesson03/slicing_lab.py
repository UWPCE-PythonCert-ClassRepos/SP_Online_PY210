#  Author      - Chieu Quach
#  Assignment  - Lesson 3
#  Exercise    - Slicing Lab



def exchange_first_last(seq):
    
    # With the first and last items exchanged
    
    # slice string
    # seq[-1:]  = take very last character
    # seq[:1]   = take very first character
    # seq[1:-1] = take all characters except the first and last one
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    
    print ("a_new_sequence", a_new_sequence)
    return a_new_sequence


def swap_element(seq):

    # Elements Reversed
    a_new_sequence = seq[::-1]

    print ("str ", a_new_sequence)
    return a_new_sequence

def other_item_removed(seq):

    # With every other item removed
   
    
    a_new_sequence = seq[::2]
    print ("a_new_sequence", a_new_sequence)
    return a_new_sequence

def first_n_last_4items(seq):

    print ("seq ", seq)
    first_char = seq[4:]
    print ("first 4 chars removed ", first_char)

    last_char = first_char[:-4]
    print ("last 4 chars removed ", last_char)
    a_new_sequence = last_char[::2]
    print (a_new_sequence)
   
    return a_new_sequence

def first_mid_last_3items(seq):

    # with the last third, then first third, then the middle third in new order
    print ("seq ", seq)
    first_char = seq[:-3]
    print ("last third items removed ", first_char)

    last_char = first_char[3:]
    print ("last_char ", last_char)
    len_str = len(last_char)
    print ("len_str ", len_str)
    
    a_new_sequence = last_char[:2] + last_char[3:]

    print ("sequence ", a_new_sequence)
    return a_new_sequence
    
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
#a_tuple = (2, 54, 13, 12, 5, 32, 14, 24, 43, 33, 31)
exchange_first_last(a_string)
exchange_first_last(a_tuple)
swap_element(a_string)
swap_element(a_tuple)
other_item_removed(a_string)
other_item_removed(a_tuple)
first_n_last_4items(a_string)
first_n_last_4items(a_tuple)
first_mid_last_3items(a_string)
first_mid_last_3items(a_tuple)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert swap_element(a_string) == "gnirts a si siht"
assert swap_element(a_tuple) == (32, 5, 12, 13, 54, 2)
assert other_item_removed(a_string) == "ti sasrn"
assert other_item_removed(a_tuple) == (2, 13, 5)
assert first_n_last_4items(a_string) == " sas"
assert first_n_last_4items(a_tuple) == ()
assert first_mid_last_3items(a_string) == "s s a str"
assert first_mid_last_3items (a_tuple) == ()
