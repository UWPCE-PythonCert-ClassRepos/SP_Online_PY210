#!/usr/bin/env python3

import sys

donor_db = [("William", [653772.32, 12.17]),
            ("Jeff", [877.33]),
            ("Paul", [663.23, 43.87, 1.32]),
            ("Mark", [1663.23, 4300.87, 10432.0]),
            ("Elon", [234.25, 2764.87, 9783.0]),
            ]


def main(donor_db):
    """
    Prompts user for navigation of donor database
    :param donor_db: Database of donations and donors
    """
    prompt = "\n".join(("Donor Database",
              "Please choose from below options (i.e. 2):",
              "1 - Send a Thank You",
              "2 - Create a Report",
              "3 - Quit",
              ">>> "))
    while True:
        response = input(prompt)
        if response == "1":
            donor_db = thank_you(donor_db)
        elif response == "2":
            create_report(donor_db)
        elif response == "3":
            sys.exit()
        else:
            print("Not a valid option!")

def thank_you(donors):
    """
    Enter donor data
    :param donor_db: Database of donations and donors
    """
    prompt = "\n".join(("Enter full name of donor",
                        "(Type list to diplay current donors):"))
    response = input(prompt)
    donor_list = []
    donation = []
    for i in range(len(donors)):
        donor_list.append(donors[i][0])

    if response.lower() == 'list':
        for i in range(len(donors)):
            print(donors[i][0])
    elif response in donor_list:
        current_donor = response
        donation = enter_donation(donors, response)
        create_card(response,donation)
    elif response not in donor_list:
        donors.append((response,[]))
        donation = enter_donation(donors, response)
        create_card(response,donation)

    return donors

def enter_donation(donors, donator):
    """
    Add donation data to donor
    :param donor: Name of donator
    :param donor: Amount of donation
    """
    prompt = "\n".join(("Enter amount of donation",
                        "(No leading $ required):"))
    donation = input(prompt)
    donation = float(donation)
    for i in range(len(donors)):
        if donator == donors[i][0]:
            donors[i][1].append(donation)
    return donation

def create_card(donator, amount):
    """
    Create thank you card text
    :param donor: Name of donator
    :param donor: Amount of donation
    """
    card_text = ['Dear {}:','','Thank you for your generosity in your gift of ${:.2f}.  It will ago aong way in supporting this charity.','']
    card_text = card_text + ['Sincerely,','','','','Kristoffer Jonson']
    card_text = "\n".join(card_text)
    print(card_text.format(donator,amount))
    return True

def create_report(donors):
    """
    Print formatted report of donors and amounts donated
    :param donor_db: Database of donations and donors
    """
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('------------------------------------------------------------------')
    format_string = '{:<26} $ {:>11.2f}{:>12d} $ {:>11.2f}'
    donors = sorted(donors,key=sort_key,reverse=True)
    for i in range(len(donors)):
        print(format_string.format(donors[i][0],sum(donors[i][1]),len(donors[i][1]),sum(donors[i][1])/len(donors[i][1])))

def sort_key(donors):
    return sum(donors[1])


if __name__ == '__main__':
    main(donor_db)
