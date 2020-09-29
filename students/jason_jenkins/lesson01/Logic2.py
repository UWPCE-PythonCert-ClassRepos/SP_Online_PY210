# Lesson 1: Logic2

def make_bricks(small, big, goal):
    if(big != 0) and big > goal // 5:
        big = goal // 5

    return big * 5 + small >= goal


def lone_sum(a, b, c):

    sum = 0

    if (a != b and a != c):
        sum += a

    if (b != a and b != c):
        sum += b

    if (c != a and c != b):
        sum += c

    return sum


def lucky_sum(a, b, c):
    if a == 13:
        return 0

    if b == 13:
        return a

    if c == 13:
        return a + b

    return a + b + c


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if(13 <= n <= 19):
        if not (15 <= n <= 16):
            return 0
    return n


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    if(num % 10 >= 5):
        return num + (10 - (num % 10))
    else:
        return num - (num % 10)


def close_far(a, b, c):
    if abs(a - b) <= 1:
        if abs(a - c) > 1 and abs(b - c) > 1:
            return True

    if abs(a - c) <= 1:
        if abs(a - b) > 1 and abs(b - c) > 1:
            return True

    return False


def make_chocolate(small, big, goal):
    if (goal // 5 < big):
        big = goal // 5

    maxCount = big * 5 + small

    if (maxCount >= goal):
        return goal - big * 5
    else:
        return -1

