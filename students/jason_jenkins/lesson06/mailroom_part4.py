#!/usr/bin/env python3

"""
Lesson 6: Mail Room Part 4
Course: UW PY210
Author: Jason Jenkins
"""
import pathlib
import sys


def send_thanks():
    """
    Method used to probt donor name or list out donors
    """

    global donor_dict

    response = ""

    while True:
        response = input('Input donors name, "list", or "exit": ').lower()

        if(response == "exit"):
            break
        elif response == "list":
            print_donor_dict()
            print()
        else:
            break

    # For dict
    if(response != "exit"):
        donate(response)


def thank_you_email(donor):
    """
    Thank donor for donation
    """

    text = f"Thank you {donor} for your donation."
    print(text)

    return text


def print_donor_dict():
    """
    Print out the donor list
    """

    global donor_dict

    text = "List of donors\n"
    text += "--------------\n"

    for k in donor_dict.keys():
        text += f"{k}\n"

    print(text)
    return text


def update_donor_list(donor, amount):
    if amount > 0:
        if donor in donor_dict:
            donor_dict[donor].append(amount)
        else:
            donor_dict.update({donor: [amount]})
        thank_you_email(donor)


def donate(donor):
    """
    Prompt donor to donate
    """

    response = 0

    try:
        response = float(input('Input amount to donate or "0" to exit: '))
    except ValueError:
        print("Must input a valid float")
    else:
        update_donor_list(donor, response)


def get_report():
    """
    Create a table like view of donors
    Includes donor name, donation total, total gifts, average gift amount

    Sorted by donation total
    """

    global donor_dict

    # Create new dict sorted by total donated
    sorted_dict = dict(sorted(donor_dict.items(),
                              key=lambda i: sum(i[1]),
                              reverse=True))

    sorted_tuple = []

    for k, v in sorted_dict.items():
        donor_name = k
        donor_total = round(sum(v), 2)
        donar_count = len(v)
        donor_ave = 0

        if donar_count != 0:
            donor_ave = round(donor_total / donar_count, 2)

        sorted_tuple.append([donor_name, donor_total, donar_count, donor_ave])

    return sorted_tuple


def display_report():
    print(f"{'Donor Name':30}|{'Total Given':^16}|", end='')
    print(f"{'Num Gifts':^14}|{'Average Gift':^16}")
    print(f"{'-'*79}")

    for row in get_report():
        print(f"{row[0]:30} ${row[1]:15.2f}{row[2]:15} ${row[3]:15.2f}")


def quit_program():
    """
    Method used to quit the program
    """

    sys.exit()


def get_letter_text(name):
    """Get letter text for file content"""

    global donor_dict

    k = name
    v = donor_dict.get(name)

    text = f"Dear {k}\n"
    text += f"\tThank you for your donation of ${sum(v):.2f}.\n"
    text += f"\tIt will be put to very good use.\n"
    text += f"Sincerely,\n"
    text += f"-The Team\n"

    return text


def send_all_thanks():
    """
    Method used to print a letter to the donors
    """

    global donor_dict

    p = pathlib.Path("emails/")

    try:
        p.mkdir(parents=True, exist_ok=True)
        for k in donor_dict.keys():
            dest = f"{p / k}.txt"
            dest = dest.replace(" ", "_").replace(",", "")
            with open(dest, 'w') as outfile:
                outfile.write(get_letter_text(k))
    except NameError:
        print("Director not found")


def startup_prompt():
    """
    Prombt user for action they what to take
    """
    global menu_dict

    print()
    print("Do you want to:")
    print('   1 - Send a Thank You to a single donor.')
    print('   2 - Create a Report.')
    print('   3 - Send letters to all donors.')
    print('   4 - Quit.')

    response = input("Input numbered option you wish to do: ").strip()

    try:
        menu_dict[response]()
    except KeyError:
        print(f"{response} is not a valid input.")


# Global Variables
donor_dict = dict()
menu_dict = {
    "1": send_thanks,
    "2": display_report,
    "3": send_all_thanks,
    "4": quit_program
}


if __name__ == "__main__":
    # Initial Setup
    donor_dict.update({"william gates": [1345.462]})
    donor_dict.update({"mark zuckerberg": [12546.124, 13445.124]})
    donor_dict.update({"jeff bezos": [1234.123, 12341431.12]})
    donor_dict.update({"paul allen": [734.12, 124.41, 10000]})
    donor_dict.update({"jason jenkins": [10, 20, 30, 40, 50, 60]})

    while True:
        startup_prompt()
