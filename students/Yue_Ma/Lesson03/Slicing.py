#!/usr/bin/env python3

def exchange(sequence):
    result = sequence[-1:] + sequence[1:-1] + sequence[:1]
    return result


def every_other_items(sequence):
    result = sequence[::2]
    return result


def last_four_first_4(sequence):
    result = sequence[4:-4:2]
    return result


def reverse(sequence):
    result = sequence[::-1]
    return result


def third(sequence):
    break_point_one_third = int(len(sequence)/3)
    result = sequence[-break_point_one_third:] + sequence[:break_point_one_third] + sequence[break_point_one_third:-break_point_one_third]
    return result

if __name__ == "__main__":
    test_string = "this is a string"
    test_tuple = (2, 54, 13, 12, 5, 32)

    assert exchange(test_string) == "ghis is a strint"
    assert exchange(test_tuple) == (32, 54, 13, 12, 5, 2)
    assert every_other_items(test_string) == "ti sasrn"
    assert every_other_items(test_tuple) == (2, 13, 5)
    assert last_four_first_4(test_string) == (" sas")
    assert last_four_first_4(test_tuple) == ()
    assert reverse(test_string) == "gnirts a si siht"
    assert reverse(test_tuple) == (32, 5, 12, 13, 54, 2)
    assert third(test_string) == "tringthis is a s"
    assert third(test_tuple) == (5, 32, 2, 54, 13, 12)

    print('test passed')