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


def thanks(db=donor_db, name=" ", donations="$0.00"):
    print("thanks")


def report(db=donor_db):
    print(donor_db)
    print()
    key = ["name", "total given", "num gifts", "average gift"]
    separator = "|"

    print(f"{key[0]:<18}",
          f"{separator:^3}",
          f"{key[1]:<18}",
          f"{separator:^3}",
          f"{key[2]:>10}",
          f"{separator:^3}",
          f"{key[3]:>15}")
    print("-"*76)

    for i in range(0, (len(donor_db))):
        entry = (donor_db[i])
        name = entry[0]
        # print(name)
        dons = entry[1]
        totes = sum(dons)
        # print(totes)
        nums = len(dons)
        # print(nums)
        aves = totes/nums
        # print(aves)
        print(f"{name:<18}", f"{separator:^3}", f"{totes:>18.2f}", f"{separator:^3}", f"{nums:^10}", f"{separator:^3}",
              f"{aves:>15.2f}")


def quit_prog():
    print("quitting - see you next time")
    quit()


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

        else:
            print("sorry, that's not a valid option")


main()
