#!/usr/bin/env python3

import sys
import os
import time

def menu_select(prompt, menu_dict):
    '''
    Provides the menu prompts for the user to select.  Allows flexible
    prompts and actions
    '''
    while True:
        response = clean_inp(prompt, menu_dict)
        if type(response) is str:
            if response == 'invalid':
                print('\nInvalid Input.  Try Again.')
            else:
                break
        else:
            response = response()
        if response == 'back':
            os.system('clear')
            break

def clean_inp(prompt, menu_dict):
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
    os.system('clear')
    return 'invalid'

def send_thanks():
    '''
    Provides a sub-menu with option to add a donation and draft thank
    you letters to individual/all donors.
    
    added terminal 'clear' to beginning and end to make things cleaner
    '''
    os.system('clear')
    menu_select(send_prompt, send_dict)
    os.system('clear')

def view_report():
    '''
    Terminal screen is cleared for visual clarity first, then the
    header block of the report is generated.
    
    The donor relevant donor information (name, total donation amount,
    number of donations, and average donation) are extracted from the
    global donors dictionary and stored as tuples in a list of the
    information in each row of the table we are creating.  Each tuple
    from this list is fed into a formatted print which prints the line
    on the terminal screen for viewing.
    
    The user is then asked if they would like to save the report.  A
    'yes' answer will result in the report being saved as a unique .txt
    file using the ASCI time code as its unique identifier.  A directory
    for reports is generated if not present in the cwd for the resulting
    file to be stored.
    
    The user is then asked if they would like to send a thank you letter
    to each of the donors in the report.  A 'yes' response generates
    a series of unique .txt files, one for each donor, saved in a
    directory within the cwd.  The user is held on this screen until
    they press ENTER so they may review the output of the program before
    the terminal screen is cleared.
    
    A 'back' response at any prompt will return the user to the main
    menu.
    '''
    os.system('clear')
    # Establish standard header strings
    header = 'Donor Name          |  Total Given  | Gifts |  Average Gift  |'
    linebreak = ('-' * 20 + '|' + '-' * 15 + '|' + '-' * 7 + '|' + '-' * 16 + '|')
    
    # Separate donor info from dictionary list with tuple for each row
    don_names = [name for name in donors]
    net_dons = [sum( x for x in donors[name]) for name in donors]
    num_dons = [len(donors[name]) for name in donors]
    avg_dons = [net_dons[i]/num_dons[i] for i in range(len(don_names))]
    report_rows = [(name, total, gifts, avg) for name, total, gifts, avg in zip(don_names, net_dons, num_dons, avg_dons)]
    # Sort rows by total donation amount
    report_rows = sorted(report_rows, key=lambda x: x[1], reverse=True)

    # Print the dang report to the terminal screen
    print('\n' + header + '\n' + linebreak)
    for i in range(len(report_rows)):
        print('{:.<20}|${:>13,.2f} | {:^5d} | ${:12,.2f}  |'.format(*report_rows[i]))
    print(linebreak + '\n')
    
    # Save a copy as a text file if user wants
    sav_file = str(input('Would you like to save this report? (yes/no): '))
    if sav_file in back_outs:
        os.system('clear')
        return 0
    elif 'y' in sav_file:
        mkdir('Mailroom_Reports')
        transtable = str.maketrans(' ', '_')
        unique_id = time.asctime(time.localtime(time.time()))
        unique_id = str(unique_id).translate(transtable)
        with open('Mailroom_Reports/Report_' + unique_id + '.txt', 'w') as outfile:
            outfile.write(header + '\n' + linebreak + '\n')
            for i in range(len(report_rows)):
                outfile.write('{:.<20}|${:>13,.2f} | {:^5d} | ${:12,.2f}  |\n'.format(*report_rows[i]))
        outfile.close()
    letters = str(input('Would you like to send letters to all donors? (yes/no): ')).lower()
    if letters in back_outs:
        os.system('clear')
        return 0
    elif 'y' in letters:
        letters2all()
    proceed = input('\npress ENTER to return to menu...')
    os.system('clear')

def exit_program():
    '''
    This function clears the terminal screen, then prints a message
    before exiting the script.  User is left with the program header
    and exit message in the terminal upon exit.
    '''
    os.system('clear')
    print('------Mailroom version 3.0------')
    print('\nEXITING MAILROOM 3... and Goodbye.\n')
    sys.exit()

def write_thanks():
    '''
    Terminal screen is first cleared for visual reasons.  User is then
    asked to give a name and donation amount.  The donation amount is
    checked to make sure it is a number, if not the input is rejected
    and the user is re-prompted.  A thank you message is then printed
    on the terminal screen for review.
    
    The user is then asked if they want to record the donation.  A 'yes'
    response results in the donor and donation being added to the
    global donors dictionary - and a new dictionary entry being added
    if the donor is new.
    
    The user is then asked if they would like to draft a letter.  A
    'yes' response will result in a unique .txt file being generated
    in the cwd.  The file information is displayed for the user and they
    are held on this screen until they hit ENTER, at which point the
    screen is cleared and they are returned to the main menu.
    
    A 'back' response at any prompt will return the user to the main
    menu.
    '''
    os.system('clear')
    print('RECORD NEW DONATION:\n')
    while True:
        who_from = str(input('Name of Donor: ')).title()
        if who_from.lower() in back_outs:
            os.system('clear')
            return 'back'
        while True:
            how_much = input(f'How much did {who_from} donate: $')
            if str(how_much).lower() in back_outs:
                os.system('clear')
                return 'back'
            # Catch non-numerical values for donation amount
            try:
                how_much = float(how_much)
            except ValueError:
                print('\nInvalid Input.  Dollar amount required.\n')
                continue
            break    # Only loop if user made error
        
        # Output message to terminal screen for review
        print('\nThank You Message Will Read:')
        print(thanks_generator(who_from, how_much) + '\n')
        
        add_to = str(input('Shall we record this donation? (yes/no): ')).lower()
        if add_to in back_outs:
            os.system('clear')
            return 'back'
        if 'n' in add_to:    # if user makes mistake they'll say "no"
            print('\nNew donation record deleted.\n')
            continue
        donors.setdefault(who_from, []).append(how_much)
        
        # User is asked if they would like the message output to a
        # .txt file.  If 'yes' one is created in a Thank_Yous directory
        # in the cwd.
        letter = str(input(f'Would you like to draft a letter to {who_from}? (yes/no): ')).lower()
        if letter in back_outs:
            os.system('clear')
            return 'back'
        if 'y' in letter:    # Writes thank you message to file.
            write_letter(who_from, how_much)
            print('Letter saved in the ' + os.getcwd() + '/Thank_Yous directory.')
        break    # Loop only if user cancels the input
    proceed = input('press ENTER to continue...')
    os.system('clear')
    return 'back'
    
def thanks_generator(to_whom, how_much):
    '''
    Uniform text used for both the terminal output and the .txt file
    outputs.
    '''
    return (f'Dear {to_whom},\n'
             '\n'
            f'\tThank you for your generous ${how_much:,.2f} '
             'donation toward our cause.\n'
             '\n'
             'Sincerely,\n'
             'Our Charity'
           )

def write_letter(to_whom, how_much):
    '''
    Creates a unique .txt file to the given recipient thanking them
    for their gift and places it inside a "Thank_Yous" directory within
    the cwd of the script.

    Each letter .txt file is made to be unique by attaching a time stamp
    to the file name (ASCI format except '_' in place of spaces)
    so multiple letters can be written to the same person without
    "cleaning up" the Thank_Yous directory.
    '''
    mkdir('Thank_Yous')
    transtable = str.maketrans(' ', '_')
    unique_id = time.asctime(time.localtime(time.time()))
    unique_id = (to_whom + '_' + str(unique_id).translate(transtable))
    outfile = open('Thank_Yous/' + unique_id + '.txt', 'w')
    outfile.write(thanks_generator(to_whom, how_much))
    print(f'Letter to {to_whom} for ${how_much:,.2f} written')

def mkdir(dir_name):
    '''
    Creates a new directory in cwd with the prescribed name if not
    already present there.
    '''
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass

def donor_list():
    '''
    Prints a list of the current donors in case user wants it for
    whatever reason.
    
    Does not clear terminal screen.  I am assuming the user wants the
    donor list visible as a reference.
    '''
    os.system('clear')
    print('\nEXISTING DONORS:')
    for i in donors.keys():
        print('\t' + i)
    print()

def letters2all():
    '''
    Drafts letters as text files for all donors.  Can be toggled
    by user to thank them for their last donation, or for the total
    sum of their donations.
    
    User can type any of the 'bail_out' terms to return to main menu.
    This is why the function is written inside a single-run while loop;
    it's a quick'n'dirty way to get it to bounce back to the main menu
    instead of quitting entirely when a 'bail-out' term is given.
    '''
    while True:
        thank_scope = str(input('Thank for all donations? (yes/no): ')).lower()
        if thank_scope in back_outs:
            os.system('clear')
            return 'back'
        if 'y' in thank_scope:
            os.system('clear')
            print('\nDonors will be thanked for all of their donations.\n')
        for name, dons in donors.items():
            amount = 0
            if thank_scope:
                for i in dons:   # sum donations if user said 'yes' above
                    amount += i
            else:
                amount = dons[-1]
            write_letter(name, amount)
        print('\nAll letters saved in the "' + os.getcwd() + '/Thank_Yous" directory.\n')
        break
    proceed = input('press ENTER to return to menu...')
    return 'back'

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
main_prompt = ('------Mailroom version 3------\n'
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
send_prompt = ('------Mailroom version 3.0------ \n\n'
               'SEND THANKS MENU\n'
               '[1] Record New Donation & Thank\n'
               '[2] Send Letter to All Donors\n'
               '[3] View List of Donors\n'
               '[4] Back to Main Menu\n\n'
               'What would you like to do?: '
              )



# Dictionary of acceptable inputs for 'Send Thanks' sub-menu
send_dict = {write_thanks: ['record',
                            'new',
                            'donation',
                            'thank',
                            'record new donation',
                            'new donation',
                            'record new donation and thank',
                            'record new donation & thank',
                            '1'
                           ],
             letters2all: ['send letter to all donors',
                           'send letters',
                           'send to all',
                           'letters',
                           'letter',
                           'send to all',
                           'send to all donors',
                           'thank all donors',
                           '2'
                          ],
             donor_list: ['view',
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

if __name__ == '__main__':
    os.system('clear')
    menu_select(main_prompt, main_disp)
