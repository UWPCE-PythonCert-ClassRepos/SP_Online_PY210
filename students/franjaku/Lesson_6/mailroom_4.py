# Mailroom_4.py
import os
import operator
import collections

# Dictionarys for the following
#   -User selections
#   -Main donor structure
#   - + .format() to produce a letter template

# Database Functions
"""
Database requirements
-keep track of: donor names, total amount donated, number of times donated
                average donation.

Database Structure
    {'Donor Name': [donation 1, donation 2,...],
     'Donor Name': [donation 1, donation 2,...],
     ...}

"""


def initialize_database():
    database = {'John Smith': [5000, 52048, 20],
                'Jane Adams': [25000, 5498, 3333, 87469],
                'Brett Johnson': [50, 6584, 20, 68, 9857, 5412],
                'Sofia Pippy': [623,98, 40658],
                'Maddy North': [85426, 10, 25]}
    return database


def print_donor_list(database):
    print('\nDonor List\n----------')
    for donor in database:
        print(donor)
    print('')


def add_new_donation(database, name, donation_amount):
    if name in database:
        database[name].append(donation_amount)
    else:
        database.setdefault(name,[donation_amount])


def sort_key(donor):
    return sum(donor[1])


# Mailroom functions
def prompt_user():
    prompt = "\n".join(('What would you like to do?',
                        '1: Send thank you note to a single donor.',
                        '2: Create report.',
                        '3: Send thank you letters to all donors.',
                        '4: Quit.',
                        '>>> '))
    UserAction = input(prompt)
    return UserAction


def get_donation_amount():
    donation_amount_prompt = 'Enter the donation amount: $ '
    amount = input(donation_amount_prompt)

    while True:
        try:
            amount = float(amount)
        except ValueError:
            print('Not a valid number.')
            amount = input(donation_amount_prompt)
        else:
            break

    return amount


def thank_you_note_prompt():
    prompt = 'Enter the donors full name or type "list" to see all donors in the database.\n>>> '
    donor_name = (input(prompt)).title()

    if donor_name == '':
        donor_name = 'List'

    return donor_name


def send_thank_you_note(database):
    # Compose an email: thank the user, print email to terminal
    email = '{} thank you for your generous donation of ${:.2f}'
    donor_name = thank_you_note_prompt()

    if donor_name == 'List':
        print_donor_list(database)
    else:
        donation_amount = get_donation_amount()
        add_new_donation(database, donor_name, donation_amount)
        print(email.format(donor_name, donation_amount))


def send_thank_you_note_all(database):
    for donor, data in database.items():
        with open(f"{donor}.txt", 'w+') as outfile:
            outfile.write(f"Dear {donor}\n")
            outfile.write(f"Thank you for you donation of ${data[0]}!\n")
            outfile.write(f"Best wishes,\nThe Team")


def create_report(database):
    # Sort database by most $$ donated
    sorted_database = collections.OrderedDict(sorted(database.items(), key=sort_key, reverse=True))
    print('-----Donation Report-----')
    print('\n{:<15} | {:>14} | {:>11} | {:>16}'.format('Donor Name', 'Total Donation', '# donations', 'Average Donation'))
    print('-'*66)
    for donor, data in sorted_database.items():
        print(f"{donor:<15} | ${sum(data):>13.2f} | {len(data):^11} | ${sum(data)/len(data):>15.2f}")

    print('\n')


def quit(database=None):
    print('Goodbye!')
    os.sys.exit()


# Driver Function
def mail_room():
    database = initialize_database()
    print('------------Welcome to the Mailroom :)------------')

    options_dict = {
        '1': send_thank_you_note,
        '2': create_report,
        '3': send_thank_you_note_all,
        '4': quit}

    while True:
        UserAction = prompt_user()

        try:
            options_dict.get(UserAction)(database)
        except TypeError:
            print('Not a valid option...\n')

    return None


# Main Interaction
if __name__ == '__main__':
    mail_room()
