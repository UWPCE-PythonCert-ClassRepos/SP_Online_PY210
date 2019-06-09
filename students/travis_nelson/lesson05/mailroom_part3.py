#!/usr/bin/env python3

import sys


donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33, 3, 555, 132, 77, 1],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Brax Dingle": [2331, 32322.87, 5566.20, 3323.23, 76, 323, 3.87],
            }


def single_thank_you():
    """Prints a letter to user-specified donor,
    including recent and historical donation amounts"""
    recipient = recipient_response()
    donation = donation_response(recipient)
    store_new_donation(recipient, donation)
    total_donations = sum_donations(recipient)
    print("Dearest {},\n"
          "We are writing to formally thank you for your generous"
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
            for i in donor_db:
                print("{}".format(i))
        else:
            donor_exists = False
            for donor in donor_db:
                if donor == response:
                    donor_exists = True
            if donor_exists:
                print("An existing patron\n")
                return response
            else:
                print("A new donor!\n")
                donor_db[response] = []
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
    updated_donations = donor_db[donor]
    updated_donations.append(float(donation))
    donor_db[donor] = updated_donations


def sum_donations(donor_name):
    """Returns sum of all historical donor donations"""
    return round(sum(donor_db[donor_name]), 2)


def sort_key(donor):
    """Returns the key to sort donations by"""
    return round(sum(donor_db[donor]))


def create_report():
    """Prints a list of all the donors, their total donation amount,
    the total number of donations they've made,
    and the average donation amount,
    in descending order based on total amount given"""
    sorted_donor_db = sorted(donor_db, key=sort_key, reverse=True)
    str_header_formatting = "{:^20}|" * 4
    str_grid_formatting = "-" * 21*4
    print(str_header_formatting.format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(str_grid_formatting)
    for i in sorted_donor_db:
        donor_name = i
        donor_total = round(sum(donor_db[i]), 2)
        number_donations = len(donor_db[i])
        average_donation = round(donor_total/number_donations)
        print("{:20} ${:>19} {:>20} ${:>20}".format(
              donor_name, donor_total, number_donations, average_donation))


def generate_all_thanks():
    for i in donor_db:
        most_recent_donation = ''.join(str(e) for e in donor_db[i][-1:])
        with open(f'{i}.txt', 'w') as f:
            f.write("Dearest {},\n"
                    "We are writing to formally thank you for your most recent"
                    " donation of ${}.\n"
                    "To date, you have donated ${} to our honorable mission.\n"
                    "You are truly a valuable patron, and we thank you "
                    "for your service (and money).\n"
                    "{}\n"
                    "{}".format(i,
                                most_recent_donation,
                                sum_donations(i),
                                "Kindest regards,",
                                "Baron Von Munchausen"))


def exit_program():
    """Exits the interactive script"""
    print("Ok Bye!")
    sys.exit()


def main():
    """Continuously asks the user for next task"""
    prompt = "\n".join((">>>",
                        "Let's do some stuff!",
                        "Please choose from below options:",
                        "1 - Send a Thank You to a single donor",
                        "2 - Create a Report",
                        "3 - Send letters to all donors",
                        "4 - Quit",
                        ">>> "))
    arg_dict = {"1": single_thank_you, "2": create_report,
                "3": generate_all_thanks, "4": exit_program}
    while True:
        response = input(prompt)
        arg_dict.get(response, "Try again!")()

if __name__ == "__main__":
    main()


# https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Exceptions.html
# Example from mailroom exercise:
# You want to convert the user’s input into an integer. And you want to give a nice message if the user didn’t provide a valid input.

# So you could do this:

# if num_in.isdigit():
#     num_in = int(num_in)
# But – int(num_in) will only work if the string can be converted to an integer.

# So you can also do:

# try:
#     num_in = int(num_in)
# except ValueError:
#     print("Input must be an integer, try again.")
#     continue
# This is particularly helpful for things like converting to a float – much more complicated to check – and all that logic is already in the float() constructor.

# Or let the Exception be raised if you can’t handle it.