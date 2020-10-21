# PY210 Lesson 01 - Chase Dullinger

def tossNameError():
    # Can't print variable that doesn't exist
    print(nonExistantVariable)

def tossTypeError():
    # Can't add incompatible types (int and str)
    x=5
    y="5"
    x+y

# def tossSynataxError():
#     # Can't start a varible name with number
#     if False:
#         pass
#     else:
#         1a

def tossAttributeError():
    # int has no lower method
    x=1
    print(x.lower())

#tossNameError()
#tossTypeError()
#tossSynataxError()
tossAttributeError()
