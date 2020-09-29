#!/usr/bin/env python3

'''
# Program takes a list of donations made by (6) donors, each donating up to 3x with varying amounts
# Program displays an intro message and asks user to select a task from the main menu
#
# If user selects option 1 by inputing "1" or anything containing "send" or "thank":
#   - User is asked for a name.  If name is a previous donor, a new donation record is made for them
#       - If name is a prior donor, program proceeds
#       - If name is not a prior donor, user is asked to confirm the new name, then program proceeds
#   - User is asked for a donation amount.  This amount is recorded on the new donation record
#   - A formatted email message is written thanking the donor for their donation
# User is returned to main menu
#
# If user selects option 2 by inputting "2" or anything containing "record" or "view", a report with the following is generated:
#   - Donor Name (one listing per donor)
#   - Total Net Donation
#   - Number of Donations Made
#   - Average Donation
# User is returned to main menu
#
# If user selects option 3 by inputing "3" or "quit" the program terminates.
#
# If at ANY prompt the user inputs "back" the function terminates and returns to main menu.
'''

Donations = [("Bill Turner", 1500.99),
    ("Bill Turner", 3500.00),
    ("Bill Turner", 800.25),
    ("Jack Yelb", 145.72),
    ("Kelly Jones", 250.00),
    ("Mark Tomles", 600.00),
    ("Guido Roccio", 1153.90),
    ("Kelly Jones", 57.00),
    ("Jack Yelb", 1350.25),
    ("Mary Jaco", 27500.00),
    ("Guido Roccio", 47.15),
    ]    # initial data for script

def intro_prompt(firstrun):    # greets user, prompts for input for what to do
    print('Welcome to the Mailroom!\nMain Menu:') if firstrun else print('Main Menu:')
    print('1) Send A Thank You')
    print('2) View Donor Report')
    print('3) Quit Program')
    print('Type what you want to do.  You may type "back" at any time to return here.')

def pick_function(firstrun):    # ask initial prompt, return user desired output
    intro_prompt(firstrun)
    whatdo = str(input('\nWhat would you like to do?: ')).lower()
    if whatdo == '1' or'send' in whatdo or 'thank' in whatdo:    # only check key words, or number from propmt, to allow user flexibility
        return 'thank'
    elif whatdo == '2' or 'view' in whatdo or 'report' in whatdo:    # only check key words or prompt # to allow user flexibility
        return 'report'
    elif 'back' in whatdo:
        return 'back'
    elif whatdo == '3' or 'quit' in whatdo:    # only check key words or prompt number to allow user flexibility
        return 'quit'
    else:
        print('\n"' + whatdo +'" is an invalid input.  Try Again.')
        return 'adfgadf'    # return intentionally non-sensical string to keep calling loop active.

def ThankYou(Donations):    # function used to send thank you and add donations
    new_donation = ['', 0]    # initialize an empty new_donation entry
    while new_donation[0] == '':
        recipient = str( input('\nWhom shall we thank?: ') ).title()
        if recipient == 'List':
            print('\nExisting Donors:')
            for i, name in enumerate(DonorList(Donations)):
                print('\t' + name)
        elif recipient == 'Back':
            print('\nReturning to Main Menu\n')
            return 0
        elif recipient not in DonorList(Donations):
            add_new = input('Confirm new donor ' + recipient + ' (yes/no): ').lower()    # in case user misspelled or mistyped
            if add_new == 'no':    # means user mistyped, return to "thank you" prompt
                recipient = 'List'    # set loop to provide list of donors
                continue    # restart loop.  User given a list of current donors and prompt
            elif add_new == 'back':
                print('\nReturning to Main Menu\n')
                return 0
            else:
                new_donation[0] = recipient    # user intentionally put new name.  Will use it.
        else:    # user gives name of existing donor.  will use it.
            new_donation[0] = recipient
    don_amount = input('How much did ' + recipient + ' donate? $')    # accept any data type in case is "back"
    if 'back' in don_amount:    # if don_amount is back, return to main menu
        print('\nReturning to Main Menu\n')
        return 0
    else:
        don_amount = float(don_amount)    # make don_amount a float value for f-string
    new_donation[0], new_donation[1] = recipient, don_amount    # tie data to donation record
    print('\nEMAIL CONTENT:')
    print( f'{recipient}, Thank you for your generous donation of ${don_amount:,.2f} toward our cause.\n' )
    Donations.append(new_donation)
    print('Return to Main Menu\n')

def DonorList(Donations):    # funtion to extract a list of existing donors
    Names = []
    for i,data in enumerate(Donations):
        if data[0] not in Names:
            Names.append(data[0])    # add name from donations if not in names list already
    return Names    # returns list with all existing donors listed only 1x

def PrintReport(Donations):
    donors = DonorList(Donations)    # get list of donor names
    contributions = DonationCount(Donations, donors)    # get a corresponding list of number of times donated
    print()
    print('Donor Name          |  Total Given  | # of Gifts |  Average Gift  |')
    print('--------------------|---------------|------------|----------------|')
    for i, name in enumerate(donors):
        total_gift = TotalDonation(Donations, name)
        times = contributions[i]
        print( f'{name:.<20}|${total_gift:>13,.2f} | {times:^10d} | $ {total_gift/times:12,.2f} |' )
    print('\nBack to Home Screen\n')

def DonationCount(Donations, donors):
    contributions = []
    for i, name in enumerate(donors):
        doncount = 0
        for j in range(0, len(Donations)):    # search through donations list for selected donor 'i'
            doncount += 1 if Donations[j][0] == donors[i] else 0    # increment for each donation by 'i'
        contributions.append(doncount)
    return contributions    # returns a list of integers (times donated) corresponding to each donor in donors list
    
def TotalDonation(Donations, donor):
    total = 0    # initialize return value at 0
    for i,records in enumerate(Donations):
        total += records[1] if records[0] == donor else 0
    return total    # returns single value of net donation by subject donor

if __name__ == '__main__':
    firsttime = True    # program will show welcome message
    whatdo = ''    # initialize whatdo as empty to enter loop
    while whatdo !='quit':    # keep program going until user types "quit"
        whatdo = pick_function(firsttime)
        firsttime = False    # welcome message will not be shown again
        if whatdo == 'thank':
            ThankYou(Donations)
        elif whatdo == 'report':
            PrintReport(Donations)
        elif whatdo == 'back':
            print('You are already at the Main Menu.\n')
