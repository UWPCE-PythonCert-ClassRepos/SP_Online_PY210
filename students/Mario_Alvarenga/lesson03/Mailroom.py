# #!/usr/bin/env python3
#Mario Alvarenga
#Lesson 04
#Mailroom

import sys

# Creating the donor data base
donors = [('Lionel Messi',[12450, 49563, 65897, 58690]),
          ('Cristiano Ronaldo',[65000, 98520]),
          ('Robert Lewandowski',[85005,48912,856940]),
          ('Neymar Dos Santos',[26598, 74158]),
          ('Karim Benzema',[865204, 58740, 15069])]

#This serves as the menu to initally face the user
menu = '\n'.join(['','Welcome to the FIFA World Donation Center ',
            'Please select one of the three options below',
            '1 - Send a Thank You note',
            '2 - Create a donations report',
            '3 - Exit Program',
            '','Input > '])

def get_donor_names():
    # Generate list of donor names for lookup
    return [donor[0] for donor in donors]

def add_donation(donor_name, donation_amount):
    # Find a donor in database
    donor_names = get_donor_names()
    donor_index = donor_names.index(donor_name)
    # Get donation history and add the latest donation
    donors[donor_index][1].append(donation_amount)


def generate_email(donor_name, donation_amount):
    # Create formatted email that can be copied & pasted
    email = ('\n'.join(['','Dear {donor_name},','',
    'Thank you for your generous donation of ${donation_amount:.2f}.',
    'Your contribution will help new arrivals receive the highest quality care possible.',
    'Please know that your donation makes a world of difference!',
    '','Sincerely,','The Good Place Team'])).format(donor_name=donor_name,donation_amount=donation_amount)
    print(email)

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
        elif name == 'quit': # Return to main menu
            return
        else:
            new_donor = False
            if name not in donor_names: # New donor, flag as new and add to database
                new_donor = True
                donors.append((name, []))
            # menu for donation amount
            amount = input('Enter donation amount in dollars: ')
            # If the user wants to bail mid-entry, remove the donor that was just
            # added (if they were new) and return to main menu
            if amount == 'quit':
                if new_donor:
                    donors.pop()
                return
            else:
                amount = float(amount)
            # Add donation amount to database
            add_donation(name, amount)
            # Generate email and return to main program
            generate_email(name, amount)
            return

def donor_key(donor):
    # Sort by total donation
    return donor[1]

def generate_report_data():
    donor_names = get_donor_names()
    # Declare and populate lists for report data
    total_donation, num_donation, avg_donation = [], [], []
    for data in donors:
        total_donation.append(sum(data[1]))
        num_donation.append(len(data[1]))
        avg_donation.append(total_donation[-1]/num_donation[-1])
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

def create_report():
    # Generate, format, and print report data
    report = generate_report_data()
    print_formatted_report(report)

def exit_program():
    print('Exiting program...')
    sys.exit()

def main():
    # Main function, repeatedly display menu and react based on user input
    while True:
        response = input(menu)
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