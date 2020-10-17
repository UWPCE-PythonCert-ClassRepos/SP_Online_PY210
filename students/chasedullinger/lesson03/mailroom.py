#!/usr/bin/env python3
# PY210 Lesson 03 MailRoom 1 - Chase Dullinger

import sys

donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]


def send_thank_you():
    """Selection to enter a donation and/or add a donor and then generate a
    thank you letter.
        :param: None
        :return: None
    """
    while True:
        response = input("Enter name of donor or type 'list' for list of current donors.\
 'back' returns to main menu'> ")
        if response == 'back':
            return
        if response == 'list':
            show_donor_list()
        elif response not in [donor[0] for donor in donor_db]:
            add_donor(response)
            add_donation(response)
            break
        else:
            add_donation(response)
            break


def show_donor_list():
    """Display donor list by looping through existing donors in donor_db
        :param: None
        :return: None
    """
    print("\n")
    print("Current donors are:")
    for donor in donor_db:
        print(donor[0])
    print("\n")


def add_donor(donor):
    """ Adds a donor to the donor database
        :param donor: string containing donor's name
        :return: None
    """
    donor_db.append((donor, []))


def add_donation(donor):
    """ Adds a donation to a donor in to the donor database, then creates the
    thank you note.
            :param donor: string containing donor's name
            :return: None
    """
    response = input(f"Enter donation amount for {donor} .\
 'back' returns to main menu> ")
    if response == 'back':
        return
    for d in donor_db:
        if d[0] == donor:
            d[1].append(float(response))

    compose_email(donor, response)


def compose_email(donor, amount):
    """ Writes the email note and prints it to the screen.
    :param donor: string containing the donors name_list
    :param amount: string containing the donation amount
    :return: None """

    print(f"\nDear {donor},\n\
Thank you for your generous gift of ${amount}! It will help Local Charity\
 achieve our mission.\n\
Best regards,\n\
Local Charity\n\n")


def get_donor_stats(donor):
    """Return donor donation stats.
    :param donor: donor item from donor_db (donor_name, [donation list])
    :return total_given: float summation of total gifts given
    :return total_gifts: int number of gifts given
    :return average_gift: float average value of gifts
    """
    total_given = sum(donor[1])
    total_gifts = len(donor[1])
    average_gift = total_given / total_gifts
    return total_given, total_gifts, average_gift


def create_report():
    """Display donor list by looping through existing donors in donor_db and
    and show their donation data.
        :param: None
        :return: None
    """
    print("\n")
    print("Donor Name                | Total Given | Num Gifts | Average Gift\n\
------------------------------------------------------------------")
    for donor in donor_db:
        total_given, total_gifts, average_gift = get_donor_stats(donor)
        print(f"{donor[0]:<26} $ {total_given:>11.2f} {total_gifts:>10}\
  $ {average_gift:>11.2f}")

    print("\n")
    return


def quit_program():
    """Cleanly exit the program"""
    sys.exit()


def get_prompt():
    """Display menu and return selection.
        :param: None
        :return: Input string
    """
    return input("Select an action:\n\
    1) Send a thank you\n\
    2) Create a report\n\
    3) Quit the program\n\
    \n\
Enter number you wish to choose > ")


def main():
    """ Main menu
        :param: None
        :return: None
    """
    while True:
        response = get_prompt()
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_program()
        else:
            print("\nInvalid Entry\n")


if __name__ == "__main__":
    main()
