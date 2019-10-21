import sys

# Global Variables
donor_db = [{"name": "William Gates, III", "donations": [653772.32, 12.17]},
            {"name": "Jeff Bezos", "donations": [877.33]},
            {"name": "Paul Allen", "donations": [663.23, 43.87, 1.32]},
            {"name": "Mark Zuckerberg", "donations": [1663.23, 4300.87, 10432.0]},
            ]

prompt = "\n".join(("Welcome to the mailroom!",
                    "Please choose from below options:",
                    "1 - Send a Thank You to a Single Donor",
                    "2 - Create a Report",
                    "3 - Send Thank you to All Donors",
                    "4 - Quit",
                    ">>> "))

letter_template = ("Dear {donor_name},\n\tThank you for your generous donation of ${last_donation}!\n"
                   "\tYour {total_donations} donations wll be used to supply children with laptop batteries.\n\n"
                   "Greatest thanks from,\n\tScott's Tots Foundation\n")


def sort_donations(donor_entry):
    """
    Sort Function to return donor donation total for sorting donor list (by donations)

    :param donor_entry: Donor database entry to return donation total for sorting
    :return: Returns donor donation total for sorting
    """
    return sum(donor_entry["donations"])


def send_thanks():
    """
    Send Thanks function that takes a user input for name and donation.
    """
    user_input = input("\n What is the Full Name of the donor?").title()
    this_donor = ""

    if user_input == "Quit":
        main()

    if user_input == "List":
        for person in donor_db:
            print(person["name"])
        send_thanks()
    else:
        this_donation = input("What is the donation amount?")

        if this_donation.title() == "Quit":
            main()
        else:
            for person in donor_db:
                if user_input.lower() == person["name"].lower():
                    this_donor = person
                    person["donations"].append(float(this_donation))
                    break

            if this_donor == "":
                donor_db.append({"name": user_input, "donations": [float(this_donation)]})
                this_donor = donor_db[-1]

            this_letter = {'donor_name': this_donor["name"],
                           'last_donation': this_donation,
                           'total_donations': len(this_donor["donations"])}

            # Build thank you email
            print(letter_template.format(**this_letter))


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
        donor_name = donor["name"]
        num_gifts = len(donor["donations"])

        total_gift = 0
        for donation in donor["donations"]:
            total_gift += donation

        avg_gift = str(round(total_gift / num_gifts, 2))

        # Print formatted donor info line
        print(f"{donor_name:26} ${round(total_gift, 2):>15} {num_gifts:^11d} ${avg_gift:>15}")


def send_thanks_all():
    for person in donor_db:
        this_letter = {'donor_name': person["name"],
                       'last_donation': person["donations"][-1],
                       'total_donations': len(person["donations"])}

        # Build thank you email
        file_name = person["name"] + ".txt"
        with open(file_name, 'w') as outfile:
            outfile.write(letter_template.format(**this_letter))

    print(f"{len(donor_db)} 'Thank You' letter files have been created!")


def quit_program():
    print("See you next time!")
    sys.exit()


def main():
    nav_dict = {1: send_thanks,
                2: create_report,
                3: send_thanks_all,
                4: quit_program}
    while True:
        response = int(input(prompt))
        if not response in nav_dict:
            print("Sorry, that isn't a valid selection.")
            main()
        nav_dict.get(response)()


if __name__ == "__main__":
    main()