#!/usr/bin/env python3
import donor_models as dm
import sys


'''
Implementation of the mailroom program from the first week, but this time using
an object oriented approach.  
'''

# create initial DonorCollection class to use throughout program
donors = dm.DonorCollection({
    'William Gates':dm.Donor("William Gates, III", [653772.32, 12.17]),
    "Mark Zuckerberg":dm.Donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
    "Jeff Bezos":dm.Donor("Jeff Bezos", [877.33]),
    "Paul Allen":dm.Donor("Paul Allen", [663.23, 43.87, 1.32])
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
            print(str(choice) + " is an invalid selection, "
                  "please make a valid selection \n")


def thank_you():
    '''
    Function for adding a donor to DonorCollection or adding additional
    donations to a previous donor and creating a thank you message.

    prompts the user for a full name.  If the user types "list", then print
    a list of donor names and re-prompt.  If a name is typed that is not
    in the list, add the name to the list.  If a name is typed that is
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
            for name in [name.capitalize() for name in donors.names]:
                print(name)
            print()
        else:
            if ty_input.lower() not in donors.names:
                while True:
                    yn_input = input(
                        f'{ty_input} was not found.  Would you like to add'
                        ' them to the donor list?').lower()
                    if yn_input == 'n' or yn_input == 'no':
                        break
                    elif yn_input == 'y' or yn_input == 'yes':
                        donation_prompt(ty_input)
                        break
                    else:
                        print("Please answer (y)es or (n)o")
            else:
                donation_prompt(ty_input)
                break
                # try:
                #     donation_amount = float(input("\nPlease enter donation amount:"
                #                                 "\n>>"))
                #     if donation_amount <= 0:
                #         raise ValueError("Donation amount must be positive")
                # except ValueError:
                #     print("\nPlease only enter a single positive number for "
                #         "donation amount\n")
                # else:
                #     add_donation(ty_input, donation_amount)
                #     print(
                #         "\n", create_email_text(ty_input, donation_amount), sep=""
                #         )
                #     break

def donation_prompt(name_input):
    while True:
        try:
            donation_amount = float(input("\nPlease enter donation amount:"
                                        "\n>>"))
            if donation_amount <= 0:
                raise ValueError("Donation amount must be positive")
        except ValueError:
            print("\nPlease only enter a single positive number for "
                "donation amount\n")
        else:
            donors.add_donation(name_input, donation_amount)
            print(
                "\n", create_email_text(ty_input, donation_amount), sep=""
                )
            break

# def add_donation(donor_name, donation_amount):
#     '''
#     Adds donation amount to donor's list of donations.  If donor does not exist
#     yet, they are created and added to the donor dictionary.
#     '''
#     donors.setdefault(donor_name, []).append(donation_amount)

def create_report():
    '''
    Prints a list of donors, sorted by total historical donation
    amount.  Includes donor name, total donated, number of donations,
    and average donation amount.
    '''
    pass
    # print("\nDonor Name" + " "*15 + "|  Total Given  | Num Gifts |   "
    #       "Average Gift")
    # print("- "*36)
    # for row in get_report_text():
    #     print(row)
    # print()

if __name__ == "__main__":
    
    main()
