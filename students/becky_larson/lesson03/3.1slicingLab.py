#!/usr/bin/env python """
"""Exchange first and last values in the list and return"""
"""learned that using = sign, they refer to same object, so used copy."""
"""      Could also use list command"""

"""tuple assert failing:    RETURNING:    (32, (54, 13, 12, 5, 32), 2). """
"""      How to remove the parans"""
"""Is there a way to use same code for both string and tuple?"""


def exchange_first_last(seq):
    if(type(seq)) == str:
        a_new_sequence = seq[len(seq)-1] + seq[1:(len(seq)-1)] + seq[0]
    else:
        a_new_sequence = []
        a_new_sequence.append(seq[len(seq)-1])
        a_new_sequence.extend(seq[1:(len(seq)-1)])
        a_new_sequence.append(seq[0])
    print("RETURNING: ", a_new_sequence)
    return tuple(a_new_sequence)


def remove_everyother(seq):
    a_new_sequence = seq[::2]
    print("RETURNING: ", a_new_sequence)
    return a_new_sequence


def remove_1stLast4_everyother(seq):
    a_new_sequence = seq[4:-4:2]
    print("RETURNING: ", a_new_sequence)
    return a_new_sequence


def elements_reversed(seq):
    a_new_sequence = seq[::-1]
    print("RETURNING: ", a_new_sequence)
    return a_new_sequence


def each_third(seq):
    thirds = len(seq)/3
    start1 = 0
    end1 = int(thirds)
    start2 = int(thirds)
    end2 = int(thirds*2)
    start3 = int(thirds*2)
    end3 = int(thirds*3)
    str1 = seq[start1:end1]
    str2 = seq[start2:end2]
    str3 = seq[start3:end3]
    a_new_sequence = str3 + str1 + str2
    print("RETURNING: ", a_new_sequence)
    return a_new_sequence


def run_assert():
    # print("run_assert")
    # assert exchange_first_last(a_string) == "ghis is a strint"
    # print("string passed")
    # assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
    # print("tuple passed")
    # assert remove_everyother(a_string) == "ti sasrn"
    # print("string passed")
    # assert remove_everyother(a_tuple) == (2, 13, 5)
    # print("tuple passed")
    # assert remove_1stLast4_everyother(a_string) == " sas"
    # print("string passed")
    # assert remove_1stLast4_everyother(a_tuple) == ()
    # print("tuple passed")
    # assert elements_reversed(a_string) == "gnirts a si siht"
    # print("string passed")
    # assert elements_reversed(a_tuple) == (32, 5, 12, 13, 54, 2)
    # print("tuple passed")
    assert each_third(a_string15) == "strinthis is a "
    print("string passed")
    assert each_third(a_tuple) == (5, 32, 2, 54, 13, 12)
    print("tuple passed")


a_string15 = "this is a strin"

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

if __name__ == "__main__":
    run_assert()
    # each_third(a_tuple)
