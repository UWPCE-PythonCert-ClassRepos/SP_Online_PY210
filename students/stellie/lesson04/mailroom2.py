#!/usr/bin/env python3

# Stella Kim
# Assignment 2: Mailroom Part 2

"""
This program lists donors and their donation amounts.  A user is able to 
choose from a menu of 3 donation-related actions: send a thank you, create 
a report or quit the program.
"""

import sys

# Lists donors and their contributions
donor_db = {'John Smith': [10000, 5000, 1000],
            'Mary Johnson': [50000],
            'David Carlton': [2500, 500],
            'James Wright': [500, 500, 500],
            'Caroline Baker': [1000]
            }

# Displays menu options to user
prompt = '\n'.join(('\nWelcome to the mail room.',
          'Please choose from the below options:',
          '1 - Send a Thank You',
          '2 - Create a report',
          '3 - Send letters to all donors',
          '4 - Quit',
          '>>> '))

def invalid_option():
    print('\nThat is not a valid option.  Please choose one of the three options above.')

def send_thank_you():
    # Prompts user to choose a thank you note option
    user_response = input('\nPlease enter your full name or type "list" to view the list of donors.\nIf you would like to see the main menu type "menu": ')
    if user_response == 'list':
        view_donors()
        send_thank_you()
    elif user_response == 'menu':
        main()
    else:
        donor = search_db(user_response)  # calls function to search for already existing donor
        if donor:
            print('\nThis donor already exists in our database.')
            donation = donation_amount()  # calls function to obtain donation amount made
            donor_db[donor].append(donation)  # adds donation amount to existing donor in database
            thank_you_email(donor, donation)
        else:
            print('\nThis is a NEW donor and will be added to the database.')
            donation = donation_amount()  # calls function to obtain donation amount made
            donor_db[user_response] = [donation]  # adds new donor and donation to database
            thank_you_email(user_response, donation)

# Displays list of donors
def view_donors():
    print('\nThe following is the list of donors:')
    for donor in donor_db.keys():
        print(donor)

# Searches database to see if user already exists
def search_db(donor_name):
    for record in donor_db.keys():
        if record == donor_name:
            return record
    return None

# Prompts user to enter a donation amount
def donation_amount():
    user_donation = input('Please enter the amount you would like to donate: $')
    return float(user_donation)

# Sends donor a thank you email
def thank_you_email(donor_name, amount):
    print(f'\nThank you {donor_name} for your generous donation amount of ${amount:.2f}.  We hope to see you again soon.')

# Creates a report for user to see list of all donors and donations made
def create_report():
    print('\n{:<20} | {:<12} | {:<10} | {:<15}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('=' * 65)
    donor_list = list(donor_db.items())  # create list out of database to iterate through
    sorted_db = sorted(donor_list, key=sum_total, reverse=True)  # sorts database by sum amounts in descending order
    for item in sorted_db:
        total = sum(item[1])  # sum of all donations
        count = len(item[1])  # total number of donations
        average = total/count  # average of all donations
        print(f'{item[0]:<20} | {total:<12.2f} | {count:<10} | {average:<15.2f}')

# Sums donation amounts for each donor record and returns amounts for sorted database
def sum_total(donor_record):
    return(sum(donor_record[1]))

# Sends letters to all donors for their donations
def send_letters():
    for record in list(donor_db.items()):
        file_name = f'{record[0]}.txt'  # creates file name using name of donor
        new_file = open(file_name, 'w')  # creates a new file
        donor_letter = f'Dear {record[0]},\n\nThank you for your {len(record[1])} donations that total ${sum(record[1]):.2f}.\nIt will be put to very good use.\n\n\tSincerely,\n\t-The Team'
        new_file.write(donor_letter)  # writes the letter to the text file
        new_file.close()

# Exits the program
def exit_program():
    print('\nThank you for visiting!')
    sys.exit()

# Main menu options for user to choose for mail program
def main():
    switch_dict = {
        1: send_thank_you,
        2: create_report,
        3: send_letters,
        4: exit_program
    }
    while True:
        response = int(input(prompt))
        switch_dict.get(response, invalid_option)()

if __name__ == "__main__":
    main()