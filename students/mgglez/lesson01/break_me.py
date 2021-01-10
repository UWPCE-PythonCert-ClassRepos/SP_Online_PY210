#!/usr/bin/env python

# ---------------------------------------------------------------------------- #
# Title: Lesson 1
# Description: Python Pushups
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,12-28-2020, Task 1 - Python Pushups
# ---------------------------------------------------------------------------- #

def raise_name_error():
    '''
    Function that raises a NameError
    '''
    text = input("Enter something here to generate the NameError exception: ")
    # A NameError exception will be raised since test variable is a typo, correct one should be text
    print(test)

def raise_type_error():
    '''
    Function that raises a TypeError
    '''
    string_value = "This is a string"
    int_value = 5
    # A TypeError exception will be raised here cause Python does not know how to add an int and a string together
    print(string_value + int_value)

def raise_syntax_error():
    '''
    Function that raises a Syntax Error when the final line of code is uncommented
    '''
    my_profile = {
        'name': 'Mercedes',
        'state': 'Nebraska',
    }
    # This raises a SyntaxError exception as there is a comma missing. Uncomment line below to raise Syntax Error
    #print("My name is %s. I live in %s" % (my_profile['name'] my_profile['state']))

def raise_attr_error():
    '''
    Function that raises an AttributeError
    '''
    int_value = 5
    # This raises an AttributeError exception as Integers do not have an 'append' method.
    int_value.append(10)


def exception_menu():
    while True:
        print("Select one of the Python Exceptions below and raise it!:")
        print("========================================================")
        print("(1) - NameError Exception")
        print("(2) - TypeError Exception")
        print("(3) - SyntaxError Exception")
        print("(4) - AttributeError Exception")
        exception_option = input("Select option from [1-4]: ")
        try:
            exception_option = int(exception_option)
        except ValueError:
            print("\nThe exception option you enter is invalid. Please select options from 1 to 4\n\n")
            continue
        if exception_option == 1:
            raise_name_error()
        elif exception_option == 2:
            raise_type_error()
        elif exception_option == 3:
            raise_syntax_error()
        else:
            raise_attr_error()

if __name__ == '__main__':
    exception_menu()