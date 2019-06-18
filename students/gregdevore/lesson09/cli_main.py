#!/usr/bin/env python3

"""
Module to handle all program flow
"""

#!/usr/bin/env python3
import sys, os
from datetime import datetime
from donor_models import Donor, DonorCollection

# Main program prompt
prompt = '\n'.join(['','Welcome to The Good Place charity donor database.',
            'Please select from the following options:',
            '1 - Send a Thank You',
            '2 - Create a Report',
            '3 - Send letters to all donors',
            '4 - Exit Program',
            '','Input > '])

def write_thank_you(donor_name=None):
    # Add donation for new or existing donor and compose 'Thank You' message.
    # Donor name can be specified in case re-calling after invalid donation amount.
    while True:
        print()
        # Prompt for name if not specified
        if not donor_name:
            name = input('Enter donor name (type \'list\' to see donors or \'quit\' to exit): ')
        else:
            name = donor_name
        if name == 'list': # List donors
            print('\nCurrent list of donors:\n')
            print('\n'.join(dc.donorNames))
        elif name == 'quit': # Return to main prompt
            return
        else: # Get donations for donors
            # Prompt for donation amount
            amount = input('Enter donation amount in dollars (type \'quit\' to exit): ')
            # If the user wants to bail mid-entry, remove the donor that was just
            # added (if they were new) and return to main prompt
            if amount == 'quit':
                return
            else: # Otherwise, convert donation amount to float
                # Capture error if 'amount' not convertable
                try:
                    amount = float(amount)
                except ValueError:
                    print('Invalid amount, please enter a numeric value.')
                    # Re-call function with current name to re-prompt for amount
                    write_thank_you(donor_name=name)
                    # Need return statement here after return from recursive call
                    return
                else:
                    if amount <= 0:
                        print('Invalid amount, please enter a positive value.')
                        # Re-call function with current name to re-prompt for amount
                        write_thank_you(donor_name=name)
                        # Need return statement here after return from recursive call
                        return
            # Update donor information
            dc.updateDonor(name,amount)
            # Generate & print email to screen, return to main program
            email = dc.getDonor(name).generateEmail()
            print(email)
            # Need return statement here, otherwise while loop will repeat
            return

def print_formatted_report(report):
    # Generate formatted report to be printed
    # Input 'report' is expected to be a list of lists with
    # [donor name, total donation, number of donations, average donation]
    formatted_report = ['',
    'Donor Name                    | Total Donation | Num Donations | Avg Donation |',
    '-------------------------------------------------------------------------------']
    for donor in report:
        donor_name, total, number, average = donor
        formatted_report.append(f'{donor_name:<30} ${total:>14.2f}  {number:14d}  ${average:>12.2f}')
    formatted_report.append('')
    print('\n'.join(formatted_report))

def create_report():
    # Generate, format, and print report data
    report = dc.generateReportData()
    print_formatted_report(report)

def create_directory(target):
    # Create directory if it does not exist within current directory
    try:
        os.makedirs(target)
        success = True
    except OSError:
        # If directory exists but error thrown, most likely accessibility issue
        if os.path.exists(target):
            print('Writing to existing directory.')
            success = True
        else:
            print('Error creating folder \'{}\'. Check directory write permissions.'.format(target))
            success = False
    return success

def write_letters(target):
    # Format current date to add as timestamp
    date = datetime.today().strftime('%Y-%m-%d')
    for name in dc.donorNames:
        print('Writing letter to {}'.format(name))
        # Generate email with donor name, last donation amount, and total donation amount
        email = dc.getDonor(name).generateEmail()
        # Create file with donor name and timestamp
        filename = '{}/{}_{}.txt'.format(target, name.replace(' ','_'), date)
        try:
            with open(filename,'w') as f:
                f.write(email)
        except OSError: # Catch file write errors.
            print('Error writing file. Check directory write permissions.')

def send_letters():
    # Prompt for directory to write to
    target = input('Enter directory to put letters > ')
    if create_directory(target):
        write_letters(target)

def exit_program():
    print('Exiting program...')
    sys.exit()

def main():
    response_dict = {'1':write_thank_you,'2':create_report,'3':send_letters,'4':exit_program}
    # Main function, repeatedly display prompt and react based on user input
    while True:
        try:
            response_dict[input(prompt)]()
        except KeyError:
            print('Not a valid option! Please try again.')

if __name__ == "__main__":
    # Create some donor data for running the program from the command line
    dc = DonorCollection()
    donors = ['Eleanor Shellstrop', 'Jason Mendoza', 'Chidi Anagonye']
    amounts = [[50.,25.,75.], [100.,50.,80.], [200.,100.,300.]]
    for donor, amount in zip(donors,amounts):
        for donation in amount:
            dc.updateDonor(donor, donation)
    # Driver for main function
    main()
