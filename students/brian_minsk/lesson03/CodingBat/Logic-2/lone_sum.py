def lone_sum(a, b, c):
    a1 = a
    b1 = b
    c1 = c
    if (a == b):
        a1 = 0
        b1 = 0
    if (a == c):
        a1 = 0
        c1 = 0
    if (b == c):
        b1 == 0
        c1 == 0
    return a1 + b1 + c1

if __name__ == "__main__":
    # run some tests
    assert lone_sum(1, 2, 3) == 6
    assert lone_sum(3, 2, 3) == 2
    assert lone_sum(3, 3, 3) == 0
