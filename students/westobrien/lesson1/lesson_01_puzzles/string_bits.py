def string_bits(str):
    result=""
    for i in range(0,len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result