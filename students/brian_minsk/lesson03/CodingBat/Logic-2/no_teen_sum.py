def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
    if n == 13 or n == 14 or (n > 16 and n < 20):
        return 0
    return n

if __name__ == "__main__":
    # run some tests
    assert no_teen_sum(1, 2, 3) == 6
    assert no_teen_sum(2, 13, 1) == 3
    assert no_teen_sum(2, 1, 19) == 3
    assert no_teen_sum(16, 1, 2) == 19
