#!/usr/bin/env python3

import sys


def yes():
    print("Yes")


def no():
    print("No")


def quit_prog():
    sys.exit()


resp_dict = {0: yes, 1: no, 3: quit_prog}

resp_dict.get(0)()

thanks_c = "peter pan"
add_q = str(input("That name is not in the list, would you like to add it? (y/n): "))
add_q = add_q.lower().strip()
if add_q == "q":
    pass
if add_q == "n":
    pass
if add_q == "y":
    print("Adding", thanks_c.title(), "to the donor list.")

