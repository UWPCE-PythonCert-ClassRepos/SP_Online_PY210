# #!/usr/bin/env python3

import sys


def y_or_n(veriable):
    """
    this is a stupid function that strips and lowers whatever is passed to it
    :param veriable: input string, usually
    :return: stripped and lowered, makes checking for y or n easier
    """
    veriable = veriable.strip().lower()
    return veriable


question = input("do you like pankakes? ")
ans = y_or_n(question)
while ans != "y" and ans != "n" and ans != "q":
    ans = input("Please enter y or n: ")
if ans == "q":
    sys.exit()
if ans == "n":
    print("no")
if ans == "y":
    print("yeah")
