def near_ten(num):
    mod2near10 = [8,9,0,1,2]
    mod = num % 10
    if mod in mod2near10:
        return True
    return False


if __name__ == "__main__":
    # run some tests
    assert near_ten(12) == True
    assert near_ten(17) == False
    assert near_ten(39) == True