#!/usr/bin/env python3

# Russell Felts
# Assignment 3 - Mailroom

# Data structure that holds a list of your donors and a history of the amounts they have donated.
donor_data = [['Lionel Messi', 100], ['Cristiano Ronaldo', 5000, 25, 9450], ["Gianluigi Buffon", 1000000, 2500.50],
              ['Neymar', 25.25, 30, 99.99, 250], ['Paolo Maldini', 9500, 6789.95, 250, 7500]]

# Menu options to be presented to the user
menu_options = ("Send Thank You", "Create Report", "Quit")


def prompt_user():
    """
    Prompt the user to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.
    """
    input_string = "\nPlease enter one of the following options: " + ', '.join(menu_options) + ": "
    response = input(input_string)

    while not "quit" == response.lower():
        if response.lower() == "send thank you":
            send_thank_you()
        elif response.lower() == "create report":
            create_report()
        elif not any(s.lower() == response.lower() for s in menu_options):
            print("\n" + response + " is not a valid option.")
        response = input(input_string)


def create_report():
    """
    Print a list including donor name, total donated, number of donations and average donation amount sorted by total
    historical donation amount.
    """
    temp_data = []
    donation_list = []
    name_list = create_name_list()

    # Create dynamic padding for the name and donation columns and a new list with the final data for the report
    for index, item in enumerate(donor_data):
        donation_list.append(sum(item[1:]))
        temp_data.append([name_list[index], donation_list[index], len(item[1:]), donation_list[index] / len(item[1:])])
    name_padding = len(max(name_list, key=len)) + 4
    donation_padding = len(str(max(donation_list)))
    donation_padding += int((donation_padding / 3) + 2)

    # Sort the list by donation total (index 1) of the list
    import operator
    temp_data.sort(key=operator.itemgetter(1), reverse=True)

    print(f"\n{'Donor Name':<{name_padding}} | {'Total Given':>{donation_padding}} | {'Num Gifts':>03} | " +
          f"{'Average Gift':<{name_padding}}\n{'-' * 65}")
    for row in temp_data:
        print(f"{row[0]:<{name_padding}}  ${row[1]:>{donation_padding},.2f} {row[2]:>11d} {row[3]:>{donation_padding},.2f}")


def send_thank_you():
    """
    Prompt for a full name, to print a list of donors, or to exit.
    If the user types a name not in the current donor list, add that name to the data structure and use it.
    Once a name has been selected, prompt for a donation amount.
    Once an amount has been given, add that amount to the donation history of the selected user.
    Compose an email thanking the donor for their generous donation.
    """

    prompt_string = "\nEnter the name of a donor, type 'list' to list donors, or type 'exit': "

    name_list = create_name_list()

    response = input(prompt_string)

    while True:
        if response.lower() == "exit":
            break
        elif response.lower() == "list":
            print("\n" + ", ".join(name_list))
            response = input(prompt_string)
        # Add the new name to the list along with the donation amount then generate the email
        elif not any(s.lower() == response.lower() for s in name_list):
            amount = prompt_donation_amount(response)
            donor_data.append([response, amount])
            compose_email(response.lower())
            break
        # Update the donor with the new donation amount then generate the email
        elif any(s.lower() == response.lower() for s in name_list):
            update_donor_history(response.lower(), prompt_donation_amount(response))
            compose_email(response.lower())
            break


def create_name_list():
    """
    Create a list containing the names of the donors
    :return - a list of donor names
    """
    return [item[0] for item in donor_data]


def prompt_donation_amount(donor):
    """
    Prompt the user for the amount donated
    :param donor - string representing the name of the person making the donation
    :return - a float representing the amount donated
    """
    prompt_string = "\nPlease enter " + donor + "'s donation amount: "
    response = input(prompt_string)

    # Verify the value entered is numeric if not prompt the user for a new value
    while True:
        try:
            response = float(response)
            return response
        except:
            print("The value enter was invalid.")
            response = input(prompt_string)


def update_donor_history(donor, donation):
    """
    Find the requested donor and their donation data in the donor_data list
    :param donor - String representing the person making the donation
    :param donation - Float representing the amount donated
    """
    for index, item in enumerate(donor_data):
        if item[0].lower() == donor:
            donor_data[index].append(donation)


def compose_email(donor):
    """
    Compose a thank you email listing the current donation and the donor's donation total
    :param donor - String representing the name of the donor
    """
    for index, item in enumerate(donor_data):
        if item[0].lower() == donor:
            print(item[0], item[-1])
            print(f"\nTo: {item[0]}\nSubject: Thank you.\n\n{item[0]} thank you for your generous donation of "
                  f"${item[-1]:<,.2f}.\nYou're total donations to date are now ${sum(item[1:])}.")


if __name__ == '__main__':
    prompt_user()
    print("\nProgram Over")
