'''
Client code for the object-oriented mailroom assignment.
'''

from donor_models import Donor, DonorCollection

import sys


def send_thankyou():
    '''Send a thank-you letter to an individual donor. Add the donor if not present.'''
    while True:
        response = input("Please input a name, 'list' to see names, or 'c' to cancel:\n")
        if response == "c":
            return
        elif response == "list":
            print(dc.display_donors())
        else:
            if dc.get_donor(response) is None:
                dc.add_donor(response)
            currentdonor = dc.get_donor(response)
            while True:
                amount = input("Please enter a donation amount:\n")
                if amount == "c":
                    return
                else:
                    try:
                        currentdonor.add_donation(float(amount))
                    except ValueError:
                        print("Please enter the donation as a number")
                    else:
                        print(currentdonor.write_indiv_letter())
                        response = input("Would you like to create another letter? 1 - Yes, 2 - No\n")
                        if response == "1":
                            break
                        if response == "2" or response == "c":
                            return
                        else:
                            print("Please enter a number that corresponds to a menu option.")


def write_report():
    '''Print a formatted report of donors, total given, num gifts, and average gift..'''
    print(dc.generate_report())


def batch_letters():
    '''Generate a thank-you letter for each donor and save to current directory.'''
    dc.batch_letters()
    print("Letters generated in current directory")


def quit_program():
    print("Goodbye!")
    sys.exit()


def menu_selection(main_prompt, main_dispatch):
    while True:
        response = input(main_prompt)
        try:
            main_dispatch[response]()
        except KeyError:
            print("Please enter a number that corresponds to a menu option.")



main_prompt = ("Select an action: 1 - Send a Thank You, 2 - Create a Report, \
3 - Generate letters to all donors, or 4 - Quit\nReturn to main menu any time by entering 'c'\n")

main_dispatch = {"1": send_thankyou,
                 "2": write_report,
                 "3": batch_letters,
                 "4": quit_program
                }



if __name__ == "__main__":
    dc = DonorCollection()
    menu_selection(main_prompt, main_dispatch)