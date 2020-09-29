def last2(str):
    endstring = str[len(str)-2:]
    count= 0
    for i in range(len(str)-2):
        if str[i:i+2] == endstring:
            count+=1
    return count