def string_bits(str):
    result = ''
    skip = False
    for i in str:
        if not skip:
            result += i
        skip = not skip
    return result
