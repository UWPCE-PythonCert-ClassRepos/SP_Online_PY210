"""
Programming In Python - Lesson 1 Task 2: Puzzles - Logic-1
Code Poet: Anthony McKeever
Date: 07/20/2019
"""

# Logic-1 > cigar_party 
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    # range(start, end) uses inclusive start and exclusive end.
    return cigars in range(40, 61)

# Logic-1 > date_fashion
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

# Logic-1 > squirrel_play
def squirrel_play(temp, is_summer):
    if is_summer:
        return temp in range(60, 101)
    return temp in range(60, 91)

# Logic-1 > caught_speeding
def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <= 65:
            return 0
        elif speed <= 85:
            return 1
        else:
            return 2
    elif speed > 60:
        if speed <= 80:
            return 1
        else:
            return 2
    else:
        return 0

# Logic-1 > sorta_sum 
def sorta_sum(a, b):
    total = a + b
    if total in range(10, 20):
        return 20
    return total

# Logic-1 > alarm_clock 
def alarm_clock(day, vacation):
    weekend = day in [0, 6]

    if vacation:
        if weekend:
            return "off"
        return "10:00"

    if not vacation:
        if weekend:
            return "10:00"
    return "7:00"

# Logic-1 > love6
def love6(a, b):
    if a == 6 or b == 6:
        return True
    elif a + b == 6:
        return True
    elif a - b == 6:
        return True
    elif b - a == 6:
        return True
    return False

# Logic-1 > in1to10 
def in1to10(n, outside_mode):
    if outside_mode:
        return n not in range(2, 10)
    elif n in range(1, 11):
        return True
    return False

# Logic-1 > near_ten
def near_ten(num):
    mod = num % 10
    return mod <= 2 or mod >= 8
