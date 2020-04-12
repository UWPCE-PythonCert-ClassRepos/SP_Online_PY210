# ------------------------------------------#
# !/usr/bin/env python3
# Title: mailroom.py
# Desc: Assignment 1
# Tian Xie, 2020-04-10, Created File
# ------------------------------------------#
# A dictionary of donor and a list of donation amounts
list_of_donors = {'Jeff Bezos': [1, 50], 'Warren Buffet': [100, 1000], 'Bill Gates': [100, 500], 'Tim Cook':[300],
              'Jack Ma':[2000]}
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
    added_donor = {name: [donation]}
    donor_list.update(added_donor)


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
        if donor_name not in list_of_donors and donor_name != "list" and donor_name != "exit":
            print('\"{}\" is not a current donor, adding to the list...'.format(donor_name))
            response = input('Please enter a donation amount for ' + donor_name + ' >')
            donation_amount = float(response) # Convert the amount into a number
            adding_donor_info(donor_name, donation_amount, list_of_donors)
            create_email(donor_name, donation_amount)
        elif donor_name == "list": #If the user types list show them a list of the donor names and re-prompt.
            show_donor_list(list_of_donors)
        elif donor_name == "exit": #If the user types exist return to main menu.
            break
        elif donor_name in list_of_donors:
            response = input('Please enter a donation amount for ' + donor_name + ' >')
            donation_amount = float(response)
            create_email(donor_name, donation_amount)
            break

def create_email(name, donation):
    print()
    print(f'Dear {name},\n\nThank you for your generousity, your donation of ${donation:.2f} will be put to good use.\n\n'
      'Warm regards,\nMailroom Staff')

def create_report():
    pass


def quit():
    print("Exiting the menu now")
    return "Exit Menu"


main_dispatch = {"1": send_thank_you,
                 '2': create_report,
                 '3': quit,
                 }

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
