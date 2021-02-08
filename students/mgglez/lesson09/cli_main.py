#!/usr/bin/env python

# ----------------------------------------------------------------------------------- #
# Title: Lesson09 - Mailroom - Object Oriented
# Description: Assignment from Lesson09 - Mailroom - Object Oriented
# ChangeLog (Who,When,What):
# Mercedes Gonzalez Gonzalez,02-06-2021, Created User Interaction module cli_main.py
# ----------------------------------------------------------------------------------- #

from donor_models import Donor, DonorCollection


# User Presentation Layer - IO Class
class IO(object):

    @staticmethod
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

    @staticmethod
    def print_thank_you_menu():
        print("""
        You will be presented with a set of questions to identify which donor should receive 
        the 'Thank you!' email.
    
        1 - Specify which donor should receive a thank you email 
        2 - List existing donors' data 
        3 - Quit (Back to Main Menu)
    
        """)

    @staticmethod
    def input_choice(msg):
        """
        Gets the menu choice from the user
        :return: string
        """
        choice = str(input(msg)).strip()
        return choice

    @staticmethod
    def print_data_to_user(data):
        print(data)

    @classmethod
    def send_thank_you_to_single_donor(cls, donor_collection):
        while True:
            cls.print_thank_you_menu()
            choice = cls.input_choice("Which action would you like to perform? ")

            if choice == '1':
                donor_full_name = cls.input_choice("What is the full name of the donor?: ").lower()
                try:
                    donation_amount = cls.input_choice(
                        "How much did {} donate to the cause? $ ".format(donor_full_name.title())
                    )
                    donation_amount = float(donation_amount)
                except ValueError:
                    cls.print_data_to_user(
                        "\nThe donation amount introduced is not a valid number (i.e: 300.00). Please try again!")
                    continue
                if donation_amount > 0:
                    donor = donor_collection.get_donor_records(donor_full_name)
                    if donor is None:
                        donor = Donor(donor_full_name, [donation_amount])
                        donor_collection.add_donor(donor)
                    else:
                        donor.add_donation(donation_amount)

                    cls.print_data_to_user("{}'s donation for $ {:.2f} will be saved in our records".format(
                        donor.full_name,
                        donation_amount)
                    )
                    email = donor.generate_thank_you_email_to_single_donor()
                    cls.print_data_to_user(email)
                else:
                    cls.print_data_to_user("A donation needs to be higher than zero dollars "
                                           "in order to be added to the donor's records")
            elif choice == '2':
                cls.print_data_to_user(donor_collection.generate_donor_report())
            elif choice == '3':
                break
            else:
                cls.print_data_to_user("Your selection is invalid. Please select a menu option from 1 to 3")


def main():
    # Loading donors data if it exists
    filename = 'donors.txt'
    donor_collection = DonorCollection()
    msg = donor_collection.load_donor_data_from_file(filename)
    IO.print_data_to_user(msg)

    # Display the menu
    while True:
        IO.print_main_menu()
        choice = IO.input_choice("Which action would you like to perform? ")

        if choice == '1':
            IO.send_thank_you_to_single_donor(donor_collection)
        elif choice == '2':
            IO.print_data_to_user(donor_collection.generate_donor_report())
        elif choice == '3':
            IO.print_data_to_user(donor_collection.generate_letter_to_all_donors())
        elif choice == '4':
            if len(donor_collection.donor_list):
                donor_collection.save_donor_data_to_file(filename)
            IO.print_data_to_user("GoodBye!")
            break
        else:
            IO.print_data_to_user("Your selection is invalid. Please select a menu option from 1 to 4")


if __name__ == "__main__":
    main()
