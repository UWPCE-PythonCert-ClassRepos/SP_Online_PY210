# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Python Push-ups Part 2 - Coding Bat String-2
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-01-2020, Activity 2.1 - Python Push-ups Part 2
# ---------------------------------------------------------------------------- #

def double_char(str):
    new_s = ""
    for char in str:
        new_s += char*2
    return new_s

def count_hi(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i:i+2] == 'hi':
            count += 1
    return count

def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str) - 2):
        if str[i:i+3] == 'cat':
            count_cat += 1
        elif str[i:i+3] == 'dog':
            count_dog += 1
    return count_cat == count_dog

def count_code(str):
    count = 0
    for i in range(len(str) - 3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count

def end_other(a, b):
    return a[-len(b):].lower() == b.lower() or b[-len(a):].lower() == a.lower()

def xyz_there(str):
    xyz_count = str.count('xyz')
    period_xyz_count = str.count('.xyz')
    return xyz_count - period_xyz_count > 0
