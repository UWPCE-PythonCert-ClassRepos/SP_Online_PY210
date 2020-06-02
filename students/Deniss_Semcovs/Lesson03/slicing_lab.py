#!/usr/bin/env python3
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
def exchange_first_last(seq):
    return seq[-1:]+seq[1:-1]+seq[:1]

if __name__ == "__main__":    
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    print("tests passed")