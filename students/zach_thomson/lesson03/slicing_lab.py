#slicing lab - updated for pull request/submission

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def every_other(seq):
    return seq[::2]

def fours_every_other(seq):
    return seq[4:-4:2]

def reversed_sequence(seq):
    return seq[::-1]

def thirds_swap(seq):
    first_third = int(len(seq)/3)
    middle_third = int(len(seq)/3*2)
    return seq[middle_third:] + seq[:first_third] + seq[first_third:middle_third]

#tests
a_string = "this is my test string"
a_tuple = (3, 6, 9, 12, 15)
fours_test = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
thirds_test = (1, 2, 3, 4, 5, 6)

assert exchange_first_last(a_string) == "ghis is my test strint"
assert exchange_first_last(a_tuple) == (15, 6, 9, 12, 3)
assert every_other(a_string) == "ti sm etsrn"
assert every_other(a_tuple) == (3, 9, 15)
assert fours_every_other(a_string) == " sm ets"
assert fours_every_other(fours_test) == (4, 6, 8)
assert reversed_sequence(a_string) == "gnirts tset ym si siht"
assert reversed_sequence(a_tuple) == (15, 12, 9, 6, 3)
assert thirds_swap(thirds_test) == (5, 6, 1, 2, 3, 4)
