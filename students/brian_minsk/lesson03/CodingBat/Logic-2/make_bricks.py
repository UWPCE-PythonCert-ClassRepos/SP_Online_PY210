def make_bricks(small, big, goal):
    if big == 0: # This is to avoid a divide by zero error later (could have combined in the same statement but this is clearer)
        if goal > small:
            return False
        else:
            return True
    else: # big >= 1
        if small >= goal % (5 * big):
            return True
        else:
            return False

if __name__ == "__main__":
    # run some tests
    assert make_bricks(3, 1, 8) == True
    assert make_bricks(3, 1, 9) == False
    assert make_bricks(3, 2, 10) == True