#!/usr/bin/env python3

#
# Data Set
#
# Intial data will be lists to maintain context with current coursework
# A dictionary would be easier to keep data matched.

donors = ['Homer Simpson','Charles Burns', 'Kent Brockman', 'Ned Flanders', 'Barney Gumble']
donations = [[25.15], [0.01, 0.05] , [105.75,225.76,387.90], [1054.85,2345.00,876.50],[15.25,35.75,12.99]]

actions = ['Send a Thank You', 'Create a Report', 'Quit']

def send_thanks():
    pass
    
def create_report():
    #TODO: Need to sort by historical donation amount
    frmt_header = '{:<26}|{:^13}|{:^11}|{:>13}'
    frmt_data   = '{:<26} ${:>11.2f} {:>11}  ${:>12.2f}'
    print('\nDonations Summary:\n')
    print(frmt_header.format('Donor Name','Total Given','Num Gifts','Average Gift'))
    print('-'*66)
    for n,d in zip(donors,donations):
        print(frmt_data.format(n,sum(d),len(d),sum(d)/len(d)))
        
    

def prompt_actions():
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
    
    