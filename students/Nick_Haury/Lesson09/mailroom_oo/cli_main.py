#!/usr/bin/env python3
import donor_models as dm
import sys


'''
Implementation of the mailroom program from the first week, but this time using
an object oriented approach.  This program acts as the client user interface,
which takes input from a user and prints output based on commands.
'''

# create initial DonorCollection class to use throughout program
donors = dm.DonorCollection({
    'william gates, iii':dm.Donor("William Gates, III", [653772.32, 12.17]),
    "mark zuckerberg":dm.Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
    "jeff bezos":dm.Donor("Jeff Bezos", [877.33]),
    "paul allen":dm.Donor("Paul Allen", [663.23, 43.87, 1.32])
})

def quit():
    print("Closing mailroom... Goodbye")
    sys.exit()  # exit the script

def main():
    '''
    Allows user to choose function from predefined list

    Prompt the user for input.  Current choices are to send a thank you or to
    create a report to display all the current donors and respective donation
    totals and averages.  The user can also quit.
    '''

    # functions for users to choose from
    choice_dict = {
                    "1": thank_you,
                    "2": create_report,
                    "3": quit
    }

    print("Welcome to the mailroom program")
    prompt = "\n".join((
        "Please choose a function from the below options:",
        "1 - Send a Thank You to a single donor.",
        "2 - Create a Report.",
        "3 - Quit",
        ">> "
        ))

    while True:
        choice = input(prompt)
        try:
            choice_dict[choice]()
        except KeyError:
            print("\n" + str(choice) + " is an invalid selection, "
                  "please make a valid selection \n")


def thank_you():
    '''
    Function for adding a donor to DonorCollection or adding additional
    donations to a previous donor.  After, creates a message thanking them for
    their generous donation.

    Prompts the user for a full name.  If the user types "list", then print
    a list of donor names and re-prompt.  If a name is typed that is not
    in the list, user is asked if they'd like to add the Donor.  Otherwise if
    already in the list, then use it.  Once a name is selected, a
    donation amount is specified.  Donation amount input by users is then
    added to the donation history of the name.  Email is then automatically
    drafted using string formatting thanking the donor for the donation.
    Return to main prompt after.
    '''

    print()
    while True:
        ty_input = input('Type "list" to display a list of donor names. '
                         'Otherwise enter a name you would like to add a '
                         'donation for:\n>>')

        if ty_input.lower() == "list":
            print("\nCurrent Donors: ")
            for name in donors.display_names:
                print(name)
            print()
        else:
            if ty_input.lower() not in donors.names:
                while True:
                    yn_input = input(
                        f'\n{ty_input} was not found.  Would you like to add'
                        ' them to the donor list?\n>>').lower()
                    if yn_input == 'n' or yn_input == 'no':
                        print()
                        break
                    elif yn_input == 'y' or yn_input == 'yes':
                        donation_prompt(ty_input)
                        break
                    else:
                        print("\nPlease answer (y)es or (n)o")
                break  # break out of upper while loop
            else:
                donation_prompt(ty_input)
                break


def donation_prompt(name_input):
    while True:
        try:
            donation_amount = float(input("\nPlease enter donation amount:"
                                        "\n>>"))
            if donation_amount <= 0:
                raise ValueError("Donation amount must be positive")
        except ValueError:
            print("\nPlease only enter a single positive number for "
                "donation amount")
        else:
            donors.add_donation(name_input, donation_amount)
            print(
                "\n", 
                donors.donors[name_input.lower()].email_text(-1), 
                sep=""
                )
            break

def create_report():
    '''
    Prints a list of donors, sorted by total historical donation
    amount and alphabetically by first name.  Includes donor name,
    total donated, number of donations, and average donation amount.
    '''
    print("".join(donors.report()))

if __name__ == "__main__":
    
    main()
