def left2(str):
    strLeft2 = str[:2]
    strTheRest = str[2:]
    return strTheRest + strLeft2

print(left2("foobar"))