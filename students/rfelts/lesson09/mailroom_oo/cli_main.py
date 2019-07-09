#!/usr/bin/env python3

# Russell Felts
# Assignment 9 - Cli Module


from donor_models import DonorCollection as Donors


def prompt_user(prompt, menu):
    """ Prompt the user to choose from a menu of 3 actions: Send a Thank You, Create a Report or Quit """

    while True:
        response = input("\nPlease enter one of the following number options: " + ', '.join(prompt) + ": ")
        try:
            if menu[response]() == "exit":
                break
        except KeyError:
            print("\n" + response + " is not a valid option.")


def send_thank_you():
    """ Prompt user to add a donation, to print a list of donors, or to exit. """

    # Thank You menu options to be presented to the user
    thank_you_menu_options = ("\n1 - Add Donation", "\n2 - List Donors", "\n0 - Return to Main Menu")
    thank_you_menu_dict = {"0": exit_menu, "1": add_donation, "2": list_donors}

    prompt_user(thank_you_menu_options, thank_you_menu_dict)


def add_donation():
    """ Prompt for a donor name and donation amount. If the user enters a name not in the current donor list, add that
    name to the data structure along with the donation amount. Then compose a thank you email. """

    donor_name = input("\nPlease enter the donor's name: ")
    amount = prompt_donation_amount(donor_name)

    # If the returned list is empty then the donor wasn't found in the current donor list
    try:
        donor = donors.donor_exists(donor_name)[0]
        donor.add_donation(amount)
        print(donor.compose_message)
    except IndexError:
        response = prompt_new_donor(donor_name, amount)
        if response != "exit":
            print(response.compose_message)


def prompt_donation_amount(donor_name):
    """ Prompt the user for the amount donated and verify the value entered is numeric if not prompt the user for
    a new value
    :return: a float representing the amount donated """

    while True:
        try:
            return float(input("\nPlease enter " + donor_name + "'s donation amount: "))
        except ValueError:
            print("The value enter was invalid.")


def prompt_new_donor(donor_name, amount):
    """ Prompt to see if the user wants to create a new donor
    :param amount: Float containing the donation amount
    :param donor_name: String containing the donor name """

    # New donor menu options to be presented to the user
    options = ("\n1 - Yes", "\n2 - No")
    menu = {"1": new_donor, "2": exit_menu}

    while True:
        response = input("\nNo record for " + donor_name + ". Do you want to create a new donor record for "
                         + donor_name + ' '.join(options) + ": ")
        try:
            return menu[response](donor_name, amount)
        except KeyError:
            print("\n" + response + " is not a valid option.")


def new_donor(donor_name, amount):
    """ Create a new donor and add it to the current list of donors
    :return donor: A Donor object representing the new donor
    """
    return donors.add_donor(donor_name, amount)


def list_donors():
    """ Print a list of the donors """
    print(donors.list_donors)


def print_report():
    """ Print a list including Donor Name, total donated, number of donations and average donation amount sorted by
    total historical donation amount. """

    name_padding = donors.get_name_padding
    report_data = donors.create_report()

    print(report_data[0])
    # Since the list is sorted just use the first item to calculate the donation padding value
    donation_padding = donors.get_donation_padding(report_data[0])

    # Print the report header
    print(f"\n{'Donor Name':<{name_padding}} | {'Total Given':>{donation_padding}} | {'Num Gifts':>03} | " +
          f"{'Average Gift':<{name_padding}}\n{'-' * 65}")

    # Print the report
    for row in report_data:
            print(f"{row[0]:<{name_padding}}  ${row[1]:>{donation_padding},.2f} {row[2]:>11d} {row[3]:>{donation_padding},.2f}")


def send_to_everyone():
    """ Create a report for every donor """
    donors.send_to_everyone()


def exit_menu(*args):
    """ Exits the current menu or program
    :param: Using *args as some methods in menus require parameters but this method does not
    :return: String to exit """
    return "exit"


# Main menu options to be presented to the user
menu_options = ("\n1 - Send Thank You", "\n2 - Create Report", "\n3 - Send Letters to Everyone", "\n0 - Exit")
menu_dict = {"0": exit_menu, "1": send_thank_you, "2": print_report, "3": send_to_everyone}

if __name__ == '__main__':

    donors = Donors()
    prompt_user(menu_options, menu_dict)
    print("\nProgram Over")
