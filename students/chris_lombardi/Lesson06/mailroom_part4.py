#UWPCE PY210
#Lesson06, Mailroom Part 4
import sys

donor_log = {} #Log of donors and their respective donation history.

def thank_you():
    """Accepts donation information and prints a thank you email."""
    response = input('Please enter a full name or "List":').title()

    #Print the list of donors in the log if requested by the user.
    while response == 'List':
        print(list_donors())
        response = input('Please enter a full name: ').title()

    try:
        amount = float(input("Please enter a donation amount:"))
    except ValueError:
        print("\nNot a valid input.\nPlease try to record donation" +
              " again using a valid amount.\n\n")
    else:
        update_donation(response, amount)
        print(thankyou_note(response, amount, len(donor_log.get(response))))

def list_donors():
    """Return a string of all the donors."""
    return '\n'.join(list(donor_log.keys()))

def update_donation(donor_name, donation_amount):
    if donor_name not in donor_log:
        donor_log[donor_name] = [donation_amount]
    else:
        donor_log[donor_name] += [donation_amount]

def create_report():
    """Generate a tabular string of donation history"""
    report_string = ''
    header ='\n{:<18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
    report_string += (header+ '\n' + '-'*len(header)+ '\n')
    donor_sort = sorted(donor_log, key = sort_key, reverse = True)
    for entry in donor_sort:
        total = sum(donor_log.get(entry))
        num = len(donor_log.get(entry))
        ave = total/num
        report_string += '{:<18} ${:>12,.2f}{:>13}  ${:>12,.2f}\n'.format(entry,total,num,ave)
    return report_string

def sort_key(entry):
    return sum(donor_log.get(entry))

def display_menu():
    """Displays the interactive menu to the user."""
    print('This program tracks the donation history for a charity.')
    print('Please select from the following options:\n' +
          '1) Record Donation and Send Thank You\n' +
          '2) Create A Report\n' +
          '3) Send Thank You Letters to All Donors\n' +
          '4) Quit')
    user_selection = input('')
    return user_selection

def exit_program():
    print("Exiting program...")
    sys.exit()

def send_letters():
    for entry in donor_log:
        filename = entry + '.txt'
        with open(filename, 'w') as f:
            f.write(thankyou_note(entry,sum(donor_log.get(entry)),len(donor_log.get(entry))))

def thankyou_note(entry, amount, num):
    note = (f'Dear {entry},\n\n\tThank you for your generous donation of '
            f'${amount:,.2f}!\n\tWe appreciate the '
            f'{num:d} total donation(s) that you have made.'
            '\n\tYour donation will be put to good use.'
            '\n\n\tSincerely,\n\t-The Mailroom Team')
    return note

def initialize_donors():
    """Add preset entries into the donor log."""
    donor_log['George Washington'] = [1789.0, 1.0, 1797.0]
    donor_log['Abraham Lincoln'] = [1861.0, 16.0]
    donor_log['James Madison'] = [1809.0,4.0]
    donor_log['Theodore Roosevelt'] = [1901.0, 26.0, 60.0]
    donor_log['Dwight Eisenhower'] = [1953.00, 34.0]

def main():
    dict_menu_opts = {'1': thank_you, '2': create_report,
                      '3': send_letters, '4': exit_program}
    menu_options = set(dict_menu_opts.keys())
    while True:
        try:
            option = display_menu()
            print(dict_menu_opts.get(option)())
        except TypeError:
            print("\nNot a valid option.\n"
                  "Please enter a valid option from the menu.\n")

if __name__ == "__main__":
    initialize_donors()
    main()