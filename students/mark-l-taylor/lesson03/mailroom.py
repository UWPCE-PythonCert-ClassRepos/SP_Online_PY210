#!/usr/bin/env python3

''' Mailroom Program Part 1
    The Last Laugh Program
    https://simpsons.fandom.com/wiki/Last_Laugh_Program
'''

#
# Data Set
#


donors = [['Homer Simpson', [25.15]],
          ['Charles Burns', [0.01, 0.05]],
          ['Kent Brockman', [105.75, 225.76, 387.90]],
          ['Ned Flanders',  [1054.85, 2345.00, 876.50]],
          ['Barney Gumble', [15.25, 35.75, 12.99]]
         ]


actions = ['Send a Thank You', 'Create a Report', 'Quit']

def get_donor_names():
    '''Generate a list of donors.'''
    return [d[0] for d in donors]

def add_donation(name):
    '''Prompt user for donation and add to donor data.'''
    amount = input('Enter donation amount in dollars: ')        
    #Determine index of donor
    donor_index = get_donor_names().index(name)
    #convert the amount to a float and add to donor
    donors[donor_index][1].append(float(amount))
    return amount

    
def generate_email(name, amount):
    '''Generate email thanking the donation.'''
    email = '\n'.join(['','Dear {},'.format(name),'',
            'Thank you for your generous donation of ${:.2f}.'.format(float(amount)),
            'Your donation will continue to allow us to put a smile on our patients faces.','',
            'Sincerly,',
            'The Last Laugh Program'])
    print(email)

def send_thanks():
    '''Generate a thank you note. '''
    #Prompt for name to send thank you
    name = input('\nWho would you like to send a thank you to?\n(Tip: type \'list\' for possible names)\n')
    if name == 'list':
        print('Current Donors:')
        for d in get_donor_names():
            print(d)
    elif name in get_donor_names():
        amount = add_donation(name)
        generate_email(name,amount)
    else:
        print('\n{} 1is a new donor! Adding to donor database.'.format(name))
        #Add new donor with empty donation
        donors.append([name,[]])
        amount = add_donation(name)
        generate_email(name,amount)        
             
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
    print(frmt_header.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    print('-'*66)
    
    #Convert the donor data into report form
    fmt_data = []
    for d in donors:
        fmt_data.append([d[0], sum(d[1]), len(d[1]), sum(d[1])/len(d[1])])

    #Sort the data by the total amount given
    fmt_data.sort(key=donation_sort, reverse=True)
    
    #Print the sorted data in the report format
    for f in fmt_data:
        print(frmt_line.format(*f))
    
def prompt_actions():
    ''' Prompt user for action they would like to perform'''
    
    print('\nWhat would you like to do?')
    for i,act in enumerate(actions):
        print(f'\t({i+1}) {act}')
    
    #Get user action
    response = input('Please select an action: ')
    while True:
        if not response.isnumeric() or int(response) not in list(range(1,len(actions)+1)):
            response = input(f'Select a number between 1 and {len(actions)}: ')
        else:
            return int(response),actions[int(response)-1]
    
if __name__ == '__main__':

    #Begin the script by asking the user what they want to do
    #program will continue to loop until the user selects the Quit option
    while True:
        resp_num,resp_str = prompt_actions()   
        if resp_str == 'Send a Thank You':
            send_thanks()
        elif resp_str == 'Create a Report':
            create_report()
        elif resp_str == 'Quit':
            print('Exiting Script.')
            exit()
    
    