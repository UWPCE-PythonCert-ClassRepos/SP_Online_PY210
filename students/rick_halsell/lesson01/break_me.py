def syntaxerror():
    print(x)
    #return print(x)


def nameerror1():
    xs = spam * x
    print(x)
    return xs

def TE():
    x = '1'
    sum = x + 1
    return sum

def attributeerror1():
    import re
    x = re.test
    return

x = 'rick'
#nameerror1()
#TE() # type error
#syntaxerror()
attributeerror1()
