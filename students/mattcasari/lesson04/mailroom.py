#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Lesson 4, Exercise 3

@author: Matt Casari

Link: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part2.html

Description:
    The Program: Part 2
    Update the program from Lesson 3 (Part 1) by using dicts where appropriate.

    Also, add file writing.

"""

DONORS = {}

PROMPT_TEXT = (
    "\nSelect an option:\n"
    "1. Send a Thank You to a single donor.\n"
    "2. Create a Report.\n"
    "3. Send letters to all donors.\n"
    "4. Quit\n"
    "> "
)


def prompt_user():

    switch_func_dict = {
        1: thank_you_email,
        2: generate_report,
        3: create_file,
        4: quit_program,
    }

    """ Prompts the user for menu option """

    result = input(PROMPT_TEXT)
    result = int(result)
    switch_func_dict.get(result)()


def initialize_donors():
    DONORS["Neil Armstrong"] = [15000.00, 15000.00]
    DONORS["Buzz Aldrin"] = [23021.10, 25020.30, 28999.29]
    DONORS["Sally Ride"] = [42917.42, 38281.28]
    DONORS["Al Shepard"] = [2387.00, 2321.42, 3700.00]
    DONORS["Alan Bean"] = [28477.13, 727.1]
    DONORS["Chris Hadfield"] = [17325.42, 13823.83, 0.99]


def calculate_stats(donor):
    """ Calculates the sum, average and number of donations for a donor """
    donor_sum = sum(donor[1])
    donor_num = len(donor[1])
    donor_average = donor_sum / donor_num

    return (donor_sum, donor_num, donor_average)


def sort_donors_by_total(donors):
    """ Function used to sort donors by total contributions """
    return donors[2]


def quit_program():
    """ 
    Exits out of program
    """
    print("Exiting Program")
    quit()


def create_file():
    pass


def generate_report():
    values = DONORS
    """ Generates a formatted report of donor names, total donation, # of donations and average donation """
    print("\n")
    column_donor_length = 0

    for idx, value in enumerate(values[:]):
        column_donor_length = max(len(value[0]), column_donor_length) + 5
        [values[idx][2], values[idx][3], values[idx][4]] = calculate_stats(value)

    f_str = " {" + f":<{column_donor_length}" + "} | {} | {} | {}"
    title_str = f_str.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(title_str)
    print("-" * len(title_str))

    values = sorted(values, key=sort_donors_by_total, reverse=True)

    for value in values:
        f_str = " {" + f":<{column_donor_length}" + "}  ${:11.2f}   {:9}  ${:12.2f}"
        v_str = f_str.format(value[0], value[2], value[3], value[4])
        print(v_str)


def print_donor_list(values):
    """ Prints the list of donors passed to function"""
    print("\nList of donors:".upper())
    for value in values:
        print(value[0])


def thank_you_email(name, amount):
    """ Format the email and print to terminal """
    txt = (
        f"""\nDear {name},\n"""
        f"""Thank you for your recent donation of ${amount:.2f}. """
        f"""Your donation will help us purchase a taxidermied seagull.\n"""
        f"""Please consider donating again at your earliest convenience.\n\n"""
        f"""Sincerely,\n"""
        f"""The Human Fund\n"""
    )

    print(txt)


def add_donor():

    # trigrams = {}
    # num_words = len(words) - 1
    # for i in range(len(words) - 2):
    #     pair = tuple(words[i : i + 2])
    #     follower = words[i + 2]
    #     trigrams.setdefault(pair, [])
    #     trigrams[pair].append(follower)
    """ Adds new donor or new donation to existing donor """
    valid_donor = False
    while not valid_donor:
        donor = input("Enter Full Name ([First Name] [Last Name])(or list): ")

        for idx, value in enumerate(DONORS):
            if value[0] == donor:
                valid_donor = True
                break
        else:
            if donor == "list":
                print_donor_list(DONORS)
                continue
            else:
                DONORS.append([donor, []])

                idx += 1
                valid_donor = True
                break

    amount = input("Enter donation amount ($): ")
    amount = float(amount)
    # break

    # Add amount to data
    values[idx][1].append(amount)
    values[idx].append([])
    values[idx].append([])
    values[idx].append([])

    thank_you_email(values[idx][0], amount)

    return values


def main():
    initialize_donors()
    """ Main Run Loop """
    while True:
        option = prompt_user()

        # if option == 1:
        #     add_donor(data)
        # elif option == 2:
        #     generate_report(data)
        # elif option == 3:
        #     print("\nExiting Program")
        #     break
        # else:
        #     print("\nPlease select a valid option")


if __name__ == "__main__":
    main()
