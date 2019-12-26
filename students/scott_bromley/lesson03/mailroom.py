#!/usr/bin/env python3
import datetime
import statistics


# prompt user to select from mailroom menu: send a thank you, create a report, or quit
# send a thank you: allows user to select a name, adds donor if not in donor list, otherwise ask for donation
# and thanks donor
# create a report summarizes the donors and their donations in a table
# quit ends the program

# donors exists in global namespace
donors = [("David Einhorn", [1800.18, 36036.36]), ("Mark Zuckerberg", [7272.72, 1818.18, 545454.54]),
          ("Seth Klarman", [180.00, 72.72, 18.00]), ("Bill Ackerman", [324.32]),
          ("Michael Bloomberg", [363363.63, 18181.81])]


def main():
    menu = ("Send a Thank You", "Create a Report", "quit")
    while True:
        response = get_user_input(f"Please enter an option from the following menu: \n {menu} > ")
        if response.lower() == "send a thank you":
            send_thank_you()
        elif response.lower() == "create a report":
            create_report()
        elif response.lower() == "quit":
            break
        else:
            print(f"The option you entered '{response}' is invalid, please try again.")
            continue


def send_thank_you():
    '''
    prompts user for a donor name; if name exists, prompts for donation, otherwise adds to donors
    list displays a list of donors
    generates
    :return: None
    '''
    full_name = get_user_input("Please enter the name of a donor: > ").title()
    for donor in donors:
        if full_name in donors:
            donation = float(get_user_input("Please enter the donation amount: $").strip('$'))
            add_donation(full_name, donation)
            format_thank_you(full_name, donation)
            break
        elif full_name.lower() == "list":
            print(f"List of donors: {', '.join(get_donors(donors))}")
            break
        else:
            print(f"Sorry, the name you entered is not in our donor list.  Adding donor to list...")
            donors.append((full_name, []))
            donation = float(get_user_input("Please enter the donation amount: $").strip('$'))
            add_donation(full_name, donation)
            print(format_thank_you(full_name, donation))
            break
    return None


def format_thank_you(full_name, donation):
    """
    :param full_name: name of the donor
    :param donation: the amount donated
    :return: None
    """
    now = datetime.datetime.now()
    thank_you = (
        f"\n\n{now.date()}\n\n"
        f""
        f"Dear {full_name},\n\n"
        f""
        f"On behalf of all of us at the ADL office we'd like to recognize and thank you for your generous\n"
        f"donation of ${donation}.  These funds will be used to further our mission in fighting hate\n"
        f"through leadership programs and education.  \n\n"
        f"We look forward to seeing you at this year's banquet.\n"
        f"\n"
        f"Sincerely, "
        f"\n"
        f"ADL")
    return thank_you


def create_report():
    """
    prints a formatted table of donors ranked in descending order by Total Given
    :return: None
    """
    names, totals, num_gifts, avg_gift = get_donor_summary(donors)
    print(f"Donor Name{'':<20} | Total Given{'':>0} | Num Gifts{'':>0} | Average Gift{'':>0}")
    print(f"-" * 72)
    for name, total, num_gift, avg_gift in zip(names, totals, num_gifts, avg_gift):
        print(f"{name:<32}${total:>11}{num_gift:>12}  ${avg_gift:>13}")
    return None


def get_donor_summary(donors=None):
    """
    :param donors: optional list of donors and donations
    :return: lists of names, totals, number of gifts, avg gift sorted by highest total
    """
    sorted_donors = sorted(donors, key=lambda x: sum(x[1]), reverse=True)
    names = tuple(map(lambda x: x[0], sorted_donors))
    totals = tuple(map(lambda x: float(format(sum(x[1]), '.2f')), sorted_donors))
    num_gifts = tuple(map(lambda x: len(x[1]), sorted_donors))
    avg_gift = tuple(map(lambda x: float(format(statistics.mean((x[1])), '.2f')), sorted_donors))
    return names, totals, num_gifts, avg_gift


def add_donation(donor_name, donation):
    """
    :param donor_name: full name of donor
    :param donation: amount of donation
    :return: None
    """
    donor_index = [donors.index(donor) for donor in donors if donor[0] == donor_name]
    donors[donor_index[0]][1].append(donation)
    return None


def get_donors(donors=None):
    """
    :param donors: optional list of donors
    :return: tuple of donor names
    """
    if donors is None:
        donors = []
    return tuple(map(lambda x: x[0], donors))


def get_user_input(prompt):
    """
    :param prompt: prompt for user to respond to
    :return: response to question/prompt
    """
    return input(prompt).strip()


if __name__ == "__main__":
    print("Running", __file__)
    main()
else:
    print("Running %s as imported module", __file__)