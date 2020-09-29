def without_end(str):
    nStrLength = len(str)
    return str[1:nStrLength - 1]

print(without_end("foobar"))
print(without_end("fo"))
print(without_end("f"))
