def make_chocolate(small, big, goal):
    small_goal = goal - (5 * big)
    if small < small_goal:
        return -1
    return small_goal

if __name__ == "__main__":
    # run some tests
    assert make_chocolate(4, 1, 9) == 4
    assert make_chocolate(4, 1, 10) == -1
    assert make_chocolate(4, 1, 7) == 2 