def missing_char(str, n):
    return str[:n] + str[(n + 1):]

print(missing_char("kitten", 10))