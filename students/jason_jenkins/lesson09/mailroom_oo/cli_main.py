#!/usr/bin/env python3

"""
Lesson 9: Mail Room Part Object Oriented (cli_main)
Course: UW PY210
Author: Jason Jenkins
"""

from donor_models import Donor, DonorCollection
import sys


def send_thanks():
    """
    Method used to probt donor name or list out donors
    """
    response = ""

    while True:
        response = input('Input donors name, "list", or "exit": ').lower()

        if(response == "exit"):
            break
        elif response == "list":
            print(donors.get_list())
        else:
            break

    if(response != "exit"):
        try:
            total = float(input('Input amount to donate or "0" to exit: '))
            if(total != 0):
                print(donors.donate(response, total))
        except ValueError:
            print("Must input a valid float")


def display_report():
    print(f"{'Donor Name':30}|{'Total Given':^16}|", end='')
    print(f"{'Num Gifts':^14}|{'Average Gift':^16}")
    print(f"{'-'*79}")

    for row in donors.get_report():
        print(f"{row[0]:30} ${row[1]:15}{row[2]:15} ${row[3]:15}")


def quit_program():
    """
    Method used to quit the program
    """

    sys.exit()


def startup_prompt():
    """
    Prombt user for action they what to take
    """

    while True:
        print()
        print("Do you want to:")
        print('   1 - Send a Thank You to a single donor.')
        print('   2 - Create a Report.')
        print('   3 - Quit.')

        response = input("Input numbered option you wish to do: ").strip()

        try:
            menu_dict[response]()
        except KeyError:
            print(f"{response} is not a valid input.")


# Global Variables
donors = DonorCollection()
menu_dict = {
    "1": send_thanks,
    "2": display_report,
    "3": quit_program
}


if __name__ == "__main__":
    # Initial Setup
    will_gates = Donor("William Gates", 1345.462)

    mark_zuck = Donor("Mark Zuckerberg", 12546.124)
    mark_zuck.give(13445.124)

    jeff_bezo = Donor("Jeff Bezos", 1234.123)
    jeff_bezo.give(12341431.12)

    paul_allen = Donor("Paul Allen", 734.12)
    paul_allen.give(124.41)
    paul_allen.give(10000)

    jason_jenkins = Donor("Jason Jenkins", 10)
    jason_jenkins.give(20)
    jason_jenkins.give(30)
    jason_jenkins.give(40)
    jason_jenkins.give(50)
    jason_jenkins.give(60)

    donors.append(will_gates)
    donors.append(mark_zuck)
    donors.append(jeff_bezo)
    donors.append(paul_allen)
    donors.append(jason_jenkins)

    startup_prompt()
