#!/usr/bin/env python

import sys
import string
from donor_models import Donor, DonorCollection

some_donors = [Donor("William Gates, III", [1.50, 653772.32, 12.17]),
            Donor("Jeff Bezos", [877.33]),
            Donor("Paul Allen", [663.23, 43.87, 1.32]),
            Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]  
donor_collec = DonorCollection()  
{donor_collec.add_donor(donor) for donor in some_donors}


def create_report(a_donor_collec):
    #prints report of donors sorted in descending order for summation of #donations of each owner
    a_donor_collec.sort()
    print("\n".join(('Donor Name                | Total Given | Num Gifts | Average Gift',
    '------------------------------------------------------------------')))
    for donor in a_donor_collec.donors:
        print(donor)


def input_donation():
    #takes new donation input
    while True:  
        try:
            new_donation = float(input("Input donation amount>"))
        except ValueError:
            print('Input must be a number, try again.')
        else:
            if new_donation >= 0.01:
                break
            else:
                print('Donations less than 1 cent are not accepted')
    return new_donation


def screen_message(name,donation):
    # prints thank you note to screen
    return f"Thank you {name} for your generous donation of ${donation}"


def send_thank_you(a_donor_collec):
    prompt = "\n".join(("Send a thank you note!",
          "Please type donor's full name or type 'list' to view list of donors",
          ">>> "))

    while True:
        response = input(prompt).title()  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "List":
            print(a_donor_collec)
       
        elif response in string.punctuation:
            print("\nDonor's name must include some letters or numbers.\n")

        else:
            new_donation = input_donation()
            a_donor_collec.add_to_list(response,new_donation)
            print(screen_message(response , new_donation))
            break


def write_to_file(a_file_name, a_message): #writes thanks you letter to a file #for each donor
    with open(a_file_name, 'w') as f:
            f.write(a_message)


def Send_letters_to_all(a_donor_collec):
    for donor in a_donor_collec.donors:
        #write letter to the file
        write_to_file(donor.letter_file_name(), donor.letter_content())
    print("\nThank-you letters were written into the files!\n")      


def exit_program(a_donor_dict):
    print("Bye!")
    sys.exit()  # exit the interactive script


def not_valid(a_donor_dict):
    print('\nNot a valid option!\n')


def main():
    prompt = "\n".join(("Please choose from below options:",
            "1 - Send a Thank You",
            "2 - Create a Report",
            "3 - Send letters to everyone",
            "4 - Quit",
            ">>> "))

    switch_func_dict = {
                       '1': send_thank_you,
                       '2': create_report,
                       '3': Send_letters_to_all,
                       '4': exit_program
                       }
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        switch_func_dict.get(response,not_valid)(donor_collec)


if __name__ == "__main__":
    main()