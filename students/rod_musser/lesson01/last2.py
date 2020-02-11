def last2(str):
    result = 0
    if (len(str) <= 2):
        return result

    lastTwoChar = str[len(str) - 2:]
    #print(lastTwoChar)

    for i in range(len(str) - 2):
        twoChar = str[i:i + 2]
        #print(twoChar)
        if lastTwoChar == twoChar:
            result = result + 1
    return result
