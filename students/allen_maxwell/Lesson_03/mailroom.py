#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 11/9/2019
# mailroom.py

from operator import itemgetter

# create an initial donor list
donors = list()
donors.append(('William Gates, III', 653784.49, 2, 326892.24))
donors.append(('Mark Zuckerberg', 16396.10, 3, 5465.37))
donors.append(('Jeff Bezos', 877.33, 1, 877.33))
donors.append(('Paul Allen', 708.42, 3, 236.14))
donors.append(('Steve Jobs', 10000.00, 1, 10000.00))

# prompts the user to select send a thank you, create a report, or quit
def menu():

    # loops through the menu options until the user selects 3, to quit
    while True:
        response = input('\n'.join(('\n',
            'Please choose from the following options:',
            '1) Send a Thank You',
            '2) Create a Report',
            '3) Quit',
            'Please enter your selection > ')))  
        if response == '1':
            thank_you()
        elif response == '2':
            print_report()
        elif response == '3':
            break
        else:
            print('\nPlease enter a number (1, 2, or 3)')

# prompts the user to search for or add a donor to the list. 
def thank_you():  
    found = False
    while not found:

        # prompt for a full name of the donor, enter 'List' to display a list of donor names, 
        # or quit to exit
        response = input("\nPlease enter the full name of the donor, 'List' for a list of donors," 
            " or 'Quit' to exit to the menu > ")

        # exit to menu if 'quit' is entered
        if response.lower() == 'quit':
            menu()

        # if response is list show a list of donor names and reprompt
        if response.lower() == 'list':
            for donor in donors:
                print(donor[0])    
        else:
            for donor in donors:

                # if the response name is on the list prompt for donation amount
                if response.lower() == donor[0].lower() and not found:
                    donor_data = donor
                    donors.remove(donor)
                    add_donation(donor_data)
                    found = True
                    break

            # if the response name is not on list add it and prompt for donation amount
            if not found:
                add_donation((response, 0, 0, 0))
                found = True
           
# prompts the user for the donor's donation ammount and adds the updated data to the list. 
def add_donation(donor):

    # prompt for a donation amount
    donation = input("Please enter the amount of the donation or 'Quit' to exit to the menu > $ ")

    # exit to menu if 'quit' is entered
    if donation.lower() == 'quit':
        menu()

    # convert the donation amount to a float
    donation = float(donation)

    # calculate sum, number donations, and the average donation
    sum_donations = donor[1] + donation
    num_donations = donor[2] + 1
    avg_donation  = sum_donations / num_donations  

    # add amount to the donor's donation history
    donors.append((donor[0], sum_donations, num_donations, avg_donation)) 

    # Print the thank you email
    print_email(donor[0], donation)

# prints an email thanking the donor for their generous donation and returns to the menu. 
def print_email(name,donation):
    print(f'''\n
    Dear {name},
    
    Thank you so much for your generous gift of ${donation:,.2f}!

    Your donation will go far in helping hundreds of orphaned puppies find homes.
    
    Thank You,
    Paws''')

# prints a sorted list of your donors, sorted by total historical donation amount.
def print_report():

    # Creates Report Header
    print('\n{:<19}{:3}{:12}{:3}{:10}{:3}{:18}'
    .format('Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift'))
    print('-'*62)

    # sorts the list of donors by total historical donation amount (highest to lowest)
    sorted_donors = sorted(donors, key = itemgetter(1))
    sorted_donors.reverse()

    for donor in sorted_donors:
        print('{:<20} ${:>11,.2f}{:>13}   ${:>12,.2f}'.format(donor[0], donor[1], donor[2], donor[3]))

if __name__ == "__main__":

    # run menu
    menu()


