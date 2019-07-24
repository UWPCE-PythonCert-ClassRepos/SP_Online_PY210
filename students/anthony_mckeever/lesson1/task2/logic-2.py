"""
Programming In Python - Lesson 1 Task 2: Puzzles - Logic-2
Code Poet: Anthony McKeever
Date: 07/20/2019
"""

# Logic-2 > make_bricks 
def make_bricks(small, big, goal):
    #  Check if big and small can equate to the goal.
    if goal < small:
        return True
    elif big == 0 and goal > small:
        return False
    elif big * 5 + small < goal:
        return False

    # get the remainder needed after putting as many bigs into goal as possible.
    modGoal = goal % 5

    # Check the various combinations of big and small can some how equate to the goal.
    if modGoal <= small:
        if (big * 5) + modGoal == goal:
            return True
        elif big % goal >= small:
            return True
        elif modGoal / big <= small:
            return True

    # No applicable solution exists.
    return False

# Logic-2 > lone_sum
def lone_sum(a, b, c):
    # Create a list for easy checking
    numsList = [a, b, c]
    total = 0

    for i in numsList:
        # Check for only one instance of the current integer in the list.
        if numsList.count(i) == 1:
            total += i
    return total

# Logic-2 > lucky_sum
def lucky_sum(a, b, c):
    # Create a list for easy checking
    numsList = [a, b, c]
    total = 0

    for i in numsList:
        # If the current number is 13, break out of the loop before we count it.
        if i == 13:
            break
        total += i

    return total

# Logic-2 > no_teen_sum 
def no_teen_sum(a, b, c):
    numsList = [a, b, c]
    total = 0

    for i in numsList:
        total += fix_teen(i)

    return total

def fix_teen(n):
    dontIgnore = [15, 16]
    if n in dontIgnore:
        return n
    # range(start, end) = inclusive start, exclusive end
    elif n in range(13, 20):
        return 0
    return n

# Logic-2 > round_sum 
def round_sum(a, b, c):
    numsList = [a, b, c]
    total = 0

    for i in numsList:
        total += round10(i)

    return total

def round10(num):
    return int(round(num/10)*10)

# Logic-2 > close_far 
def close_far(a, b, c):
    abClose = abs(a - b) < 2
    bcClose = abs(b - c) < 2
    acClose = abs(a - c) < 2

    abFar = abs(a - b) >= 2
    bcFar = abs(b - c) >= 2
    acFar = abs(a - c) >= 2

    if abClose:
        return not abFar and bcFar and acFar
    if bcClose:
        return not bcFar and abFar and acFar
    if acClose:
        return not acFar and abFar and bcFar

# Logic-2 > make_chocolate 
def make_chocolate(small, big, goal):
    maxBig = big * 5
    if goal >= maxBig:
        remain = goal - maxBig
    else:
        remain = goal % 5

    if remain <= small:
        return remain

    return -1
