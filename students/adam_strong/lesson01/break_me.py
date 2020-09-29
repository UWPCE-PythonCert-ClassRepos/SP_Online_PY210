## BREAK-ME.PY - Lesson 1 Assignment

print('This code has 4 functions which introduce errors: namebreak() is NameError, typebreak() is TypeError, synbreak() is Syntax Error (which is commented out), atrerror() is an AtributeError')

def namebreak(x):
    return x*y

def typebreak(t):
    z = 'str'
    return t**z

##def synerror(b):
##    .     

def atrerror(c):
    c.append(4)
    return