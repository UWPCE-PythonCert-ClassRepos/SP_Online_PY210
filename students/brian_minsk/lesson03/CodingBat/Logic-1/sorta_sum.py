def sorta_sum(a, b):
    real_sum = a + b
    if real_sum >= 10 and real_sum <= 20:
        return 20
    else:
        return real_sum

if __name__ == "__main__":
    # run some tests
    assert sorta_sum(3, 4) == 7
    assert sorta_sum(9, 4) == 20
    assert sorta_sum(10, 11) == 21