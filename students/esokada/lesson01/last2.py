def last2(str):
    substring = str[-2:]
    count = 0
    for a in range(len(str)-2):
        if str[a:a+2] == substring:
            count += 1
    return count