
def exchange_first_last(seq):

    # slice string
    # seq[-1:]  = take very last character
    # seq[:1]   = take very first character
    # seq[1:-1] = take all characters except the first and last one
    a_new_sequence = seq[-1:] + seq[1:-1] + seq[:1]
    
    print ("a_new_sequence", a_new_sequence)
    return a_new_sequence


def even_string(seq):

     # With every other item removed
     # The line end = " " - means to print output in the same line
     lstr = len(seq)
     n = 0
     for n in range(0,lstr):
         v = n % 2
         if v == 1:
            print(seq[n], end = " ")
            return seq(n)
def swap_element(seq):

    # Elements Reversed
    a_new_sequence = seq[::-1]

    print ("str ", a_new_sequence)
    return a_new_sequence
    
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
#exchange_first_last(a_string)

#swap_element(a_string)
#swap_element(a_tuple)
assert swap_element(a_string) == "gnirts a si siht"
assert swap_element(a_tuple) == (32, 5, 12, 13, 54, 2)
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

