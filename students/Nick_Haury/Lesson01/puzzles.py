def string_match(a, b):
    # find shortest string to iterate over
    strLen = 0
    if len(a) > len(b):
        strLen = len(b)
    else:
        strLen = len(a)

    # count the number of len 2 substring matches
    count = 0
    for i in range(strLen - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1;

    return count