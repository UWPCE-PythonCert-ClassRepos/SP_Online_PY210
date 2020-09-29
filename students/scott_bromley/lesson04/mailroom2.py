#!/usr/bin/env python3
import datetime
import statistics
import tempfile


# prompt user to select from mailroom menu: send a thank you, create a report, or quit
# send a thank you: allows user to select a name, adds donor if not in donor list, otherwise ask for donation
# and thanks donor
# create a report summarizes the donors and their donations in a table
# quit ends the program

# donors exists in global namespace
donors = {"David Einhorn": [1800.18, 36036.36], "Mark Zuckerberg": [7272.72, 1818.18, 545454.54],
          "Seth Klarman": [180.00, 72.72, 18.00], "Bill Ackerman": [324.32],
          "Michael Bloomberg": [363363.63, 18181.81]}
now = datetime.datetime.now()


def main():
    main_prompt = ("\nPlease enter an option from the following menu\n"
                   "1 - Send a Thank You to a single donor\n"
                   "2 - Create a Report\n"
                   "3 - Send letters to all donors\n"
                   "4 - Quit\n>> ")
    dispatch = {1: send_thank_you, 2: create_report, 3: send_thank_you_all_donors, 4: quit_mailroom}
    menu_selection(main_prompt, dispatch)


def menu_selection(prompt, dispatch_dict):
    """
    prompts user for input and calls function object in dispatch_dict
    :param prompt: user input prompt
    :param dispatch_dict: dict of dispatch functions
    :return:
    """
    while True:
        response = int(get_user_input(f"{prompt}"))
        if dispatch_dict[response]() == 4:
            break


def quit_mailroom():
    """
    quits the mailroom
    :return:
    """
    return 4


def send_thank_you():
    """
    prompts user for a donor name; if name exists, prompts for donation, otherwise adds to donors
    list displays a list of donors
    generates
    :return: None
    """
    donor_name = get_user_input("Please enter the name of a donor: > ")
    if donor_name == 'list':
        print(f"List of donors: {', '.join(k for k, v in donors.items())}")
    else:
        donation = float(get_user_input("Please enter the donation amount: ").strip('$'))
        donor_info = {"first_name": donor_name.strip().split(' ')[0], "last_name": donor_name.strip().split(' ')[1],
                      "donation_amount": donation}
        if donor_name in donors:
            donors.setdefault(donor_name, []).append(donation)
        else:
            print(f"Sorry, the name you entered is not in our donor list.  Adding donor to list...")
            donors.setdefault(donor_name, []).append(donation)
        print(format_thank_you(donor_info))


def send_thank_you_all_donors():
    """
    generate a thank you letter for all donors, write each letter to disk as .txt in tempdir
    :return: None
    """
    with tempfile.TemporaryDirectory(suffix='mailroom2', prefix='tys_all_donors', dir='.') as tempdir:
        for donor in donors:
            donor_info = {"first_name": donor.strip().split(' ')[0],
                          "last_name": donor.strip().split(' ')[1],
                          "donation_amount": format(donors.get(donor)[-1], '.2f')}
            with open(f"{donor_info['first_name']}_{donor_info['last_name']}_{now.date()}.txt", 'w') as f:
                f.write(format_thank_you(donor_info))


def format_thank_you(donor_info={}):
    """
    :param donor_info: dict containing donor first and last name, donation
    :return:
    """
    thank_you = (
        f"\n\n{now.date()}\n\n"
        f""
        f"Dear {donor_info['first_name']} {donor_info['last_name']},\n\n"
        f""
        f"On behalf of all of us at the ADL office we'd like to recognize and thank you for your generous\n"
        f"donation of ${donor_info['donation_amount']}.  "
        f"These funds will be used to further our mission in fighting hate\n"
        f"through leadership programs and education.  \n\n"
        f"We look forward to seeing you at this year's banquet.\n"
        f"\n"
        f"Sincerely, "
        f"\n"
        f"ADL")
    return thank_you


def create_report():
    """
    print a formatted table of donors ranked in descending order by Total Given
    :return: None
    """
    donor_summary = []
    for donor in donors:
        donor_summary.append([donor, sum(donors.get(donor)), len(donors.get(donor)),
                              statistics.mean(donors.get(donor))])
    donor_summary.sort(key=lambda x: float(x[1]), reverse=True)
    print(donor_summary)
    print(f"Donor Name{'':<20} | Total Given{'':>0} | Num Gifts{'':>0} | Average Gift{'':>0}")
    print(f"-" * 72)
    for name, total, num_gift, avg_gift in donor_summary:
        print(f"{name:<32}${total:>11.2f}{num_gift:>12}  ${avg_gift:>13.2f}")


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