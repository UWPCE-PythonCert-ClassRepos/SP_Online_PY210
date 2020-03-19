# series.py
# opcode6502
#
# REQ-01: Create a new module series.py in the lesson02 folder in your student folder.
# [ note: This file. ]


# REQ-02: In it, add a function called fibonacci.
# REQ-03: The function should have one parameter n.
def fibonacci(n):

    # Check if (n == 0) or (n == 1)
    if n < 2:
        return n
    else:
        # REQ-04: The function should return the nth value in the fibonacci series
        # (starting with zero index).
        return fibonacci(n - 2) + fibonacci(n - 1)

    # REQ-05: Docstring for fibonacci().
    # TODO: Add docstring
