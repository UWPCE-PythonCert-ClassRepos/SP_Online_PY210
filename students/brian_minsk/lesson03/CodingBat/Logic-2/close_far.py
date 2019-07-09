def close_far(a, b, c):
    if is_close(a, b):
        return not is_close(a, c)
    elif is_close(a, c):
        return not is_close(a, b) 

def is_close(a, b):
    if abs(a - b) > 1:
        return False
    return True

if __name__ == "__main__":
    # run some tests
    assert close_far(1, 2, 10) == True
    assert close_far(1, 2, 0) == False
    assert close_far(4, 1, 3) == True