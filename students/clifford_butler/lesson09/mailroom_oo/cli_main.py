#!/usr/bin/env python3

"""
User interaction functions and main program flow
"""

from donor_models import DonorCollection
import sys

def main_menu():
    # display the main menu
    print("\n".join(("Welcome to the MailRoom!",
        "Please choose from below options:",
        "1 - Send a Thank You",
        "2 - Create a Report",
        "3 - Send letters to all donors",
        "4 - Quit",
        ">>> ")))
    return input()

def send_thank_you(donors):
    # send thank you email based on user input information
    try: 
        name = input("Type the donors full name or type list to display donor names.")
        if name == 'list':
            for key in donors.name:
                print(key)
            print('')
        elif name == "":
            raise TypeError
        else:
            donors.add_donor(name)
    except TypeError:
        print("not valid name")
    return name
    print(donors)

def create_report():
    # generate and display a report of the donors in donor_dict
    pass

def letter_to_all():
    # send thank you letter to all donors 
    pass

def exit_program():
    # exit the interactive script
    print("Bye!")
    sys.exit() 

def main():
    # prompt user to select option
    donors = DonorCollection()
    
    #dict with the user options and the functions
    switch_dict = {
        '1': send_thank_you,
        '2': create_report,
        '3': letter_to_all,
        '4': exit_program
    } 

    while True:
        try:
            response = main_menu()
            switch_dict[response](donors)
        except KeyError:
            print("\n'{}'  is not a valid option, please enter 1, 2, 3, or 4!. \n >> ".format(response))

if __name__ == "__main__":
    # runs the main function
    main()