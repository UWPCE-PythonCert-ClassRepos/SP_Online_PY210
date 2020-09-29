#!/usr/bin/env python3
# Lesson 05: incorporating exceptions

import sys
from operator import itemgetter

donor_db = {'Bob': [5.00, 10.00, 20.00, 15000.00],
            'Kathy': [20, 00],
            'Sherry': [50.00, 100.00],
            'Sophia': [1000.00],
            'Chet': [10000.00, 10000.00]}

main_prompt = "\n".join(("\nDonation Database Menu\n",
                         "Please choose from below options:",
                         "1 - Send a Thank You to an single Donor",
                         "2 - Create a Report",
                         "3 - Send a letter to all Donors",
                         "4 - Quit",
                         ">>> "))


def thank_you():
    amount = ()
    name = input("\n".join(("\nPlease type a Full Name:",
                            ">>> ")))
    if name == "list":
        message_1 = print_list()
        print(message_1)
        thank_you()
    elif name in donor_db:
        thank_you_2(name)
    else:
        thank_you_3(name)


def print_list():
    return donor_db.keys()


def thank_you_2(name):
    amount = input("\n".join(("\nPlease type a donation amount:",
                              ">>> ")))
    message_2 = donation_amount(name, amount)
    print(message_2)


def donation_amount(name, amount):
    try:
        donor_db.get(name).append(float(amount))
        return "\n Thank you {} For your generous donation of {} dollars! We appreciate your generous support".format(name, amount)
    except ValueError:
        print("Please type in a valid number!")
        amount = ()
        thank_you_2(name)


def thank_you_3():
    amount = input("\n".join(("\nPlease type a donation amount: ",
                              ">>> ")))
    message_3 = add_donor(name, amount)
    print(message_3)


def add_donor(name, amount):
    try:
        donor_db[name] = [float(amount)]
        return "\n Thank you {} For your generous donation of {} dollars! We appreciate your generous support".format(name, amount)
    except ValueError:
        print("Please type in a valid number!")
        amount = ()
        thank_you()


def create_report():
    donor_db_sum = []
    for donor in donor_db.copy():
        sum_donation = 0
        num_gifts = 0
        avg_gift = 0
        for donation in donor_db.get(donor):
            sum_donation += donation
            num_gifts += 1
        avg_gift = sum_donation / num_gifts
        donor_db_sum_object = (donor, sum_donation, num_gifts, avg_gift)
        donor_db_sum.append(donor_db_sum_object)

    donor_db_sum = sorted(donor_db_sum, key=itemgetter(1), reverse=True)
    report = "Donor Name" + " " * 16 + \
        "|  Total Given  |  Num Gifts  |  Average Gift\n" + "-" * 71
    for donor in donor_db_sum[:]:
        report += create_report_2(donor)
    print(report)


def create_report_2(*donor):
    return "\n {:25s} $ {:13.2f} {:13}  $ {:12.2f}".format(*donor)


def sort_key(donors):
    return donors


def exit_program():
    print("Quitting...")
    sys.exit()


def letters():
    for donor in donor_db.copy():
        file_create(donor)


def file_create(donor):
    with open(donor + ".txt", "w") as f:
        letter_text = letter_write(donor, f)
        f.write(letter_text)

def letter_write(donor, f):
    return "\n".join(("Dear {},".format(donor),
                         "Thank you for your very kind donation of ${:.2f}".format(sum(donor_db.get(donor))),
                         "\nIt will be put to very good use",
                         "Sincerely, \n\t The Team",
                         ))

main_dispatch = {
    1: thank_you,
    2: create_report,
    3: letters,
    4: exit_program
}


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        try:
            dispatch_dict.get(int(response))()
        except (ValueError, TypeError):
            print("Please type a number 1-4!")


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
