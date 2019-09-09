#!/usr/bin/env python3

from donor_models import *

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
    print('\n'.join(generate_report()))
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
