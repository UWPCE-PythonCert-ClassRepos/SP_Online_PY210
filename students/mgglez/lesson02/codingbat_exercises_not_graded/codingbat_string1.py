# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Python Push-ups Part 2 - Coding Bat String-1
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,12-31-2020, Activity 2.1 - Python Push-ups Part 2
# ---------------------------------------------------------------------------- #

def hello_name(name):
    return "Hello {}!".format(name)

def make_abba(a, b):
    return "{0}{1}{1}{0}".format(a, b)

def make_tags(tag, word):
    return "<{0}>{1}</{0}>".format(tag, word)

def make_out_word(out, word):
    return out[:len(out)/2] + word + out[len(out)/2:]

def extra_end(str):
    return 3 * str[-2:]

def first_two(str):
    return str if len(str) < 2 else str[:2]

def first_half(str):
    return str[:len(str)/2]

def without_end(str):
    return str[1:-1]

def combo_string(a, b):
    if len(a) > len(b):
        long, short = a, b
    else:
        long, short = b, a
    return short + long + short

def non_start(a, b):
    return a[1:] + b[1:]

def left2(str):
    return str[2:] + str[:2]