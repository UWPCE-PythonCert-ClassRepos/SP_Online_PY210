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
    print ('\nDonor List\n')
    for donor in database:
        print('{}'.format(donor[0]))

def add_new_donor(database, name, amount):
    new_donor = (name,amount,1,amount)
    database.append(new_donor)
    return database

def add_new_donation(database,name,amount):
    #by default this is for existing donors
    donor_found=0

    for idx,donor in enumerate(database):
        if donor[0] == name:
            donor_found=1

            #update donor data
            total_donation_new= donor[1] + amount
            number_donations_new = donor[2] + 1
            average_donation_new = total_donation_new/number_donations_new
            donor_updated = (name,total_donation_new,number_donations_new,
                            average_donation_new)

            database[idx] = donor_updated

    if donor_found==0:
        print(f"Error: Donor '{name}' not found in")
        print_donor_list(database)

    return database

# Mailroom functions
def prompt_user():
    prompt = "\n".join(('1: Send thank you note',
             '2: Create report',
             '3: Quit',
             '>>> '))

    UserAction = input(prompt)
    return UserAction

def send_thank_you_note(database):

    #Prompt for donation amount
        #convert amount to number
        #add donation to user history

    #Compose an email: thank the user, print email to terminal
    thank_you_prompt = 'Enter the donors full name or type "list" to see all donors in the database.'
    donor_name = input(thank_you_prompt)

    if donor_name == 'list':
        #print list of donors and re-prompt for name
        print_donor_list(database)
    elif donor_name in database:
        # (Name in database) use it
        pass
    elif donor_name not in database:
        #add donor name to list and use it
        pass
    else:
        #function error catching
        print('somethings not right')

    return None

def create_report():
    #Print the list of donors sorted by historical donation amount
    #Include
        #Donor name
        #Total donated
        #Number of donations
        #Average donation amount
    #End result should be nice and tabular
    #Re-prompt for an action
    return None

# Driver Function
def mail_room():
    initialize_database()
    welcome_message = "\n".join(('',
                      '------------Welcome to the Mailroom :)------------',
                      'What would you like to do?'))
    print(welcome_message)
    while True:
        #Prompt the user for one of the following actions:
        #print('Pick and action\n 1: Send thank you note\n 2: Create report\n 3: quit')
        #UserAction = input()

        UserAction = prompt_user()

        if UserAction == '1':
            #1 Send thank you: Prompt for a full name
            print('User option 1')
            #send_thank_you_note()
        elif UserAction == '2':
            #2 Create a report
            print('User option 2')
            #create_report()
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