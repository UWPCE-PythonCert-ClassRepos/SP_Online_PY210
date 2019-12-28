#!/usr/bin/env python3
import sys

donor_records = {}

# Initial donations
initial_donations = {"Rhianna": [747, 3030303, 1968950],
                     "Grumps": [5.99],
                     "EatPraySlay": [100000, 200000, 300000],
                     "Muir": [469503, 50000, 186409],
                     "Spacewalker": [4406, 342]}


def update_record(donor_name):
    """
    Update donor record of donor_name after a new donation.

    :param donor_name: The donor record to update.
    """

    donations = donor_records[donor_name]["donations"]
    donor_records[donor_name]["sum"] = sum(donations, 0)
    donor_records[donor_name]["numGifts"] = len(donations)
    donor_records[donor_name]["avgGift"] = sum(donations, 0)/len(donations)


# Populate initial donor records
for donor in initial_donations:
    donor_records[donor] = {"name": donor,
                            "donations": initial_donations[donor]}
    update_record(donor)


def get_donor_name():
    """Get donor name from user."""

    while True:
        donor_name = input("Who would you like to thank? (Type 'list' "
                           "to see a list of donors.)\n  Full Name: ")

        # Print list of existing donors to choose from
        if donor_name.lower() == "list":
            print("\n".join(donor_records.keys()))

        # Ensure the user has entered a name
        elif donor_name.replace(" ", "").replace(".", "").replace(",", "").\
                replace("'", "").isalpha():

            if donor_name not in donor_records:
                print(f"\nAdding {donor_name} to the database. "
                      "Enter c to confirm and x to undo.")

                while True:
                    confirmation = input(">>>")

                    if confirmation.lower() == "c":
                        return donor_name

                    elif confirmation.lower() == "x":
                        break

                    else:
                        print("Please enter c to confirm or x to undo!")

            else:
                return donor_name

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


def store_donation(donor_name, donation_amount):
    """
    Store new donation record.

    :param donor_name: The donor record to update.
    :param donation_amount: The value of the new donation.
    """

    if donor_name in donor_records:
        donor_records[donor_name]["donations"].append(donation_amount)

    else:  # If this is a new donor, create new donor entry
        donor_records[donor_name] = {
            "name": donor_name,
            "donations": [donation_amount]}


def write_letter(donor_name):
    """
    Write a thank you note to donor_name.

    :param donor_name: The donor record to update.
    """

    last_donation = donor_records[donor_name]["donations"][-1]
    return f"To the esteemed {donor_name}:\n\n" \
           "Thank you for your generous donation of " \
           f"${last_donation:.2f}. You're a champion!"


def thank_donor():
    """Get, store and update donor info, then thank donor."""

    donor_name = get_donor_name()
    store_donation(donor_name, get_donation())
    update_record(donor_name)
    print(write_letter(donor_name))


def thank_all():
    """Thank each donor for their most recent donations."""

    for donor in donor_records:
        f = donor + ".txt"
        with open(f, 'w') as f:
            f.write(write_letter(donor))


def create_report():
    """Sort donor records by greatest total donations."""

    return sorted(donor_records.items(), key=lambda x: x[1]["sum"],
                  reverse=True)


def display_report():
    """Display a report of all donor records to date."""

    print(" " + "-" * 60 + "\n Donor Name" + " " * 10 +
          "| Total Given | Num Gifts | Average Gift\n " + "-" * 60)

    for row in create_report():
        print(" {name:<20} ${sum:>11.2f}{numGifts:>12}  "
              "${avgGift:>12.2f}".format(**row[1]))


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
