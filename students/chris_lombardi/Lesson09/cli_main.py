import sys
import donor_models as dm

don_list = dm.DonorCollection()

def display_menu():
    """Displays the interactive menu to the user."""
    print('This program tracks the donation history for a charity.')
    print('Please select from the following options:\n' +
          '1) Record Donation and Send Thank You\n' +
          '2) Create A Report\n' +
          '3) Quit')
    user_selection = input('')
    return user_selection

def record_donation():
    """
    Menu Option 1
    Add donation amount for the requested doonr to the donor list.
    """
    response = input('Please enter a full name or "List":').title()

    #Print the list of donors in the log if requested by the user.
    while response == 'List':
        print(don_list)
        response = input('Please enter a full name: ').title()

    try:
        amount = float(input('Please enter a donation amount:'))
    except ValueError:
        print('\nNot a valid input.\nPlease try to record donation' +
              ' again using a valid amount.\n\n')
    else:
        d1 = check_donor(response)
        print(d1)
        d1.add_donation(amount)
        print(d1.send_thank_you(amount))

def check_donor(name):
    for i, x in enumerate(don_list.list_donors):
        if x.name == name:
            return don_list.list_donors[i]
    else:
        donor_new = dm.Donor(name)
        don_list.add_donor(donor_new)
        return donor_new

def create_report():
    """Menu option to create a tabular report of donor information."""
    print(don_list.create_report())

def exit_program():
    """Menu option to exit the script."""
    print("Exiting program...")
    sys.exit()

def initialize_donors():
    """Add preset entries into the donor log."""
    d1, d2 = dm.Donor('George Washington'), dm.Donor('Abraham Lincoln')
    d3 = dm.Donor('James Madison')
    d4, d5 = dm.Donor('Theodore Roosevelt'), dm.Donor('Dwight Eisenhower')
    d1.add_donation(1789.0, 1.0, 1797.0)
    d2.add_donation(1861.0, 16.0)
    d3.add_donation(1809.0,4.0)
    d4.add_donation(1901.0, 26.0, 60.0)
    d5.add_donation(1953.00, 34.0)
    don_list.add_donor(d1, d2, d3, d4, d5)

def main():
    dict_menu_opts = {'1': record_donation, '2': create_report,
                      '3': exit_program}
    menu_options = set(dict_menu_opts.keys())
    while True:
        try:
            option = display_menu()
            dict_menu_opts.get(option)()
        except TypeError:
            print("\nNot a valid option.\n"
                  "Please enter a valid option from the menu.\n")

if __name__ == '__main__':
    initialize_donors()
    main()