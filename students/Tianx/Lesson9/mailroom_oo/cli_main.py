# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: cli_main.py
# Desc: The module cli_main.py would include all of your user interaction functions and main program flow.
# Tian Xie, 2020-05-21, Created File
# ------------------------------------------------------------------------#

from donor_models import DonorCollection

# Initiate Default donor collection
donor_collection = DonorCollection()


def menu_selection(prompt, dispatch_dict):
    """Displays a menu of choices to the user
    Args:
        prompt: main menu
        dispatch_dict: choices for user to choose from
    Returns:
        None.
    """
    while True:
        response = input(prompt)  # continuously collect user selection
        try:
            int(response)
            if dispatch_dict[response]() == "Exit Menu":
                break
        except KeyError:
            print('\nError: you entered {}, which is not a number from 1-4. '
                  'Please select again >'.format(response))
        except ValueError:
            print('\nError: you entered {}, which is not a number from 1-4. '
                  'Please select again >'.format(response))


def handle_donation_input(donor_name):
    """Handles donation input, making sure donation amount is positive
    Args:
        donor_name: name of the donor

    Returns:
        donation_amount.
    """

    # Make sure users don't enter a negative donation.
    donation_amount = input('Please enter a donation amount for ' + donor_name + ' >')
    while True:
        try:
            float(donation_amount)
            assert float(donation_amount) > 0
            break
        except ValueError:
            donation_amount = input('Error: Please enter a number for the donation amount>')
        except AssertionError:
            donation_amount = input('Error: Please enter a positive number for the donation '
                                    'amount>')
    return donation_amount


def adding_donation(donor_name):
    """adds a donation, then displays an email.
        Args:
            donor_name: name of the donor

        Returns:
            none.
        """
    donor_collection.add_new_donation(donor_name, handle_donation_input(donor_name))
    print(donor_collection.get_donor(donor_name).create_email)


def send_thank_you():
    """Handles send_.

    Args:
       None

    Returns:
       None

    """
    # Ask user for a donor's name or to display current list of donors,
    # then ask for donation amount
    print()
    while True:
        donor_name = input('======= The Thank you Menu: =======\n'
                           "Enter 'list' for to see the list of donors\n"
                           "or enter full name of donor. \n"
                           "Enter 'exit' to return to the main menu >").title()
        # If the user types exist return to main menu.
        if donor_name == "Exit":
            break
        # If the user types list show them a list of the donor names and re-prompt.
        elif donor_name == "List":
            print('======= The Donor List: =======')
            print(donor_collection.show_donor_list)
        elif donor_collection.donor_exists(donor_name)is False:
            choice = input((f'{donor_name} is not currently in the donor list, '
                            f'are you sure you want to add to the list? Y/N')).upper()
            if choice == "Y":
                adding_donation(donor_name)
            else:
                print('You did not enter Y, back to main menu')
                break
        else:
            adding_donation(donor_name)
            break


def create_report():
    """Creating a report with donor summary.

    Args:
       None

    Returns:
       None

    """
    report = donor_collection.create_report()
    for item in report:
        print(item)


def send_all():
    """Writing a letter for each donor and save them into a directory with the donor's name.

    Args:
       None

    Returns:
       None.
   """
    donor_collection.send_all()
    print('Letters sent to all donors.')


def quit():
    print("Exiting the menu now")
    return "Exit Menu"


if __name__ == '__main__':
    main_prompt = "\n".join(("=======  Main Menu ======= \n",
                             "Welcome to the Mailroom. Please select an option:",
                             "1: Send a Thank You to a single donor",
                             "2: Create a Report",
                             "3: Send letters to all donors",
                             "4: Exit",
                             ">>> "))
    main_dispatch = {'1': send_thank_you,
                     '2': create_report,
                     '3': send_all,
                     '4': quit,
                     }
    menu_selection(main_prompt, main_dispatch)

