# Lesson 1: String2

def double_char(str):
    result = ""

    for x in str:
        result += x + x

    return result


def count_hi(str):
    count = 0

    for x in range(len(str) - 1):
        if str[x:(x + 2)] == "hi":
            count += 1

    return count


def cat_dog(str):
    catCount = 0
    dogCount = 0

    for x in range(len(str) - 2):
        if(str[x:(x + 3)] == "cat"):
            catCount += 1

        if(str[x:(x + 3)] == "dog"):
            dogCount += 1

    return catCount == dogCount


def count_code(str):
    count = 0

    for x in range(len(str) - 3):
        if(str[x:x + 2] == "co" and str[x + 3] == "e"):
            count += 1

    return count


def end_other(a, b):
    a = a.lower()
    b = b.lower()

    if (len(a) == len(b)):
        return a == b

    if (len(a) < len(b)):
        return b[len(b) - len(a):] == a

    return a[len(a) - len(b):] == b


def xyz_there(str):
    if str[0:3] == "xyz":
        return True

    for x in range(len(str) - 3):
        if not (str[x] == ".") and str[x + 1: x + 4] == "xyz":
            return True

    return False
