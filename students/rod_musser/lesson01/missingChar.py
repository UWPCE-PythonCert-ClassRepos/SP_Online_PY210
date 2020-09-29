def missing_char(str, n):
    length = len(str)
    firstStr = str[0:n]
    secondStr = str[(n+1):length]
    return firstStr + secondStr