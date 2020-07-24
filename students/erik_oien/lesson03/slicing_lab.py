#!/usr/bin/env python3

def exchange_first_last(seq):
    return seq[-1:] + seq[1:-1] + seq[:1]

def remove_every_other(seq):
    return seq[::2]

def remove_first_last_four_every_other(seq):
    return seq[4:-4:2]

def reverse(seq):
    return seq[::-1]

def thirds(seq):
    thirds = int(len(seq)/3)
    return seq[-thirds:] + seq[:thirds] + seq[thirds:-thirds]

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

if __name__ == "__main__":    
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)

    assert remove_first_last_four_every_other(a_string) == " sas"
    assert remove_first_last_four_every_other(a_tuple) == ()

    assert reverse(a_string) == "gnirts a si siht"
    assert reverse(a_tuple) == (32, 5, 12, 13, 54, 2)

    assert thirds(a_string) == "tringthis is a s"
    assert thirds(a_tuple) == (5, 32, 2, 54, 13, 12)

print("tests passed")