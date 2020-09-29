#!/usr/bin/env python3
# Lesson 09: incorporating Object Oriented Programming

import sys
from operator import itemgetter
from donor_models import Donor, DonorCollection

# donor_db = {'Bob': [5.00, 10.00, 20.00, 15000.00],
#             'Kathy': [20, 00],
#             'Sherry': [50.00, 100.00],
#             'Sophia': [1000.00],
#             'Chet': [10000.00, 10000.00]}

bob = Donor('Bob', [5.00, 10.00, 20.00, 15000.00])
kathy = Donor('Kathy', [20])
sherry = Donor('Sherry', [50.00, 100.00])
sophia = Donor('Sophia', [1000.00])
chet = Donor('Chet', [10000.00, 10000.00])

donors = DonorCollection([bob, kathy, sherry, sophia, chet])





def exit_program():
    print("Quitting...")
    sys.exit()

def create_report():
    print(donors.generate_report())


def thank_you():
    amount = ()
    name = input("\n".join(("\nPlease type a Full Name:",
                            ">>> ")))
    if name == "list":
        #message_1 = print_list()
        message_1 = donors.donor_names()
        print(message_1)
        thank_you()
    elif donors.is_in_list(name):
        thank_you_2(name)
    else:
        thank_you_3(name)


def thank_you_2(name):
    amount = input("\n".join(("\nPlease type a donation amount:",
                              ">>> ")))
    message_2 = donation_amount(name, amount)
    print(message_2)


def donation_amount(name, amount):
    try:
        donor = donors.get_donor(name)
        donor.donation_list.append(float(amount))
        return "\n Thank you {} For your generous donation of {} dollars! We appreciate your generous support".format(name, amount)
    except ValueError:
        print("Please type in a valid number!")
        amount = ()
        thank_you_2(name)


def thank_you_3(name):
    amount = input("\n".join(("\nPlease type a donation amount: ",
                              ">>> ")))
    message_3 = add_donor(name, amount)
    print(message_3)


def add_donor(name, amount):
    try:
        new_donor = Donor(name, [float(amount)])
        donors.add_donor(new_donor)
        return "\n Thank you {} For your generous donation of {} dollars! We appreciate your generous support".format(name, amount)
    except ValueError:
        print("Please type in a valid number!")
        amount = ()
        thank_you()


def letters():
    for donor in donors.list_donors:
        file_create(donor)


def file_create(donor):
    with open(donor.name + ".txt", "w") as f:
        #letter_text = letter_write(donor, f)
        letter_text = donor.letter_write()
        f.write(letter_text)


main_prompt = "\n".join(("\nDonation Database Menu\n",
                         "Please choose from below options:",
                         "1 - Send a Thank You to an single Donor",
                         "2 - Create a Report",
                         "3 - Send a letter to all Donors",
                         "4 - Quit",
                         ">>> "))

main_dispatch = {
    1: thank_you,
    2: create_report,
    3: letters,
    4: exit_program
}


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        dispatch_dict.get(int(response))()
        # try:
        #     dispatch_dict.get(int(response))()
        # except (ValueError, TypeError):
        #     print("Please type a number 1-4!")


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)