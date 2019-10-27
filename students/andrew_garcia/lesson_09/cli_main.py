'''
Andrew Garcia
Main Mailroom
8/22/19
'''

from donor_models import *


donation_list = DonorCollection()  # main donation storage


# menu of options for user
def options_menu():
    """Menu of options the user is shown, allowing them to navigate through the script"""

    while True:
        try:
            option = int(input('''
        Options:
            1 - Send a Thank You 
            2 - View a Report
            3 - Quit

        Select an Option: '''))

            switcher = {1: thank_donor, 2: create_report}

            if option == 1:
                switcher.get(1)()
            elif option == 2:
                switcher.get(2)()
            elif option == 3:
                break
            else:
                print('That is not a valid choice.')
        except ValueError:
            print('Your choice must be in the form of a number.')


# create thank you for donor, adds them to donation list
def thank_donor():
    """Adds a single donor and donation, creates a thank you note"""

    while True:
        donor_name = input('Who would you like to thank?: ')
        donor_name = donor_name.title()

        if donor_name == 'List':  # checks if there are donors to list
            if not donation_list.list_donors():
                print('There are no current donors to list.')
            else:
                print(donation_list.list_donors())
        elif donor_name == 'Quit':
            break
        else:
            donor_amount = int(input('How much did {} donate? '.format(donor_name)))
            donor_amount = round(donor_amount, 2)

            thanking_donor = Donor(donor_name, donor_amount)  # formats thank you
            donation_list.add_donor(thanking_donor)  # adds to main donation storage

            print('\n' + thanking_donor.thank_you_donor())
            break


# prints donor report to user
def create_report():
    sorted_donors = donation_list.sort_donors()  # sorts donors based on total donation amount
    if not sorted_donors:  # checks if there are donors to report
        print('There are no current donors to list.')
    else:
        print('\nDonor Name          | Total Donations | # Donations | Average Donations | ')
        print('--------------------------------------------------------------------------')
        for item in sorted_donors:
            print(f'{item[0]:22}$     {item[1]:8.2f} {item[2]:8}        ${item[3]:18.2f}')


# starts script
if __name__ == '__main__':
    options_menu()












