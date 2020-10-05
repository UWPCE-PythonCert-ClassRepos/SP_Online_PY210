# !/usr/bin/env python3

import sys
from OOP_Mailroom_Donar_Model import Donar
from OOP_Mailroom_Donar_Model import DonarCollection


donars = DonarCollection.initialize_donars_dict(
    {'Mike': [200, 100, 340],
     'Tony': [300, 100],
     'Sarah': [150, 250, 100]})


# Main Menu
def options():
    print("\n".join(("Please select from the following options:",
                     "s - Send a Thank You letter to a single donar.",
                     "c - Create a Report.",
                     "sa - Send Letters to All Donors",
                     "q - Quit."
                     ">>> ")))
    option = input('')
    return option


def quit():
    print("System shutting down!")
    sys.exit()


# Send a Thank you note to Donar
def send_thank_you():
    mail_to = input(
        "Enter the name of a donar or 'list' for current donars \n")
    while mail_to.lower() == "list":
        print(donars.list_of_donars())
        mail_to = input("Please enter the name of a donar \n")
    try:
        donation_amt = float(input("Enter the donation amount \n"))
    except ValueError:
        print("\n Invalid Amount. Please enter a valid amount! \n")
    else:
        if donars.donor_exists(mail_to) is False:
            donar = Donar(mail_to)
            donars.add(donar)
        else:
            donar = donars.donars[mail_to]
        donar.add_donation(donation_amt)
        print(donar.print_thank_you_message())


def create():
    """Print a report showing donations."""
    donars.create()


def send_to_all():
    """Generate a letter for each donar in the collection."""
    donars.send_to_all()
    print('Sending Letters to all donars.\n')


def start():
    switch_dict = {"s": send_thank_you, "c": create,
                   "sa": send_to_all, "q": quit}
    while True:
        try:
            option = options().lower()
            switch_dict.get(option)()
        except TypeError:
            print("Not a valid option. Please try again!")


if __name__ == "__main__":
    start()
