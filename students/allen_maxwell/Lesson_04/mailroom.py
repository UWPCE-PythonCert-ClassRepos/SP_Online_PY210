#!/usr/bin/env python3

# Allen Maxwell
# Python 210
# 12/3/2019
# Part 2
# mailroom.py

import os

# Creates a single donor dictionary
donors = {
    'William Gates, III': [653784.49, 2, 326892.24],
    'Mark Zuckerberg': [16396.10, 3, 5465.37],
    'Jeff Bezos': [877.33, 1, 877.33],
    'Paul Allen': [708.42, 3, 236.14],
    'Steve Jobs': [10000.00, 1, 10000.00]}

def menu():
    '''
    Creates a user input menu selection.
     Input:  None
     Output: None '''

    # Loops through the menu options until the user selects 3, to quit
    while True:
        response = input('\n'.join(('\n',
            'Please choose from the following options:',
            '1) Create a Report',
            '2) Send a Thank You letter to a single donor',
            '3) Send a Thank You letter to all donors',
            '4) Quit',
            'Please enter your selection > ')))  
        menu_func(response)

def menu_func(selection):
    '''
    Processes menu input using dictionary values for switching.
     Input:  String: numeric value
     Output: None'''

    menu_dict = {
        1: print_report,
        2: thank_you,
        3: thank_all,
        4: quit,}
    
    # Check if selection is a valid input
    if not selection.isnumeric() or int(selection) not in menu_dict:
        print('\nPlease enter a number 1 - 4')
    else:
        # Gets and calls the value associated with the selection
        menu_dict.get(int(selection))()

def sort_key(values): 
    '''
    Sorts the dictionary by values.
     Input:  Dictionary: values
     Output: Dictionary: sorted values'''
    return values[1][0]

def print_report():
    '''
    Prints a sorted list of your donors, sorted by total historical donation amount.
     Input:  None
     Output: Display: formatted donor list'''

    # Create Report Header
    print('\n{:<19}{:3}{:12}{:3}{:10}{:3}{:<10}'
    .format('Donor Name', '|', 'Total Given', '|', 'Num Gifts', '|', 'Average Gift'))
    print('-'*62)

    # Print donor list into a table format
    for name, donor in sorted(donors.items(), key = sort_key, reverse = True):
        print('{:<21}${:>11,.2f}{:^16}${:>11,.2f}'.format(name, *donor))

def thank_you():  
    '''
    Creates a Thank You letter for a donor.
     Input:  None
     Output: None'''

    found = False
    while not found:

        # Prompt for a full name of the donor, list of donor names, or quit to menu
        response = input("\nPlease enter the full name of the donor, 'List' for a list of donors," 
            " or 'Quit' to exit to the menu > ")

        # Exit to main menu if 'quit' is entered
        if response.lower() == 'quit':
            menu()

        # If input value is empty
        if response == '':
            print('\nPlease enter a name')
        # If response is list show a list of donor names and reprompt
        elif response.lower() == 'list':
            for donor in sorted(donors):
                print(donor)    
        else:
            for donor in donors:        
                # If the response name is on the list prompt for donation amount
                if response.lower() == donor.lower() and not found:
                    add_donation(donor)
                    found = True
                    break

            # If the response name is not on list add it and prompt for donation amount
            if not found:
                add_donation(response.title(), True)
                found = True

def add_donation(donor, is_new = False):
    '''
    Appends or adds a donation to the donor list.
     Input:  String: name, Boolean: is_new
     Output: Display: Thank You letter'''

    # Check for valid entry or quit
    while True:
        # Prompt user for a donation amount
        donation = input("Please enter the amount of the donation for {} or 'Quit' to exit to the main menu > $ ".format(donor))

        # Exit to main menu if 'quit' is entered
        if donation.lower() == 'quit':
            menu()
        elif donation.isnumeric():
            break
        else:
            print("Please enter a numeric value")

    # Convert the donation amount to a float
    donation = float(donation)

    donor_data = ()
    # Set new donor data values 
    if is_new:
        donor_data = [0, 0, 0]
    # Get current donor values
    else:
        donor_data = donors.get(donor)

    # Calculate sum, number donations, and the average donation
    sum_donations = donor_data[0] + donation
    num_donations = donor_data[1] + 1
    avg_donation  = sum_donations / num_donations  

    # Add amount to the donor's donation history
    donors.update({donor : [sum_donations, num_donations, avg_donation]}) 

    # Print the thank you email
    print(format_letter(donor, donation))

def format_letter(name, donation):
    '''
    Formats an email thanking the donor for their donation.
     Input:  String: name, Float: donation
     Output: String: Formatted thank you letter'''

    donor = {'first_name': name.split()[0], 'last_name': name.split()[1].strip(','), 'amount': donation}

    return('''\n
    Dear {first_name} {last_name},\n
    Thank you so much for your generous gift of ${amount:,.2f}!\n
    Your donation will go far in helping so many orphaned kittens and puppies find a new home.\n    
    Thank You,
    Paws'''.format(**donor))

def thank_all():
    '''
    Formats and saves a letter thanking all the donor for their donations.
     Input:  None
     Output: Files: Formatted thank you letters'''

    for donor in donors:
        first_name = donor.split()[0]
        last_name = donor.split()[1].strip(',')

        # Creates file and path
        file_path = os.path.join("./{}_{}.txt".format(first_name, last_name))

        # Opens and writes the Thank You letter to the file
        with open(file_path, 'w+') as new_file:
            new_file.write(format_letter(donor, donors.get(donor)[0]))
    print('\nTask Complete')

def quit():
    '''
    Exit the program
     Input:  None
     Output: Exit to terminal'''

    print('\nGood Bye!\n\n')
    exit()

if __name__ == "__main__":

    menu()


