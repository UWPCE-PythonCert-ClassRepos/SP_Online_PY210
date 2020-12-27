#!/usr/bin/env python3

#John Hunter
#Python210 Lesson 3 Mailroom

import sys

## Donors in the global namespace

donors = [['Frank Merriweather', 10, 15, 100], ['Thomas Tran', 5, 17, 23], \
          ['Stephanie Terrance', 31, 48, 108], ['Sam Robidas', 4, 90, 101], \
          ['Sandy Cohen', 29, 41, 70], ['Shioban Kemp', 2, 23000, 19]]

def user_selection():
    """Basic UI to prompt user and handle selections

    Returns: 'entry' a string with value 1, 2, or 3 selected by the user
    """
    options = ('Send a Thank You', 'Create a Report', 'quit')
    print('Enter \'exit\' at anytime to quit')
    print('Select the Menu Option by Number')#Menu Selection Direction Output
    for item in options:##Prints the options for the user to select
        index = options.index(item)
        print(str(index+1)+ '. ' + item)
    entry = input('enter option by number:')
    if entry == 'exit':
        quit_it()
    if not entry.isnumeric() or int(entry) < 1 or int(entry) > 3:
        print('You must select a number 1, 2, or 3.')
        user_selection()
    else:
        print('You have selected ' + options[int(entry)-1])
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
    names = list()
    #Format a list of the Donor names
    max_len_of_name = 0

    for i in range(1, len(donors)):
        if len(donors[i][0]) > max_len_of_name:
            max_len_of_name = len(donors[i][0])

    while True:
        input_name = input('Enter full name of donor or \'list\' to request list of donors: ')
        for j in range(len(donors)):
            names.append(donors[j][0])

        if input_name == 'list':
            for k in range(len(donors)):
                name = donors[k][0]
                print('{:{align}{width}}'.format(name, align='<', width=max_len_of_name))
            else:
                continue

        if input_name == 'exit':
            quit_it()

        if input_name in names:
            list_or_not = 'y'
            break

        else:
            list_or_not = 'n'
        if list_or_not == 'n':
            add_donor(input_name)
            list_or_not = 'n'
            more_donations = 'n'
            break
    mas_donations = 'Would you like to add more donations for ' + input_name + '? y/n: '
    if list_or_not == 'y':
        more_donations = input(mas_donations)
    if more_donations == 'y':
        totals = add_donations(input_name)
    else:
        totals = 0
        for z in range(len(donors)):
            if input_name == donors[z][0]:
                for c in range(len(donors[z])-1):
                    totals = totals + int(donors[z][c+1])
                break


    email_text_1 = "Dear " + input_name
    email_text_2 = "Thank you for your generous donation(s) of $" + str(totals) + '.'
    email_text_3 = "Sincerely," + '\n' + 'John Hunter'
    print(email_text_1 + '\n'*2 + email_text_2 + '\n'*2 + email_text_3)

def add_donor(name):
    """Adds a donor to the donor dictionary and allows the user to add donation values

    Returns: None
    """
    choice = 'y'
    donations = list()
    print('The name submitted is not on the list of donors.')
    print('The donor name will be added, please add donation values: ')
    while choice == 'y':
        donation = int(input('Enter a donation amount, enter \'0\' to stop adding donation values: '))
        if donation == 0:
            choice = False
        else:
            donations.append(donation)
    donations.insert(0, name)
    new_donor = donations
    donors.append(new_donor)
    print('The new donor has been added:')
    print(new_donor)
    print('The Thank You email for the new donor is:')

def order(total):
    return sum(total[1:])

def add_donations(name):
    """
    For either an existing donor or a new donor, we allow the user to add additional donations
    input variable, 'name' allows the user to specify which key in the global dict has the
    list values appended.
    returns the sum of the donor's donations
    """
    donations = list()
    donation = int()
    while True:
        donation = \
        int(input('Enter a donation amount, enter \'0\' to stop adding donation values: '))
        if donation == 0:
            break
        else:
            int(donation)
            donations.insert(-1, donation)
    for i in range(len(donors)):
        if name == donors[i][0]:
            donors[i] = donors[i] + donations
            break
    print(donors[i])
    return sum(donors[i][1:])

def run_report():
    """Returns a report of the donors by total historical amount
    The report should contain the Donor Name, total donated, number of
    donations, and average donation amount as values in each row
   """
    max_len_of_name = 0
    donors_temp_two = donors

    for i in range(len(donors_temp_two)):#calculates the longest name for formating
        if len(donors_temp_two[i][0]) > max_len_of_name:
            max_len_of_name = len(donors_temp_two[i][0])
    
    print_order = sorted(donors, key=order, reverse=True)

    print('{:{align}{width}}'.format('Donor Name', align='^', width=max_len_of_name) + \
          ' |   Total Given   |     Num of Gifts    | Avgerage Gift')
    print('-'*max_len_of_name + '--------------------------------------------------------')
    for donor in print_order:
        total = sum(donor[1:])
        number = len(donor[1:])
        average = total/number
        person = donor[0]
        print('{:{align}{width}}'.format(person, align='<', width=max_len_of_name) + \
        ' ' + '$ ' + '{:{align}{width}.5}'.format(str(total), align='^', width=16) + \
        ' ' + '{:{align}{width}.5}'.format(str(number), align='^', width=21) + '$' + \
        ' ' + '{:{align}{width}.2f}'.format(average, align='^', width=14))

def quit_it():
    """
    offers the user a quick exit from the script
    """
    sys.exit(0)

def main():

    while True:
        entry = user_selection()
        if entry == '1':
            send_ty()
        elif entry == '2':
            run_report()
        elif entry == '3':
            quit_it()

if __name__ == '__main__':
    main()
