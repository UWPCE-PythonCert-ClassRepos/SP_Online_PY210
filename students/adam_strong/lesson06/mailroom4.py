#!/usr/bin/env python3
# Mailroom4.py - Lesson06 Assignment - Unittesting with Pytest

import sys
import pathlib

donor_db = {"Scrooge McDuck": [8000.00, 70000.00],
            "Montgomery Burns": [49.53],
            "Richie Rich": [1000000.00, 500000.00],
            "Chet Worthington": [200.00, 44387.63, 10200.00],
            "Silas Skinflint": [0.25, 1.00, 0.43]}

main_prompt = "\n".join(("", "Welcome to the donors list",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Send a letter to all the donors",
          "4 - Quit",
          "Type a number to select >>> "))

ty_prompt = "\n".join(("", "Please type the full name of the donor OR",
        "type 'list' to see a list of donors",
        "Type input here >>>"))

ty_message = "\n".join(("", "Dear {}",
        "Thank you for your generous donation of {:.2f}",))

letter = "\n".join(("", "Dear {},","",
        "    Thank you for your very kind donations totaling ${:.2f}.","",
        "    It will be put to very good use.","",
        "               Sincerely,",
        "                  - The team"))

def exit_program():
    '''Exit the program - TESTED'''
    print('\nShutting down the program\n')
    sys.exit()

# THANK YOU LOGIC -------------------------------------------------------------------

def thank_you():
    ''' Main thank_you logic'''
    tyname = input(ty_prompt)
    list_invoked(tyname)
    amt = input("Please enter the donation amount >>>")
    amt_logic(tyname, amt)

def amt_logic(tyname, amt):
    '''Validates the amount - TESTED'''
    try:
        amt = float(amt)
    except ValueError:
        print('\n--->Not a valid amount, please try your submission again')
    else:
        ty_logic(tyname,amt)

def ty_logic(tyname, amt):
    '''Adds the new names and generates a message - TESTED'''
    if donor_db.get(tyname) is None:
        donor_db[tyname] = [amt]
    else:
        donor_db.get(tyname).append(amt)
    print(ty_message.format(tyname, amt))
    print('')

def list_invoked(tyname):
    '''Checks if list is entered - TESTED'''
    if tyname == 'list':
        report()
    else:
        return tyname

# REPORT LOGIC ---------------------------------------------------------------------

def report():
    '''Checks validity of report - TESTED'''
    print('')
    head = '{:20}| {:>15}|{:>15}| {:>15}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift')
    print(head)
    print('-'*72)
    for key,value in sorted(donor_db.items(),key=lambda i:sum(i[1]),reverse=True):
        line = '{:20} ${:>15.2f}  {:>15}  ${:15.2f}'.format(key, sum(value),len(value), (sum(value)/len(value)))
        print(line)
    print('')

    if __name__ == '__main__':
        main()
    else:
        return

def write_letter(key,value):
    '''Writes an individual letter - TESTED'''
    form_letter = letter.format(key, sum(value))
    return form_letter

def send_letter():
    '''Writes files for the user'''
    for key,value in sorted(donor_db.items(),key=lambda i:sum(i[1]),reverse=True):
        create_text_file(key,value)


def create_text_file(key,value):
    '''Creates the thank you file for a specific person - TESTED'''
    form_letter = write_letter(key,value)
    file_name = key.replace(" ", "_") + ".txt"
    pth = pathlib.Path('./')
    dest = pth.absolute() / file_name
    with open(dest, 'w') as outfile:
        outfile.write(form_letter)  

# MENU LOGIC --------------------------------------------------------------------------

def main_switch(response):
    '''Main logic from response menu - TESTED'''
    try:
        switch_func_dict.get(int(response))()
    except (ValueError,TypeError):
        print('\n----> Invalid Selection: Please input a number 1-4')

# Switch function dict
switch_func_dict = {
    1: thank_you,
    2: report,
    3: send_letter,
    4: exit_program,
}

################## PRIMARY CODE BLOCK ######################################################


def main():
    while True:
        response = input(main_prompt)
        main_switch(response)

if __name__ == '__main__':
    # Guards against running automatically if this script is imported
    main()
    