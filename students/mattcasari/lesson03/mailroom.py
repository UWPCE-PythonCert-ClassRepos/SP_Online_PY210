#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 3, Excercise 1

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part1.html

Description:
    The Program: Part 1
    Write a small command-line script called mailroom.py. This script should be
    executable. The script should accomplish the following goals:

    It should have a data structure that holds a list of your donors and a 
    history of the amounts they have donated. This structure should be 
    populated at first with at least five donors, with between 1 and 3 
    donations each. You can store that data structure in the global namespace.
    The script should prompt the user (you) to choose from a menu of 3 
    actions: “Send a Thank You”, “Create a Report” or “quit”.    

"""

def prompt_user():
    PROMPT_TEXT = ("Select an option:\n"
    "1. Send a Thank You\n"
    "2. Create a Report\n"
    "3. Quit\n"
    "> ")

    result = False
    while True:
        result = int(input(PROMPT_TEXT))
        if 0 < result < 4:
            break;

    return result

def generate_report():
    pass

def send_thank_you():
    pass


def main():
    while True:
        option = prompt_user()

        if option == 1:
            send_thank_you()
        elif option == 2:
            generate_report()
        elif option == 3:
            print("\nExiting Program")
            break
        else:
            pass
    

if __name__ == "__main__":
    main()