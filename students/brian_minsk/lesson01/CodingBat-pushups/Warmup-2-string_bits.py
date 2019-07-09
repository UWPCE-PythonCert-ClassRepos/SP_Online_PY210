def string_bits(str):
    strBits = str[0]
    for i in range(2, len(str), 2):
        strBits = strBits + str[i]
    return strBits

print(string_bits("abcdefghijklmn"))
  
