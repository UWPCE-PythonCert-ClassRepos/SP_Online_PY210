def exchange(s):
    s = s[-1:] + s[1:-1] + s[:1]
    return s


def every_other(s):
    s = s[::2]
    return s


def every_other_mid(s):
    s = s[4:-4:2]
    return s


def reverse(s):
    s = s[::-1]
    return s


def third_switch(s):
    third = -int(len(s)/3)
    s = s[third:] + s[:third]
    return s


a = "accio"
b = "expectopatronum"
c = (1, 2, 3, 4, 5, 6, 7, 8,  9, 10)

assert exchange(a) == "occia"
assert exchange(c) == (10, 2, 3, 4,   5,  6, 7, 8, 9, 1)

assert every_other(a) == "aco"
assert every_other(c) == (1, 3, 5, 7, 9)

assert every_other_mid(a) == ""
assert every_other_mid(b) == "coar"
assert every_other_mid(c) == (5,)

assert reverse(a) == "oicca"
assert reverse(c) == (10, 9,  8, 7, 6,  5, 4, 3, 2, 1)

assert third_switch(a) == "oacci"
assert third_switch(c) == (8, 9, 10, 1, 2, 3, 4, 5, 6, 7)
