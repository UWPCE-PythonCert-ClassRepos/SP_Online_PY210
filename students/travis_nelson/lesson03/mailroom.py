#!/usr/bin/env python3

import sys


donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33, 3, 555, 132, 77, 1]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Brax Dingle", [2331, 32322.87, 5566.20, 3323.23, 76, 323, 3.87]),
            ]


def thank_you():
    """Prints a letter to user-specified donor,
    including recent and historical donation amounts"""
    recipient = recipient_response()
    donation = donation_response(recipient)
    store_new_donation(recipient, donation)
    total_donations = sum_donations(recipient)
    print("Dearest {},\n"
          "We are writing to formmally thank you for your generous"
          " donation of ${}.\n"
          "To date, you have donated ${} to our honorable mission.\n"
          "You are truly a valuable patron, and we thank you"
          " for your service"
          " (and money)".format(recipient, donation, total_donations))


def recipient_response():
    """Returns a recipient from the user...
    If recipient was not previously in donor database, they are added"""
    keep_asking = True
    while keep_asking:
        response = input("To whom should we address this Thank You?\n"
                         "(Type 'list' to view existing donors)\n").title()
        if response.lower() == "list":
            for i in range(len(donor_db)):
                print("{}".format(*donor_db[i]))
        else:
            donor_exists = False
            for donor, _ in donor_db:
                if donor == response:
                    donor_exists = True
            if donor_exists:
                print("An existing patron\n")
                return response
            else:
                print("A new donor!\n")
                new_donor = (response, [])
                donor_db.append(new_donor)
                return response


def donation_response(donor):
    """Returns the donation amount from the user"""
    keep_asking = True
    while keep_asking:
        donation = input("How much did they donate?\n")
        try:
            if float(donation):
                print("Nice!\n")
                keep_asking = False
                return donation
        except ValueError:
            print("Try again")


def store_new_donation(donor, donation):
    """Stores the donation amount in the donor database"""
    donor_names = []
    for j, _ in donor_db[:]:
        donor_names.append(j)
    donor_index = donor_names.index(donor)
    donor_db[donor_index][1].append(float(donation))


def sum_donations(donor_name):
    """Returns sum of all historical donor donations"""
    for i in (donor_db[:]):
        if i[0] == donor_name:
            return round(sum(i[1]), 2)


def sort_key(donor):
    return round(sum(donor[1]))


def create_report():
    """Prints a list of all the donors, their total donation amount,
    the total number of donations they've made,
    and the average donation amount,
    in descending order based on total amount given"""
    def sort_key(donor):
        return sum(donor[1])

    sorted_donor_db = sorted(donor_db, key=sort_key, reverse=True)
    str_header_formatting = "{:^20}|" * 4
    str_grid_formatting = "-" * 21*4
    print(str_header_formatting.format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(str_grid_formatting)
    for i in sorted_donor_db:
        donor_name = i[0]
        donor_total = round(sum(i[1]))
        number_donations = len(i[1])
        average_donation = round(donor_total/number_donations)
        print("{:20} ${:>19} {:>20} ${:>20}".format(
              donor_name, donor_total, number_donations, average_donation))


def exit_program():
    """Exits the interactive script"""
    print("Ok Bye!")
    sys.exit()


def main():
    '''Continuously asks the user for next task'''
    prompt = "\n".join((">>>",
                        "Let's do some stuff!",
                        "Please choose from below options:",
                        "1 - Send a Thank You",
                        "2 - Create a Report",
                        "3 - Quit",
                        ">>> "))
    while True:
        response = input(prompt)
        if response == "1":
            thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Try again!")

if __name__ == "__main__":
    main()
