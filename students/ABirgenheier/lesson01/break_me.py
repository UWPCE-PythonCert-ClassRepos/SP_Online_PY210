print("This code has four functions which introduce the following errors: \n")
print("-    name_break() will create a NameError\n")
print("-    type_break() will create a TypeError\n")
print("-    syn_break() will create a SyntaxError\n")
print("-    attr_break() will create a AttribruteError\n")


def name_break(x):
    return x*y


def type_break(t):
    z = "string"
    return t ** z


# def syn_break(t):
#     .


def attr_break(a):
    a.append(10)
