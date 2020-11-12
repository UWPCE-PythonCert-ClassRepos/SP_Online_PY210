def createNameError():
    name = "Kristy"
    try:
        print("My name is " + nome)
    except NameError:
        print("You have a NameError")

def createTypeError():
    name = "Kristy"
    try:
        new_name = name + 5
    except TypeError:
        print("You have a TypeError")

def createSyntaxError():
    name = "Kristy"
    # try:
    #     print name
    # except SyntaxError:
    #     print("You have a SyntaxError")

def createAttributeError():
    name = "Kristy"
    try:
        print(name.last())
    except AttributeError:
        print("You have an AttributeError")

def sleep_in(weekday, vacation):
    if vacation: 
        return True
    elif not weekday and not vacation:
        return True
    elif weekday and not vacation:
        return False

if __name__ == "__main__":
    createNameError()
    createTypeError()
    createSyntaxError()
    createAttributeError()
