## Lesson 3, Exercise 1, Slicing Lab
## By: B. Matthews
## 9/14/2020

a_string = "this is a string"
b_str = "Today is a great day!"
a_tuple = [2, 54, 13, 12, 5, 32]
b_tup = [3.14, 9.86, 3.26, 100000000]

def exchange_first_last(seq):
    """This exchanges the first and last items in a string or tuple."""

    a_new_seq = seq[:]
    last = seq[-1:]
    print(last)
    first = seq[0:1]
    print(first)

    a_new_seq = last + a_new_seq[1:-1] + first
    print(a_new_seq)
    return a_new_seq

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == [32, 54, 13, 12, 5, 2]
assert exchange_first_last(b_str) == "!oday is a great dayT"
assert exchange_first_last(b_tup) == [100000000, 9.86, 3.26, 3.14]

