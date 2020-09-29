def NameError_fun(a):
    try:
        return(a+b)

    except NameError:
        print ("Houston we have a \"NameError\"")


def TypeError_fun(a):
    try:
        return a + 'This is a string'
    except TypeError:
        print("Houston we have a \"TypeError\" exception happened. What you entered as argument is {}".format(type(a)))


def SyntaxError_fun(a):
    try:
        eval('abs(-1')
    except SyntaxError:
        print ("Houston we have a \'SyntaxError\'")

def AttributeError_fun(a):
    try:
       b = a.isupper()
       return b
    except AttributeError:
        print ("Houston we have a \'AttributeError\'")

NameError_fun(3)
TypeError_fun(3)
SyntaxError_fun(3)
AttributeError_fun(3)

