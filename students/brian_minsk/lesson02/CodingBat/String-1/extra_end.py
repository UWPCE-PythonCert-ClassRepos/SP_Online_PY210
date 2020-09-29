def extra_end(str):
    nStrLength = len(str)
    strLast2 = str[nStrLength - 2:nStrLength]
    return strLast2 + strLast2

print(extra_end("foobar"))