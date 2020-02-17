def string_match(a, b):
    result = 0
    if (len(a) <= 1):
        return result
    for i in range(len(a) - 1):
        subA = a[i: i + 2]
        subB = b[i: i + 2]
        if subB == subA:
          result = result + 1
    return result
