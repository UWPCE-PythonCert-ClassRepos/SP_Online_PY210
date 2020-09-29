
def func_name_error():
    #try to print a undefined variable
    print(var_name)

def func_syntax_error():
    #try to print without parentheses, sytax error with Python3
    print "Hello World"
    #print("Hello World!")

def func_type_error():
    #try to add a string to an integer 
    x=2
    y="2"
    print(x+y)

def func_attribute_error():
    #try to return uppercase of a integer
    x=2
    x.upper()


