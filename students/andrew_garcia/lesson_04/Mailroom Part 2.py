'''
Andrew Garcia
Mailroom Part 2
7/6/19
'''

#!/usr/bin/env python3

all_donations = {'Jayson Black': [156.80, 207.32, 219.92],
          'Bryan Fultan': [1236.28],
          'Danica Dolores': [163.51, 100.42, 186.22],
          'Skylar Odell': [167.90, 151.62],
          'Roy Max': [137.97, 227.63]}

def options_menu():
    """Menu of options the user is shown, allowing them to navigate through the script """

    answer = input('''
Options:
1 - Send a Thank You 
2 - Send All Donors a Thank You
3 - View a Report
4 - Quit

    Select an Option: ''')

    if answer == '1':
        send_thank_you()
    elif answer == '2':
        thank_all()
    elif answer == '3':
        create_report()
    elif answer == '4':
        pass
    else:
        print('That is not a valid answer!')
        options_menu()


def thank_all(all_donations = all_donations):
    """Creates a text file for all donors and their donations"""

    thank_donations = []  # create a list of donor and donation amount
    donation_amount = []  # takes note of all donation amounts from one donor
    for key in all_donations:
        donation_amount += all_donations[key]
        for item in donation_amount:
            thank_donations += [[key, item]]
        donation_amount = []
    print(thank_donations)
    for item in thank_donations:
        filename = item[0] + '-' + str(item[1])  # creates file named after donor and donation amount
        with open(f'{filename}.txt', 'w+') as f:
            text = (f'''\nDear {item[0]},
    
            Thank you so much for your generous donation of ${item[1]:.2f}!
            The kind generosity that you and others give us helps us complete the great work we are doing for others.
    
            From,
            Your Local Charity
            \n''')
            f.write(text)
    print('Thank You Saved.')
    options_menu()

def format_thank_you(name, amount):
    """Creates thank you note for one donor"""

    print(f'''\nDear {name.title()},

Thank you so much for your generous donation of ${amount:.2f}!
The kind generosity that you and others give us helps us complete the great work we are doing for others.

From,
Your Local Charity
\n''')
    options_menu()

def existing_donor(name, all_donations = all_donations):
    """Creates a Thank You Letter based on existing donations"""

    if name.title() in all_donations:  # looks for donation amounts from a donor
        print('List of Donations:')
        for item in all_donations[name.title()]:
            print(item)

        donation_number = float(input('Which donation amount would you like to use?: '))
        if donation_number in all_donations[name.title()]:  # takes a donation amount anf formats a thank you
            format_thank_you(name, donation_number)
        else:
            print('That is not a valid donation amount!')
            options_menu()

def add_donation(name, all_donations = all_donations):
    """Takes a new or existing donor and adds their donation to the list"""

    amount = input(f'How much did {name} donate?: ')
    if name.title() in all_donations:  # adds donation amount to dictionary with existing donor
        all_donations[name.title()] += [amount]
    elif name.title() not in all_donations:  # adds donor to the dictionary if it does not exist
        all_donations[name.title()] = [float(amount)]
    format_thank_you(name, float(amount))


def send_thank_you(all_donations = all_donations): #edit for dict
    """Gets donor name so that a thank you letter can be formatted"""

    name = input('Which Donor would you like to send a note to?: ')
    if name.lower() == 'list':  # gives list of donors
        print(all_donations)
        send_thank_you()
    elif name.lower() == 'quit':
        options_menu()
    elif name.title() in all_donations.keys():  # uses existing donor
        new_or_old = input('{} is already an existing donor. Would you like to use a new or existing donation?: [new/existing] '.format(name))
        if new_or_old.lower() == 'new':  # allows user to add a new donation for existing donor
            add_donation(name)
        elif new_or_old.lower() == 'existing':  # uses an existing donation amount
            existing_donor(name)
        else:
            print('That is not a valid answer!')
            send_thank_you()
    else: # adds donor if they do not exist in dictionary
        add_donation(name)


def sorting_donors(all_donations = all_donations):
    """Sorts the all_donations, ordering them in terms of highest total donation amount"""

    sorting_donors = []
    donor_info = []
    for item in all_donations:  # adds a single donor information at a time
        donation_amount = len(all_donations[item])
        total_donations = sum(all_donations[item])
        average_donation = total_donations / donation_amount
        sorting_donors += [[item, donation_amount, total_donations, average_donation]]

    def sort_key(sorting_donors):  # creating the sorting format
        return sorting_donors[2]

    # sorts donor by total amount of money donated
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








