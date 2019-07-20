def caught_speeding(speed, is_birthday):
    if speed <= 60 or (is_birthday and speed <= 65):
        return 0
    elif (speed >= 61 and speed <=80) or (is_birthday and speed >= 66 and speed <=85):
        return 1
    else:
        return 2

if __name__ == "__main__":
    # run some tests
    assert caught_speeding(60, False) == 0
    assert caught_speeding(65, False) == 1
    assert caught_speeding(65, True) == 0