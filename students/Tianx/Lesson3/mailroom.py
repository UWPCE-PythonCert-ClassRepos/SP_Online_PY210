# ------------------------------------------#
# !/usr/bin/env python3
# Title: mailroom.py
# Desc: Assignment 1
# Tian Xie, 2020-04-10, Created File
# ------------------------------------------#
# A dictionary of donor and a list of donation amounts
dict_of_donors = {'Jeff Bezos': [1.00, 50.00],
                  'Warren Buffet': [100.00, 1000.00],
                  'Bill Gates': [100.00, 500.00],
                  'Tim Cook': [300.00],
                  'Jack Ma': [2000.00]}
# Main Prompt
main_prompt = "\n".join(("=======  Main Menu ======= \n",
                         "Welcome to the Mailroom. Please select an option:",
                         "1: Send a Thank You",
                         "2: Create a Report",
                         "3: Exit",
                         ">>> "))


def menu_selection(prompt, dispatch_dict):
    """Displays a menu of choices to the user
    Args:
        None.
    Returns:
        None.
    """
    while True:
        response = input(prompt)  # continuously collect user selection
        while True:
            try:
                int(response)
                break
            except ValueError:
                response = input('Error: Please enter a number. Please select again >').strip()
        if dispatch_dict[response]() == "Exit Menu":
            break


def show_donor_list(donor_list):
    """Displays current donor list.

            Args:
                donor_list: 2D data structure (dictionary of objects).

            Returns:
                None.

            """
    print('======= The Donor List: =======')
    print('Donor Name\n')
    for i in donor_list:
        print(i)
    print('======================================')


def adding_donor_info(name, donation, donor_list):
    """Adding donor info to the list.

                Args:
                    name: donor name
                    donation: donation amount
                    donor_list: 2D data structure (dictionary of objects).

                Returns:
                    None.

                """
    if name not in donor_list:
        added_donor = {name: [donation]}
        donor_list.update(added_donor)
    else:
        donor_list[name].insert(0, donation) # If donor name exists, insert the donation amount rather than updating the dictionary


def send_thank_you():
    """Sending a thank you email using user input.

           Args:
               None

           Returns:
               None

           """

    # Ask user for a donor's name or to display current list of donors, then ask for donation amount
    print()
    while True:
        donor_name = input('======= The Thank you Menu: =======\n'
                           "Enter 'list' for to see the list of donors\n"
                           "or enter full name of donor \n"
                           "Enter 'exit' to return to the main menu >")
        if donor_name not in dict_of_donors and donor_name != "list" and donor_name != "exit":
            print('\"{}\" is not a current donor, adding to the list...'.format(donor_name))
            response = input('Please enter a donation amount for ' + donor_name + ' >')
            donation_amount = float(response) # Convert the amount into a number
            adding_donor_info(donor_name, donation_amount, dict_of_donors)
            create_email(donor_name, donation_amount)
        elif donor_name == "list": #If the user types list show them a list of the donor names and re-prompt.
            show_donor_list(dict_of_donors)
        elif donor_name == "exit": #If the user types exist return to main menu.
            break
        elif donor_name in dict_of_donors:
            response = input('Please enter a donation amount for ' + donor_name + ' >')
            donation_amount = float(response)
            adding_donor_info(donor_name, donation_amount, dict_of_donors)
            create_email(donor_name, donation_amount)
            print(dict_of_donors)
            break


def create_email(name, donation):
    print('=======Email Template=======')
    print(f'Dear {name},\n\nThank you for your generousity, your donation of ${donation:.2f} will be put to good use.\n\n'
      'Warm regards,\nMailroom Staff')


def create_report():
    """Formating a report.

           Args:
               None

           Returns:
               None

           """
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('------------------------------------------------------------------')
    for name in dict_of_donors:
        total_given = sum(dict_of_donors[name])
        number_gifts = len(dict_of_donors[name])
        avg = total_given / number_gifts
        print(f'{name:26} ${total_given:>11.2f} {number_gifts:>11.0f}  ${avg:>12.2f}')
    print('------------------------------------------------------------------')


def quit():
    print("Exiting the menu now")
    return "Exit Menu"


main_dispatch = {"1": send_thank_you,
                 '2': create_report,
                 '3': quit,
                 }

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
