#!/usr/bin/env python3
"""
Jack Anderson
02/18/2020
UW PY210
Mailroom assignment part 2
"""
from datetime import date

# The list of donors and their amounts donated
donors_list = [
    ['Bubbles Trailer',[1500, 2523, 3012]],
    ['Julien Park',[2520.92, 8623.12]],
    ['Ricky Boys',[7042.76, 3845.56, 5123.25]],
    ['Jack Anderson',[1044, 2232, 4123.56]],
    ['Lacey Coffin Greene',[7500.32, 6625, 1305, 3400.78]]
  ]

d = dict()
donors_dict = d

def create_dictionary():
    # Convert donors_list to a dictionary
    for i in donors_list:
        d[i[0]] = i[1]


def create_file(name, template):
    """
    Action to create a file containing email template
    :param name: Name of donor
    :param template: Email template to use
    """
    x = get_date()
    z = name.replace(" ", "_")
    with open(f'{z}_{x}.txt', 'w') as f:
        f.write(template)
    print(f"Email file '{z}_{x}.txt' has been created for {name}")


def prompt_input():
    # Return the name entered by user
    name = input("Enter the full name of the donor (enter 'q' to cancel or 'list' to view a list of donors)\n")
    if name.lower() == 'q':
        start()
    elif name.lower() == 'list':
        list_names()
        return prompt_input()
    else:
        return name



def prompt_amount():
    # Return the donation amount entered by user
    donation = input("Please enter a donation amount (enter 'q' to cancel): $")
    if donation.lower() == 'q':
        start()
    else:
        return float(donation)



def list_names():
    # Return a list of donors
    donors = list(donors_dict)
    print(donors)


def add_items(name, donation):
    """
    Action to add items to the donor_dict
    :param name: Donor name
    :param donation: Donation made by donor
    :return: Donor name, Donor Donation
    """
    l = []
    l.append(float(donation))
    if name in donors_dict.keys():
        m = donors_dict[name]
        x = l + m
        donors_dict[name] = x

    else:
        donors_dict[name] = l
    return name, donation



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


def send_email(name, donation):
    """
    Action to print out donor email
    :param name: Name of the donor
    :param donation: The amount provided by the donor
    """
    template = (f"Hello {name},\n\n"
                f"Thank you for your recent gift of ${donation:.2f}! \n"
                "We will use your gift to help with costs for our upcoming play! \n"
                "Thank you for giving!\n\n"
                "Best Regards, \n"
                "The Blanchford Community Center!")
    create_file(name, template)


def print_report_header():
    # Print a header for the report
    print()
    print('{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}' \
          .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10))
    print("=" * 70)


def print_report_template():
    # Action to call report generation functions
    print_report_header()
    for key, value in donors_dict.items():
        donor_details(key, value)


def send_thanks():
    # Action to create Thank you email for single person
    x, y = add_items(prompt_input(), prompt_amount())
    send_email(x, y)


def send_all_thanks():
    # Action to create Thank you email for ALL persons
    for key, value in donors_dict.items():
        send_email(key, value[0])


def get_date():
    # Return the current date
    today = date.today()
    return today


def start():
    """
    Action to prompt user to select various menu items or to close the program. Checks in place to ensure user
    enters a numerical key.
    """
    mailroom_start = {1: send_thanks, 2: print_report_template, 3: send_all_thanks, 4: quit}
    while True:
        print()
        action = input("Select a number to perform one of the following actions...\n"
               "1 -- Send a Thank You to a single donor \n"
               "2 -- Create a Report. \n"
               "3 -- Send a Thank You to all donors \n"
               "4 -- Quit \n")

        x = int(action)
        mailroom_start.get(x)()


if __name__ == '__main__':
    create_dictionary()
    start()
