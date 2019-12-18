#!/usr/bin/env python

"""
string format lab

Tasks 1-6
"""


def Task_One():
    a_in, b_in, c_in, d_in = query()  # common prompt function for Task Two as well
    # remaining lines format values per instructions
    a_out = "file_" + a_in.zfill(3) + " : "
    b_out = "{0:8.2f}, ".format(b_in)
    c_out = "{0:8.2e}, ".format(c_in)
    d_out = "{0:8.2e}".format(d_in)
    print(a_out + b_out + c_out + d_out)


def Task_Two():
    a_in, b_in, c_in, d_in = query()  # common prompt function for Task One as well
    # single statement with 3x placeholders.  Used 9 spaces instead of 8, and got rid of
    # manual last space.  Used right justify.
    print("file_" + a_in.zfill(3) + " :" + "{:>9.2f},{:>9.2e},{:>9.2e}".
          format(b_in, c_in, d_in))


def query():  # prompt function for Tasks One and Two
    a_Qin = input("enter 1st of 4 tuple values, a positive integer up to and including 999: ")
    b_Qin = float(input("enter 2nd of 4 tuple values, any float: "))
    c_Qin = int(input("enter 3rd of 4 tuple values, any float: "))
    d_Qin = float(input("enter last of 4 tuple values, any float: "))
    return (a_Qin, b_Qin, c_Qin, d_Qin)


def Task_Three(value_tuple):
    length_tuple = len(value_tuple)
    print(("the {:d} numbers are: " + ", ".join(["{}"] * length_tuple)).
          format(length_tuple, *value_tuple))


def Task_Four(tuple5):
    list5 = []
    for i, item in enumerate(tuple5):
        list5. insert(i, str(item))
    print("{} {} {} {} {}".format(list5[3].zfill(2), list5[4].zfill(2), list5[2], list5[0].
                              zfill(2), list5[1].zfill(2)))


def Task_Five(list4):
    vowels = "aeiouAEIOU"
    fruits = list4[::2]  # fruits isolated
    weight_fruit = list4[1::2]  # weights isolated
    an = 'an'
    a = 'a'
    # this f-string is meant to demonstrate what can be done with the feature.  It's probably
    # unnecessarily difficult to read, and can be made simpler by using iteration and
    # conditionals to define input values.  Also, a format string can be used instead for any
    # length of input values.
    print(f'The weight of {an if fruits[0][0] in vowels else a} {"".join(list(fruits[0][0:-1])).upper() if fruits[0][-1] == "s" else "".join(list(fruits[0])).upper()} is {weight_fruit[0] * 1.2} and the weight of {an if fruits[1][0] in vowels else a} {"".join(list(fruits[1][0:-1])).upper() if fruits[1][-1] == "s" else "".join(list(fruits[1])).upper()} is {weight_fruit[1] * 1.2}')


def Task_Six():
    query = 'yes'  # next 6 lines setup space for the input loop
    last = []
    first = []
    age = []
    cost = []
    i = 0
    while query == 'yes':  # this is the input loop
        last.insert(i, input("Please provide a last name: "))
        first.insert(i, input("Please provide a first name: "))
        age.insert(i, int(input("Please provide an age in integer years: ")))
        cost.insert(i, float(input("Please provide a cost in float dollars: ")))
        query = input("Is there another entry? ")
        i += 1
    for l, f, a, c, in zip(last, first, age, cost):  # this prints the rows
        print("{:<15}| {:<15}|{:>4} |{:8.2f}".format(l, f, a, c))

    # This is the start of input based tuple construction.  Afterwards, only one line will be
    # used to print as specified
    length = int(input("Please provide a tuple length: "))
    num = (input("Please provide a number (it will constitute every value of the tuple): "))
    list10 = [num] * length
    tuple10 = tuple(list10)  # now we have the tuple built.  Only one more line from here:
    print(("{:^5}|" * (length - 1) + "{:^5}").format(*tuple10))

