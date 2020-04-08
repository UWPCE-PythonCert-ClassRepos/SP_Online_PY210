#!/usr/bin/env python3

import sys

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Elon Musk", [234.25, 2764.87, 9783.0]),
            ]

if __name__ == '__main__':
    main()

def main()
    prompt = "\n".join(("Donor Database",
              "Please choose from below options (i.e. 2):",
              "1 - Send a Thank You",
              "2 - Create a Report",
              "3 - Quit",
              ">>> "))
    while True:
        response = input(prompt)
        if response == "1":
            view_fruits()
        elif response == "2":
            add_fruit()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")