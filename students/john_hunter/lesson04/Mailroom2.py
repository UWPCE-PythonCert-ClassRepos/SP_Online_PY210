#!/usr/bin/env python3
#----------------------------------------#
#Python 210
# Assignment04: mailroom2.py
# Desc: Allows a user to read, and update a list of donors and thier donations.
#       Allows the user to generate a thank you email or report on historical
#       summaries of the donors activities.
# Change Log:
# Johnh, 2020-Nov-22 Script Created
# Johnh, 2020-Nov-22 Updated menu selection with dictionary variable type
# Johnh, 2020-Nov-23 Modified user email print to use .format()
# Johnh, 2020-Nov-23 Initial debugging, code running again after updates
# Johnh, 2020-
# Johnh, 2020-
# Johnh, 2020-
# Johnh, 2020-
# Johnh, 2020-
#----------------------------------------#

#import time
import sys
import pathlib
from operator import itemgetter

path = pathlib.Path("./")
path.is_dir()
path.absolute()

#the basic data structure now uses the donor's name as the key with a list for the donation values
donors =	{'frank merriweather' : [10, 15, 100], 'thomas tran' : [5, 17, 23],
          'stephanie terrance' : [31, 48, 108], 'sam robidas': [4, 90, 101],
          'sandy cohen' : [29, 41, 70], 'shioban kemp' : [2, 23000, 19]}
#the menu options are now held in a dictionary which we can "switch" on for the user selection
options = {1 :'Send a Thank You', 2 : 'Report', 3 : 'Send Thank You to all Donors', 4 : 'Exit'}

def menu_prompt(options):
    """Basic UI to prompt user and handle selections

    Returns: 'entry' a string with value 1, 2, 3, or 4 selected by the user
    """
    print('Enter \'exit\' at anytime to quit')
    print('Select the Menu Option by Number')

    for key in options:
        print(str(key)+'. '+ options[key])

    entry = input('enter option by number:')

    if entry == 'exit':
        quit_it()
    if not entry.isnumeric() or int(entry) < 1 or int(entry) > 4:
        print('You must select a number 1, 2, 3, or 4.')
        menu_prompt()
    else:
        print('You have selected ' + options[int(entry)])

    return entry

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

        names = donor_list_format(donors)
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
        mas_donations = 'Would you like to add more donations for ' + input_named + '? y/n: '
        if list_or_not == 'y':
            more_donations = input(mas_donations)
        if more_donations == 'y':
            donors[input_name] = donors[input_name] + add_donations(input_name, list_or_not)
        elif more_donations == 'n':
            break
        else:
            pass

    totals = 0
    for z in range(len(donors[input_name])):
        totals = totals + int(donors[input_name][z])

    print(email_text(input_name, totals))

def order(total):
    """
    key method for the sorted function needed to show the donors in order by total donations
    input variable is the pairing of a donor and list of donations
    Return the sum of the donations
    """
    return sum(total)

def donor_list_format(donor_list):
    """
    enables the formatting of the donor list by finding the longest name
    Returns the maximum length of all the names and the list of names
    """
    max_len_name = 0
    names = list()
    for key in donor_list:
        names.append(key)
        if len(key) > max_len_name:
            max_len_name = len(key)

    return [max_len_name, names]

def run_report():
    """
    Collects remaining formatting and prints an ordered list of te donors by donation total
    """
    max_len_of_name = 0
    for key in donors:  #get max length of any donor's name
        if len(key) > max_len_of_name:
            max_len_of_name = len(key)

    print_order = list(donors.items())
    print_ordered = list()
    for i in range(len(print_order)):
        print_ordered.append([print_order[i][0], sum(print_order[i][1][:])])

    print_order = sorted(print_ordered, key=itemgetter(1), reverse=True)

    print('{:{align}{width}}'.format('Donor Name', align='^', width=max_len_of_name) \
          +' | Total Donations | Number of Donations | Avg Donation')
    print('-'*max_len_of_name + '-------------------------------------------------------')
    for donor in print_order:
        total = donor[1]
        number = len(donors[donor[0]])
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
        donors[name] = []
    while True:
        donation = int(input('Enter a donation amount, enter \'0\' for no donation: '))
        if donation == 0:
            break
        elif list_or_not == 'n':
            donors[name].append(donation)
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
    f"Thank you for your generous donation(s) of ${total:,d}\n"
    "\n"
    "Sincerly,\n"
    "John Hunter\n")
    return email

def save_emails():
    """
    saves the emails by donor to the directory location
    """
    for key in donors:
        total = sum(donors[key])
        with open(f"{key}.txt", "w") as location:
            location.write(email_text(key, total))

def quit_it():
    """
    offers the user a quick exit from the script
    """
    sys.exit(0)

def main():
    """main"""
    while True:
        entry = menu_prompt(options)
        if entry == '1':
            send_ty()
        elif entry == '2':
            run_report()
        elif entry == '3':
            save_emails()
        elif entry == '4':
            quit_it()
    if __name__ == '__main__':
        True
main()
