def front_times(str, n):
    result =""
    repeatlength = 3
    if len(str) < 3:
        repeatlength = len(str)
    for i in range(n):
        result+= str[0:repeatlength]
    return result