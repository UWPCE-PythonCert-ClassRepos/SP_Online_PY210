# ---------------------------------------------------------------------------- #
# Title: Lesson 03
# Description: Slicing Lab
# ChangeLog (Who,When,What):
# Kate Golenkova, 10/16/2020, Created script
# ---------------------------------------------------------------------------- #

# Data ----------------------------------------------------------------------- #
# Declare variables
a_string = "This is my string"
a_tuple = (1, 0, 3, 0, 10, 36, 17, 8, 75, 4, 2, 0)

# Functions ------------------------------------------------------------------ #

def exchange_last_first(s):
    """ Returns new sequence with the first and last items exchanged """
    new_s = s[-1:] + s[1:-1] + s[:1]
    return new_s


def remove_every_other(s):
    """ Returns new sequence with every other item removed """
    new_s = s[::2]
    return new_s


def remove_4last_4first_every_other(s):
    """ Returns new sequence with the first 4 and the last 4 items removed,
        and then every other item in the remaining sequence """
    a = s[4:-4]
    new_s = remove_every_other(a)
    return new_s


def reverse_elements(s):
    """ Returns new sequence with the elements reversed """
    new_s = s[::-1]
    return new_s


def thirds_new_order(s):
    """ Returns new sequence with the last third, then first third, then the middle third in the new order """
    a = len(s) // 3
    new_s = s[-a:] + s[:a+1] + s[a+1:-a]
    return new_s

# Tests ------------------------------------------------------------------ #

assert exchange_last_first(a_string) == "ghis is my strinT"
assert exchange_last_first(a_tuple) == (0, 0, 3, 0, 10, 36, 17, 8, 75, 4, 2, 1)
assert remove_every_other(a_string) == "Ti sm tig"
assert remove_every_other(a_tuple) == (1, 3, 10, 17, 75, 2)
assert remove_4last_4first_every_other(a_string) == " sm t"
assert remove_4last_4first_every_other(a_tuple) == (10, 17)
assert reverse_elements(a_string) == "gnirts ym si sihT"
assert reverse_elements(a_tuple) == (0, 2, 4, 75, 8, 17, 36, 10, 0, 3, 0, 1)
assert thirds_new_order(a_string) == "tringThis is my s"
assert thirds_new_order(a_tuple) == (75, 4, 2, 0, 1, 0, 3, 0, 10, 36, 17, 8)

print("Tests passed")