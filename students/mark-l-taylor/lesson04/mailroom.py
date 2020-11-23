#!/usr/bin/env python3

''' Mailroom Program Part 1
    The Last Laugh Program
    https://simpsons.fandom.com/wiki/Last_Laugh_Program
'''
import os, datetime

def get_donor_names():
    '''Generate a list of donors.'''
    return donors.keys()

def add_donation(name):
    '''Prompt user for donation and add to donor data.'''
    amount = input('Enter donation amount in dollars: ')        
    #convert the amount to a float and add to donor
    donors[name].append(float(amount))
    return amount

    
def generate_email(name, amount):
    '''Generate email thanking the donation.'''
    email = '\n'.join(['', 'Dear {},'.format(name), '',
            'Thank you for your generous donation of ${:.2f}.'.format(float(amount)),
            'Your donation will continue to allow us to put a smile on our patients faces.', '',
            'Sincerly,',
            'The Last Laugh Program'])
    return email

def send_thanks():
    '''Generate a thank you note. '''
    #Prompt for name to send thank you
    name = input('\nWho would you like to send a thank you to?\n(Tip: type \'list\' for possible names)\n')
    if name == 'list':
        print('Current Donors:')
        for d in get_donor_names():
            print(d)
        #Repeat question for donor email
        send_thanks()
    elif name in get_donor_names():
        amount = add_donation(name)
        print(generate_email(name, amount))
    elif name.lower() == 'quit':
        print('Returning to main menu.')
        return
    else:
        print('\n{} is a new donor! Adding to donor database.'.format(name))
        #Add new donor with empty donation
        donors[name] = []
        amount = add_donation(name)
        print(generate_email(name, amount))

def letters_all():
    '''Generate letters to each donor'''
    print('\nGenerating donations letters:')
    date = datetime.date.today().isoformat()
    for name, donations in donors.items():
        filename = name.replace(' ', '_') + f'_{date}' + '.txt'
        print(f'{name:20} --> {filename}')
        with open(filename, 'w') as outf:
            outf.writelines(generate_email(name, donations[-1]))
             
def donation_sort(data):
    ''' Sort the report data by the total given.'''
    #Report data is a list: [name, total given, num donations, avg donation]
    #Sorting on the total given
    return data[1]
    
def create_report():
    ''' Create a formatted report of the donor data.'''
    
    frmt_header = '{:<26}|{:^13}|{:^11}|{:>13}'
    frmt_line   = '{:<26} ${:>11.2f} {:>11}  ${:>12.2f}'
    print('\nDonations Summary:\n')
    print(frmt_header.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*66)
    
    #Convert the donor data into report form
    fmt_data = []
    for d in donors:
        fmt_data.append([d, sum(donors[d]), len(donors[d]), sum(donors[d])/len(donors[d])])

    #Sort the data by the total amount given
    fmt_data.sort(key=donation_sort, reverse=True)
    
    #Print the sorted data in the report format
    for f in fmt_data:
        print(frmt_line.format(*f))

def quit_program():
    '''Quit the program'''
    print('Exiting Script.')
    exit()
    
def prompt_actions():
    ''' Prompt user for action they would like to perform'''
    
    print('\nWhat would you like to do?')
    
    #Simplify the input to prompt for a numbered response
    #Create a dictionary from an enumerated list
    enumerate_actions = dict(enumerate(main_actions.keys(), start=1))
    for i, act in enumerate_actions.items():
        print(f'\t({i}) {act}')
        
    #Get user action
    response = input('Please select an action: ')
    while True:
        if not response.isnumeric() or int(response) not in enumerate_actions:
            response = input(f'Select a number between 1 and {len(main_actions)}: ')
        else:
            return int(response), enumerate_actions[int(response)]

#
# Main Action (Dictionary Switch
#
main_actions = {'Send thank you to single donor': send_thanks,
                'Create report': create_report,
                'Send letters to all donors': letters_all,
                'Quit' : quit_program,
                }

#
# Data Set
#
donors = {'Homer Simpson': [25.15],
          'Charles Burns': [0.01, 0.05],
          'Kent Brockman': [105.75, 225.76, 387.90],
          'Ned Flanders' : [1054.85, 2345.00, 876.50],
          'Barney Gumble': [15.25, 35.75, 12.99],
         }

                
if __name__ == '__main__':
    #Begin the script by asking the user what they want to do
    #program will continue to loop until the user selects the Quit option
    while True:
        resp_num, resp_str = prompt_actions()
        main_actions.get(resp_str)()
    
    