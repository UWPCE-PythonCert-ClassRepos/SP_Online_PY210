#UWPCE PY210
#Lesson04, Mailroom Part 2
import sys

DONOR_LOG = {} #Log of donors and their respective donation history.

def thank_you():
    """Accepts donation information and prints a thank you email."""
    response = input('Please enter a full name or "List":').title()

    #Print the list of donors in the log if requested by the user.
    while response == 'List':
        for entry in DONOR_LOG:
            print(entry)
        response = input('Please enter a full name: ').title()

    amount = float(input("Please enter a donation amount:"))

    #Check if name exists in log and either create new entry or update history.
    if response not in DONOR_LOG:
        DONOR_LOG[response] = [amount]
    else:
        DONOR_LOG[response] += [amount]

    #Print a thank you email for the latest donation.
    email_template(response, amount)

def create_report():
    """Generate a tabular report of donation history"""
    header ='\n{:<18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
    print(header + '\n' + '-'*len(header))
    for entry in DONOR_LOG:
        total = total_donation(entry)
        num = len(DONOR_LOG.get(entry))
        average = total/num
        print('{:<18} ${:>12,.2f}{:>13}  ${:>12,.2f}'.format(entry,total,num,average))
    print('')

def total_donation(name):
    """Return the sum of donations for a particular donor."""
    total = 0.0
    for donation in DONOR_LOG.get(name):
        total += donation
    return total

def email_template(name, amount):
    print(f'\nDear {name.title()},')
    print(f'Thank you for your generous donation of ${amount:,.2f}!' +
          '\nWe appreciate your contribution to our charity.' +
          '\n\nSincerley,\nThe Mailroom\n')

def display_menu():
    """Displays the interactive menu to the user."""
    print('This program tracks the donation history for a charity.')
    print('Please select from the following options:\n' +
          '1) Send a Thank You\n' +
          '2) Create A Report\n' +
          '3) Quit')
    user_selection = input('')
    return user_selection

def exit_program():
    print("Exiting program...")
    sys.exit()

def initialize_donors():
    """Add preset entries into the donor log."""
    DONOR_LOG['George Washington'] = [1789.0, 1.0, 1797.0]
    DONOR_LOG['Abraham Lincoln'] = [1861.0, 16.0]
    DONOR_LOG['James Madison'] = [1809.0,4.0]
    DONOR_LOG['Theodore Roosevelt'] = [1901.0, 26.0, 60.0]
    DONOR_LOG['Dwight Eisenhower'] = [1953.00, 34.0]

def main():
    dict_menu_opts = {'1': thank_you, '2': create_report, '3': exit_program}
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