#!/usr/bin/env python3
import sys, os
from datetime import datetime

# Donor database (use dictionary)
donors = {'Eleanor Shellstrop':[25.00, 57.00],
            'Chidi Anagonye':[150.00, 300.00, 275.00],
            'Tahani Al-Jamil':[2000.00,7500.00,12000.00],
            'Jason Mendoza':[15.00,40.00,60.00],
            'Mindy St. Claire':[500.00]}

# Main program prompt
prompt = '\n'.join(['','Welcome to The Good Place charity donor database.',
            'Please select from the following options:',
            '1 - Send a Thank You',
            '2 - Create a Report',
            '3 - Send letters to all donors',
            '4 - Exit Program',
            '','Input > '])

def get_donors(donors):
    return list(donors.keys())

def generate_email(donor_name, donation_amount, total_amount):
    email_dict = {'donor_name':donor_name, 'donation_amount':donation_amount, 'total_amount':total_amount}
    # Create formatted email that can be copied & pasted
    email = ('\n'.join(['Dear {donor_name},','',
    'Thank you for your generous donation of ${donation_amount:.2f}.',
    'To date, you have donated a total of ${total_amount:.2f} to our charity.',
    'Your contributions help new arrivals receive the highest quality care possible.',
    'Please know that your donations make a world of difference!',
    '','Sincerely,','The Good Place Team'])).format(**email_dict)
    return(email)

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
            print('\n'.join(get_donors(donors)))
        elif name == 'quit': # Return to main prompt
            return
        else: # Get donations for donors
            donations = donors.get(name,[])
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
            # Add donation to database
            donations.append(amount)
            donors[name] = donations
            # Generate & print email to screen, return to main program
            email = generate_email(name, amount, sum(donations))
            print(email)
            # Need return statement here, otherwise while loop will repeat
            return

def donor_key(donor):
    # Donor is a tuple of the form (name, total donation, number of donations, average donation)
    # Sort by total donation
    return donor[1]

def generate_report_data():
    # Declare and populate lists for report data
    total_donation, num_donation, avg_donation = [], [], []
    # Use single for loop instead of three separate comprehensions
    for donor,donations in donors.items():
        total_donation.append(sum(donations))
        num_donation.append(len(donations))
        avg_donation.append(total_donation[-1]/num_donation[-1])
    report = list(zip(donors.keys(), total_donation, num_donation, avg_donation))
    # Sorty by total donation, descending
    report.sort(key=donor_key, reverse=True)
    return report

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
    report = generate_report_data()
    print_formatted_report(report)

def send_letters():
    # Prompt for directory to write to
    target = input('Enter directory to put letters > ')
    # Create directory if it does not exist within current directory
    try:
        os.makedirs(target)
    except OSError:
        # If directory exists but error thrown, most likely accessibility issue
        if not os.path.exists(target):
            print('Error creating folder \'{}\'. Check directory write permissions.'.format(target))
            return

    # Format current date to add as timestamp
    date = datetime.today().strftime('%Y-%m-%d')
    for donor, donation in donors.items():
        print('Writing letter to {}'.format(donor))
        # Generate email with donor name, last donation amount, and total donation amount
        email = generate_email(donor,donation[-1],sum(donation))
        # Create file with donor name and timestamp
        filename = '{}/{}_{}.txt'.format(target, donor.replace(' ','_'), date)
        try:
            with open(filename,'w') as f:
                f.write(email)
        except OSError: # Catch file write errors.
            print('Error writing file. Check directory write permissions.')

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
    # Driver for main function
    main()
