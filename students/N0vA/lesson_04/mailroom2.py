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

# Send a thank you
def thank_you():
    
    print('Alright.  Which donor would you like to send a thank you card?')
    
    while True:
        person = input('Enter their name here or type "list" to see a list of donors: ')
        past_donor = False

        # Print list option
        if person.lower() == 'list':
            past_donor = True
            for per in database.keys():
                print(per)

        else:
            for name in database.keys():
                if person.lower() == name.lower():
                    past_donor = True
                    amount_donated = input('How much was their donation? ')
                    amount_donated = int(amount_donated)
                    database.get(name).append(amount_donated)      
                    break

            # Adding a new donor
            if past_donor == False:
                amount_donated = input('How much was their donation? ')
                amount_donated = int(amount_donated)
                database[person] = [amount_donated]


            # Write thank you email        
            email = print(f'Dear {person}:\n\n'
                    'On behalf of your Local Charity, I would like to thank you for your generous donation.'
                    'We appreciate your support not only for us but for our cause.\n\n'
                    'We wish you all the best,\n\n'
                    'Local Charity Persident\n')

            email
            return False

# Define sort key
def sort_key(donor):
    return int(sum(donor[1]))

# Create a report of donors
def report():

    # Sort Data
    sorted_data = sorted(database.items(), key=sort_key, reverse=True)

    # Format table
    member_row = '{:<24}{:^5} ${:>14,}{:^5} {:^5}{:^5} ${:>14,.2f}'
    print('Generating report of donors....')
    # Header
    print(""+"-" * 80 + "\n Donor Name"+" " * 19 + "| Total Donated | Num Donations | Average Donation\n"+"-" * 80)

    # Print 
    for per in sorted_data:
        print(member_row.format(per[0], ' ', int(sum(per[1])), ' ', round(len(per[1]),2), ' ', round(sum(per[1])/len(per[1]),2)))
    
    # Exit to main menu
    exit = 'none'
    while exit != 'quit':
        exit = input('Type quit to return to the menu... ')

def quick_letter():
    # Write a letter to all donors

    print('Ok.  Sending letters to all donors now...')

    pth = pathlib.Path('./')
    folder = pth.absolute()

    for donor in database.keys():
        first_name = donor.split()[0]
        last_name = donor.split()[1]
        file_format = "{0}_{1}.txt".format(first_name, last_name)
        file_path = folder / file_format

        # Donation amount
        charity_amount = sum(database[donor])

        # Write new files
        with open(file_path, 'w') as new_file:
            letter = ('Dear {0}\n\n'
                'Thank you for your donations totaling' 
                '$ {1:,}.  We appreciate your contributions'
                'for the year.\n\nHappy holidays,\n\n' 
                'Your loal charity President').format(first_name, charity_amount)

            # Writing files
            new_file.write(letter)
       
# Execute file when running
if __name__ == '__main__':
    
    arg_dict = {'1': thank_you,
                '2': report,
                '3': quick_letter,
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
        arg_dict.get(task)()

