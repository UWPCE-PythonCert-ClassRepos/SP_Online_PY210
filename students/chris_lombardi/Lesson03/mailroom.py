#UWPCE PY210
#Lesson03, Mailroom Part 1
import sys

donor_log = [] #Log of donors and their respective donation history.
menu_options = ('1', '2', '3') #Available menu options.

def thank_you():
    """Accepts donation information and prints a thank you email."""
    response = input('Please enter a full name or "List":').title()

    #Print the list of donors in the log if requested by the user.
    while response == 'List':
        for entry in donor_log:
            print(entry[0])
        response = input('Please enter a full name from the list: ').title()

    #Check if the donor name is already in the log.
    if not check_donor_list(response):
        add_log_entry(response)

    #Add a donation amount to the donation history.
    amount = float(input("Please enter a donation amount:"))
    update_donation_history(response, amount)

    #Print a thank you email for the latest donation.
    email_template(response, amount)

def create_report():
    """Generate a tabular report of donation history"""
    header ='\n{:<18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given",
                                                   "Num Gifts", "Average Gift")
    print(header)
    print('-'*len(header))
    donor_sort = sorted(donor_log, key = sort_key, reverse = True)
    for entry in donor_sort:
        total = sum(entry[1])
        num = len(entry[1])
        average = total/num
        print('{:<18} ${:>12,.2f}{:>13}  ${:>12,.2f}'.format(entry[0],total,num,average))
    print('')

def sort_key(entry):
    return sum(entry[1])

def check_donor_list(name):
    """Check the global DONOR_LOG for an existing donor name."""
    for entry in donor_log:
        if name == entry[0]:
            return True
    return False

def update_donation_history(name, amount):
    """Add a donation to the history of a particular donor."""
    for entry in donor_log:
        if name == entry[0]:
            amnt_entry = [float(amount),]
            entry[1] += amnt_entry
            break

def add_log_entry(name):
    """Create a new donor entry into the global DONOR_LOG."""
    hist = []
    add_entry = [name.title(), hist]
    donor_log.append(add_entry)

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
    donor_log.append(['George Washington', [1789.0, 1.0, 1797.0]])
    donor_log.append(['Abraham Lincoln', [1861.0, 16.0]])
    donor_log.append(['James Madison', [1809.0,4.0]])
    donor_log.append(['Theodore Roosevelt',[1901.0, 26.0, 60.0]])
    donor_log.append(['Dwight Eisenhower', [1953.00, 34.0]])

def main():
    while True:
        option = display_menu()
        if option == '1':
            thank_you()
        elif option == '2':
            create_report()
        elif option == '3':
            exit_program()
        elif option not in menu_options:
            print("\nNot a valid option.\n"
                  "Please enter a valid option from the menu.\n")

if __name__ == "__main__":
    initialize_donors()
    main()