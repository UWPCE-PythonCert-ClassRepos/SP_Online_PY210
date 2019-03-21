#UWPCE PY210
#Lesson05, Mailroom Part 3
import sys

donor_log = {} #Log of donors and their respective donation history.

def thank_you():
    """Accepts donation information and prints a thank you email."""
    response = input('Please enter a full name or "List":').title()

    #Print the list of donors in the log if requested by the user.
    while response == 'List':
        for entry in donor_log:
            print(entry)
        response = input('Please enter a full name: ').title()

    try:
        amount = float(input("Please enter a donation amount:"))
            #Check if name exists in log and either create new entry or update history.
        if response not in donor_log:
            donor_log[response] = [amount]
        else:
            donor_log[response] += [amount]
        #Print a thank you email for the latest donation.
        print(thankyou_note(response))
    except ValueError:
        print("\nNot a valid input.\nPlease try to record donation" +
              " again using a valid amount.\n\n")

def create_report():
    """Generate a tabular report of donation history"""
    header ='\n{:<18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
    print(header + '\n' + '-'*len(header))
    donor_sort = sorted(donor_log, key = sort_key, reverse = True)
    for entry in donor_sort:
        total = sum(donor_log.get(entry))
        num = len(donor_log.get(entry))
        average = total/num
        print('{:<18} ${:>12,.2f}{:>13}  ${:>12,.2f}'.format(entry,total,num,average))
    print('')

def sort_key(entry):
    return sum(donor_log.get(entry))

def total_donation(name):
    """Return the sum of donations for a particular donor."""
    total = 0.0
    for donation in donor_log.get(name):
        total += donation
    return total

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
            f.write(thankyou_note(entry))
        f.close()

def thankyou_note(entry):
    note = (f'Dear {entry},\n\n\tThank you for your generous donation of '
            f'${sum(donor_log.get(entry)):,.2f}!\n\tWe appreciate the '
            f'{len(donor_log.get(entry)):d} total donation(s) that you have made.'
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
        option = display_menu()
        if option not in menu_options:
            print("\nNot a valid option.\n"
                  "Please enter a valid option from the menu.\n")
        else:
            dict_menu_opts.get(option)()

if __name__ == "__main__":
    initialize_donors()
    main()