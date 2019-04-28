def name_error():
    """ Generate a NameError """
    return something

def type_error():
    """ Generate a TypeError """
    a = 5
    b = "10"
    return a + b

#def syntax_error():
#    """ Generate a SyntaxError """
#    print("Error"

def attribute_error():
    """ Generate an AttributeError """
    print({}.thing)


#name_error()
#type_error()
#syntax_error()
attribute_error()