import sys
#Mailroom.py


# Database Functions
"""
Database requirements
-keep track of: donor names, total amount donated, number of times donated
                average donation.

Database Structure
    [('Donor Name', Total donated, number dontations, average donation),
     ('Donor Name', Total donated, number dontations, average donation),
     ...]

"""

def initialize_database():
    database = [('John Smith',5000, 1, 5000),
                ('Jane Adams',25000,1, 25000),
                ('Brett Johnson', 50, 1, 50),
                ('Sofia Pippy', 623, 1, 623),
                ('Maddy North', 85426, 1, 85426)]
    return database

def print_donor_list(database):
    print ('\nDonor List\n----------')
    for donor in database:
        print('{}'.format(donor[0]))
    print('----------')

def add_new_donor(database, name,donation_amount):
    new_donor = (name,donation_amount,1,donation_amount)
    database.append(new_donor)
    return database

def add_new_donation(database,name,donation_amount):
    #by default this is for existing donors
    donor_found=0

    for idx,donor in enumerate(database):
        if donor[0] == name:
            donor_found=1

            #update donor data
            total_donation_new= donor[1] + donation_amount
            number_donations_new = donor[2] + 1
            average_donation_new = total_donation_new/number_donations_new
            donor_updated = (name,total_donation_new,number_donations_new,
                            average_donation_new)

            database[idx] = donor_updated

    if donor_found==0:
        print(f"Error: Donor '{name}' not found in")
        print_donor_list(database)

    return database

def sort_key(donor):
    return donor[1]

# Mailroom functions
def prompt_user():
    prompt = "\n".join(('What would you like to do?',
             '1: Send thank you note',
             '2: Create report',
             '3: Quit',
             '>>> '))

    UserAction = input(prompt)
    return UserAction

def get_donation_amount():
    donation_amount_prompt = 'Enter the donation amount: $ '
    amount = input(donation_amount_prompt)
    amount = float(amount)
    return amount

def send_thank_you_note(database):

    #Compose an email: thank the user, print email to terminal
    Email = '{} thank you for your generous donation of ${:.2f}'

    thank_you_prompt = 'Enter the donors full name or type "list" to see all donors in the database.\n>>> '
    donor_name = (input(thank_you_prompt)).title()

    if donor_name == 'List':
        print_donor_list(database)
    elif donor_name in database:
        donation_amount = get_donation_amount()
        database = add_new_donation(database,donor_name,donation_amount)
        print(Email.format(donor_name,donation_amount))
    elif donor_name not in database:
        donation_amount = get_donation_amount()
        database = add_new_donor(database,donor_name,donation_amount)
        print(Email.format(donor_name,donation_amount))
    else:
        #function error catching
        print('somethings not right')


    return None

def create_report(database):
    #Print the list of donors sorted by historical donation amount
    #Include
        #Donor name
        #Total donated
        #Number of donations
        #Average donation amount
    #End result should be nice and tabular
    #Re-prompt for an action

    database = sorted(database, key=sort_key, reverse=True)
    print('-----Donation Report-----')
    print('\n{:<15} | {:>14} | {:>11} | {:>16}'.format('Donor Name', 'Total Donation', '# donations','Average Donation'))
    print('-'*(15+14+11+16+10))
    for donor in database:
        print(f"{donor[0]:<15} | ${donor[1]:>13.2f} | {donor[2]:^11} | ${donor[3]:>15.2f}")

    print('\n')
    return None

# Driver Function
def mail_room():
    database = initialize_database()
    welcome_message = '------------Welcome to the Mailroom :)------------'
    print(welcome_message)
    while True:
        #Prompt the user for one of the following actions:
        #print('Pick and action\n 1: Send thank you note\n 2: Create report\n 3: quit')
        #UserAction = input()

        UserAction = prompt_user()

        if UserAction == '1':
            send_thank_you_note(database)
        elif UserAction == '2':
            #2 Create a report
            print('User option 2')
            create_report(database)
        elif UserAction == '3':
            #3 quit
            print('Goodbye!')
            return False
        else:
            print('Not a valid option...\n')
            UserAction = prompt_user()

    return None

# Main Interaction
if __name__ == '__main__':
    mail_room()