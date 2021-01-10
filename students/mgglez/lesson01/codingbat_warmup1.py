# ---------------------------------------------------------------------------- #
# Title: Lesson 1
# Description: Python Pushups
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,12-28-2020, Task 2 - Puzzles - CodingBat Warmup-1
# ---------------------------------------------------------------------------- #

def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    both_smiling = a_smile and b_smile
    neither_smiling = not(a_smile or b_smile)
    return both_smiling or neither_smiling

def sum_double(a, b):
    sum = a + b
    if a == b:
        return 2 * sum
    return sum

def diff21(n):
    diff = abs(n - 21)
    if n > 21:
        return 2 * diff
    return diff

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

def makes10(a, b):
    return a == 10 or b == 10 or (a + b) == 10

def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)

def not_string(my_str):
    if my_str.startswith('not'):
        return my_str
    else:
        return 'not' + my_str

def missing_char(my_str, n):
    return my_str[0:n] + my_str[n+1:]

def front_back(my_str):
    return my_str[-1] + my_str[1:-1] + my_str[0]

def front3(my_str):
    if len(my_str) < 3:
        return my_str * 3
    else:
        return my_str[:3] * 3