#!/usr/bin/env python3

Donations = [("Bill Turner", 1500.99),
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
    print('Welcome to the Mailroom!') if firstrun else print('You can:')
    print('1) Send A Thank You')
    print('2) View Donor Report')
    print('3) Quit Program')
    print('Type your respone or respone number.  You may type "back" at any time to return here.')

def pick_function(firstrun):    # ask initial prompt, return user desired output
    intro_prompt(firstrun)
    whatdo = str(input('\nWhat would you like to do?: ')).lower()
    if whatdo == '1' or'send' in whatdo or 'thank' in whatdo:    # only check key words to allow user flexibility
        return 'thank'
    elif whatdo == '2' or 'view' in whatdo or 'report' in whatdo:    # only check key words to allow user flexibility
        return 'report'
    elif 'back' in whatdo:    # only check key words to allow user flexibility
        return 'back'
    elif whatdo == '3' or 'quit' in whatdo:    # only check key words to allow user flexibility
        return 'quit'
    else:
        print('\n"' + whatdo +'" is an invalid input.  Try Again.')
        return 'adfgadf'    # generic non-sensical string, to keep calling loop active.

def ThankYou(Donations):    # function used to send thank you and add donations
    new_donation = ['',0]    # initialize an empty new_donation entry
    while new_donation[0] == '':
        recipient = str(input('\nWhom shall we thank?: ')).title()
        if recipient == 'List':
            print('\nExisting Donors:')
            for i, name in enumerate(DonorList(Donations)):
                print(name)
        elif recipient == 'Back':
            return 0    # exits function immediately and returns to main
        elif recipient not in DonorList(Donations):
            add_new = input('Confirm new donor ' + recipient + ' (yes/no): ').lower()    # in case user misspelled or mistyped
            if add_new == 'no':    # means user mistyped, return to "thank you" prompt
                recipient = 'List'    # set loop to provide list of donors
                continue    # restart loop.  User given a list of current donors and prompt
            elif add_new == 'back':
                return 0    # exits function immediately and returns to main
            else:
                new_donation[0] = recipient    # user intentionally put new name.  Will use it.
        else:    # user gives name of existing donor.  will use it.
            new_donation[0] = recipient
    don_amount = float(input('How much did ' + recipient + ' donate? $'))
    new_donation[0], new_donation[1] = recipient, don_amount
    print('\nEMAIL CONTENT:')
    print(f'{recipient}, Thank you for your generous donation of ${don_amount:.2f} toward our cause.\n')
    Donations.append(new_donation)
    print('Return to Prompt\n')

def DonorList(Donations):    # funtion to extract a list of existing donors
    Names = []
    for i,data in enumerate(Donations):
        if data[0] not in Names:
            Names.append(data[0])
    return Names

def AmountsDonated(Donations):
#    Names = DonorList(Donations)
#    total_donation = []
#    for i, donor in enumerate(Names):
#
#        for j, data in enumerate(Donations):
#            if
    return 0

if __name__ == '__main__':
    firsttime = True    # program will show welcome message
    whatdo = ''    # initialize whatdo as empty to enter loop
    while whatdo !='quit':    # keep program going until user types "quit"
        whatdo = pick_function(firsttime)
        firsttime = False    # welcome message will not be shown again
        if whatdo == 'thank':
            ThankYou(Donations)
        elif whatdo == 'report':
            print('this is a report')
        elif whatdo == 'back':
            print('You are already at the top prompt.  Cannot go back any further.\n')
