# This problem seems to be underspecified. It's possible to always return True when outside_mode is True.
# Let's assume that, when outside_mode is True, it will return False when n > 1 or n < 10

def in1to10(n, outside_mode):
    if not outside_mode and (n >= 1 and n <= 10):
        return True
    if outside_mode and (n <= 1 or n >= 10):
        return True
    return False

if __name__ == "__main__":
    # run some tests
    assert in1to10(5, False) == True
    assert in1to10(11, False) == False
    assert in1to10(11, True) == True
