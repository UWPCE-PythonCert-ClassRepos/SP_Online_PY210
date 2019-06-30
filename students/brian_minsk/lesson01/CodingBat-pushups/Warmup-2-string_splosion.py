def string_splosion(str):
    strSplosion = str[0]
    for i in range(2, len(str) + 1):
        strSplosion = strSplosion + str[:i]
    return strSplosion

print(string_splosion("foobar"))