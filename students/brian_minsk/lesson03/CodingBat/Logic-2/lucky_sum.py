def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a + b
    return a + b + c

if __name__ == "__main__":
    # run some tests
    assert lucky_sum(1, 2, 3) == 6
    assert lucky_sum(1, 2, 13) == 3
    assert lucky_sum(1, 13, 3) == 1
    assert lucky_sum(13, 1, 2) == 0