#!/usr/bin/env python3

# Russell Felts
# Assignment 6 - Updated Mailroom


import datetime
import operator


# Dictionary that has donors as the key and a list of the amounts they have donated as the value.
donor_data = {"Lionel Messi": [100], "Cristiano Ronaldo": [5000, 25, 9450], "Gianluigi Buffon": [1000000, 2500.50],
              "Neymar": [25.25, 30, 99.99, 250], "Paolo Maldini": [9500, 6789.95, 250, 7500]}


def prompt_user(prompt, menu):
    """ Prompt the user to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.
    :param prompt: String representing the menu options to present to the user
    :param menu: Dictionary of valid menu values """

    while True:
        response = input("\nPlease enter one of the following options: " + ', '.join(prompt) + ": ")
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


def create_report():
    """ Print a list including Donor Name, total donated, number of donations and average donation amount sorted by
    total historical donation amount. """

    # Create dynamic padding for the name
    name_padding = len(max(donor_data, key=len)) + 4

    temp_data = create_report_data()

    donor_totals = [temp_value[1] for temp_value in temp_data]

    # Create dynamic padding for the donation amount data
    donation_padding = len(str(max(donor_totals)))
    donation_padding += int((donation_padding / 3) + 2)

    # Sort the list by donation total (index 1) of the list
    temp_data.sort(key=operator.itemgetter(1), reverse=True)

    # Print the report
    print(f"\n{'Donor Name':<{name_padding}} | {'Total Given':>{donation_padding}} | {'Num Gifts':>03} | " +
          f"{'Average Gift':<{name_padding}}\n{'-' * 65}")
    for row in temp_data:
        print(f"{row[0]:<{name_padding}}  ${row[1]:>{donation_padding},.2f} {row[2]:>11d} {row[3]:>{donation_padding},.2f}")


def create_report_data():
    """ Build a list containing donor names, total donation amounts, number of donations, average donation
    :return: list of lists containing: donor name, total donation amount, number of donation, average donation """

    temp_data = [[donor, sum(donations), len(donations), sum(donations) / len(donations)]
                 for donor, donations in donor_data.items()]

    return temp_data


def send_to_everyone():
    """ Write a file for each donor containing the thank you message. """

    now = datetime.datetime.now()

    donor_list = create_donor_list()

    for donor in donor_list:
        write_letter(now, donor)


def list_donors():
    """ Print the list of the donors. """

    name_list = donor_data.keys()

    print("\n")
    for name in sorted(name_list):
        print(name)


def create_donor_list():
    """ Create a list of dicts containing: the donor name, last donation amount, and total donation amount.
    :return: a list of donor dicts """

    donor_info = [{'name': name, 'last_donation': donations[-1], 'total_donations': sum(donations)}
                  for name, donations in donor_data.items()]

    return donor_info


def write_letter(now, donor):
    """ Write a file to disk with the requested donation message
    :param: now is the current datetime
    :param: donor is the dict containing the donor info """

    with open(donor["name"] + '_' + str(now.month) + '_' + str(now.year) + '.txt', 'w') as f:
        f.write(compose_message(donor))


def add_donation():
    """ Prompt for a donor name and donation amount. If the user enters a name not in the current donor list, add that
    name to the data structure along with the donation amount. Then compose a thank you email. """

    donor_name = input("\nPlease enter the donor's name: ")

    amount = prompt_donation_amount(donor_name)

    update_donation_amount(donor_name, amount)

    # Pass in a dict with the required info for the message
    print(compose_message({'name': donor_name, 'last_donation': donor_data.get(donor_name)[-1],
                           'total_donations': sum(donor_data.get(donor_name))}))


def prompt_donation_amount(donor):
    """ Prompt the user for the amount donated and verify the value entered is numeric if not prompt the user for a new
    value
    :param donor: string representing the name of the person making the donation
    :return: a float representing the amount donated """

    while True:
        try:
            return float(input("\nPlease enter " + donor + "'s donation amount: "))
        except ValueError:
            print("The value enter was invalid.")


def update_donation_amount(donor_name, amount):
    """ Update the donation amount for current donors or add a new donor with their donation amount
    :param donor_name: string representing the donor's name
    :param amount: float representing the amount donated """

    if donor_name in donor_data:
        donor_data[donor_name].append(amount)
    else:
        donor_data[donor_name] = [amount]


def compose_message(donor_info):
    """ Compose a thank you message listing the current/previous donation and the donor's donation total
    :param donor_info: dict containing the donor's info: name, last donation, and total donation amount
    :return: a String containing the thank you message for the user """

    return("\nTo: {name}\nSubject: Thank you.\n\n{name} thank you for your previous generous donation of "
           "{last_donation:<,.2f}.\nYou're total donations to date are now: {total_donations:<,.2f}.".format(**donor_info))


def exit_menu():
    """ Exits the current menu or program
    :return - a String to exit """
    return "exit"


# Main menu options to be presented to the user
menu_options = ("\n1 - Send Thank You", "\n2 - Create Report", "\n3 - Send Letters to Everyone", "\n0 - Exit")
menu_dict = {"0": exit_menu, "1": send_thank_you, "2": create_report, "3": send_to_everyone}


if __name__ == '__main__':
    prompt_user(menu_options, menu_dict)
    print("\nProgram Over")
