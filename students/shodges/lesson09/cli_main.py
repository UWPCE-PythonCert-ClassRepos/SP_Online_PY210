#!/usr/bin/env python3

from donor_models import *

marmots_ledger = DonorCollection('marmots')

def send_thank_you():
    while True:
        donor = input('Please enter a donor name: ')
        if donor == 'quit':
            break
        elif donor == 'list':
            for item in donors.keys():
                print(item)
        else:
            amount = input('Please enter a donation amount: ')
            if add_donor_record(donor, amount) == False:
                print('Invalid donation amount {}\n'.format(amount))
            else:
                print(format_letter(donor, True))
            break


def print_report():
    print('{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*68)
    donor_report = sorted([[x, len(donors[x]), sum(donors[x])] for x in
        marmots_ledger.generate_report()], key = lambda x: x[2], reverse = True)
    for item in donor_report:
        try:
            report_output = {'name': item[0], 'total': item[2], 'gifts': item[1], 'average': (item[2] / item[1])}
            report_lines.append('{name:24}  ${total:10.2f}   {gifts:10d}   ${average:12.2f}'.format(**report_output))
        except ZeroDivisionError: # this occurs if an invalid donation amount is entered in send_thank_you for a new donor and the donor entry isn't removed
            continue
    print()


def save_all_letters():
    letter_dir = create_letter_dir(input('Please specify a directory to save letters in: '))

    if letter_dir == False:
        print('Error creating letter directory.')
    else:
        for donor in donors.keys():
            letter = save_letter(letter_dir, donor)
            if letter != False:
                print('{} created successfully'.format(letter.absolute()))


if __name__ == '__main__':
    menu_dispatch = {1: send_thank_you, 2: print_report, 3:save_all_letters, 4: quit}
    while True:
        print("""Mailroom -- Main Menu

Options:
  1 Send a Thank You
  2 Generate a Report
  3 Send letters to all donors
  4 Quit
""")
        option = input('Please select an option (1, 2, 3, 4): ')
        try:
            menu_dispatch.get(int(option))()
        except (TypeError, ValueError):
            print('Invalid option {}\n'.format(option))
