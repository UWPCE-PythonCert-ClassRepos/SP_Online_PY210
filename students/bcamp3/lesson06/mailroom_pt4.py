#!/usr/bin/env python3

"""
Mailroom script - Part 4.

This script accepts user input to perform donation database tasks:
    1 - Display the donor database list or update the donation database with
        a new donation. Then display a 'Thank You' message to the donor of the
        new donation.
    2 - Display a donation database report
    3 - Create Thank You letter for each donor and save to separate text files.
    4 - Quit out of the script

"""
# creating the donor database using nested lists:
donors = [['Katherine Elmhurst', 'David Anderson', 'Edward Harvik',
           'Rebecca Manriquez', 'Callum Fuller'],
          [[1000., 1500., 1900.], [10865., 5750.], [200., 200., 200.],
          [1750., 1500.], [101.]]]
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


def get_letter_text(name, tmp=thank_you_tmp):
    """Return Thank You message text."""
    return tmp.format(**msg_vars(name))


def msg_vars(name):
    """Get letter message variables from database for given donor."""
    return {'name': name,
            'donation_amt': db[name][-1],
            'donation_num': len(db[name]),
            'donation_sum': sum(db[name])}


def list_of_donors():
    """Print an alphabetically sorted list of donor names."""
    sorted_donor_list = [x for x in db]
    sorted_donor_list.sort()
    donor_list_out = []
    for donor in sorted_donor_list:
        donor_list_out.append(donor)
    return donor_list_out


def add_donor(name):
    """Check if name is in database. If name not in database, add it."""
    proper_name = ' '.join([word.capitalize() for word in name.split(" ")])
    if proper_name not in db:
        msg_txt = f'\nAdding donor to database : {proper_name}'
        db[proper_name] = []
    else:
        msg_txt = f'\nFound donor {proper_name} in database.'
    return proper_name, msg_txt


def add_donation(name, amt):
    """Add donation amount to specified donor's donation history."""
    if amt > 0:
        # if non-zero donation amount provided, add amount to donor donations
        db[name].append(amt)
        msg_txt = '\nEMAIL MESSAGE :\n'+get_letter_text(name)
    else:
        # zero donation amount provided, return to main menu
        msg_txt = ('\nZero or negative donation amount provided. '
                   'Returning to menu...')
        # removing new dnor if no donation amount provided
        if not db[name]:
            del db[name]
    return msg_txt


def get_report():
    """Generate report summary of donations by donor."""
    total_donation = []
    for name, donations in db.items():
        total_donation.append([sum(x for x in donations), name])
    total_donation.sort(reverse=True)
    report_out = []
    for x in total_donation:
        total_given = x[0]
        num_gifts = len(db[x[1]])
        avg_gift = total_given/num_gifts
        report_out.append((f' {x[1]:<25} ${total_given:>11.2f}  '
                           f'{num_gifts:>10d}  ${avg_gift:>12.2f}'))
    return report_out


def send_thank_you():
    """Process donation and send Thank You to individual donor."""
    name = input('\nEnter the full name of the donor > ')
    if name == 'list':
        print('\nPrinting list of current donors :\n')
        for donor in list_of_donors():
            print('  ', donor)
        send_thank_you()
    elif name in ['quit', 'q']:
        return None
    else:
        proper_name, msg = add_donor(name)
        print(msg)
        amt = input('\nEnter a donation amount > $ ')
        while True:
            try:
                famt = float(amt)
            except ValueError:
                amt = input('\nPlease enter a valid dollar amount > $ ')
            else:
                break
        print(add_donation(proper_name, famt))


def create_report():
    """Create a donor database report."""
    print('\nREPORT :\n')
    #       1234567890123456789012345 $12345678901  1234567890  $123456789012
    print(' Donor Name               | Total Given | Num Gifts | Average Gift')
    print(' -----------------------------------------------------------------')
    for row in get_report():
        print(row)


def send_letters_to_all_donors():
    """Create Thank You letters for all donors in database."""
    print("\nCREATING LETTERS ...\n")
    for donor in db:
        with open(donor.replace(' ', '_') + '.txt', 'w') as letter:
            letter.write(get_letter_text(donor))


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
