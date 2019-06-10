def TestNameError():
    try:
        namelist = ["Jinee","Evan"]

        while(True):
            userInput = input("Choose the name -- Jinee or Evan")
            if userInput in namelist:
                print(userInput)
                print("This is it. There is no function to continue.")
            else:
                raise NameError("The name is incorrect.")
    except NameError as e:
        print("the exception is: {0}".format(e))


def TestAttributeError():
    try:
        alist = 1
        alist.append(10)

    except AttributeError as e:
        print("the exception is: {0}".format(e))

def TestValueError():
    try:
        valuelist = ["Ring","Laptop"]

        while(True):
            print (valuelist)
            uservalue = input("Choose what to remove")
            if uservalue in valuelist:
                valuelist.remove(uservalue)
                print("You want to remove", uservalue)
                print("This is it. There is no function to continue.")
            else:
                raise ValueError("The value is incorrect.")
    except ValueError as e:
        print("the exception is: {0}".format(e))

def TestTypeError():
    try:
        typeInt = 2
        typeString = "test string"
        print(typeInt + typeString)
    except TypeError as e:
        print("the exception is: {0}".format(e))

print("Testing Value Error")
print("------------------------")
TestValueError()
print("------------------------")
print("Testing Attirbute Error")
print("------------------------")
TestAttributeError()
print("------------------------")
print("Testing Name Error")
print("------------------------")
TestNameError()
print("------------------------")
print("Testing Type Error")
print("------------------------")
TestTypeError()
print("------------------------")
