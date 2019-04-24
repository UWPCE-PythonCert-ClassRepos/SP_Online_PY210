def diff21(n):
    if n<=21:
        return 21 - n
    else:
        return (n-21) * 2

def missing_char(str, n):
    if len(str) ==0:
        return ('Cant be an empty string')
    if n > (len(str)):
        return ("There is no character in {} at index {}". format(str, n))
    else:
        return str.replace(str[n], '')


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return False
    return False

def sum_double(a, b):
    if a ==b:
        return 2*(a+b)
    else:
        return a+b


def parrot_trouble(talking, hour):
    if hour < 7 or hour >20 :
        if talking:
            return True
        else:
            return False
    else:
        return False


def makes10(a, b):
    # if a ==10 or b ==10 or a+b ==10:
    #     return True
    # else:
    #     return False
    return (if a ==10 or if b ==10 or if a+b ==10)


