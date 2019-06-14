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
        response = input("\nTo whom should we address this Thank You?\n"
                         "(Type 'list' to view existing donors)\n\n").title()
        try:
            if response[0].isalpha():
                if response.lower() == "list":
                    print("\n")
                    for i in donor_db:
                        print("{}".format(i))
                else:
                    donor_exists = False
                    for donor in donor_db:
                        if donor == response:
                            donor_exists = True
                    if donor_exists:
                        print("\nAn existing patron!\n")
                        return response
                    else:
                        print("\nA new donor!\n")
                        donor_db[response] = []
                        return response
            else:
                raise TypeError
        except TypeError:
            print("\nType a name, plz\n")


def donation_response(donor):
    """Returns the donation amount from the user"""
    keep_asking = True
    while keep_asking:
        donation = input("How much did they donate?\n")
        try:
            if float(donation):
                print("\nNice!\n")
                keep_asking = False
                return donation
        except ValueError:
            print("\nJust a number is fine.\n")


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
    """Creates text files containing a thank you letter to each of the donors.
    Document provides their total amount contributed, as well as their most
    recent donation amount."""
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
        print(f'Thank you letter created for {i}')
    print('\nAll Thank You letters have been created.\n')


def exit_program():
    """Exits the interactive script"""
    print("\nOk Bye!\n")
    sys.exit()


def invalid_response():
    """ To be called if user input doesn't map to the
    dict of available tasks. Specifically necessary due to dict.get()"""
    print("\nTry again!\n")


def main():
    """Continuously asks the user for next task"""
    prompt = "\n".join(("_________\n",
                        "Welcome to the Donation Station!\n",
                        "Please choose from below options:\n",
                        "1 - Send a Thank You to a single donor",
                        "2 - Create a Report",
                        "3 - Send letters to all donors",
                        "4 - Quit\n\n",))
    arg_dict = {"1": single_thank_you, "2": create_report,
                "3": generate_all_thanks, "4": exit_program}
    while True:
        response = input(prompt)
        arg_dict.get(response, invalid_response)()

if __name__ == "__main__":
    main()
