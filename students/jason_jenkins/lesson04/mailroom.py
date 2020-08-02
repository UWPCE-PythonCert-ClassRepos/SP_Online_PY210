#!/usr/bin/env python3

"""
Lesson 3: Mail Room Part 1
Course: UW PY210
Author: Jason Jenkins
"""
import pathlib


# Global Variables
run_program = True
donor_dict = dict()


def send_thanks():
    """
    Method used to probt donor name or list out donors
    """

    global donor_dict

    response = ""

    while(True):
        response = input('Input donors full name, "list", or "exit": ')

        if(response.lower() == "exit"):
            break
        elif response.lower() == "list":
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

    print(f"Thank you {donor} for your donation.")


def print_donor_dict():
    """
    Print out the donor list
    """

    global donor_dict

    print("List of donors")
    print("--------------")

    for k in donor_dict.keys():
        print(k)


def donate(donor):
    """
    Prompt donor to donate
    """

    response = float(input('Input amount to donate or "0" to exit: '))

    if(response != 0):
        if donor in donor_dict:
            donor_dict[donor].append(response)
        else:
            donor_dict.update({donor: [response]})
    thank_you_email(donor)


def create_report():
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

    print(f"{'Donor Name':30}|{'Total Given':^16}|", end='')
    print(f"{'Num Gifts':^14}|{'Average Gift':^16}")
    print(f"{'-'*79}")

    for k, v in sorted_dict.items():
        donor_name = k
        donor_total = sum(v)
        donar_count = len(v)
        donor_ave = 0

        if donar_count != 0:
            donor_ave = donor_total / donar_count

        donor_output = f"{donor_name:30}"
        donor_output += f" ${donor_total:15.2f}"
        donor_output += f"{donar_count:15}"
        donor_output += f" ${donor_ave:15.2f}"
        print(donor_output)


def quit_program():
    """
    Method used to quit the program
    """

    global run_program
    run_program = False


def send_all_thanks():
    """
    Method used to print a letter to the donors
    """

    global donor_dict

    p = pathlib.Path("emails/")
    p.mkdir(parents=True, exist_ok=True)

    for k, v in donor_dict.items():
        dest = f"{p / k}.txt"
        dest = dest.replace(" ", "_").replace(",", "")
        with open(dest, 'w') as outfile:
            outfile.write(f"Dear {k}\n")
            outfile.write(f"\tThank you for your donation of ${sum(v):.2f}.\n")
            outfile.write(f"\tIt will be put to very good use.\n")
            outfile.write(f"Sincerely,\n")
            outfile.write(f"-The Team\n")


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

    response = input("Input numbered option you wish to do: ")

    if response in menu_dict:
        menu_dict[response]()
    else:
        print(f"{response} is not a valid input.")


# Dict used as similar to a switch statement
menu_dict = {
    "1": send_thanks,
    "2": create_report,
    "3": send_all_thanks,
    "4": quit_program
}


if __name__ == "__main__":
    # Initial Setup
    donor_dict.update({"William Gates, III": [1345.462]})
    donor_dict.update({"Mark Zuckerberg": [12546.124, 13445.124]})
    donor_dict.update({"Jeff Bezos": [1234.123, 12341431.12]})
    donor_dict.update({"Paul Allen": [734.12, 124.41, 10000]})
    donor_dict.update({"Jason Jenkins": [10, 20, 30, 40, 50, 60]})

    while(run_program):
        startup_prompt()
