#!/usr/bin/env python3

"""
Lesson 3: Mail Room Part 1
Course: UW PY210
Author: Jason Jenkins
"""


# Global Variables
run_program = True
donor_list = []


def send_thanks():
    """
    Method used to probt donor name or list out donors
    """

    global donor_list
    response = ""

    while(True):
        response = input('Input donors full name, "list", or "exit": ')

        if(response.lower() == "exit"):
            break
        elif response.lower() == "list":
            print_donor_list()
            print()
        else:
            break

    if(response != "exit"):
        for donor in donor_list:
            if donor[0] == response:
                donate(donor)
                break
        else:
            new_donor = [response]
            donate(new_donor)
            donor_list.append(new_donor)


def thank_you_email(donor):
    """
    Thank donor for donation
    """

    print(f"Thank you {donor[0]} for your donation.")


def print_donor_list():
    """
    Print out the donor list
    """

    global donor_list

    print("List of donors")
    print("--------------")

    for donor in donor_list:
        print(donor[0])


def donate(donor):
    """
    Prompt donor to donate
    """

    response = float(input('Input amount to donate or "0" to exit: '))
    if(response != 0):
        donor.append(response)
        thank_you_email(donor)


def sort_by_total(tmp_donor_list):
    """
    Used to sort donor list by total donations
    """

    return sum(tmp_donor_list[1:])


def create_report():
    """
    Create a table like view of donors
    Includes donor name, donation total, total gifts, average gift amount

    Sorted by donation total
    """

    global donor_list

    donor_list.sort(key=sort_by_total, reverse=True)

    print(f"{'Donor Name':30}|{'Total Given':^16}|", end='')
    print(f"{'Num Gifts':^14}|{'Average Gift':^16}")
    print(f"{'-'*79}")

    for donor in donor_list:
        donor_name = donor[0]
        donor_total = sum(donor[1:])
        donar_count = len(donor) - 1
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


def startup_prompt():
    """
    Prombt user for action they what to take
    """

    print()
    print("Do you want to:")
    print('   "Send a thank you"')
    print('   "Create a Report"')
    print('   "quit"')

    response = input("Input option you wish to do: ")

    if(response.lower() == "send a thank you"):
        send_thanks()
    elif(response.lower() == "create a report"):
        create_report()
    elif(response.lower() == "quit"):
        quit_program()
    else:
        print(f"{response} is not a valid input.")


if __name__ == "__main__":
    # Initial Setup
    donor_list.append(["William Gates, III", 1345.462])
    donor_list.append(["Mark Zuckerberg ", 12546.124, 13445.124])
    donor_list.append(["Jeff Bezos", 1234.123, 12341431.12])
    donor_list.append(["Paul Allen", 734.12, 124.41, 10000])
    donor_list.append(["Jason Jenkins", 10, 20, 30, 40, 50, 60])

    while(run_program):
        startup_prompt()
