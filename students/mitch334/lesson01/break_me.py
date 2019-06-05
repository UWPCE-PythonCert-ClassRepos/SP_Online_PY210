# In the break_me.py file write four simple Python functions:
#
# Each function, when called, should cause an exception to happen
# Each function should result in one of the four most common exceptions you’ll find.
# for review: NameError, TypeError, SyntaxError, AttributeError
# (hint – the interpreter will quit when it hits a Exception – so you can comment out all but the one you are testing at the moment)
#
# Use the Python standard library reference on Built In Exceptions as a reference

def NameError():
    print(x)

def TypeError():
    x = 1
    y = "2"
    print(x + y)

def SyntaxError():
    z=1
    print(z$0)

def AttributeError():
    x = 1
    print(x.name)
    
