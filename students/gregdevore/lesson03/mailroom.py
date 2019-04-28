#!/usr/bin/env python3
import sys

# Donor database
donors = [('Eleanor Shellstrop',[25.00, 57.00]),
            ('Chidi Anagonye',[150.00, 300.00, 275.00]),
            ('Tahani Al-Jamil',[2000.00,7500.00,12000.00]),
            ('Jason Mendoza',[15.00,40.00,60.00]),
            ('Mindy St. Claire',[500.00])]

# Main program prompt
prompt = '\n'.join(['','Welcome to The Good Place charity donor database.',
            'Please select from the following options:',
            '1 - Send a Thank You',
            '2 - Create a Report',
            '3 - Exit Program',
            '','Input > '])

def get_donor_names():
    # Generate list of donor names for lookup
    return [donor[0] for donor in donors]

def add_donation(donor_name, donation_amount):
    # Find donor in database
    donor_names = get_donor_names()
    donor_index = donor_names.index(donor_name)
    # Get donation history and add latest donation
    donations = donors[donor_index][1]
    donations.append(donation_amount)
    # Note: Even though each donor's data is stored as a tuple, which is immutable,
    #       their donation history is stored as a list, which is mutable. The tuple only
    #       contains a reference to the list, so the list can be changed even
    #       though it resides inside of a tuple. Hence, the above append statement works.
    return

def generate_email(donor_name, donation_amount):
    # Create formatted email that can be copied & pasted
    email = ('\n'.join(['','Dear {donor_name},','',
    'Thank you for your generous donation of ${donation_amount:.2f}.',
    'Your contribution will help new arrivals receive the highest quality care possible.',
    'Please know that your donation makes a world of difference!',
    '','Sincerely,','The Good Place Team'])).format(donor_name=donor_name,donation_amount=donation_amount)
    print(email)
    return

def write_thank_you():
    # Add donation for new or existing donor and compose 'Thank You' message
    # Get current list of donors
    donor_names = get_donor_names()
    while True:
        print()
        name = input('Enter donor name: ')
        if name == 'list': # List donors
            print('\nCurrent list of donors:\n')
            print('\n'.join(donor_names))
            print()
        elif name == 'quit': # Return to main prompt
            return
        else:
            new_donor = False
            if name not in donor_names: # New donor, flag as new and add to database
                new_donor = True
                donors.append((name, []))
            # Prompt for donation amount
            amount = input('Enter donation amount in dollars: ')
            # If the user wants to bail mid-entry, remove the donor that was just
            # added (if they were new) and return to main prompt
            if amount == 'quit':
                if new_donor:
                    donors.pop()
                return
            else: # Otherwise, convert donation amount to float
                amount = float(amount)
            # Add donation to database
            add_donation(name, amount)
            # Generate email
            generate_email(name, amount)
            # Return to main program
            return

def donor_key(donor):
    # Donor is a tuple of the form (name, total donation, number of donations, average donation)
    # Sort by total donation
    return donor[1]

def generate_report_data():
    donor_names = get_donor_names()
    total_donation = [sum(data[1]) for data in donors ]
    num_donation = [len(data[1]) for data in donors]
    avg_donation = [sum(data[1])/len(data[1]) for data in donors]
    report = list(zip(donor_names, total_donation, num_donation, avg_donation))
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
    return

def create_report():
    # Generate, format, and print report data
    report = generate_report_data()
    print_formatted_report(report)

def exit_program():
    print('Exiting program...')
    sys.exit()

def main():
    # Main function, repeatedly display prompt and react based on user input
    while True:
        response = input(prompt)
        if response == '1':
            write_thank_you()
        elif response == '2':
            create_report()
        elif response == '3':
            exit_program()
        else:
            print('Not a valid option! Please try again.')

if __name__ == "__main__":
    # Driver for main function
    main()
