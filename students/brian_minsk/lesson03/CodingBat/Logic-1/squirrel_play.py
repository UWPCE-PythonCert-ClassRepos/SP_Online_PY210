def squirrel_play(temp, is_summer):
    return temp >= 60 and (temp <= 90 or (is_summer and temp <= 100))

if __name__ == "__main__":
    # run some tests
    assert squirrel_play(70, False) == True
    assert squirrel_play(95, False) == False
    assert squirrel_play(95, True) == True