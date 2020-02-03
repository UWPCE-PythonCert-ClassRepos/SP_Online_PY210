def string_times(string, n):
    """ Duplicate a string multiple times given a string and a number of times to diisplicate the string."""
    if not isinstance(string, str):
        return ""
    if not isinstance(n, int):
        return ""    

    if n == 0:
        return ""
    else:
        return string + string_times(string, n -1)

if __name__ == "__main__":
    assert(string_times('Hi', 1) == "Hi")
    assert(string_times('Hi', 2) == "HiHi")
    assert(string_times('Hi', 3) == "HiHiHi")
    assert(string_times(4, 3) == "")
    assert(string_times("Bye", 2.5) == "")
    print("Passed all tests.")