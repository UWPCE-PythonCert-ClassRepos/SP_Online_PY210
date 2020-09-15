## Lesson 3, Exercise 1, Slicing Lab
## By: B. Matthews
## 9/14/2020

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

def exchange_first_last(seq):


    print(seq, type(seq))

    swap = seq[0]
    a_new_seq = []
    a_new_seq[0] = seq[-1:]
    a_new_seq[-1:] = swap
    return a_new_seq

#assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == [32, 54, 13, 12, 5, 2]
