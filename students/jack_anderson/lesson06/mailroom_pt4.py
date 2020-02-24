#!/usr/bin/env python3
"""
Jack Anderson
02/24/2020
UW PY210
Lesson 06
Mailroom assignment part 4
"""
from datetime import date
import os

# The list of donors and their amounts donated
donors_list = [
    ['Bubbles Trailer', [1500.99, 2523, 3012]],
    ['Julien Park', [2520.92, 1623.12]],
    ['Ricky Boys', [345.56, 5123.25]],
    ['Jack Anderson', [1044, 2232, 4123.56]],
    ['Lacey Coffin Greene', [1500.32, 625.34, 1305, 340.78]]
  ]

donors_dict = { donor[0]:donor[1] for donor in donors_list}


def prompt_user(x):
    """
    Action to prompt user and handle keyboard interrupt
    :param x: Prompt to display to user
    :return: value input by user
    """
    try:
        user_prompt = input(x)
        if user_prompt.lower() == 'q':
            start()
        else:
            return user_prompt
    except(KeyboardInterrupt):
        print()
        quit()


def prompt_name():
    # Return the name entered by user
    name = prompt_user("Enter the full name of the donor (enter 'q' to cancel or 'list' to view a list of donors): ")
    namecheck = check_name(name)
    return namecheck


def prompt_amount():
    # Return the donation amount entered by user
    donation = prompt_user("Please enter a donation amount (enter 'q' to cancel): $ ")
    donation_check = check_donation(donation)
    return donation_check

def list_names():
    # Return a list of donors
    donors = list(donors_dict)
    return donors


def add_items(name, donation):
    """
    Action to add items to the donor_dict
    :param name: Donor name
    :param donation: Donation made by donor
    :return: Donor name, Donor Donation
    """
    donated = []
    donated.append(float(donation))
    donor = name.title()
    donors = list_names()
    for i in donors:
        if name.lower() == i.lower():
            donations = donors_dict[donor]
            total = donated + donations
            donors_dict[donor] = total

        else:
            donors_dict[donor] = donated


def get_donor_values(donor):
    """
    Action to get all values for donor
    :param donor: Name of donor
    :return: Values for donor
    """
    donor_values = donors_dict[donor]
    return donor_values


def donor_details(name, donations):
    """
    Action to summarize the details of a donor in the list
    :param name: Name of the donor
    :param donations: Donations made by the donor
    :return: Name of donor, total amount donated, number of donations donor made, avg donation of donor
    """
    num_donations = len(donations)
    total_donated = sum(donations)
    avg_donation = total_donated / num_donations
    report_template(name, total_donated, num_donations, avg_donation)
    return (name, total_donated, num_donations, avg_donation)


def report_template(name, total, count, avg):
    """
    Action to print out a report using the same template for all donors
    :param name: Name of donor
    :param total: Total Amount donated from donor
    :param count: Total amounts of donations made
    :param avg:  The average donation made
    """
    x = name
    y = total
    c = count
    a = float(avg)
    z = '{name:<21}\t$ {total:>{width}.2f}\t{count:^{width}}\t$ {avg:>{width}.2f}' \
        .format(name=x, total=y, count=c, avg=a, width=10)
    print(z)


def thanks_template(name, donation):
    """
    Action to print out donor email
    :param name: Name of the donor
    :param donation: The amount provided by the donor
    """
    template = (f"\nHello {name},\n\n"
                f"Thank you for your recent gift of ${donation:.2f}! \n"
                "We will use your gift to help with costs for our upcoming play! \n"
                "Thank you for giving!\n\n"
                "Best Regards, \n"
                "The Blanchford Community Center!")
    return(template)



def report_header():
    # Print a header for the report
    print()
    header = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}' \
          .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10)
    print(header)


def create_report():
    # Action to call report generation functions
    report_header()
    action = [donor_details(name, donations) for name, donations in (sorted(donors_dict.items(), key =
             lambda x:(sum(x[1]), x[0]), reverse=True))]
    return action


def send_email_to_all():
    # Action to create Thank you email for ALL persons
    location = prompt_confirmation()
    action = [create_file(name, thanks_template(name, donation[0]), location) for name, donation in donors_dict.items()]
    return action


def send_thanks():
    # Print out a Thank you letter for single person
    name = prompt_name()
    donation = prompt_amount()
    add_items(name, donation)
    print(thanks_template(name, donation))


def create_file(name, template, location):
    """
    Action to create a file containing email template
    :param name: Name of donor
    :param template: Email template to use
    """
   # location = create_directory()
    z = name.replace(" ", "_")
    x = date.today()
    with open(f'{location}/{z}_{x}.txt', 'w') as f:
        f.write(template)
    print(f"Email file '{z}_{x}.txt' has been created for {name} in the {location} directory")


def create_directory(name):
    """
    Action to create directory for bulk email files if directory is not already created
    :param name: name of directory to create or store files
    :return: name of the created or existing directory
    """
    dir_list = list(os.listdir())
    if name in dir_list:
        return name
    else:
        try:
            os.mkdir(name)
            return name
        except ValueError:
            prompt_directory()


def prompt_directory():
    """
    Action to prompt user for name of directory to create when storing outgoing email files
    :return: directory name
    """
    dir_list = list(os.listdir())
    print()
    print(dir_list)
    user_input = prompt_user("Please enter the name of the directory from the list above to store email files. \n"
                             "To create a new folder, enter a new folder name or press 'enter/return' on the keyboard \n"
                             "to create a default outgoing email directory (enter 'q' to cancel). \n")

    if len(user_input) == 0:
        return('outgoing_emails')

    else:
        return user_input


def prompt_confirmation():
    """
    Action to prompt user for confirmation on creating outgoing email files.
    Any input other than 'YES' or 'Y' will return user to start(), otherwise the directory is created
    :return: directory name
    """
    name = prompt_directory()
    user_confirm = prompt_user(f"Are you sure you want to create files for all Donors in the >>> {name} <<< directory (YES/NO)? \n"
                               f"Enter 'YES' or 'Y' to confirm or 'q' to cancel.\n")

    if user_confirm.lower() == 'yes' or 'y':
        location = create_directory(name)
        return location
    else:
        start()



def start():
    """
    Action to prompt user to select various menu items or to close the program. Checks in place to ensure user
    enters a numerical key.
    """
    while True:
        mailroom_start = {1: send_thanks, 2: create_report, 3: send_email_to_all, 4: quit}
        try:
            print()
            action = input("Select a number to perform one of the following actions...\n"
                "1 -- Send a Thank You to a single donor \n"
                "2 -- Create a Report. \n"
                "3 -- Send a Thank You to all donors \n"
                "4 -- Quit \n")

            x = int(action)
            try:
                mailroom_start.get(x)()
            except (ValueError, TypeError):
                print("Not a valid option: Please enter a number from 1 to 4")
        except KeyboardInterrupt:
            print()
            return quit()


def check_name(name):
    """
    Takes name parameter and performs action based on user input
    :param name: Name entered by user
    :return: List donor names and prompt user or name provided by user input
    """
    if len(name) == 0:
        print("Must enter a donor name")
        return prompt_name()
    elif name.lower() == 'list':
        print(list_names())
        return prompt_name()
    else:
        return name.title()



def check_donation(donation):
    """
    Takes donation parameter entered by user and performs action based on user input
    :param donation: donation amount entered by user
    :return: prompt user for donation amount if invalid input else return donation as float type
    """
    # if len(donation) == 0:
    #     print("Must enter a donation amount")
    #     prompt_amount()
    # else:
    try:
        return float(donation)
    except ValueError:
        print("You must enter a numerical value")
        return prompt_amount()



if __name__ == '__main__':
    start()