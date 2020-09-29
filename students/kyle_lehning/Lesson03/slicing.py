#!/usr/bin/env python3


def exchange_first_last(seq):
    a_new_seq = seq[-1:] + seq[1:-1] + seq[:1]
    return a_new_seq


def remove_every_other(seq):
    a_new_seq = seq[0::2]
    return a_new_seq


def remove_first_4_last_4(seq):
    a_new_seq = seq[4:]
    a_new_seq = a_new_seq[:-4]
    return a_new_seq


def reverse_elements(seq):
    a_new_seq = seq[::-1]
    return a_new_seq


def change_thirds(seq):
    thirds = len(seq) // 3
    a_new_seq = seq[thirds*2:] + seq[:thirds] + seq[thirds:thirds*2]
    return a_new_seq


if __name__ == '__main__':
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32)
    a_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    assert exchange_first_last(a_string) == "ghis is a strint"
    assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    assert remove_every_other(a_string) == "ti sasrn"
    assert remove_every_other(a_tuple) == (2, 13, 5)
    assert remove_first_4_last_4(a_string) == " is a st"
    assert remove_first_4_last_4(a_tuple) == ()
    assert remove_first_4_last_4(a_list) == [50]
    assert reverse_elements(a_string) == "gnirts a si siht"
    assert reverse_elements(a_tuple) == (32, 5, 12, 13, 54, 2)
    assert change_thirds(a_string) == "stringthis is a "
    assert change_thirds(a_tuple) == (5, 32, 2, 54, 13, 12)
    print("All tests passed")
