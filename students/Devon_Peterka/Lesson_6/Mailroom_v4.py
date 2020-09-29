#!/usr/bin/env python3

import os
import sys

def menu_select(prompt, menu_dict):
    '''
    provides user with prompt, sends their response to a clean-up
    function which compares it against a library of expected responses
    and returns the key the program needs to proceed (or 'invalid' if
    no key is present, which re-iterates the loop), then directs the
    workflow to the function corresponding to the user input.
    '''
    while True:
        response = clean_input(prompt, menu_dict)
        if type(response) is str:
            if response == 'invalid':
                os.system('clear')
                print('\nInvalid Input.  Try Again.\n')
            else:
                break
        else:
            response = response(donors)
        if response == 'back':
            break

def clean_input(prompt, menu_dict):
    '''
    Grants greater flexibility in user input.  Function reads user input
    then compares it against a list of acceptable inputs for each
    function response, then returns the exact response the calling
    function is looking for.
    '''
    usr_input = str(input(prompt))
    for key, value in menu_dict.items():
        if usr_input.lower() in value:
            return key
    return 'invalid'

def send_thanks(donors):
    '''
    Sub-menu for the 'send_thanks' main menu option.  Functions similar
    to main menu.
    '''
    os.system('clear')
    menu_select(send_prompt, send_dict)
    os.system('clear')

def add_donation(donors):
    '''
    Prompts user for a donor name and donation amount, checks
    the inputs to verify they are as expected and not 'back-out' words
    (which would return to main menu).  Script then prints the thank you
    message for the donation on the terminal screen, prompting the user
    to verify it is correct (a 'no' answer erases the input and
    re-prompts).  Upon user verification, the donor/donation information
    is saved to the donors dictionary and a thank you .txt file
    generated (along with a Thank_Yous directory, if necessary).
    
    A 'back-out' word at any prompt will exit and return to main menu
    '''
    while True:
        who = str(input("Name of Donor: ")).title()
        if who.lower() in back_outs:
            os.system('clear')
            return 'back'
        while True:
            amount = input("Donation Amount: $")
            if amount.lower() in back_outs:
                os.system('clear')
                return 'back'
            try:
                amount = float(amount)
            except ValueError:
               print('Invalid Input.  Needs to be a dollar amount.\n')
               continue
            break
 
        message = thanks_message(who, amount)
        print('\nMessage Will Read:\n\n' + 53 *'-' + '\n' +
              message + '\n'+  '-' * 53 + '\n')
        correct = input('Is this correct? (yes/no): ')
        if 'n' in correct:
            print('Record erased.  Resetting Form...\n')
            print('\n')
            continue
        elif correct in back_outs:
            os.system('clear')
            return 'back'
        donors.setdefault(who, []).append(amount)
        write_letter(who, amount)
        print('\nLetter written and saved at:\n'
              + os.getcwd() + 'Thank_Yous\n')
        return 'back'

def write_letter(who, amount):
    '''
    Establishes a proposed file name using the donor name (who) and
    donation (amount).  Searches the 'Thank_Yous' directory (which it
    creates in the cwd if not present) for that file name.  If it
    doesn't exist, it saves the thank you message text into a .txt file
    named with the proposed name.  If the file already exists, the
    number at the end of the file name is incremented, and searched as
    a new proposed file name.
    '''
    mkdir('Thank_Yous')

    # Make new letter file in 'Thank Yous' directory
    i, valid = -1, False
    # Find a valid, unique file name in Thank Yous directory
    # i.e. - one that does not exist yet, but is predictable for testing
    while valid == False:
        i += 1
        valid = False if (f'{who}_{amount:,.2f}_{i}.txt') in os.listdir('Thank_Yous') else True
    with open(f'Thank_Yous/{who}_{amount:,.2f}_{i}.txt', 'w') as writefile:
        writefile.write(thanks_message(who, amount))
    writefile.close()

def mkdir(name):
    '''
    Attempts to create a new directory within the cwd with the name
    provided.  If present, the function is aborted.  If not present,
    the directory is now created and permanently available for use - at
    least until specifically deleted by user from the cwd.
    '''
    try:
        os.mkdir(name)
    except FileExistsError:
        pass

def thank_all_donors(donors):
    '''
    Iterates through entire donor dictionary, generating a thank you
    .txt file for each donor's most recent donation in the 'Thank_Yous'
    directory.  Prints the location of the 'Thank_Yous' directory on
    the terminal screen.
    '''
    for i in donor_list(donors):
        write_letter(i, donors[i][-1])
    print('\nLetters written and available to view/print in:\n'
           + os.getcwd() + '/Thank_Yous\n')

def view_donors(donors):
    '''
    Simply prints the names of each of the current donors to the
    terminal.
    '''
    print('\nExisting Donors:')
    for i in donor_list(donors):
        print ('\t' + i)
    print()

def donor_list(donors):
    '''
    Extracts the donor names from the global donors dictionary.
    '''
    return list(donors.keys())

def thanks_message(who, amount):
    '''
    Generates the text for the thank you message.  Used for terminal
    and letter when called by those respective programs.
    '''
    amount = float(amount)
    message = (f'Dear {who},\n'
                '\n'
                '\tThank you for your generous donation of '
               f'${amount:,.2f}'
                '\n toward our cause.  It is very appreciated.\n'
                '\n'
                'Sincerely,\n'
                'Local Charity Inc.\n')
    return message

def view_report(donors):
    '''
    Formats and prints a table with the donor name, total donation,
    number of donations, and average donation to the terminal screen
    (sorted by most generous donor)
    '''
    os.system('clear')
    rows = table_rows(donors)
    header = '| Donor Name' + ' ' * 9 + '|  Total Given  | Gifts |  Average Gift  |'
    linebreak = '|' + '-' * 20 + '|---------------|-------|----------------|'
    endline = '|' + 20 * '_' + '|' + '_' * 15 + '|' + '_' * 7 + '|' + '_' * 16 + '|'
    
    print(header)
    print(linebreak)
    for i in range(len(rows)):
        print('|{:.<20}|${:>13,.2f} | {:^5d} | ${:12,.2f}  |'.format(*rows[i]))
    print(endline)

def table_rows(donors):
    '''
    Creates a list with the rows used for a donor report and sorts
    by total donation amount.
    '''
    don_names = [name for name in donors]
    net_dons = [float(sum( x for x in donors[name])) for name in donors]
    num_dons = [int(len(donors[name])) for name in donors]
    avg_dons = [net_dons[i]/num_dons[i] for i in range(len(don_names))]
    report_rows = [(name, total, gifts, avg) for name, total, gifts, avg in zip(don_names, net_dons, num_dons, avg_dons)]
    # Sort rows by total donation amount
    report_rows = sorted(report_rows, key=lambda x: x[1], reverse=True)
    return report_rows

def exit_program(donors):
    '''
    Clears screen, gives exit message, and exits.
    '''
    os.system('clear')
    print('\n-----Mailroom version 4.0----')
    print('\nEXITING MAILROOM 4... and Goodbye.\n')
    sys.exit()


# List of values that will universally return to menu or quit
back_outs = ['back', 'exit', 'quit', 'q', 'end', 'clear']

# Initial donor data for script
donors = {'Bill Turner': [1500.99, 3500, 800.25],
          'Jack Yelb': [145.72, 1350.25],
          'Kelly Jones': [250.00, 57.00],
          'Mark Tomles': [600.00],
          'Guido Roccio': [1153.90, 47.15],
          'Mary Jaco': [27500.00],
         }
         
# Main menu prompt
main_prompt = ('------Mailroom version 4.0------\n'
               '\nMAIN MENU:\n'
               '[1] Thank Donor(s)\n'
               '[2] View Donor Report\n'
               '[3] Quit\n'
               '\nYou may input "back" at any \n'
               'input to return here.\n\n'
               'What would you like to do?: '
              )

# dictionary of acceptable inputs for prompt
main_disp = {send_thanks: ['thank',
                           '1',
                           'thank donor',
                           'thank donors',
                           'thank donor(s)'
                           'thank you',
                           'thank yous',
                          ],
             view_report: ['view',
                           'donor',
                           'report',
                           '2',
                           'view report',
                           'view donor report'
                           'donor report'
                          ],
             exit_program: ['3'] + back_outs
            }

# Dispatch disctionary for 'Send Thanks' sub-menu
send_prompt = ('------Mailroom version 4.0------ \n\n'
               'SEND THANKS MENU\n'
               '[1] Record New Donation & Thank\n'
               '[2] Send Letter to All Donors\n'
               '[3] View List of Donors\n'
               '[4] Back to Main Menu\n\n'
               'What would you like to do?: '
              )

# Dictionary of acceptable inputs for 'Send Thanks' sub-menu
send_dict = {add_donation: ['record',
                            'new',
                            'donation',
                            'thank',
                            'record new donation',
                            'new donation',
                            'record new donation and thank',
                            'record new donation & thank',
                            '1'
                           ],
             thank_all_donors: ['send letter to all donors',
                               'send letters',
                               'send to all',
                               'letters',
                               'letter',
                               'send to all',
                               'send to all donors',
                               'thank all donors',
                               '2'
                               ],
             view_donors: ['view',
                           'list',
                           'donors',
                           'view list',
                           'view list of donors',
                           '3'
                          ],
             'back': ['main',
                      'menu',
                      'main menu',
                      '4',
                     ] + back_outs
             }

# main script start
if __name__ == '__main__':
    os.system('clear')
    menu_select(main_prompt, main_disp)
    exit_program()
