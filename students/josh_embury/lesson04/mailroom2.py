#!/usr/bin/env python3
# ------------------------------------------------------------------------ #
# Title: Mailroom 2
# Description: Updating mailroom script using dicts and IO files

# ChangeLog (Who,When,What):
# JEmbury,12/12/2020,Created started script
# JEmbury, 12/15/2020, Updated script per notes from CRobinson
# ------------------------------------------------------------------------ #

# Data
#-----------------------------------------------#
dict_donor_table = {
'Henry Henrickson' : [10, 500, 25],
'Geraldo Duckworth' : [76],
'Galileo Humpkins' : [22000, 100, 490],
'Methusela Honeysuckle' : [18, 69, 76000],
'Lavender Goombs' : [55000, 25],
}
#-----------------------------------------------#
# IO methods
#-----------------------------------------------#
def show_menu():
    # shows user list of options
    # return is void
    """  Display a menu of choices to the user
    :return: nothing
    """
    print('''
    Menu of Options
    1) Send a Thank You to a single donor
    2) Create a Report
    3) Send letters to all donors
    4) Quit
    ''')
    print()  # Add an extra line for looks
def get_user_choice():
    # asks user for choice
    # returns integer value of user's choice
    """ Gets the menu choice from a user
    :return: string
    """
    choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
    print()  # Add an extra line for looks
    return choice

def send_thank_you():
    donor = input('Please enter full name of donor >>> ')
    new_donation = int(input('Please enter the donation amount >>> '))
    if donor in dict_donor_table.keys():
        dict_donor_table[donor].append(new_donation)
    else:
        dict_donor_table[donor] = [new_donation]
    print(thank_you_letter(donor, new_donation))

def write_to_file(input_dict):
    for key in input_dict.keys():
        #print(thank_you_letter(key,get_donor_data(input_dict[key])[0]))
        with open(key + '.txt', 'w') as new_file:
            new_file.write(thank_you_letter(key, get_donor_data(input_dict[key])[0]))
        new_file.close()
#-----------------------------------------------#
# Processing methods
#-----------------------------------------------#
def get_donor_data(lst_gifts):
    # input is a list of donor gift history
    # output is list data in format:
    # [Sum of gifts, num of gifts, average gift amount]
    return [sum(lst_gifts), len(lst_gifts), sum(lst_gifts)/len(lst_gifts)]

def thank_you_letter(donor, amount):
    str_thankyou = f'Dear {donor},\n'\
    f'    Thank you so much for the generous gift of {amount} dollars. '\
    'This donation is going to help us so much for so many reasons. '\
    'You are incredibly nice and are obviously an outstanding person.\n'\
    '    If you are able to make any further donations please feel free '\
    'to access the Python Donation console application. \n'\
    'Sincerely,\n'\
    'The Python Development Team'
    return str_thankyou

def sums_donor_table(dict_input):
    copy_donor_table = dict_input.copy()
    donor_table_sums = {}
    for item in copy_donor_table:
        donor_table_sums[item] = sum(copy_donor_table[item])
    return donor_table_sums

def format_row(info_list):
    return '{:<26} {:<2} {:10.2f} {:>11} {:^2} {:10.2f}'.format(info_list[0], info_list[1], info_list[2], info_list[3], info_list[4], info_list[5])

def create_report():
    header = '{:<25} {:^10} {:^10} {:^10}'.format('Donor Name', '| Total Given', '| Num Gifts', '| Average Gift')
    print(header)
    print('------------------------------------------------------------------')
    dict_sums = sums_donor_table(dict_donor_table)
    n = 0
    while(n < len(dict_donor_table)):
        for item in dict_sums:
            if dict_sums[item] == max(dict_sums.values()):
                current_donor = item
        del dict_sums[current_donor]
        donor_data = get_donor_data(dict_donor_table[current_donor])
        new_row = [current_donor, '$', donor_data[0], donor_data[1], "$", donor_data[2]]
        print(format_row(new_row))
        n += 1

def send_letters():
    write_to_file(dict_donor_table)# invoke write method with dict

def quit_program():
    exit()# break out of while loop
dictMenu = {
    1: send_thank_you,
    2: create_report,
    3: send_letters,
    4: quit_program
}
#-----------------------------------------------#
# Main
#-----------------------------------------------#
if __name__ == '__main__':
    while(True):
        show_menu()  # Displays menu to console
        dictMenu.get(int(get_user_choice()))()  # Get menu option by dict switch
