#!/usr/bin/env python
# mailroom.py
# Lisa Ferrier, Python 210, Lesson 03


import sys
from operator import itemgetter

donations = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Oprah Winfrey", [15000.00, 12500.00]),
             ]


def user_options():
    while True:
        response = input('''
                     1 - Send a Thank You
                     2 - Create a Report
                     3 - Quit.
                     Select option 1, 2, or 3.
                     ''')
        if response == "1":
            print("Okay, let's send a thank you.")
            send_thank_you()
        elif response == "2":
            print("Okay, here's the report:")
            create_report()
        elif response == "3":
            quit_program()
        else:
            print("That's not a valid option. Please enter 1, 2, or 3.")


def send_thank_you():
    while True:
        donor_name = input("\nEnter the donor's full name. Enter 'list' to see the complete donation list. Enter 'home' to return to main menu.\n")
        donor_name = donor_name.title()
        if donor_name == 'Home':
            user_options()
        elif donor_name == "List":
            for d in donations:
                print(d[0])
        else:
            for d in donations:
                if donor_name == d[0]:
                    donation_amount = sum(d[1])
                    break
            else:
                donation_amount = float(input("Donor not found. Enter donation amount."))
                donations.append([donor_name, [donation_amount]])
            print('''
Dear {},
Thank you for your generous donation in the amount of {:.2f}.
Sincerely,
This charity.
                  '''.format(donor_name, donation_amount))


def create_report():
    sort_donations = sorted(summarize_donations(), key=itemgetter(1), reverse=True)
    print("|  {:<26s}|{:^15s}|{:^15s}|{:^15s}|".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print('-' * 78)

    for i in sort_donations:
        print(f'|  {i[0]:26}| ${i[1]:12.2f} |{i[3]:^15}| ${i[2]:12.2f} |')
    user_options()


def summarize_donations():
    donation_summary = []
    for donor in donations:
        num_gifts = len(donor[1])
        sum_gifts = sum(donor[1])
        avg_gift = sum_gifts / num_gifts
        donor_summary = [donor[0], sum_gifts, avg_gift, num_gifts]
        donation_summary.append(donor_summary)
    return(donation_summary)
    user_options()


def quit_program():
    print("Quitting program.")
    sys.exit()


if __name__ == "__main__":
    user_options()
