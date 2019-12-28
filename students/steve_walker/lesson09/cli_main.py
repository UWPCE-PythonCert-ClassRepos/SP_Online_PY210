#!/usr/bin/env python3

"""
Stores donor information and allows users to automatically create individual
thank you notes, bulk thank you notes, and reports about donors.

    Donor class contains individual records (name, a list of donations, and
    several stats about their donations (sum, number, and avg).

    DonorCollection class contains a list of Donor objects for the purpose
    of storing and returning data on all donors, as through bulk thank you
    notes and detailed donor reports.
"""

import sys
from donor_models import Donor, DonorCollection

# Initial donations
initial_donations = {"Rhianna": [747, 3030303, 1968950],
                     "Grumps": [5.99],
                     "EatPraySlay": [100000, 200000, 300000],
                     "Muir": [469503, 50000, 186409],
                     "Spacewalker": [4406, 342]}

donors = DonorCollection.from_dict(initial_donations)


def get_donor_name():
    """Get donor name from user."""

    while True:
        donor_name = input("Who would you like to thank? (Type 'list' "
                           "to see a list of donors.)\n  Full Name: ")

        # Print list of existing donors to choose from
        if donor_name.lower() == "list":
            print("\n".join(donors.list()))

        # Ensure the user has entered a name
        elif donor_name.replace(" ", "").replace(".", "").replace(",", "").\
                replace("'", "").isalpha():

            # Create new Donor object if one doesn't already exist
            if donor_name not in donors.list():
                print(f"\nAdding {donor_name} to the database. "
                      "Enter c to confirm and x to undo.")

                while True:
                    confirmation = input(">>>")

                    if confirmation.lower() == "c":
                        donor = Donor(donor_name)
                        donors.add(donor)
                        return donor

                    elif confirmation.lower() == "x":
                        break

                    else:
                        print("Please enter c to confirm or x to undo!")

            else:
                # Return existing Donor from list of existing donors
                donor = donors.donors[donors.list().index(donor_name)]
                return donor

        else:
            print("Please type a name! Use alpha or basic punctuation.\n")


def get_donation():
    """Get new donation amount from user."""

    while True:
        try:
            donation_amount = float(input(
                "Please enter the donation amount: "))
            if donation_amount < 0:
                print("\nPlease enter a positive number!\n")
                continue

        except ValueError:
            print("\nPlease enter a positive number!\n")

        else:
            return donation_amount


def thank_donor():
    """Get, store and update donor info, then thank donor."""

    donor = get_donor_name()  # Returns donor object
    donor.add_donation(get_donation())  # Adds donation to that donor object
    print(donor.write_letter())


def thank_all():
    """Thank each donor for their most recent donations."""

    for donor in donors.donors:
        f = donor.name + ".txt"
        with open(f, 'w') as f:
            f.write(donor.write_letter())


def display_report():
    """Display a report of all donor records to date."""

    print(" " + "-" * 60 + "\n Donor Name" + " " * 10 +
          "| Total Given | Num Gifts | Average Gift\n " + "-" * 60)

    for donor in donors.sorted():
        print(f" {donor.name:<20} ${donor.sum_donations:>11.2f}"
              f"{donor.num_donations:>12}  ${donor.avg_donation:>12.2f}")


def end_game():
    """Quit program."""

    print("\nThanks for playing!")
    sys.exit()


def main():
    """Display the user menu, then act on the user's selection."""

    main_menu = {"1": thank_donor,
                 "2": thank_all,
                 "3": display_report,
                 "q": end_game}

    while True:
        user_action = input("\n".join((
            "\nWhat would you like to do?",
            "  Enter 1 to create a thank you for a single donor",
            "  Enter 2 to create a thank you for all donors",
            "  Enter 3 to create a report",
            "  Enter q to quit.",
            "  >>>")))

        try:
            main_menu[user_action]()

        except SystemExit:
            sys.exit(1)

        except KeyError:
            print("Let's behave. Try again using one of the options!")


if __name__ == "__main__":
    main()
