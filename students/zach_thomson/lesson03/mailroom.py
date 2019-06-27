#!/usr/bin/env python3

import sys

donor_db = [('Eddie Vedder', [10000.00, 20000.00, 4500.00]),
            ('Chris Cornell', [100.00, 500.00]),
            ('Kurt Cobain', [25.00]),
            ('Dave Matthews', [100000.00, 50000.00, 125000.00]),
            ('Dave Grohl', [50.00])]


prompt = '\n'.join(('Welcome to the mailroom',
         'Please choose from the following options:',
         '1 - Send a Thank You',
         '2 - Create a Report',
         '3 - Quit',
         '> '))

#send a thank you tasks
def donor_in_list(x):
    """takes in a name and determines if it is in the donor database"""
    i = 0
    result = False
    while i < len(donor_db):
        if x == donor_db[i][0]:
            result = True
            break
        else:
            i = i + 1
    return result

def donor_idx(x):
    """takes in a name and finds the index number in donor database"""
    i = 0
    while i < len(donor_db):
        if x == donor_db[i][0]:
            return i
        else:
            i += 1

def donor_names():
    """return a list of names in the donor database"""
    i = 0
    donors = []
    while i < len(donor_db):
        donors.append(donor_db[i][0])
        i += 1
    return donors

donation_email = "\nDear {},\nThank you for your generous donation of ${:.2f}!\n"

def thank_you():
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    while ty_prompt.lower() == 'list':
        print(donor_names())
        ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    else:
        if donor_in_list(ty_prompt) == True:
            donation_amount = float(input('Please enter a donation amount: '))
            donor_db[donor_idx(ty_prompt)][1].append(float(donation_amount))
        else:
            donation_amount = float(input('Please enter a donation amount: '))
            new_entry = (ty_prompt, [donation_amount])
            donor_db.append(new_entry)
    print(donation_email.format(ty_prompt, donation_amount))


#create a report functions
def sum_function(x):
    total = 0
    for i in donor_db[x][1]:
        total = total + i
    return total

def number_donations(x):
    return len(donor_db[x][1])

def average_gift(x):
    return sum_function(x)/len(donor_db[x][1])

def sum_second(elem):
    total = 0
    for i in elem[1]:
        total = i + total
    return total

def create_table():
    """takes the donor database and sorts on total given. also makes a summary
    table with total given, number of gifts and average amount of gift"""
    donor_db.sort(key = sum_second, reverse = True)
    report_table = []
    i = 0
    while i < len(donor_db):
        report_table.append(donor_db[i][0])
        report_table.append(sum_function(i))
        report_table.append(number_donations(i))
        report_table.append(average_gift(i))
        i = i + 1
    return report_table

header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
table_header = "{:<20}| {} | {} | {}".format(*header) + '\n' + "-" * 60

def create_report():
    '''formats create_table into the create_report format'''
    table = create_table()
    print(table_header)
    line_format = ("{:<20}" + " $" + "{:>12.2f}" + "{:>11}" + "  $" + "{:>12.2f}" + '\n') * len(donor_db)
    print(line_format.format(*table))

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

if __name__ == "__main__":
    main()
