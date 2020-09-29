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
    menu = ("1 - Send a Thank You", "2 - Create a Report", "3 - quit")
    while True:
        response = int(get_user_input(f"Please enter an option from the following menu: \n {menu} > "))
        if response == 1:
            send_thank_you()
        elif response == 2:
            create_report()
        elif response == 3:
            break
        else:
            print(f"The option you entered '{response}' is invalid, please try again.")


def send_thank_you():
    """
    prompts user for a donor name; if name exists, prompts for donation, otherwise adds to donors
    list displays a list of donors
    generates
    :return: None
    """
    donor_name = get_user_input("Please enter the name of a donor: > ")
    if donor_name == 'list':
        print(f"List of donors: {[', '.join(donor[0]) for donor in donors]}")
    else:
        donation = float(get_user_input("Please enter the donation amount: $").strip('$'))
        for donor in donors:
            if donor[0] == donor_name:
                donor[1].append(donation)
        else:
            print(f"Sorry, the name you entered is not in our donor list.  Adding donor to list...")
            donors.append((donor_name, [donation]))
        print(format_thank_you(donor_name, donation))


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
    donor_summary = []
    for donor in donors:
        donor_summary.append([donor[0], format(sum(donor[1]), '.2f'), len(donor[1]), format(statistics.mean(donor[1]), '.2f')])
    donor_summary.sort(key=lambda x: float(x[1]), reverse=True)
    print(donor_summary)
    print(f"Donor Name{'':<20} | Total Given{'':>0} | Num Gifts{'':>0} | Average Gift{'':>0}")
    print(f"-" * 72)
    for name, total, num_gift, avg_gift in donor_summary:
        print(f"{name:<32}${total:>11}{num_gift:>12}  ${avg_gift:>13}")


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