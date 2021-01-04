# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Python Push-ups Part 2 - Coding Bat Logic-2
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-01-2020, Activity 2.1 - Python Push-ups Part 2
# ---------------------------------------------------------------------------- #

def make_bricks(small, big, goal):
    if goal > big * 5 + small:
        return False

    if goal % 5 > small:
        return False

    return True

def lone_sum(a, b, c):
    my_list = [a, b, c]
    sum = 0
    for number in my_list:
        if my_list.count(number) == 1:
            sum += number
    return sum

def lucky_sum(a, b, c):
    my_list = [a, b, c]
    sum = 0
    for number in my_list:
        if number == 13:
            break
        sum += number
    return sum

def no_teen_sum(a, b, c):
    my_list = [a, b, c]
    sum = 0
    for number in my_list:
        number_fixed = fix_teen(number)
        sum += number_fixed
    return sum

def fix_teen(n):
    if n < 13 or n > 19 or n in [15, 16]:
        return n
    else:
        return 0


def round_sum(a, b, c):
    my_list = [a, b, c]
    sum = 0
    for number in my_list:
        sum += round10(number)
    return sum

def round10(num):
    result = num % 10
    if result >= 5:
        return (num//10 + 1) * 10
    else:
        return (num//10) * 10

def close_far(a, b, c):
    return (abs(b - a) <= 1 or abs(c - a) <= 1) and ((abs(b - a) >= 2 and abs(b - c) >= 2) or (abs(c - a) >= 2 and abs(c - b) >= 2))

def make_chocolate(small, big, goal):
    if goal > big * 5 + small:
        return -1
    if goal % 5 > small:
        return -1
    return (goal - 5 * min(big, goal//5))