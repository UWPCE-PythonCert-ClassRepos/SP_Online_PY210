#!/usr/bin/env python3
import tempfile
import time
import sys
import donor_models as dm
"""
A  module for handling command line interface for a donor program
"""


def thank_you():
    new_donor = dm.donor()

def print_report():
    pass


def print_all():
    pass


def menu_input():
    return input(
        "\nSelect an option number:"
        "\n1. Send a Thank You"
        "\n2. Create a Report"
        "\n3. Send letters to all donors"
        "\n4. Quit\n"
    )


def list_donors():
    pass


def main():
    menu_switch = {
        "1": thank_you,
        "2": print_report,
        "3": print_all,
        "4": sys.exit
    }
    while True:
        user_selection = menu_input()
        action = menu_switch.get(user_selection)
        try:
            action()
        except TypeError:
            print("Please provide a valid option \n")


if __name__ == '__main__':
    main()
