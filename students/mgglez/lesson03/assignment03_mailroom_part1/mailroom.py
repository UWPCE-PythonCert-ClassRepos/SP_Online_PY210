#!/usr/bin/env python

# ------------------------------------------------------------------------------ #
# Title: Assignment03 - Mailroom Part 1
# Description: Assignment from Lesson03 - Mailroom Part 1 (Graded)
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,01-10-2021, Created Mailroom Part 1 Script
# ------------------------------------------------------------------------------ #

def display_menu():
    """
    Display a menu of actions
    :return: nothing
    """
    print("""
    Menu of Actions:
    1) Send a Thank You
    2) Create a Report
    3) Quit
    \n""")

def input_menu_choice():
    """
    Gets the menu choice from the user
    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
    return choice

def generate_donor_report(donor_records):
    print("******* The current donors are: *******")
    headers = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    header_str = "{:<20s}|{:>16s}|{:^15s}|{:>16s}".format(*headers)
    print(header_str)
    print("-"*len(header_str))
    for donor_name, donor_donations in donor_records.items():
        print("{:<20s} ${:>15.2f} {:>15d} ${:>15.2f}".format(
                donor_name.title(),
                sum(donor_donations),
                len(donor_donations),
                (sum(donor_donations) / len(donor_donations))
            )
        )
    print("*******************************************\n")

def send_thanks_email(donor_name, donation_amount, nums_donation):
    email_to_donor = (
        "Dear {},\nWe would like to thank you for your donation of ${:.2f}.\n"
        "You have donated {} times to our organization and with that "
        "you are helping us continue our work supporting and growing our "
        "community.\nYou truly make a difference! We could not do this work "
        "without your support.\n\n"
    ).format(donor_name.title(), donation_amount, nums_donation)
    print(email_to_donor)

def send_thank_you(donor_records):
    while True:
        print("\nYou will be presented with a set of questions to identify which "
              "donor should receive the 'Thank you!' email.\nPlease provide the "
              "donor's full name. Type 'list' to get all existing donor's data "
              "or type 'exit' to go back to the main menu.\n"
              )
        donor_name = str(input("To which donor would you like to send a 'Thank you' email?: "))
        donor_name = donor_name.strip().lower()
        if donor_name == 'exit':
            break
        elif donor_name == 'list':
            generate_donor_report(donor_records)
        else:
            while True:
                try:
                    donation_amount = input("How much did {} donate to the cause? "
                    "Type the amount or 'exit' to go back to the main menu: $ ".format(donor_name.title())).strip()
                    if donation_amount != 'exit':
                        donation_amount = float(donation_amount)
                except ValueError:
                    print("\nThe donation amount introduced is not a valid number (i.e: 300.00). Please try again! "
                          "Or type 'exit' to go back to the main menu.\n"
                          )
                    continue
                if donation_amount == 'exit':
                    break
                elif donation_amount > 0:
                    donor_records.setdefault(donor_name, [])
                    donor_records[donor_name].append(donation_amount)
                    print("{}'s donation for $ {:.2f} will be saved in our records".format(donor_name.title(), donation_amount))
                    send_thanks_email(donor_name, donation_amount, len(donor_records[donor_name]))
                else:
                    print("A donation needs to be higher than zero dollars in order to be added to our records")
                break
            break


def main():
    donor_records = {
        'john silver': [300.0, 1200.0, 500.0],
        'mark stuart': [600.0, 100.0],
        'julie black': [1000.0, 3000.0, 4000.0],
        'bob howard': [30000.0, 20000.0, 50000.0],
        'patrice clark': [100.0]
    }
    while True:
        display_menu()
        choice = input_menu_choice()
        if choice == '1':
            send_thank_you(donor_records)
        elif choice == '2':
            donor_records = {k: v for k, v in sorted(donor_records.items(), key=lambda item: sum(item[1]), reverse=True)}
            generate_donor_report(donor_records)
        elif choice == '3':
            print('Goodbye!')
            break

if __name__ == "__main__":
    main()