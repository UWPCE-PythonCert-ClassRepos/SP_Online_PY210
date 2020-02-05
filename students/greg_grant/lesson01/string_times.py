def string_times(string, n):
    """ Return a duplicated string given a string and a number of times to duplicate the string.
    :param arg1: The string to duplicate
    :param arg2: An integer stating the number of times to duplicate the string

    """
    if not isinstance(string, str):
        raise TypeError
    if not isinstance(n, int):
        raise TypeError

    if n == 0:
        return ""
    else:
        return string + string_times(string, n - 1)


if __name__ == "__main__":
    assert(string_times('Hi', 1) == "Hi")
    assert(string_times('Hi', 2) == "HiHi")
    assert(string_times('Hi', 3) == "HiHiHi")

    try:
        assert(string_times(4, 3) == TypeError)
    except TypeError:
        print("Invalid type for string argument raised successfully.")

    try:
        assert(string_times("Bye", 2.5) == TypeError)
    except TypeError:
        print("Invalid type for number argument raised successfully.")

    print("Passed all tests.")
