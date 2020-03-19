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


# REQ-10: Add a block of code to the end of your series.py module.
# Use the block to write a series of assert statements that demonstrate that
# your three functions work properly.
if __name__ == "__main__":
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
