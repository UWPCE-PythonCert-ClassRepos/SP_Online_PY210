#!/usr/bin/env python3

from donor_models import *
import atexit

marmots_ledger = DonorCollection('marmots')

def send_thank_you():
    while True:
        donor = input('Please enter a donor name: ')
        if donor == 'quit':
            break
        elif donor == 'list':
            for item in marmots_ledger.donors:
                print(item)
        else:
            try:
                marmots_ledger.add_donor(donor)
            except ValueError:
                pass
            try:
                donor_management_process(donor, False)
            except ValueError:
                if marmots_ledger.donor(donor).count < 1:
                    # Clean up the donor record if this invalid donation was the first record
                    marmots_ledger.del_donor(donor)
                break
            else:
                print(marmots_ledger.donor(donor).format_letter(True))
            break


def print_report():
    print('{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*68)
    tmp_report = marmots_ledger.generate_report()
    for item in tmp_report:
        print('{:24}  ${total:10.2f}   {count:10d}   ${average:12.2f}'.format(item, **tmp_report[item]))
    print()


def save_all_letters():
    letter_dir = marmots_ledger.save_letters(
            input('Please specify a directory to save letters in: '))

    if letter_dir[0] == False:
        print('Error creating letter directory.')
    else:
        for i, file in enumerate(letter_dir[1]):
            print('{}-- {}'.format(('`' if i == len(letter_dir[1]) - 1 else '|'),
                file))


def donor_management():
    donor = ''
    while True:
        donor = (input('Enter the name of the donor to manage: ') if donor == '' else donor)
        if donor == 'quit':
            break
        else:
            try:
                print()
                print('Donor record for: {}'.format(marmots_ledger.donor(donor).name))
                print('Number of Donations: {}'.format(marmots_ledger.donor(donor).count))
                print('Total Donations: ${:.2f}'.format(marmots_ledger.donor(donor).donations))
                print()
                print("""Actions:

1 Delete Donor Record
2 Process Donation

Enter anything else to return to main menu.
""")
                option = input('Please enter an option: ')
                donor_management_dispatch = {1: donor_management_del,
                                             2: donor_management_process}
                try:
                    donor_management_dispatch.get(int(option))(donor)
                except (TypeError, ValueError):
                    # This will catch all manner of bad things, but we always want to pass
                    # e.g., non-called out options, donor_management_process bad input, etc.
                    pass
                break
            except KeyError:
                while True:
                    create = input('Donor {} does not exist.  Create it? (y/n) '.format(donor))
                    if create == 'n':
                        return
                    elif create == 'y':
                        marmots_ledger.add_donor(donor)
                        break


def donor_management_del(donor):
    marmots_ledger.del_donor(donor)
    print('Deleted donor {}\n'.format(donor))


def donor_management_process(donor):
    amount = input('Please enter a donation amount: ')
    try:
        marmots_ledger.donor(donor).process(amount)
        print('Recorded donation of {}\n'.format(amount))
    except ValueError:
        print('Invalid donation amount {}\n'.format(amount))
        # re-raise the exception so that send_thank_you can clean up if necessary
        raise

if __name__ == '__main__':
    atexit.register(marmots_ledger.db_close)
    menu_dispatch = {1: send_thank_you, 2: print_report, 3:save_all_letters,
                     4: donor_management, 5: quit}
    while True:
        print("""Mailroom -- Main Menu

Options:
  1 Send a Thank You
  2 Generate a Report
  3 Send letters to all donors
  4 Donor Management
  5 Quit
""")
        option = input('Please select an option (1, 2, 3, 4, 5): ')
        try:
            menu_dispatch.get(int(option))()
        except (TypeError, ValueError):
            print('Invalid option {}\n'.format(option))
