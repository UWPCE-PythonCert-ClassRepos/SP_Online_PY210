#!/usr/bin/env python3

import sys


donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33, 3, 555, 132, 77, 1],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Brax Dingle": [2331, 32322.87, 5566.20, 3323.23, 76, 323, 3.87],
            }


def elicit_donor():
        return input("\nTo whom should we address this Thank You?\n"
                     "(Type 'list' to view existing donors)\n\n").title()


def validate_input_donor(response_str):
    try:
        if response_str[0].isalpha():
            if response_str.lower() == "list":
                return "list"
            else:
                return response_str
        else:
            raise TypeError
    except TypeError:
            print("Please enter a correct value.")
            return None


def process_donor(donor_name):
    try:
        if donor_db[donor_name]:
            print("\nAn existing patron!\n")
            return donor_name
    except KeyError:
        print("\nA new donor!\n")
        donor_db[donor_name] = []
        return donor_name


def list_donors():
    for i in donor_db:
        print("{}".format(i))


def donor_input_flow():
    while True:
        response = elicit_donor()
        if validate_input_donor(response):
            if response == 'List':
                list_donors()
            else:
                donor_name = process_donor(response)
                return donor_name


def print_single_thanks(recipient, donation, total_donations):
    print(f"Dearest {recipient},\n"
          "We are writing to formally thank you for your generous"
          f" donation of ${donation}.\n"
          f"To date, you have donated ${total_donations} "
          "to our honorable mission.\n"
          "You are truly a valuable patron, and we thank you "
          "for your service (and money)")


def single_thank_you():
    """Prints a letter to user-specified donor,
    including recent and historical donation amounts"""
    recipient = donor_input_flow()
    donation = donation_input_flow()
    store_new_donation(recipient, donation)
    total_donations = sum_donations(recipient)
    print_single_thanks(recipient, donation, total_donations)


def elicit_donation():
    return input("How much did they donate?\n")


def validate_donation(donation_response_str):
    """Returns the donation amount from the user"""
    while True:
        try:
            if float(donation_response_str):
                print("\nNice!\n")
                return donation_response_str
        except ValueError:
            print("\nJust a number is fine.\n")
            return None


def donation_input_flow():
    while True:
        response = elicit_donation()
        if validate_donation(response):
            return response


def store_new_donation(donor, donation):
    """Stores the donation amount in the donor database"""
    updated_donations = donor_db[donor]
    updated_donations.append(float(donation))
    donor_db[donor] = updated_donations


def sum_donations(donor_name):
    """Returns sum of all historical donor donations"""
    return round(sum(donor_db[donor_name]), 2)


def sort_key(donor_name):
    """Returns the key to sort donations by"""
    return round(sum(donor_db[donor_name]))


def get_report():
    sorted_donor_db = sorted(donor_db, key=sort_key, reverse=True)
    for i in sorted_donor_db:
            donor_name = i
            donor_total = round(sum(donor_db[i]), 2)
            number_donations = len(donor_db[i])
            average_donation = round(donor_total/number_donations)
            print("{:20} ${:>19} {:>20} ${:>20}".format(
                donor_name, donor_total, number_donations, average_donation))


def create_report():
    """Prints a list of all the donors, their total donation amount,
    the total number of donations they've made,
    and the average donation amount,
    in descending order based on total amount given"""
    str_header_formatting = "{:^20}|" * 4
    str_grid_formatting = "-" * 21*4
    print(str_header_formatting.format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(str_grid_formatting)
    get_report()


def generate_all_thanks():
    """Creates text files containing a thank you letter to each of the donors.
    Document provides their total amount contributed, as well as their most
    recent donation amount."""
    for i in donor_db:
        most_recent_donation = ''.join(str(e) for e in donor_db[i][-1:])
        with open(f'{i}.txt', 'w') as f:
            f.write(f"Dearest {i},\n"
                    "We are writing to formally thank you for your most recent"
                    f" donation of ${most_recent_donation}.\n"
                    f"To date, you have donated ${sum_donations(i)} "
                    "to our honorable mission.\n"
                    "You are truly a valuable patron, and we thank you "
                    "for your service (and money).\n"
                    "Kindest regards\n"
                    "Baron Von Munchausen")
        print(f'Thank you letter created for {i}')
    print('\nAll Thank You letters have been created.\n')


def exit_program():
    """Exits the interactive script"""
    print("\nOk Bye!\n")
    sys.exit()


def launch_user_interface():
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
        try:
            arg_dict[response]()
        except KeyError:
            print("\nNot a valid choice! Try again.\n")

if __name__ == "__main__":
    launch_user_interface()
