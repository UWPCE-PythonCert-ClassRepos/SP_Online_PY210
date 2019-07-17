def love6(a, b):
    if a == 6 or b == 6 or a + b == 6 or abs(a-b) == 6:
        return True
    return False

if __name__ == "__main__":
    # run some tests
    assert love6(6, 4) == True
    assert love6(4, 5) == False
    assert love6(1, 5) == True
    assert love6(4, -2) == True