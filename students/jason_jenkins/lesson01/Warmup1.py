# Lesson 1: Warmup Puzzles

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
         return False

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

def sum_double(a, b):
    if (a == b):
        return (a+b) * 2
    else:
        return a+b

def diff21(n):
    if(n > 21):
        return abs(21 - n) * 2
    else:
        return abs(21 - n)

def parrot_trouble(talking, hour):
    if (talking and (hour < 7 or hour > 20)):
        return True
    else:
        return False

def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif (a + b == 10):
        return True
    else:
        return False

def near_hundred(n):
    if(abs(n-100) <= 10 or abs(n-200) <= 10):
        return True
    else:
        return False

def pos_neg(a , b, negative):
    if(negative):
        return (a < 0 and b < 0)
    else:
        return (a * b < 0)

def not_string(str):
    if(str[0:3] == "not"):
        return str
    else:
        return "not " + str

def missing_char(str, n):
    str = str[0:n] + str[n+1:len(str)]
    return str

def front_back(str):
    if(len(str) <= 1):
        return str
    elif (len(str) == 2):
        return str[1] + str[0]
    else:
        return str[len(str)-1] + str[1:len(str)-1] + str[0]

def front3(str):
    if(str > 3):
        str = str[0:3]

    result = ""

    for x in range(3):
        result += str

    return result
