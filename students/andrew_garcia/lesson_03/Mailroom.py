'''
Andrew Garcia
Mailroom Part 1
6/22/19
'''

#!/usr/bin/env python3

all_donations = [['Jayson Black', [156.80, 207.32, 219.92]],
          ['Bryan Fultan', [1236.28]],
          ['Danica Dolores', [163.51, 100.42, 186.22]],
          ['Skylar Odell', [167.90, 151.62]],
          ['Roy Max', [137.97, 227.63]]]


def options_menu():
    answer = input('''
Options:
1 - Send a Thank You
2 - View a Report
3 - Quit
    
    Select an Option: ''')

    if answer == '1':
        send_thank_you()
    elif answer == '2':
        create_report()
    elif answer == '3':
        pass
    else:
        print('That is not a valid answer!')
        options_menu()


def format_thank_you(name, amount):
    print(f'''\nDear {name.title()},

Thank you so much for your generous donation of ${amount:.2f}!
The kind generosity that you and others give us helps us complete the great work we are doing for others.

From,
Your Local Charity
\n''')
    options_menu()

def add_donation(name, all_donations = all_donations):
    """Takes a new or existing donor and adds their donation to the list"""
    amount = input(f'How much did {name} donate?: ')
    for item in all_donations:
        if name.title() == item[0]:
            item[1] += [float(amount)]

    if name.title() != item[0]:
        all_donations.append([name, [float(amount)]])
    format_thank_you(name, float(amount))


def send_thank_you():
    """Gets donor name so that a thank you letter can be formatted"""

    name = input('Which Donor would you like to send a note to?: ')
    if name.lower() == 'list':
        print(all_donations)
        send_thank_you()
    elif name.lower() == 'quit':
        options_menu()
    else:
        add_donation(name)


def sorting_donors(all_donations = all_donations):
    """Sorts the all_donations, ordering them in terms of highest total donation amount"""

    sorting_donors = []
    donor_info = []
    for item in all_donations:  # adds a single donor information at a time
        donor_info = item
        donation_amount = len(donor_info[1])
        total_donations = sum(donor_info[1])
        average_donation = total_donations / donation_amount
        sorting_donors += [[item[0], donation_amount, total_donations, average_donation]]

    def sort_key(sorting_donors):  # creating the sorting format
        return sorting_donors[2]

    highest_donation = sorted(sorting_donors, key = sort_key)
    highest_donation = highest_donation[::-1]
    return highest_donation


def create_report(sorting_donors = sorting_donors()):
    """Creates the report format for donors, sorting by highest donation amount
    Uses the sorting_donors function to have the list of donors in the right order"""


    print('\nDonor Name          | # Donations |   Average Donation   |   Total Donations  | ')
    print('-------------------------------------------------------------------------------')
    for item in sorting_donors:
        print(f'{item[0]:27}{item[1]}       ${item[2]:18.2f}    ${item[3]:18.2f}')
    options_menu()

if __name__ == '__main__':
    options_menu()








