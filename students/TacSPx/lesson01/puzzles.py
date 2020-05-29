# ---------------------------------------------------------------------------- #
# Title: puzzles.py
# Description: Solved puzzles from “Coding Bat”: http://codingbat.com/python
#
#
# ---------------------------------------------------------------------------- #

# Puzzle #1
# Warmup-1 > sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

# ******************************** #
# Puzzle #2
# String-1 > make_abba
# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
#
# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'
def make_abba(a, b):
  return a + b + b + a

# ******************************** #
# Puzzle #3
# Warmup-1 > monkey_trouble
#
# We have two monkeys, a and b, and the parameters a_smile and b_smile# indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  else:
    return False

# ******************************** #
# Puzzle #4
# Warmup-1 > sum_double
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a, b):
    if a != b:
        sum = a + b
    if a == b:
        sum = (a + b) * 2
    return sum

# ******************************** #
# Puzzle #5
# String-1 > hello_name
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
#
# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
  return "Hello " + name + "!"
