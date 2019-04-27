#!/usr/bin/env python3
import sys

donors = [('Eleanor Shellstrop',[25.00, 57.00]),
            ('Chidi Anagonye',[150.00, 300.00, 275.00]),
            ('Tahani Al-Jamil',[2000.00,7500.00,12000.00]),
            ('Jason Mendoza',[15.00,40.00,60.00]),
            ('Mindy St. Claire',[500.00])]

prompt = '\n'.join(['Welcome to The Good Place charity donor database.',
            'Please select from the following options:',
            '1 - Send a Thank You',
            '2 - Create a Report',
            '3 - Exit Program',
            'Input > '])

def return_donor_names():
    # Generate list of donor names for lookup
    return [donor[0] for donor in donors]

def add_donation(donor_name, donation_amount):
    # Find donor in database and add donation
    donor_names = return_donor_names()
    donor_index = donor_names.index(donor_name)
    donations = donors[donor_index][1]
    donations.append(donation_amount)
    return

def generate_email(donor_name, donation_amount):
    email = ('\n'.join(['','Dear {donor_name},','',
    'Thank you for your generous donation of ${donation_amount:.2f}.',
    'Your contribution will help new arrivals receive the highest quality care possible.',
    'Please know that your donation makes a world of difference!',
    '','Sincerely,','The Good Place Team',''])).format(donor_name=donor_name,donation_amount=donation_amount)
    return email

def write_thank_you():
    donor_names = return_donor_names()
    while True:
        name = input('Enter donor name: ')
        if name == 'list': # List donors
            print('\nCurrent list of donors:\n')
            print('\n'.join(donor_names))
            print()
        else:
            if name not in donor_names: # New donor, add to list and refresh names
                donors.append((name, []))
            # Prompt for donation amount
            amount = float(input('Enter donation amount in dollars: '))
            # Add donation to database
            add_donation(name, amount)
            # Generate and print email
            email = generate_email(name, amount)
            print(email)
            # Return to main program
            return

def exit_program():
    print('Exiting database...')
    sys.exit()

def main():
    while True:
        # Prompt user for input using prompt
        response = input(prompt)
        if response == '1':
            write_thank_you()
        elif response == '2':
            continue
        elif response == '3':
            exit_program()
        else:
            print('Not a valid option! Please try again.')

if __name__ == "__main__":
    main()
