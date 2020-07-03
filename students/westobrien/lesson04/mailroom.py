#!/usr/bin/env python3

import sys
from operator import itemgetter

donor_db = {'Bob': [5.00, 10.00, 20.00, 15000.00],
            'Kathy': [20, 00],
            'Sherry': [50.00, 100.00],
            'Sophia': [1000.00],
            'Chet': [10000.00, 10000.00]}

main_prompt = "\n".join(("\nDonation Database Menu\n",
                         "Please choose from below options:",
                         "1 - Send a Thank You to an single Donor",
                         "2 - Create a Report",
                         "3 - Send a letter to all Donors",
                         "4 - Quit",
                         ">>> "))


def thank_you():
    name = input("\n".join(("\nPlease type a Full Name:",
                            ">>> ")))
    if name == "list":
        print(donor_db.keys())
        thank_you()
    elif name in donor_db:
        amount = input("\n".join(("\nPlease type a donation amount:",
                                  ">>> ")))

        donor_db.get(name).append(float(amount))
    else:
        amount = input("\n".join(("\nPlease type a donation amount: ",
                                  ">>> ")))
        donor_db[name] = [float(amount)]
        print(donor_db)

    print("\n Thank you {} For your generous donation of {} dollars! We appreciate your generous support"
          .format(name, amount))


def create_report():
    donor_db_sum = []
    for donor in donor_db.copy():
        sum_donation = 0
        num_gifts = 0
        avg_gift = 0
        for donation in donor_db.get(donor):
            sum_donation += donation
            num_gifts += 1
        avg_gift = sum_donation / num_gifts
        donor_db_sum_object = (donor, sum_donation, num_gifts, avg_gift)
        donor_db_sum.append(donor_db_sum_object)

    donor_db_sum = sorted(donor_db_sum, key=itemgetter(1), reverse=True)
    print(len(donor_db_sum))
    report = "Donor Name" + " " * 16 + \
        "|  Total Given  |  Num Gifts  |  Average Gift\n" + "-" * 71
    for donor in donor_db_sum[:]:
        report += "\n {:25s} $ {:13.2f} {:13}  $ {:12.2f}".format(*donor)
    print(report)


def sort_key(donors):
    return donors


def exit_program():
    print("Quitting...")
    sys.exit()


def letters():
    for donor in donor_db.copy():
        with open(donor + ".txt", "w") as f:
            f.write("Dear {}".format(donor))
            f.write("\nThank you for your very kind donation of ${:.2f}".format(sum(donor_db.get(donor))))
            f.write("\n\nIt will be put to very good use")
            f.write("\nSincerely, \n\t The Team")

main_dispatch={
    1: thank_you,
    2: create_report,
    3: letters,
    4: exit_program
}


def menu_selection(prompt, dispatch_dict):
    while True:
        response=input(prompt)
        print(response)
        dispatch_dict.get(int(response))()


if __name__ == "__main__":
    menu_selection(main_prompt, main_dispatch)
