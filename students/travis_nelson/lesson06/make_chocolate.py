#!

# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always
# use big bars before small bars.
# Return -1 if it can't be done.


def make_chocolate(small, big, goal):
    if (small * 1) + (big * 5) < goal:
        print('Returning -1')
        return -1
    if (big * 5) == goal:
        print('Returning 0')
        return 0
    while big > 0 and goal > 5:
        big -= 1
        goal -= 5
    smalls_needed = 0
    while small > 0 and goal > 0:
        small -= 1
        goal -= 1
        smalls_needed += 1
    if goal == 0:
        print('Returning smalls_needed')
        return smalls_needed
    return -1
