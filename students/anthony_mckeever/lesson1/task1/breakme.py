"""
Programming In Python - Lesson 1 Task 1: Explore Errors
Code Poet: Anthony McKeever
Date: 07/18/2019
"""

# Intentionally raise a NameError exception.
def raiseNameError():
    # Intentionally undefined function will result in a NameError.
    failHere()

# Intentionally raise a TypeError exception.
def raiseTypeError():
    myInt = 5
    myStr = "5"
    # Attempting to add an integer and a string together will result in a TypeError.
    return myInt + myStr

"""
# Intentionally raise a SyntaxError exception.
# Commented out as this will fail at runtime or at import.
def raiseSyntaxError():
    # Attempting to assign multiple values to a variable using an equal after the inital assignment will result in a SyntaxError.
    x = "oops" = "fail"
"""

# Intentionally raise an AttributeError exception.
def raiseAttributeError():
    myString = "I'm about to fail"
    # A string type does not contain a definition for "pleaseFail" and will result in an AttributeError.
    myString.pleaseFail
