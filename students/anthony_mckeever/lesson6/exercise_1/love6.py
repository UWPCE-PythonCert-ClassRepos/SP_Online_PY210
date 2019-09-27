"""
Programming In Python - Lesson 6 Exercise 1: Unit Tests
Code Poet: Anthony McKeever
Start Date: 08/19/2019
End Date: 08/19/2019
"""

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
