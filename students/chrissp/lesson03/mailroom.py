import sys

# Global Variables
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

prompt = "\n".join(("Welcome to the mailroom!",
                    "Please choose from below options:",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Quit",
                    ">>> "))


def sort_donations(donor_entry):
    """
    Sort Function to return donor donation total for sorting donor list (by donations)

    :param donor_entry: Donor database entry to return donation total for sorting
    :return: Returns donor donation total for sorting
    """
    return sum(donor_entry[1])


def send_thanks():
    """
    Send Thanks function that takes a user input for name and donation.
    """
    donor_name = input("\n What is the Full Name of the donor?").title()
    this_donor = ""

    if donor_name == "Quit":
        main()

    if donor_name == "List":
        for person in donor_db:
            print(person[0])
        send_thanks()
    else:
        this_donation = input("What is the donation amount?")

        if this_donation.title() == "Quit":
            main()
        else:
            for person in donor_db:
                if donor_name == person[0]:
                    this_donor = person[0]
                    person[1].append(int(this_donation))
                    break

            if this_donor == "":
                donor_db.append((donor_name, [int(this_donation)]))

            # Build thank you email
            print(f"\n\nDear {donor_name},\n Thank you for your generous donation of ${this_donation}!\n",
                  "Sincerly,\n Scott's Tots Foundation\n\n")


def create_report():
    """
    Print Report function of current donor database.
    """
    # Sort the donor database by donations (donation total)
    sorted_donors = sorted(donor_db, key=sort_donations, reverse=True)

    # Print table header
    print('Donor Name                |  Total Given  | Num Gifts |  Average Gift ')
    print('----------------------------------------------------------------------')

    for donor in sorted_donors:
        donor_name = donor[0]
        num_gifts = len(donor[1])

        total_gift = 0
        for donation in donor[1]:
            total_gift += donation

        avg_gift = str(round(total_gift / num_gifts, 2))

        # Print formatted donor info line
        print(f"{donor_name:26} ${round(total_gift, 2):>15} {num_gifts:^11d} ${avg_gift:>15}")


def quit_program():
    print("See you next time!")
    sys.exit()


def main():
    while True:
        response = input(prompt)
        if response == "1":
            send_thanks()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_program()
        else:
            print("Sorry, that isn't a valid option.")


if __name__ == "__main__":
    main()