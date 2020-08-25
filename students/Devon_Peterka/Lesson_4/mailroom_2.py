#!/usr/bin/env python3

import os
import time

def menu_select(prompt, menu_dict, disp):
    '''
    Provides the menu prompts in a loop so script will run until quit
    by user
    '''
    while True:
        response = clean_inp(prompt, menu_dict)
        if response == 'invalid':
            print('Invalid Input.  Try Again.')
            continue
        if disp[response]() == 'quit':
            break

def clean_inp(prompt, menu_dict):
    '''
    Allows greater user input flexibility by comparing the user
    input against a list of acceptable inputs for each program response.
    Then returns the exact response the program is looking for.
    '''
    usr_input = str(input(prompt))
    for key, value in menu_dict.items():
        if usr_input.lower() in value:
            return key
    return 'invalid'

def send_thanks():
    '''
    Provides a sub-menu with option to add a donation (thank someone,
    from part 1 assignment) AND to draft letters per part 2 assignment.
    '''
    menu_select(send_prompt, send_resps, send_disp)

def view_report():
    '''
    Prints the report to terminal and to a .txt file if directed to by
    user.
    
    User is first asked if they want to save the report (to a .txt file)
    The timing is odd, but it makes everything easier this way... for
    me at least.

    If user selects 'yes' then a directory for the reports is created
    in the cwd if not already present and the program outputs text to
    both the terminal screen and a new .txt file.  The .txt file is
    made unique by adding an ASCI time stamp to the file name (with
    spaces replaced with '_') so that multiple report print outs can be
    done without having to purge the Mailroom_Reports directory every
    time.
    
    The donors dictionary is broken out into (3) lists for the names
    of the donors, # of donations from each, and total donations of
    each donor.  The lists are built so the indices all pull data for
    the same donor.  The output table is then built by "popping" the
    data corresponding to the index for the highest donation total
    from all (3) lists (the donation total list being "popped" last
    so we don't get a "moving target"), then repeated with the new,
    shorter lists until the lists are all empty.  This results in a
    table that is sorted by donation amount, from largest to smallest.
    
    Finally, the user is asked if they would like to send letters to
    all donors, for which a 'yes' response will result in a series of
    .txt files with thank you notes for each donor
    
    User can type any of the 'bail_outs' words at any prompt to quit
    program.  This is why this function is built inside a while loop
    even though it will only run once; I probably could have found a
    more elegant way to do it, but this seems to work.
    '''
    while True:
        sav_file = str(input('Would you like to save this report? (yes/no): ')).lower()
        if sav_file in bail_outs:
            break
        sav_file = True if 'y' in sav_file else False
        # making sav_file a bool so it doesn't need to be re-evaluated
        # at each call (one of which occurs inside a proper loop)
        if sav_file:
            mkdir('Mailroom_Reports')
            transtable = str.maketrans(' ', '_')
            unique_id = time.asctime(time.localtime(time.time()))
            unique_id = str(unique_id).translate(transtable)
            outfile = open('Mailroom_Reports/Report_' + unique_id + '.txt', 'w')

        # print table header on terminal for viewing
        header = 'Donor Name          |  Total Given  | # of Gifts |  Average Gift  |'
        linebreak = ('-' * 20 + '|' + '-' * 15 + '|' + '-' * 12 + '|' + '-' * 16 + '|')
        print()
        print(header)
        print(linebreak)

        # create same header in .txt file if user is saving report
        if sav_file:
            outfile.write(header + '\n')
            outfile.write(linebreak + '\n')

        # Break out donor info into separate lists
        net_dons = []    # initialize an empty list for donation sums
        don_names = []    # initialize list of donor names
        num_dons = []    # initialize # donations/donor
        for name, dons in donors.items():
            don_names.append(name)    # populate list of donors
            total = 0
            num_dons.append(len(dons))    # populate list of # of donations
            for i in dons:    # calculate the sum of each donor's gifts
                total += i
            net_dons.append(total)    # populate net_don list for each donor

        # break out names, # donations, and total donations into lists
        while len(net_dons) > 0:
            name = don_names.pop(net_dons.index(max(net_dons)))
            times = num_dons.pop(net_dons.index(max(net_dons)))
            total_gift = net_dons.pop(net_dons.index(max(net_dons)))
            new_line = f'{name:.<20}|${total_gift:>13,.2f} | {times:^10d} | $ {total_gift/times:12,.2f} |'
            print(new_line)    # print for terminal viewing
            if sav_file:    # add same line to output file if writing
                outfile.write(new_line + '\n')
        if sav_file:
            outfile.close()    # Close it if ya opened it
        
        # Ask user if they would like to send letters to all donors
        send_letters = str(input('\nShall we send letters to the donors? (yes/no): ')).lower()
        if send_letters in bail_outs:
            break
        if 'y' in send_letters:
            letters2all()
        break

def write_thanks():
    '''
    Asks for and records new donation information (who and how much)
    then outputs a thank you message to the terminal screen and a .txt
    file if directed to do so by user.
    
    User is prompted to give a name of the donor (recipient of the
    thank you) then an amount to thank them for.  A message is then
    drafted and output to the terminal screen.

    The user is asked if the donation is to be recorded for which a
    'yes' answer will result in the donor/amount being added to the
    global donors dictionary.  If they say 'no' (if they mispelled the
    name, for example) the transaction is deleted and the user is given
    another prompt for a name.

    The user is also asked if they would like to draft a letter to the
    donor.  A 'yes' answer will result in a .txt file being generated
    with the message displayed in the terminal window and saved to the
    "Thank_Yous" directory in the cwd (which is created if not
    present).  A 'no' answer results in the function terminating
    without further action.

    User can type any of the 'bail_out' terms to any prompt to return
    to main menu.
    '''
    while True:
        who_from = input('Whom Shall We Thank?: ')
        who_from = 'back' if who_from.lower() in bail_outs else who_from.title()
        if who_from == 'back':
            return 'quit'    # exit and return to main menu
        how_much = input(f'How much did {who_from} donate?: $')
        if str(how_much).lower() in bail_outs:
            return 'quit'    # exit and return to main menu
        how_much = float(how_much)
        
        # output message to terminal screen
        print('Message Reads:')
        print(thanks_generator(who_from, how_much) + '\n')

        # user asked if the information is correct and to be recorded
        count = str(input('Shall we record this donation? (yes/no): ')).lower()
        if count in bail_outs:
            return 'quit'
        if 'n' in count:    # if user made a mistake, they can abort here
            print('new donation record deleted.')
            continue    # stay in 'Send Thanks' sub-menu
        # Record donation information to global donors dictionary
        donors.setdefault(who_from, []).append(how_much)

        # User is asked if they would like the message output to a
        # .txt file.  If 'yes' one is created in a Thank_Yous directory
        # in the cwd.
        letter = str(input(f'Would you like to draft a letter to {who_from}? (yes/no): ')).lower()
        if letter in bail_outs:
            return 'quit'
        if 'y' in letter:    # writes thank you message to file.
            write_letter(who_from, how_much)
            print('All letters saved in the ' + os.getcwd() + '/Thank_Yous directory.')
        break   # only need to loop if user made a mistake
    return 'quit'    # return to main menu, not 'Send Thanks' sub-menu

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

def donor_list():
    '''
    Prints a list of the current donors in case user wants it for
    whatever reason.
    '''
    print('\nEXISTING DONORS:')
    for i in donors.keys():
        print(i)

def letters2all():
    '''
    drafts letters as text files for all donors.  Can be toggled
    by user to thank them for their last donation, or for the total
    sum of their donations.
    
    User can type any of the 'bail_out' terms to return to main menu.
    This is why the function is written inside a single-run while loop;
    it's a quick'n'dirty way to get it to bounce back to the main menu
    instead of quitting entirely when a 'bail-out' term is given.
    '''
    while True:
        thank_scope = str(input('Thank for all donations? (yes/no): ')).lower()
        if thank_scope in bail_outs:
            return 'quit'
        if 'y' in thank_scope:
            print('\nDonors will be thanked for all of their donations.')
        for name, dons in donors.items():
            amount = 0
            if thank_scope:
                for i in dons:   # sum donations if user said 'yes' above
                    amount += i
            else:
                amount = dons[-1]
            write_letter(name, amount)
            print('All letters saved in the ' + os.getcwd() + '/Thank_Yous directory.')
        break

def back_out():
    '''
    returns Ye Olde Magic 'quit' response
    '''
    return 'quit'

def mkdir(dir_name):
    '''
    creates a new directory in cwd with the prescribed name if not
    already present there.
    '''
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        return 0

# list of values that will universally return to menu or quit
bail_outs = ['back', 'exit', 'quit', 'q', 'end', 'clear']
    # clear is in there because sometimes I attempt to clear my terminal screen prematurely.

# initial donor data for script
donors = {'Bill Turner': [1500.99, 3500, 800.25],
          'Jack Yelb': [145.72, 1350.25],
          'Kelly Jones': [250.00, 57.00],
          'Mark Tomles': [600.00],
          'Guido Roccio': [1153.90, 47.15],
          'Mary Jaco': [27500.00],
         }

# main menu prompt
main_prompt = ('\nMAIN MENU:\n'
               '[1] Thank Donor(s)\n'
               '[2] View Donor Report\n'
               '[3] Quit\n'
               'you may input "back" at any input to return here.\n\n'
               'What would you like to do?: '
              )

# dictionary of acceptable inputs for prompt
main_resps = {'send': ['thank',
                       '1',
                       'thank donor',
                       'thank donors',
                       'thank donor(s)'
                      ],
             'view': ['view',
                      'donor',
                      'report',
                      '2',
                      'view report',
                      'view donor report'
                     ],
             'quit': ['3'] + bail_outs
            }

# dispatch dictionary for main menu
main_dispatch = {'send': send_thanks,
                 'view': view_report,
                 'quit': back_out
                }

# dispatch disctionary for 'Send Thanks' sub-menu
send_prompt = ('\nSEND THANKS MENU\n'
               '[1] Record New Donation & Thank\n'
               '[2] Send Letter to All Donors\n'
               '[3] View List of Donors\n'
               '[4] Back to Main Menu\n\n'
               'What would you like to do?: '
              )

# dictionary of acceptable inputs for 'Send Thanks' sub-menu
send_resps = {'new': ['record',
                      'new',
                      'donation',
                      'thank',
                      'record new donation',
                      'new donation',
                      'record new donation and thank',
                      'record new donation & thank',
                      '1'
                     ],
              'letter': ['send letter to all donors',
                         'send letters',
                         'send to all',
                         'letters',
                         'letter',
                         'send to all',
                         'send to all donors',
                         'thank all donors',
                         '2'
                        ],
              'list': ['view',
                       'list',
                       'donors',
                       'view list',
                       'view list of donors',
                       '3'
                      ],
              'quit': ['main',
                       'menu',
                       'main menu',
                       '4',
                      ] + bail_outs
             }

# dispatch menu for 'Send Thanks' sub-menu
send_disp = {'new': write_thanks,
             'letter': letters2all,
             'list': donor_list,
             'quit': back_out
            }

if __name__ == '__main__':
    print('\nWelcome to Mailroom')
    menu_select(main_prompt, main_resps, main_dispatch)
