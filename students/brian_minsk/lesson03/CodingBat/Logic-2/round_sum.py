def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    mod = num % 10
    floor = num // 10
    if mod < 5:
        return floor * 10
    return (floor * 10) + 10

if __name__ == "__main__":
    # run some tests
    assert round_sum(15, 17, 18) == 60
    assert round_sum(12, 13, 14) == 30
    assert round_sum(6, 4, 4) == 10
