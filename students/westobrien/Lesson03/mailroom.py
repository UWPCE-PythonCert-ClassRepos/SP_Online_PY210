#!/usr/bin/env python3

import sys
from operator import itemgetter

donor_db = [('Bob', [5.00, 10.00, 20.00, 150000.00]), ('Kathy', [20.00]),
            ('Sherry', [50.00, 100.00]), ('Sophia', [1000.00]),
            ('Chet', [10000.00, 10000.00])]

prompt = "\n".join(("\nDonation Database Menu\n",
                    "Please choose from below options:",
                    "1 - Send a Thank You",
                    "2 - Create a Report",
                    "3 - Quit",
                    ">>> "))


def thank_you():
    name = input("\n".join(("\nPlease type a Full Name:",
                            ">>> ")))
    name_list = []
    for names in donor_db:
        name_list.append(names[0])
    # change to while name == "list"
    if name == "list":
        print(name_list)
        thank_you()
    elif name in name_list:
        amount = input("\n".join(("\nPlease type a donation amount:",
                                  ">>> ")))

        donor_db[name_list.index(name)][1].append(float(amount))
        print(donor_db)
    else:
        amount = input("\n".join(("\nPlease type a donation amount: ",
                                  ">>> ")))
        new_donor = (name, [float(amount)])
        donor_db.append(new_donor)
        print(donor_db)

    print("\n Thank you {} For your generous donation of {} dollars! We appreciate your generous support"
          .format(name, amount))


def create_report():
    donor_db_sum = []
    len_name = 0
    for donor in donor_db[:]:
        sum_donation = 0
        num_gifts = 0
        avg_gift = 0
        if len(donor[0]) > len_name:
            len_name = len(donor[0])
        for donation in donor[1]:
            sum_donation += donation
            num_gifts += 1
        avg_gift = sum_donation / num_gifts
        donor_db_sum_object = (donor[0], sum_donation, num_gifts, avg_gift)
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


def main():
    while True:
        response = input(prompt)

        if response == "1":
            thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main()
