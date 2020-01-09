#!/usr/bin/env python3

# sample data for donor db from tutorial; db is a list of tuples, with a donor name and list of donations

donor_db = [
            ("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])
            ]

# The script should prompt the user (you) to choose
# from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

# def


def thanks(donor_db, name, donations):
    print("thanks")


def report(donor_db):
    print(donor_db)


def quit_prog():
    print("quit")


def main():
    while True:
        print("""
        Menu of Options
        1) Send a 'Thank You'
        2) Create a report
        3) Exit Program
        """)
        usrchoice = str(input("Which option would you like to perform? [1 to 3]: "))
        print()  # adding a new line

        # Choice 1 -Show the current items in the table
        if usrchoice.strip() == '1':
            thanks()

        elif usrchoice.strip() == '2':
            report()

        elif usrchoice.strip() == '3':
            quit_prog()


main()
