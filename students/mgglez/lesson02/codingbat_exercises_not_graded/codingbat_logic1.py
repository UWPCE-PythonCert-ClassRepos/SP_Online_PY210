# ---------------------------------------------------------------------------- #
# Title: Lesson 2
# Description: Python Push-ups Part 2 - Coding Bat Logic-1
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,12-31-2020, Activity 2.1 - Python Push-ups Part 2
# ---------------------------------------------------------------------------- #

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    else:
        return cigars >= 40 and cigars <= 60

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

def squirrel_play(temp, is_summer):
    if is_summer:
        return temp >= 60 and temp <= 100
    else:
        return temp >= 60 and temp <= 90

def caught_speeding(speed, is_birthday):
    low_speed = 60
    max_speed = 80
    if is_birthday:
        low_speed += 5
        max_speed += 5
    if speed <= low_speed:
        return 0
    elif speed > low_speed and speed <= max_speed:
        return 1
    else:
        return 2

def sorta_sum(a, b):
    sum = a + b
    if sum >= 10 and sum <= 19:
        return 20
    else:
        return sum

def alarm_clock(day, vacation):
    if not vacation:
        if day >= 1 and day <= 5:
            return "7:00"
        else:
            return "10:00"
    else:
        if day >= 1 and day <= 5:
            return "10:00"
        else:
            return "off"

def love6(a, b):
    return a == 6 or b == 6 or (a + b) == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    if not outside_mode:
        return n >= 1 and n <= 10
    else:
        return n <= 1 or n >= 10

def near_ten(num):
    return (num % 10 <= 2) or ((num + 2) % 10 <= 2)