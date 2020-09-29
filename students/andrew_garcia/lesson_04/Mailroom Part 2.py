'''
Andrew Garcia
Mailroom Part 2
7/25/19
'''

#!/usr/bin/env python3

all_donations = {'Jayson Black': [156.80, 207.32, 219.92],
          'Bryan Fultan': [1236.28],
          'Danica Dolores': [163.51, 100.42, 186.22],
          'Skylar Odell': [167.90, 151.62],
          'Roy Max': [137.97, 227.63]}

def options_menu():
    """Menu of options the user is shown, allowing them to navigate through the script """
    while True:
        answer = input('''
    Options:
    1 - Send a Thank You 
    2 - Send All Donors a Thank You
    3 - View a Report
    4 - Quit
    
        Select an Option: ''')

        switch_dict = {1: send_thank_you, 2: thank_all, 3: create_report}
        if answer == '1':
            switch_dict.get(1)()
        elif answer == '2':
            switch_dict.get(2)()
        elif answer == '3':
            switch_dict.get(3)()
        elif answer == '4':
            break
        else:
            print('That is not a valid answer!')



def thank_all(all_donations = all_donations):
    """Creates a text file for all donors, thanking their total donation amount"""

    thank_donations = []
    donation_amount = []

    for key in all_donations:
        donation_amount = all_donations[key]
        thank_donations = sum(donation_amount)
        filename = key
        with open(f'{filename}.txt', 'w+') as f:
            text = (f'''\nDear {key},

            Thank you so much for the donations you have been giving to our charity.
            You have made {len(donation_amount)} donations, giving a total of ${thank_donations:.2f}
            The kind generosity that you and others give us helps us complete the great work we are doing for others.

            From,
            Your Local Charity
            \n''')
            f.write(text)
    print('Thank You Saved.')


def format_thank_you(name, amount):
    """Creates thank you note for one donor"""

    print(f'''\nDear {name.title()},

Thank you so much for your generous donation of ${float(amount):.2f}!
The kind generosity that you and others give us helps us complete the great work we are doing for others.

From,
Your Local Charity
\n''')


def existing_donor(name, all_donations = all_donations):
    """Creates a Thank You Letter based on existing donations"""

    if all_donations.get(name):  # looks for donation amounts from a donor
        print('List of Donations:')
        for item in all_donations[name.title()]:
            print(item)

        donation_number = float(input('Which donation amount would you like to use?: '))
        if donation_number in all_donations[name.title()]:  # takes a donation amount and formats a thank you
            format_thank_you(name, donation_number)
        else:
            print('That is not a valid donation amount!')


def add_donation(name, all_donations = all_donations):
    """Takes a new or existing donor and adds their donation to the list"""

    amount = input(f'How much did {name} donate?: ')

    if name.title() in all_donations:  # adds donation amount to dictionary with existing donor
        all_donations[name.title()] += [float(amount)]
    elif name.title() not in all_donations:  # adds donor to the dictionary if it does not exist
        all_donations[name.title()] = [float(amount)]
    format_thank_you(name, float(amount))


def send_thank_you(all_donations = all_donations): #edit for dict
    """Gets donor name so that a thank you letter can be formatted"""
    while True:
        name = input('Which Donor would you like to send a note to?: ')
        if name.lower() == 'list':  # gives list of donors
            print(all_donations)
        elif name.lower() == 'quit':
            options_menu()
        elif all_donations.get(name):  # uses existing donor
            while True:
                new_or_old = input('{} is already an existing donor. Would you like to use a new or existing donation?: [new/existing] '.format(name))
                if new_or_old.lower() == 'new':  # allows user to add a new donation for existing donor
                    add_donation(name)
                elif new_or_old.lower() == 'existing':  # uses an existing donation amount
                    existing_donor(name)
                else:
                    print('That is not a valid answer!')
                break
        else:  # adds donor if they do not exist in dictionary
            add_donation(name)
        break

def sorting_donors(all_donations = all_donations):
    """Sorts the all_donations, ordering them in terms of highest total donation amount"""

    sorting_donors = []
    donor_info = []
    for item in all_donations:  # adds a single donor information at a time
        donation_amount = len(all_donations[item])
        total_donations = sum(all_donations[item])
        average_donation = total_donations / donation_amount
        sorting_donors.append([item, donation_amount, total_donations, average_donation])

    def sort_key(sorting_donors):  # creating the sorting format
        return sorting_donors[2]

    # sorts donor by total amount of money donated
    highest_donation = sorted(sorting_donors, key = sort_key)
    highest_donation.reverse()
    return highest_donation


def create_report():
    """Creates the report format for donors, sorting by highest donation amount
    Uses the sorting_donors function to have the list of donors in the right order"""


    print('\nDonor Name          | # Donations |   Total Donation   |   Average Donations  | ')
    print('-------------------------------------------------------------------------------')
    sorted_donors = sorting_donors()
    for item in sorted_donors:
        print(f'{item[0]:27}{item[1]}       ${item[2]:18.2f}    ${item[3]:18.2f}')



if __name__ == '__main__':
    options_menu()








