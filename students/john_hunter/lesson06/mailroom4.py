#!/usr/bin/env python3
#----------------------------------------#
#Python 210
# Assignment04: mailroom3.py
# Desc: Allows a user to read, and update a list of donors and thier donations.
#       Allows the user to generate a thank you email or report on historical
#       summaries of the donors activities.
# Change Log:
# Johnh, 2020-Dec-22 Script Created
# Johnh, 2020-Dec-25 Added try except blocks
# Johnh, 2020-Dec-28 Add list comprhensions
# Johnh, 2020-Dec-29 Testing
#----------------------------------------#

#import time
import sys
import pathlib
from operator import itemgetter

PATH = pathlib.Path("./")
PATH.is_dir()
PATH.absolute()

#the basic data structure now uses the donor's name as the key with a list for the donation values
DONORS =	{'frank merriweather' : [10, 15, 100], 'thomas tran' : [5, 17, 23],
          'stephanie terrance' : [31, 48, 108], 'sam robidas': [4, 90, 101],
          'sandy cohen' : [29, 41, 70], 'shioban kemp' : [2, 23000, 19]}
#the menu options are now held in a dictionary which we can "switch" on for the user selection


def menu_prompt(options):
    """Basic UI to prompt user and handle selections

    Returns: 'entry' a string with value 1, 2, 3, or 4 selected by the user
    """
    display_options = {1 :'Send a Thank You', 2 : 'Report', 3 \
                       : 'Send Thank You to all Donors', 4 : 'Exit'}

    print('Enter \'exit\' at anytime to quit')
    print('Select the Menu Option by Number')

    for key in display_options:
        print(str(key)+'. '+ display_options[key])

    while True:
        entry = input('enter option by number:')
        try:
            if entry == 'exit':
                quit_it()
            entry = int(entry)
            options[entry]()
            menu_prompt(options)
        except KeyError:
            print("\nPlease choose from 1, 2, 3, or 4")
            break

def send_ty():
    """Returns the text of the email with the donor name, description of the
    donations
    Prompts to enter a 'Full Name' or list, if the name is not part of the
    list, then add that name to the list of donors and use the name
    Prompt for a donation amount, type as a number and enter into the dictionary
    Generate the Email thanking the donor, print it to terminal
    return to the prompt
    """
    #Provide for the possible need to format a list of the Donor names, length
    #sorted in donor list format function
    #provide for the need to sort by donation total as well
    names = list()

    while True:
        input_named = str(input('Enter full name of donor or \'list\' to request list of donors: '))
        input_named = input_named.lower()
        names = donor_list_format(DONORS)
        valid_values = list(DONORS.keys()) + ['list', 'List', 'exit', 'Exit']
        """
        try:
            x = valid_values.index(input_named)
            print('You selected ' + valid_values[x])
        except ValueError:
            print('Please choose one of the following:')
            for value in valid_values:
                if (value == 'exit') or (value == 'list'):
                    continue
                print(value.title())
            continue
        """
        if input_named == 'list':
            print('List of Current Donors')
            for key in names[1]:
                print('{:{align}{width}}'.format(key.title(), align='<', width=names[0]))
            continue
        if input_named == 'exit':
            quit_it()
        input_name = input_named.lower()
        if input_name in names[1]:
            list_or_not = 'y' #local variable which tracks whether the user
            # provided name is on the list of donors or not
            break
        else:
            list_or_not = 'n'
        if list_or_not == 'n':
            add_donor(input_name)
            list_or_not = 'n'
            more_donations = 'n'
            break

    while True:
        local_options = ['n', 'y']
        mas_donations = 'Would you like to add more donations for ' + input_named.title() + '? y/n: '
        if list_or_not == 'y':
            more_donations = input(mas_donations)
            try:
                more_donations = more_donations.lower()
                yes_no = local_options.index(more_donations)
            except ValueError:
                print('The only valid entries are \'y\' and \'n\'')
                continue
        if more_donations == 'y':
            DONORS[input_name] = DONORS[input_name] + add_donations(input_name, list_or_not)
        elif more_donations == 'n':
            break
        else:
            pass

    totals = 0
    totals = [int(DONORS[input_name][z]) for z in range(len(DONORS[input_name]))]
    totals_sum = sum(totals[:])
    print(email_text(input_name, totals_sum))
"""
def order(total):#Not being used
"""
    #key method for the sorted function needed to show the donors in order by total donations
    #input variable is the pairing of a donor and list of donations
    #Return the sum of the donations
"""
    return sum(total)
"""
def donor_list_format(donor_list):
    """
    enables the formatting of the donor list by finding the longest name
    Returns the maximum length of all the names and the list of names
    """
    max_len_name = 0
    names = list()

    names = [key for key in donor_list]
    max_len_name = [len(key) for key in donor_list]
    max_len_name1 = max(max_len_name)

    return [max_len_name1, names]

def run_report():
    """
    Collects remaining formatting and prints an ordered list of te donors by donation total
    """
    max_len_of_name = 0

    for key in DONORS:  #get max length of any donor's name
        if len(key) > max_len_of_name:
            max_len_of_name = len(key)

    print_order = list(DONORS.items())
    print_ordered = list()

    print_ordered = [[print_order[i][0], sum(print_order[i][1][:])] \
                      for i in range(len(print_order))]
    print_order = sorted(print_ordered, key=itemgetter(1), reverse=True)

    print('{:{align}{width}}'.format('Donor Name', align='^', width=max_len_of_name) \
          +' | Total Donations | Number of Donations | Avg Donation')
    print('-'*max_len_of_name + '-------------------------------------------------------')

    for donor in print_order:
        total = donor[1]
        number = len(DONORS[donor[0]])
        average = total/number
        person = donor[0]
        print('{:{align}{width}}'.format(person.title(), align='<', width=max_len_of_name) + \
        ' ' + '{:{align}{width}.0f}'.format(total, align='^', width=17) + \
        ' ' + '{:{align}{width}.5}'.format(str(number), align='^', width=21) + \
        ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=15))

def add_donor(name):
    """
    function receives the value of the new donor's name, and requests that
    donation values values be added for that donor and calls the add donations function
    input variable name is the new donor to be added
    return none
    """
    print('Add a donations for ' + name.title() + ' by entering the values as requested: ')
    list_or_not = 'n'
    add_donations(name, list_or_not)

def add_donations(name, list_or_not):
    """
    adds donations to the selected donor. The donor may be from the initial donors list
    or it could be added by the use
    input variable determines whether the selected donor is on the list already or not
    returns the donations by donor
    """
    donations = list()
    if list_or_not == 'n':
        DONORS[name] = []
    while True:
        donation = input('Enter a donation amount, enter \'0\' for no donation: ')
        try:
            donation = int(donation)
        except ValueError:
            print('Entry must be an integer')
            continue
        if donation == 0 and any(DONORS[name]):
            break
        elif list_or_not == 'n':
            DONORS[name].append(donation)
            continue
        else:
            donations.append(donation)
    return donations

def email_text(full_name, total):
    """
    constructs the email text
    returns the email text
    """
    email = (f"Dear {full_name.title()},\n\n"
    f"Thank you for your generous donation(s) of ${total:,d}.\n"
    "\n"
    "Sincerly,\n"
    "John Hunter\n")
    return email

def save_emails():
    """
    saves the emails by donor to the directory location
    """
    for key in DONORS:
        total = sum(DONORS[key])
        with open(f"{key}.txt", "w") as location:
            location.write(email_text(key, total))

def quit_it():
    """
    offers the user a quick exit from the script
    """
    sys.exit(0)

def main():
    
    options = {1 : send_ty, 2 : run_report, 3 : save_emails, 4 : quit_it}
    while True:
        menu_prompt(options)
    if __name__ == '__main__':
        True
main()
