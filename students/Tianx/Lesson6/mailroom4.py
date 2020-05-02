# ------------------------------------------------------------------------#
# !/usr/bin/env python3
# Title: mailroom3.py
# Desc: Mailroom Part 3
# Tian Xie, 2020-04-12, Created File
# Tian Xie, 2020-04-26, Adding exception handler
# Tian Xie, 2020-04-30, fixing problems from previous week
# ------------------------------------------------------------------------#

# A dictionary of donor paired with a list of donation amounts
dict_of_donors = {'Jeff Bezos': [1.00, 50.00],
                  'Warren Buffet': [100.00, 1000.00],
                  'Bill Gates': [100.00, 500.00],
                  'Tim Cook': [300.00],
                  'Jack Ma': [2000.00]}
# Main Prompt
main_prompt = "\n".join(("=======  Main Menu ======= \n",
                         "Welcome to the Mailroom. Please select an option:",
                         "1: Send a Thank You to a single donor",
                         "2: Create a Report",
                         "3: Send letters to all donors",
                         "4: Exit",
                         ">>> "))


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
            print('\nError: you entered {}, which is not a number from 1-4. Please select again >'.format(response))
        except ValueError:
            print('\nError: you entered {}, which is not a number from 1-4. Please select again >'.format(response))


def show_donor_dict(donor_dict):
    """Displays current donor list.

    Args:
        donor_dict: dictionary of donors.

    Returns:
        None.

    """
    donor_lst = []
    for name in donor_dict:
        donor_lst.append(name)
    return donor_lst

def adding_donor_info(name, donation, donor_dict):
    """Adding donor info to the dict.

    Args:
        name: donor name
        donation: donation amount
        donor_dict: dictionary of donors.

    Returns:
        None.

    """
    if name not in donor_dict:
        added_donor = {name: [float(donation)]}
        donor_dict.update(added_donor)
    else:
        donor_dict[name].append(float(donation)) # If donor name exists, append the donation amount rather than updating the dictionary


def create_email(name, donation):
    #Creating a list of email components
    email = ['=======Email Template=======']
    body ='Dear {},\n\nThank you for your generosity, your donation of ${:.2f} will be put to good use.\n\n''Warm regards,\nMailroom Staff'.format(name, float(donation))
    email.append(body)
    return email


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
                           "or enter full name of donor. \n"
                           "Enter 'exit' to return to the main menu >").title()
        if donor_name == "Exit": #If the user types exist return to main menu.
            break
        elif donor_name == "List": #If the user types list show them a list of the donor names and re-prompt.
            print('======= The Donor List: =======')
            for name in show_donor_dict(dict_of_donors):
                print(name)
        else:
            if donor_name in dict_of_donors:
                donation_amount = input('Please enter a donation amount for ' + donor_name + ' >')
                while True:
                    try:
                        float(donation_amount)
                        break
                    except ValueError:
                        donation_amount = input('Error: Please enter a number for the donation amount>')
                adding_donor_info(donor_name, donation_amount, dict_of_donors)
                for email in create_email(donor_name, donation_amount):
                    print(email)
            else:
                print('\"{}\" is not a current donor, adding to the list...'.format(donor_name))
                donation_amount = input('Please enter a donation amount for ' + donor_name + ' >')
                while True:
                    try:
                        float(donation_amount)
                        break
                    except ValueError:
                        donation_amount = input('Error: Please enter a number for the donation amount>')
                adding_donor_info(donor_name, donation_amount, dict_of_donors)
                for email in create_email(donor_name, donation_amount):
                    print(email)
            break


def send_all():
    """Writing a letter for each donor and save them into a directory with the donor's name.

    Args:
       None

    Returns:
       None.
   """
    for name in dict_of_donors:
        file_name = f'{name.replace(" ", "_"):}.txt'
        with open(file_name, 'w') as objfile:
            objfile.write(f'Dear {name},\n\nThank you for your generosity, your donation of ${dict_of_donors[name][-1]:.2f} will be put to very good use.\n\n'
                          f'Your total donation amount is ${sum(dict_of_donors[name]):.2f}.\n\nWarm regards,\nMailroom Staff')

# Function to help with sorting
def sort_donor(dict_of_donors):
    return sum(dict_of_donors[1])

def create_report_format():
    """Formatting a report.

    Args:
       None

    Returns:
       report object

    """
    report = ['Donor Name                | Total Given | Num Gifts | Average Gift','------------------------------------------------------------------']
    for name, donation in sorted(dict_of_donors.items(), key=sort_donor, reverse=True):
        total_given = sum(donation)
        number_gifts = len(donation)
        avg = total_given / number_gifts
        report.append(f'{name:26} ${total_given:>11.2f} {number_gifts:>11.0f}  ${avg:>12.2f}')
    return report


def display_report(report):
    """Displaying the report.

    Args:
       report generated from create_report_format function

    Returns:
       None

    """
    for item in report:
        print(item)

def create_report():
    """Creating format and then display.

    Args:
       None

    Returns:
       None

    """
    report = create_report_format()
    display_report(report)

def quit():
    print("Exiting the menu now")
    return "Exit Menu"


main_dispatch = {'1': send_thank_you,
                 '2': create_report,
                 '3': send_all,
                 '4': quit,
                 }

if __name__ == '__main__':
    menu_selection(main_prompt, main_dispatch)
