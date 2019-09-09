#! /usr/bin/env python3

import sys
from operator import itemgetter

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Marc Benioff", [45023.15, 442.30])
            ]


prompt = "\n".join(("Please choose from below options:",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Quit",
                    ">>> "))


def quit_program():
    """
    Informs the user the program will exit and 
    gracefully exits the program.
    """

    print("The program will now exit.")
    sys.exit()


def send_thank_you():
    """
    Prints a  in a nice formatted way that contains the 
    table/titles that will organize  donor name, the total amount 
    they have donated, the number of donations, and their 
    corresponding average gift amount in a neat formatted manner.
    """

    donor = "List"
    names = []
    while donor == "List":
        donor = input(
            "Please type a donor's full name or type 'list' to view donors. \n >>> ").title()
        if donor == "Quit":
            quit_program()

        # Prints a list of donors for the user to view   
        elif donor == "List":
            for row in donor_db:
                names.append(row[0])
            print("\n".join(["{}"] * len(donor_db)).format(*names))

        # If the user isn't a past donor, the donor gets added
        elif donor not in names:
            donor_db.append((donor, []))

    new_donation = find_tuple(donor)

    # Print out template that will be emailed to donor.
    print("Thank you {} for your generous donation of ${:.2f}. ".format(
        donor, new_donation), end=" ")
    print("Your contribution will help our organization do good out in the community.")


def find_tuple(user_input):
    """
    Accepts user input for a donation amount, adds the amount
    to the donor database and returns the donation amount.

    :param user_input: string used to find tuple in database 
    :type user_input: string
    """

    donation = float(input("What's the new donation amount? \n >>> "))
    if donation <= 0:
        print("Not a valid donation amount!")
        quit_program()

    # Append donation amount to the donor's donation list
    for index in donor_db:
        if user_input == index[0]:
            index[1].append(donation)
    return donation


def create_report():
    """
    Prints a table in a nice formatted way that contains the 
    donor name, the total amount they have donated, the number
    of donations, and their corresponding average gift amount.
    """

    create_header()
    sorted_list = []
    computed_list = []

    for user_input in donor_db:
        total_donation, avg_donation, num_of_donations = compute_donation(
            user_input[1])

        # Create a sorted list that is based on the total donation amount
        computed_list.append(
            (user_input[0], total_donation, num_of_donations, avg_donation))
    sorted_list = sorted(computed_list, key=itemgetter(1), reverse=True)

    for sorted_item in sorted_list:
        print("{:<27}${:>12.2f}{:>14}   ${:>13.2f}".format(*sorted_item))


def create_header():
    """
    Prints a table in a nice formatted way that contains the 
    table/titles that will organize  donor name, the total amount 
    they have donated, the number of donations, and their 
    corresponding average gift amount in a neat formatted manner.
    """

    header = "{:<26}|{:^15}|{:^13}|{:>14}".format(
        "Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print("\n" + header)
    print("-" * len(header))


def compute_donation(donations):
    """
    Accepts a list and calculates the total amount given,
    the number of donations, and the average amount of each
    donor's donation.

    :param donations: list of donations per donor
    :type donations: list
    """

    total_amount = 0
    donation_num = 0

    # Increment both number of donations and the total donation amount
    for amount in donations:
        donation_num += 1
        total_amount += amount

    total_amount = round(total_amount, 2)
    avg_amount = round(total_amount / donation_num, 2)

    return total_amount, avg_amount, donation_num


def main():

    # Prints the main menu that the user can interact with
    print("Welcome to the Mailroom App!")

    while True:
        print("Choose the selection by typing in the action name or")
        print("by typing in the corresponding number")
        response = input(prompt).title()
        if response == "3" or response == "Quit":
            quit_program()
        elif response == "1" or response == "Send A Thank You":
            send_thank_you()
            print("\n\n")
        elif response == "2" or response == "Create A Report":
            create_report()
            print("\n\n")
        else:
            print("Not a valid option!\n\n")


if __name__ == '__main__':
    main()
