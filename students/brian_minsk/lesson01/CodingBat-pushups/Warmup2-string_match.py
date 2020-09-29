def string_match(a, b):
    nCount = 0
    nEnd = len(a)
    if len(b) < nEnd:
        nEnd = len(b)
    for i in range(nEnd - 1):
        strSubA = a[i:i+2]
        strSubB = b[i:i+2]
        if strSubA == strSubB:
            nCount = nCount + 1
    return nCount

print(string_match('xxcaazz', 'xxbaaz'))
