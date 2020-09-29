# Lesson 1: Logic1

def cigar_party(cigars, is_weekend):
    if(is_weekend and cigars >= 40):
        return True

    return 40 <= cigars <= 60

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

def squirrel_play(temp, is_summer):
    if(temp < 60):
        return False
    elif temp <= 90:
        return True
    elif is_summer and temp <= 100:
        return True
    else:
        return False


def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    elif speed <= 80:
        return 1
    else:
        return 2


def sorta_sum(a, b):
    sum = a + b

    if 10 <= sum <= 19:
        return 20
    else:
        return sum


def alarm_clock(day, vacation):
    if day == 6 or day == 0:
        if vacation:
            return "off"
        else:
            return "10:00"
    elif vacation:
        return "10:00"
    else:
        return "7:00"


def love6(a, b):
    if a == 6 or b == 6:
        return True
    elif a + b == 6:
        return True
    elif abs(a - b) == 6:
        return True
    else:
        return False


def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10


def near_ten(num):
    return num % 10 <= 2 or num % 10 >= 8
