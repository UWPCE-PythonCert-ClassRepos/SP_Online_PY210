#!/usr/bin/env python3
"""
Jack Anderson
02/14/2020
UW PY210
Mailroom assignment part 1
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
    for i in donors_list:
        d[i[0]] = i[1]


def prompt_input():
    name = input("Enter the full name of the donor (enter 'q' to cancel or 'list' to view a list of donors)\n")
    if name.lower() == 'list':
        list_names()
        return prompt_input()

    elif name.lower() == 'q':
        start()

    else:
        return name


def prompt_amount():
        donation = input("Please enter a donation amount (enter 'q' to cancel): $")
        if donation.lower() == 'q':
            start()
        return float(donation)


def list_names():
    x = list(donors_dict)
    print(x)


def add_items(name, donation):
    """
    Action to check if name exists in list and add name if not exists
    :param x: Name of donor
    :return:
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



def donor_details(key, value):
    """
    Action to summarize the details of a donor in the list
    :param x: The donors index number in the donor list
    :return: Name of donor, total amount donated, number of donations donor made, avg donation of donor
    """
    name = key
    donations = value
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
    :param amount: The amount provided by the donor
    """
    template = (f"Hello {name},\n\n"
                f"Thank you for your recent gift of ${donation:.2f}! \n"
                "We will use your gift to help with costs for our upcoming play! \n"
                "Thank you for giving!\n\n"
                "Best Regards, \n"
                "The Blanchford Community Center!")
    create_file(name, template)


def print_report_header():
    print()
    print('{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}' \
          .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10))
    print("=" * 70)


def print_report_template():
    """
    Action to create a report
    :return: Print report header followed by summary of all donors
    """
    print_report_header()
    for key, value in donors_dict.items():
        donor_details(key, value)


def send_thanks():
    x, y = add_items(prompt_input(), prompt_amount())
    send_email(x, y)

def send_all_thanks():
    for key, value in donors_dict.items():
        send_email(key, value[0])


def get_date():
    today = date.today()
    return today


def create_file(name, template):
    x = get_date()
    z = name.replace(" ", "_")
    with open(f'{z}_{x}.txt', 'w') as f:
        f.write(template)
    print(f"Email file '{z}_{x}.txt' has been created for {name}")



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