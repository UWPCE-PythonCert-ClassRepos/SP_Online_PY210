def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return a*b < 0

def not_string(str):
    if str[:3] == 'not':
        return str
    else:
        return 'not ' + str

def missing_char(str, n):
    return str[:n] + str[n+1:]
 