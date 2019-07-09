def date_fashion(you, date):
    if (you > 7 or date > 7):
        return 2
    elif (you < 3 or date < 3):
        return 0
    else:
        return 1

if __name__ == "__main__":
    # run some tests
    assert (date_fashion(5,10)) == 2
    assert (date_fashion(5,2)) == 0
    assert (date_fashion(5,5)) == 1
    