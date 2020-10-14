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
    pass

def prompt_actions():
    print('What would you like to do:')
    for i,act in enumerate(actions):
        print(f'\t({i+1}) {act}')
    
    #Get user action
    response = input('Please select an action:')
    while True:
        if not response.isnumeric() or int(response) not in list(range(1,len(actions))):
            response = input(f'Select a number between 1 and {len(actions)}:')
        else:
            return int(response),actions[int(response)-1]
    
if __name__ == '__main__':
    print(prompt_actions())