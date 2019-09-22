#!/usr/bin/env python3

from donor_models import DonorCollection
import atexit

marmots_ledger = DonorCollection('marmots')

def send_thank_you():
    """
    User interface allowing the user to:
    * Enter a donor
      - Special values: list to list all donors, quit to return to main menu
    * If the donor does not exist, the user is given the option to create it
    * If the donor exists or is created, the user is given the option to add a donation
    * If a previous donation exists for the donor, the formatted letter is printed
    """
    while True:
        donorname = input('Please enter a donor name: ')
        if donorname == 'quit':
            break
        elif donorname == 'list':
            for item in marmots_ledger.donors:
                print(item)
        else:
            donor = donor_management_fetch(donorname)
            if donor is None:
                break
            while True:
                newdonation = input('Process new donation? (y/n) ')
                if newdonation == 'y':
                    donor_management_process(donor.name)
                    break
                elif newdonation == 'n':
                    break
            try:
                print(marmots_ledger.donor(donor.name).format_letter(True))
            except IndexError:
                print('{} has no donation history.\n'.format(donor.name))
            break


def print_report():
    """
    Print a report of all donors' names, donation totals, count of donations, and average
    gift.
    """
    print('{:24} | {:10} | {:10} | {:12}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print('-'*68)
    tmp_report = marmots_ledger.generate_report()
    for item in tmp_report:
        print('{:24}  ${total:10.2f}   {count:10d}   ${average:12.2f}'.format(item, **tmp_report[item]))
    print()


def save_all_letters():
    """
    Save thank you letters for all donors who have a donation on file in the user's specified
    directory.
    """
    results = marmots_ledger.save_letters(
            input('Please specify a directory to save letters in: '))

    if results[0] == False:
        print('Error creating letter directory.')
    else:
        print(results[0])
        for i, file in enumerate(results[1]):
            print('{}-- {}'.format(('`' if i == len(results[1]) - 1 else '|'), file.name))
        if len(results[2]) > 0:
            print()
            print('Failed to save letters for:')
            for file in results[2]:
                print(' * {}'.format(file))


def donor_management():
    """
    User interface allowing the user to:
    * Enter a donor
      - Special values: list to list all donors, quit to return to main menu
    * View the user's donations quantity and totals
    * Allow the user to delete donor record or process a donation
    """

    while True:
        donorname = input('Enter the name of the donor to manage: ')
        if donorname == 'quit':
            break
        elif donorname == 'list':
            for item in marmots_ledger.donors:
                print(item)
        else:
            donor = donor_management_fetch(donorname)
            if donor is None:
                break
            else:
                print()
                print('Donor record for: {}'.format(donor.name))
                print('Number of Donations: {}'.format(donor.count))
                print('Total Donations: ${:.2f}'.format(donor.donations))
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
                    donor_management_dispatch.get(int(option))(donor.name)
                except (TypeError, ValueError):
                    # This will catch all manner of bad things, but we always want to pass
                    # e.g., non-called out options, donor_management_process bad input, etc.
                    pass
                break


def donor_management_del(donor):
    """
    Delete the specified user from the DonorCollection class and print confirmation.
    """
    marmots_ledger.del_donor(donor)
    print('Deleted donor {}\n'.format(donor))


def donor_management_process(donor):
    """
    Prompt the user for a donation amount and attempt to process.

    Re-raise an exception if the donation is invalid; calling methods are expected to catch
    this.  This is passed through as the implementing method may have cleanup to perform.
    """
    amount = input('Please enter a donation amount: ')
    try:
        marmots_ledger.donor(donor).process(amount)
        print('Recorded donation of {}\n'.format(amount))
    except ValueError:
        print('Invalid donation amount {}\n'.format(amount))
        # re-raise the exception so that calling methods can clean up if necessary
        raise


def donor_management_fetch(donorname):
    """
    Return donorname's Donor object.  If donorname is not in the database, prompt the user to
    create it; if successfully created, return the object.  Else return None.
    """
    try:
        return marmots_ledger.donor(donorname)
    except KeyError:
        while True:
            create = input('Donor {} does not exist.  Create it? (y/n) '.format(donorname))
            if create == 'n':
                return None
            elif create == 'y':
                marmots_ledger.add_donor(donorname)
                return marmots_ledger.donor(donorname)

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
