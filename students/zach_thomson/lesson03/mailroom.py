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
def donor_names():
    """return a list of names in the donor database"""
    donor_list = []
    for donor in donor_db:
        donor_list.append(donor[0])
    return donor_list

def thank_you():
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    while ty_prompt.lower() == 'list':
        print(donor_names())
        ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    else:
        donation_amount = float(input('Please enter a donation amount: '))
        for idx, donor in enumerate(donor_db):
            if donor[0] == ty_prompt:
                donor_db[idx][1].append(donation_amount)
                break
        else:
            new_entry = (ty_prompt, [donation_amount])
            donor_db.append(new_entry)
    donation_email = "\nDear {},\nThank you for your generous donation of ${:.2f}!\n"
    print(donation_email.format(ty_prompt, donation_amount))

#create a report functions
def number_donations(idx):
    return len(donor_db[idx][1])

def average_gift(idx):
    return sum(donor_db[idx][1])/len(donor_db[idx][1])

def sum_second(elem):
    total = 0
    for i in elem[1]:
        total = i + total
    return total

def second_sort(elem):
    return elem[1]

def create_table():
    """takes the donor database and sorts on total given. also makes a summary
    table with total given, number of gifts and average amount of gift"""
    report_table = []
    i = 0
    while i < len(donor_db):
        new_entry = (donor_db[i][0], sum(donor_db[i][1]), number_donations(i), average_gift(i))
        report_table.append(new_entry)
        i = i + 1
    report_table.sort(key = second_sort, reverse = True)
    return report_table

def create_report():
    '''formats create_table into the create_report format'''
    header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    table_header = "{:<20}| {} | {} | {}".format(*header) + '\n' + "-" * 60
    line_format = ("{:<20}" + " $" + "{:>12.2f}" + "{:>11}" + "  $" + "{:>12.2f}")
    print(table_header)
    table = create_table()
    for entry in table:
        print(line_format.format(*entry))

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
