#!/usr/bin/env python3

"""
Mailroom script - Part 3.

This script accepts user input to perform donation database tasks:
    1 - Display the donor database list or update the donation database with
        a new donation. Then display a 'Thank You' message to the donor of the
        new donation.
    2 - Display a donation database report
    3 - Create Thank You letter for each donor and save to separate text files.
    4 - Quit out of the script

"""
# creating the donor database using nested lists:
donors = [['Katherine Elmhurst', 'David Anderson', 'Edward Hoffstein',
           'Rebecca Manriquez', 'Callum Foxbright'],
          [[1000., 1500., 1900.], [10865., 5750.], [200., 200., 200.],
          [1750., 1500.], [130.75]]]
# creating dictionary database 'db' from nested list database 'donors'
#
# using a for loop:
# db = {}
# for i, donor in enumerate(donors[0]):
#     db[donor] = donors[1][i]
#
# using dictionary comprehension:
# db = {k: donors[1][i] for i, k in enumerate(donors[0])}
#
# using dict() constructor:
db = dict([donors[0][i], donors[1][i]] for i, _ in enumerate(donors[0]))

# creating a 'Thank You' formatted string message template
thank_you_tmp = ("\n Subject: Thank You !!!\n"
                 "\n Dear {name},\n"
                 "\n Thank you for your latest donation of"
                 " ${donation_amt:,.2f}.\n"
                 " We are so glad you have made {donation_num} donation(s)"
                 " totaling ${donation_sum:,.2f}.\n"
                 " Your continued support will help our"
                 " foundation achive our goals.\n\n"
                 " Regards,\n       Foundation Leadership Team\n"
                 )


def msg_vars(donor):
    """Get letter message variables from database for given donor."""
    return {'name': donor,
            'donation_amt': db[donor][-1],
            'donation_num': len(db[donor]),
            'donation_sum': sum(db[donor])
            }


def send_thank_you():
    """Send Thank You to individual donor."""
    name = input('\nEnter the full name of the donor > ')
    if name == 'list':
        print('\nPrinting list of current donors :\n')
        sorted_donor_list = [x for x in db]
        sorted_donor_list.sort()
        for donor in sorted_donor_list:
            print('  ', donor)
        send_thank_you()
    elif name in ['quit', 'q']:
        return None
    else:
        proper_name = ' '.join([word.capitalize() for word in name.split(" ")])
        if proper_name not in db:
            print('\nAdding donor to database :', proper_name)
            db[proper_name] = []
        else:
            print(f'\nFound donor {proper_name} in database.')
        amt = input('\nEnter a donation amount > $ ')
        while True:
            try:
                famt = float(amt)
            except ValueError:
                amt = input('\nPlease enter a valid dollar amount > $ ')
            else:
                break
        if famt:
            # if non-zero donation amount provided,
            # add amount to donor donations
            db[proper_name].append(famt)
            print('\nEMAIL MESSAGE :')
            print(thank_you_tmp.format(**msg_vars(proper_name)))
        else:
            # zero donation amount provided, return to main menu
            print('\nZero donation amount provided. Returning to menu...')
            # removing new donor if no donation amount provided
            if not db[proper_name]:
                del db[proper_name]


def create_report():
    """Create a donor database report."""
    total_donation = []
    for name, donations in db.items():
        total_donation.append([sum(x for x in donations), name])
    total_donation.sort(reverse=True)
    print('\nREPORT :\n')
    #       1234567890123456789012345 $12345678901  1234567890  $123456789012
    print(' Donor Name               | Total Given | Num Gifts | Average Gift')
    print(' -----------------------------------------------------------------')
    for x in total_donation:
        total_given = x[0]
        num_gifts = len(db[x[1]])
        avg_gift = total_given/num_gifts
        print(f' {x[1]:<25} ${total_given:>11.2f}  '
              f'{num_gifts:>10d}  ${avg_gift:>12.2f}')


def send_letters_to_all_donors():
    """Send letters to all donors in database."""
    print("\nCREATING LETTERS ...\n")
    for donor in db:
        with open(donor.replace(' ', '_') + '.txt', 'w') as letter:
            letter.write(thank_you_tmp.format(**msg_vars(donor)))


def menu_selection(prompt, dispatch_dict):
    """Menu prompt."""
    while True:
        response = input(prompt)
        if response not in ['1', '2', '3', '4']:
            print("\n!!! INVALID INPUT.  PLEASE PROVIDE A VALID INPUT !!!")
        elif dispatch_dict[response]() == "exit menu":
            break


def quit_msg():
    """Quit menu."""
    print("Quitting...")
    return "exit menu"


main_prompt = ('\nChoose one of the following options:   \n'
               '   1 - Send Thank You to a single donor. \n'
               '   2 - Create a Report.                  \n'
               '   3 - Send letters to all donors.       \n'
               '   4 - Quit                              \n'
               )

main_dispatch = {'1': send_thank_you,
                 '2': create_report,
                 '3': send_letters_to_all_donors,
                 '4': quit_msg,
                 }

# main_dispatch.setdefault('0', 'nothing')

if __name__ == "__main__":
    """Execute the main menu prompt."""
    while True:
        try:
            menu_selection(main_prompt, main_dispatch)
        except KeyboardInterrupt:
            print("\nPlease use the menu option '4' to Quit.")
        else:
            break
