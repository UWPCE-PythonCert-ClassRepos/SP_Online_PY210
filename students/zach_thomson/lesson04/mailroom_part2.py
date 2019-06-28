#!/usr/bin/env python3

import sys

donor_db = {'Eddie Vedder': [10000.00, 20000.00, 4500.00],
            'Chris Cornell': [100.00, 500.00],
            'Kurt Cobain': [25.00],
            'Dave Matthews': [100000.00, 50000.00, 125000.00],
            'Dave Grohl': [50.00]}


prompt = '\n'.join(('Welcome to the mailroom',
         'Please choose from the following options:',
         '1 - Send a Thank You',
         '2 - Create a Report',
         '3 - Quit',
         '> '))

#send a thank you tasks
def donor_in_list(x):
    result = False
    if x in donor_db.keys():
        result = True
    return result

donation_email = "\nDear {},\nThank you for your generous donation of ${:.2f}!\n"

def thank_you():
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    while ty_prompt.lower() == 'list':
        print(donor_db.keys())
        ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    else:
        if donor_in_list(ty_prompt) == True:
            donation_amount = float(input('Please enter a donation amount: '))
            donor_db[ty_prompt].append(donation_amount)
        else:
            donation_amount = float(input('Please enter a donation amount: '))
            donor_db[ty_prompt] = [donation_amount]
    print(donation_email.format(ty_prompt, donation_amount))

#create a report functions
donor_db_copy = donor_db.copy()

def sum_function(x):
    total = 0
    i = 0
    for i in x:
        total = total + i
        i += 1
    return total


def number_donations(x):
    return len(x)

def average_gift(x):
    return sum_function(x)/len(x)

def create_table(d):
    """takes the donor database and sorts on total given. also makes a summary
    table with total given, number of gifts and average amount of gift"""
    report_table = []
    for key in d:
        report_table.append(key)
        report_table.append(sum_function(d[key]))
        report_table.append(number_donations(d[key]))
        report_table.append(average_gift(d[key]))
    return report_table

header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
table_header = "{:<20}| {} | {} | {}".format(*header) + '\n' + "-" * 60

def create_report(db):
    '''formats create_table into the create_report format'''
    table = create_table(db)
    print(table_header)
    line_format = ("{:<20}" + " $" + "{:>12.2f}" + "{:>11}" + "  $" + "{:>12.2f}" + '\n') * len(donor_db)
    print(line_format.format(*table))

print(create_report(donor_db))

#make a function to exit the program
def exit_program():
    print('Have a nice day!')
    sys.exit() # exit the interactive script

def main():
    while True:
        response = input(prompt)
        if response == '1':
            thank_you()
        elif response == '2':
            create_report()
        elif response == '3':
            exit_program()
        else:
            print('Not a valid option')

#if __name__ == "__main__":
#    main()
