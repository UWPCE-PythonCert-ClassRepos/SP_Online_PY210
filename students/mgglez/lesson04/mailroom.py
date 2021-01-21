#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Lesson04 - Assignment 2 - Mailroom Part 2
# Description: Assignment from Lesson04 - Mailroom Part 2 (Graded)
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-15-2021, Created Mailroom Part 2 Script
# ------------------------------------------------------------------------------ #
import os


def print_main_menu():
    """
    Display a menu of actions
    :return: nothing
    """
    print("""
    Choose an action:
     
    1 - Send a Thank You to a single donor
    2 - Create a Report.
    3 - Send letters to all donors.
    4 - Quit

    """)

def print_thank_you_menu():
    print("""
    You will be presented with a set of questions to identify which donor should receive 
    the 'Thank you!' email.
    
    1 - Specify which donor should receive a thank you email 
    2 - List existing donors' data 
    3 - Quit (Back to Main Menu)

    """)


def input_menu_choice():
    """
    Gets the menu choice from the user
    :return: string
    """
    choice = str(input("Which action would you like to perform? ")).strip()
    return choice


def generate_email(donor_full_name, total_donation):
    email_to_donor = (
        "Dear {},\nWe would like to thank you for your donation. So far, you "
        "have donated ${:.2f} to our organization and for that, we are grateful."
        "You are helping us continue our work supporting and growing our "
        "community.\nYou truly make a difference! We could not do this work "
        "without your support.\n\n"
    ).format(donor_full_name.title(), total_donation)
    return email_to_donor


def send_thank_you_to_single_donor(donor_records):
    while True:
        print_thank_you_menu()
        choice = input_menu_choice()

        if choice == '1':
            donor_full_name = input("What is the full name of the donor?: ").strip().lower()
            try:
                donation_amount = input(
                    "How much did {} donate to the cause? $ ".format(donor_full_name.title())
                )
                donation_amount = float(donation_amount)
            except ValueError:
                print("\nThe donation amount introduced is not a valid number (i.e: 300.00). Please try again!")
                continue
            if donation_amount > 0:
                for donor in donor_records:
                    if donor_full_name == donor['full_name']:
                        donor['donation_history'].append(donation_amount)
                        total_donation = sum(donor['donation_history'])
                        break
                else:
                    donor_records.append(
                        {
                            'full_name': donor_full_name,
                            'donation_history': [donation_amount]
                        }
                    )
                    total_donation = donation_amount
                print("{}'s donation for $ {:.2f} will be saved in our records".format(
                    donor_full_name.title(),
                    donation_amount)
                )
                email = generate_email(donor_full_name, total_donation)
                print(email)
            else:
                print("A donation needs to be higher than zero dollars in order to be added to the donor's records")
        elif choice == '2':
            list_donor_records(donor_records)
        elif choice == '3':
            break
        else:
            print("Your selection is invalid. Please select a menu option from 1 to 3")


def list_donor_records(donor_records):
    if len(donor_records):
        print("******* The current donors are: *******")
        headers = ('Donor Full Name', 'Total Given', 'Num Gifts', 'Average Gift')
        header_str = "{:<20s} | {:>16s} | {:^15s} | {:>16s}".format(*headers)
        print(header_str)
        print("-"*len(header_str))
        for donor in donor_records:
            print("{:<20s}   ${:>15.2f}   {:>15d}   ${:>15.2f}".format(
                    donor['full_name'].title(),
                    sum(donor['donation_history']),
                    len(donor['donation_history']),
                    sum(donor['donation_history'])/len(donor['donation_history'])
                )
            )
    else:
        print("There are no donors in our current database records. Please add them")


def create_donor_report(donor_records):
    donor_records = sorted(donor_records, key=lambda donor: sum(donor['donation_history']), reverse=True)
    list_donor_records(donor_records)


def read_data_from_file(filename, donor_records):
    donor_records.clear()
    if os.path.exists(filename):
        with open(filename, 'r') as fh:
            for line in fh:
                full_name, donation_history = line.strip().split(';')
                donor = {
                    'full_name': full_name.strip().lower(),
                    'donation_history': [float(amount) for amount in donation_history.strip().split(',')]
                }
                donor_records.append(donor)
    return donor_records


def write_data_to_file(filename, donor_records):
    with open(filename, "w+") as fh:
        donor_str = ''
        for donor in donor_records:
            donation_history = [str(amount) for amount in donor['donation_history']]
            donor_str = "{};{}\n".format(donor['full_name'], ','.join(donation_history))
            fh.write(donor_str)


def say_goodbye(filename, donor_records):
    if len(donor_records):
        write_data_to_file(filename, donor_records)
    print('Goodbye!')


def send_letter_to_all_donors(donor_records):
    if len(donor_records):
        for donor in donor_records:
            email = generate_email(donor['full_name'], sum(donor['donation_history']))
            donor_filename = "{}.txt".format(donor['full_name'].replace(' ', '_'))
            with open(donor_filename, "w+") as fh:
                fh.write(email)
        print("A letter has been set to every donor in our records!")
    else:
        print("There are no donors in our current database records. Please add them")


def main():

    # Loading donors data if it exists
    filename = 'donors.txt'
    donor_records = []
    donor_records = read_data_from_file(filename, donor_records)

    # Display the menu
    while True:
        print_main_menu()
        choice = input_menu_choice()

        if choice == '1':
            send_thank_you_to_single_donor(donor_records)
        elif choice == '2':
            create_donor_report(donor_records)
        elif choice == '3':
            send_letter_to_all_donors(donor_records)
        elif choice == '4':
            say_goodbye(filename, donor_records)
            break
        else:
            print("Your selection is invalid. Please select a menu option from 1 to 4")


if __name__ == "__main__":
    main()