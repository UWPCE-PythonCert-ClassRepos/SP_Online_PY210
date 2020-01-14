#!/usr/bin/env python3
#### Mailroom Project Part 2 ####

import sys
import pathlib


# Create list of donors and their donation history
database = {'Bill Gates': [2000000, 250000000], 
            'Jeff Bezos': [2000000],
            'Elon Musk': [50000000, 10000000], 
            'Howard Schultz': [1000000], 
            'Paul Allen': [450000000]}


def add_donor(name, donation): # Add a new donor to the database

    database[name] = [donation]


def add_donation(name, donation): # Add a donation for an existing donor
    
    database[name].append(donation)


def text_thank_you(name): # Write thank you email        
    
    email = (f'Dear {name}:\n\n'
                    'On behalf of your Local Charity, I would like to thank you for your generous donation. '
                    'We appreciate your support not only for us but for our cause.\n\n'
                    'We wish you all the best,\n\n'
                    'Local Charity Persident\n')

    return email

def donation_amount(name): # User inputs donation
    
    # Enter donation amount
    while True:
        try:
            amount = int(input('How much was their donations? '))
        except ValueError:
            print('Sorry that is an invalid')
            continue
        else:
            break

    return amount


def thank_you(): # Send a thank you
    
    # Set up inputs for appending database
    name = 'list'
    while name == 'list':
        name = input("Alright.  Which donor would you like to send a thank you card?\nType 'list' to see a list of past donors >>>")   
        if name == 'list':
            print(list(database.keys()))
    
    donation = donation_amount(name)

    # Add new donation to database
    if database.get(name):
        add_donation(name, donation)
    else:
        add_donor(name, donation)

    # Print thank you email
    text_thank_you(name)


def sort_key(donor): # Define sort key
    return int(sum(donor[1]))


def sort_database(database): # Sort Data by total amount donated
    
    sorted_data = sorted(database.items(), key=sort_key, reverse=True)

    return sorted_data


def format_report(sorted_data): # Format data to display in report
    """Requires a sorted dictionary that will print each member row"""

    member_row = '{:<24}{:^5} ${:>14,}{:^5} {:^5}{:^5} ${:>14,.2f}'

    report_rows = list()
    # Print each row to format table
    for per in sorted_data:
        report_rows.append(member_row.format(per[0], ' ', int(sum(per[1])), ' ', round(len(per[1]),2), ' ', round(sum(per[1])/len(per[1]),2)))

    return report_rows


def display_report(): # Create a report of donors
    
    # Format table with header
    print('Generating report of donors....')
    # Header
    print(""+"-" * 80 + "\n Donor Name"+" " * 19 + "| Total Donated | Num Donations | Average Donation\n"+"-" * 80)

    for row in format_report(sort_database(database)):
        print(row)

    # Exit to main menu
    exit = 'none'
    while exit != 'quit':
        exit = input('Type quit to return to the menu... ')


def letter_text(name): # Text for letters for all donors

    # Donation amount
    charity_amount = sum(database[name])
    
    letter = ('Dear {0}\n\n'
            'Thank you for your donations totaling' 
            '$ {1:,}.  We appreciate your contributions'
            'for the year.\n\nHappy holidays,\n\n' 
            'Your loal charity President').format(name, charity_amount)
    
    return letter


def send_letters(): # Write a letter to all donors

    print('Ok.  Sending letters to all donors now...')

    pth = pathlib.Path('./')
    folder = pth.absolute()

    for name in database.keys():
        first_name = name.split()[0]
        last_name = name.split()[1]
        file_format = "{0}_{1}.txt".format(first_name, last_name)
        file_path = folder / file_format

        # Write new files
        with open(file_path, 'w') as new_file:
            # Writing files
            new_file.write(letter_text(name))

    print('Ok.  The letters have been sent to all donors.')
       
# Execute file when running
if __name__ == '__main__':
    
    arg_dict = {'1': thank_you,
                '2': display_report,
                '3': send_letters,
                '4': exit}

    while True:
    # Opens up the mailroom
        task = 0
        task = input("\n".join(("What do you need to do?",
              "Please choose from the options below:",
              "1 - Send Thank You Card",
              "2 - Print A Report",
              "3 - Send Thank You to all donors",
              "4 - Exit",
              ">>> ")))

        # Run functions for tasks based on user's response
        while True:
            try:
                arg_dict.get(task)()
            except (ValueError, TypeError, KeyError) as e:
                task = input('Please enter a valid option from 1-4: ')
                continue
            else:
                break
