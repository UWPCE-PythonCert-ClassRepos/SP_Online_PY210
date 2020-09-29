#!/usr/bin/env python3

import sys


donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33, 3, 555, 132, 77, 1],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "Brax Dingle": [2331, 32322.87, 5566.20, 3323.23, 76, 323, 3.87]
            }


def elicit_donor():
    '''Simple input to receive donor name'''
    return input("\nTo whom should we address this Thank You?\n"
                 "(Type 'list' to view existing donors)\n\n").title()


def validate_input_donor(response_str):
    '''Checks response string for certain conditions'''
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
    '''Returns donor name after validating or adding name to donor db'''
    try:
        if donor_db[donor_name]:
            print("\nAn existing patron!\n")
            return donor_name
    except KeyError:
        print("\nA new donor!\n")
        donor_db[donor_name] = []
        return donor_name


def list_donors():
    '''Prints names of all donors'''
    for i in donor_db:
        print("{}".format(i))


def donor_input_flow():
    '''Continues to ask for valid input until given'''
    while True:
        response = elicit_donor()
        if validate_input_donor(response):
            if response == 'List':
                list_donors()
            else:
                donor_name = process_donor(response)
                return donor_name


def print_single_thanks(recipient, donation, total_donations):
    '''Prints a summary thank you letter to a donor'''
    print(f"Dearest {recipient},\n"
          "We are writing to formally thank you for your generous"
          f" donation of ${donation}.\n"
          f"To date, you have donated ${total_donations} "
          "to our honorable mission.\n"
          "You are truly a valuable patron, and we thank you "
          "for your service (and money)")


def single_thank_you():
    '''Process flow for storing a donation and sending a thank you letter'''
    recipient = donor_input_flow()
    donation = donation_input_flow()
    store_new_donation(recipient, donation)
    total_donations = sum_donations(recipient)
    print_single_thanks(recipient, donation, total_donations)


def elicit_donation():
    '''Simple function to receive donation amount'''
    return input("How much did they donate?\n")


def validate_donation(donation_response_str):
    '''Logic for handling user input donation'''
    while True:
        try:
            if float(donation_response_str):
                print("\nNice!\n")
                return donation_response_str
        except ValueError:
            print("\nJust a number is fine.\n")
            return None


def donation_input_flow():
    '''Asks for valid donation until given'''
    while True:
        response = elicit_donation()
        if validate_donation(response):
            return response


def store_new_donation(donor_name, donation):
    '''Updates donor db with new donation'''
    updated_donations = donor_db[donor_name]
    updated_donations.append(float(donation))
    donor_db[donor_name] = updated_donations


def sum_donations(donor_name):
    '''Returns sum of all historical donor donations'''
    return round(sum(donor_db[donor_name]), 2)


def sort_key(donor_name):
    '''Returns key with which to sort donations'''
    return round(sum(donor_db[donor_name]))


def get_report():
    '''Prints a list of all the donors, their total donation amount,
    the total number of donations they've made,
    and the average donation amount,
    in descending order based on total amount given'''
    sorted_donor_db = sorted(donor_db, key=sort_key, reverse=True)
    counter = 0
    for i in sorted_donor_db:
        donor_name = i
        donor_total = round(sum(donor_db[i]), 2)
        number_donations = len(donor_db[i])
        average_donation = round(donor_total/number_donations)
        print("{:20} ${:>19} {:>20} ${:>20}".format(
            donor_name, donor_total, number_donations, average_donation))
        counter += 1
    return counter


def create_report():
    '''Prints donation summary report'''
    str_header_formatting = "{:^20}|" * 4
    str_grid_formatting = "-" * 21*4
    print(str_header_formatting.format(
          "Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print(str_grid_formatting)
    get_report()


def generate_all_thanks():
    '''Creates text files containing a thank you letter to each of the donors.
    Document provides their total amount contributed, as well as their most
    recent donation amount.'''
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
    '''Exits the interactive script'''
    print("\nOk Bye!\n")
    sys.exit()


def launch_user_interface():
    '''Continuously asks the user for next task'''
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
