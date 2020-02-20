#!/usr/bin/env python3
"""
Jack Anderson
02/14/2020
UW PY210
Mailroom assignment part 1
"""


# The list of donors and their amounts donated
donors_list = [
    ['Bubbles Trailer',[1500, 2523, 3012]],
    ['Julien Park',[2520.92, 8623.12]],
    ['Ricky Boys',[7042.76, 3845.56, 5123.25]],
    ['Jack Anderson',[1044, 2232, 4123.56]],
    ['Lacey Coffin Greene',[7500.32, 6625, 1305, 3400.78]]
    ]


def prompt_name():
    name = input("Enter the full name of the donor (enter 'q' to cancel or 'list' to view a list of donors)\n")

    if name.lower() == "list":
        print(donor_names())
        send_thanks()

    elif len(name) == 0:
        send_thanks()

    elif name.lower() == 'q':
        start()

    return name


def prompt_donation(name):
    donation = input("Please enter a donation amount for {} "
                     "(enter 'q' to cancel) : ".format(name))

    if len(donation) == 0:
        send_thanks()

    elif donation.lower() == 'q':
        start()

    return float(donation)


def donor_names():
    # Return a list of donor names
    names = []
    for donors in donors_list:
        names.append(donors[0])
    return names


def add_items(name, donation):
    """
    Action to check if name exists in list and add name if not exists
    :param x: Name of donor
    :return:
    """
    for donor in donors_list:
        if donor[0] == name:
            donor[1].append(donation)
            return
    else:
        new_donor = [name, [donation]]
        donors_list.append(new_donor)



def get_donor_index(x):
    """
    Action to search list by donor name and return index value of donor
    :param x: Name of donor
    :return: Index number of donor
    """
    count = len(donor_names())
    current = donor_names()
    index = 0
    while index < count:
        if x == current[index]:
            return (index)
        index = index + 1


def donor_details(x):
    """
    Action to summarize the details of a donor in the list
    :param x: The donors index number in the donor list
    :return: Name of donor, total amount donated, number of donations donor made, avg donation of donor
    """
    donor = x
    name = donor[0]
    donations = donor[1]
    num_donations = len(donor[1])
    total_donated = sum(donations)
    avg_donation = total_donated / num_donations
    return(name, total_donated, num_donations, avg_donation)


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


def print_email_template(name, amount):
    """
    Action to print out donor email
    :param name: Name of the donor
    :param amount: The amount provided by the donor
    """
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f"Hello {name},\n"
          f"Thank you for your gift of ${amount}! \n"
          f"We appreiate your gift to help with costs for our upcoming play! \n"
          f"Thank you for giving!\n"
          f"Best Regards, \n"
          f"The Blanchford Community Center!")
    print()


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
    for i in donors_list:
        name, totals, num_donations, avg_donation = donor_details(i)
        report_template(name, totals, num_donations, (avg_donation))
    print()

def send_thanks():
    """
    Action to prompt user for name then calls the name_check function and the prompt_donation_amount function
    """
    name = prompt_name()
    donation = prompt_donation(name)
    add_items(name, donation)
    print_email_template(name, donation)


def start():
    """
    Action to prompt user to select various menu items or to close the program. Checks in place to ensure user
    enters a numerical key.
    """
    while True:
        action = input("Select a number to perform one of the following actions...\n"
               "1. Send a Thank You Email \n"
               "2. Create a Report \n"
               "3. Quit \n")

        if action.isnumeric():
            action = int(action)
            if action > 3 or action < 1:
                print("Please select a number 1, 2 or 3")

            elif action == 1:
                send_thanks()

            elif action == 2:
                print_report_template()

            elif action == 3:
                print("Quitting program ....")
                exit()

        else:
            print("Please enter a numerical value")


if __name__ == '__main__':
    start()