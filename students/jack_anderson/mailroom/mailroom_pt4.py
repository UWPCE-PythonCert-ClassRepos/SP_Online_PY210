#!/usr/bin/env python3
"""
Jack Anderson
02/19/2020
UW PY210
Mailroom assignment part 4
"""
from datetime import date

# The list of donors and their amounts donated
donors_list = [
    ['Bubbles Trailer', [1500.99, 2523, 3012]],
    ['Julien Park', [2520.92, 1623.12]],
    ['Ricky Boys', [345.56, 5123.25]],
    ['Jack Anderson', [1044, 2232, 4123.56]],
    ['Lacey Coffin Greene', [1500.32, 625.34, 1305, 340.78]]
  ]

donors_dict = { donor[0]:donor[1] for donor in donors_list}


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


def prompt_name():
    # Return the name entered by user
    name = safe_input("Enter the full name of the donor "
                      "(enter 'q' to cancel or 'list' to view a list of donors): ", is_name=True)
    return name


def prompt_amount():
    # Return the donation amount entered by user
    donation = safe_input("Please enter a donation amount "
                          "(enter 'q' to cancel): $ ",is_name=False)
    return donation


def list_names():
    # Return a list of donors
    donors = list(donors_dict)
    return(donors)


def add_items(name, donation):
    """
    Action to add items to the donor_dict
    :param name: Donor name
    :param donation: Donation made by donor
    :return: Donor name, Donor Donation
    """
    donated = []
    donated.append(float(donation))
    if name in donors_dict.keys():
        donations = donors_dict[name]
        total = donated + donations
        donors_dict[name] = total

    else:
        donors_dict[name] = donated
    return name, donation

def get_donor_values(donor):
    x = donors_dict[donor]
    return x

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
    return (name, num_donations, total_donated, avg_donation)


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
    return(z)


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
    return(template)



def report_header():
    # Print a header for the report
    print()
    header = '{name:<21}\t| {total:^{width}}\t| {count:^{width}}\t| {avg:>{width}}' \
          .format(name='Donor Name', total='Total Given', count='Num Gifts', avg='Average Gift', width=10)
    return header


def create_report():
    # Action to call report generation functions
    print(report_header())
    action = [donor_details(name, donations) for name, donations in (sorted(donors_dict.items(), key =
             lambda x:(sum(x[1]), x[0]), reverse=True))]
    return action


def send_thanks():
    # Action to create Thank you email for single person
    x, y = add_items(prompt_name(), prompt_amount())
    send_email(x, y)


def send_all_thanks():
    # Action to create Thank you email for ALL persons
    action = [send_email(name, donation[0]) for name, donation in donors_dict.items()]
    return action



def get_date():
    # Return the current date
    today = date.today()
    return today


def start(*args):
    """
    Action to prompt user to select various menu items or to close the program. Checks in place to ensure user
    enters a numerical key.
    """
    while True:
        mailroom_start = {1: send_thanks, 2: create_report, 3: send_all_thanks, 4: quit}
        try:
            print()
            action = input("Select a number to perform one of the following actions...\n"
                "1 -- Send a Thank You to a single donor \n"
                "2 -- Create a Report. \n"
                "3 -- Send a Thank You to all donors \n"
                "4 -- Quit \n")

            x = int(action)

            mailroom_start.get(x)()
        except (ValueError, TypeError):
            print("Not a valid option: Please enter a number from 1 to 4")
        except KeyboardInterrupt:
            print()
            quit()


def safe_input(prompt, is_name):
    """
    Check user prompt and perform action based on user input if no conditions are met
    :param prompt: A string to display to the user when requesting input
    :param is_name: set to True for name check, set to False for donation check
    :return: Return user input or re-prompt user for input if invalid input received
    """
    try:
        user_input = input(prompt)
        if len(user_input) == 0:
            print("Must enter a value")
            return safe_input(prompt, is_name)

        elif user_input.lower() == 'q':
            start()

        else:
            if is_name == True:
                if user_input.lower() == 'list':
                    print(list_names())
                    return prompt_name()
                else:
                    return user_input

            else:
                try:
                    return float(user_input)
                except ValueError:
                    print("You must enter a numerical value")
                    return prompt_amount()

    except(KeyboardInterrupt):
        print()
        quit()




if __name__ == '__main__':
    start()