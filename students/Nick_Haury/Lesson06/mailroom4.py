#!/usr/bin/env python3
import sys  # importing for script exit functionality

'''
This is the Lesson05 rendition of the mailroom program.  Copying the dictionary
mailroom program, but then attempting to replace functionality with
exceptions and comprehensions wherever sensible to do so.

Program starts with a list of donors toupled with a list of amounts they have
donated in the past.  The program gives a user the option to add new donations
from previous donors to the list.  It also gives the option to add a new donor
along with their first donation.  After a donation amount is recorded, a
template 'thank you' email is automatically generated.  A user also has the
option to create a report showing details about all donors.  This report
contains names, sum of donations, number of donations, and average donation
amount; donors sorted by largest donation sum to smallest.
'''

# create initial donor dictionary
donors = {
    "William Gates, III": [653772.32, 12.17],
    "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
    "Jeff Bezos": [877.33],
    "Paul Allen": [663.23, 43.87, 1.32]
}


def quit():
    print("Closing mailroom... Goodbye")
    sys.exit()  # exit the script


def main():
    '''
    Prompt the user for input.  Current choices are to send a thank you or to
    create a report to display all the current donors and respective donation
    totals and averages.  The user can also quit.
    '''

    # functions for users to choose from
    choice_dict = {
                    "1": thank_you,
                    "2": create_report,
                    "3": write_letters,
                    "4": quit
    }

    print("Welcome to the mailroom program")
    prompt = "\n".join((
        "Please choose a function from the below options:",
        "1 - Send a Thank You to a single donor.",
        "2 - Create a Report.",
        "3 - Write letters to all donors to file.",
        "4 - Quit",
        ">> "
        ))

    while True:
        choice = input(prompt)
        try:
            choice_dict[choice]()
        except KeyError:
            print(str(choice) + " is an invalid selection, "
                  "please make a valid selection \n")


def thank_you():
    '''
    prompts the user for a full name.  If the user types "list", then print
    a list of donor names and re-prompt.  If a name is typed that is not
    in the list, add the name to the list.  If a name is typed that is
    already in the list, then use it.  Once a name is selected, a
    donation amount is specified.  Donation amount input by users is then
    added to the donation history of the name.  Email is then automatically
    drafted using string formatting thanking the donor for the donation.
    Return to main prompt after.
    '''

    print()
    while True:
        ty_input = input('Type "list" to display a list of donor names. '
                         'Otherwise enter a name you would like to add a '
                         'donation for:\n>>')

        if ty_input.lower() == "list":
            print("\nCurrent Donors: ")
            for row in get_donor_list():
                print(row)
            print()
        else:
            try:
                donation_amount = float(input("\nPlease enter donation amount:"
                                              "\n>>"))
                if donation_amount <= 0:
                    raise ValueError
            except ValueError:
                print("\nPlease only enter a single positive number for "
                      "donation amount\n")
            else:
                add_donation(ty_input, donation_amount)
                print(
                    "\n", create_email_text(ty_input, donation_amount), sep=""
                    )
                break


def get_donor_list():
    return list(donors.keys())


def create_email_text(donor_name, donation_amount):
    '''
    Takes a donor's name and donation amount as parameters, and then creates
    an email template thanking them for their donation
    '''

    return(f"Dear {donor_name},\n\n"
           f"It is with incredible gratitude that we accept your wonderfully "
           f"generous donation of ${donation_amount:,.2f}.  Your "
           "contribution will truly make a difference in the path forward "
           "towards funding our common goal."
           "\n\nEver Greatefully Yours,\n\n"
           "X" + ("_" * 20) + "\n")


def add_donation(donor_name, donation_amount):
    '''
    Adds donation amount to donor's list of donations.  If donor does not exist
    yet, they are created and added to the donor dictionary.
    '''
    donors.setdefault(donor_name, []).append(donation_amount)


def create_report():
    '''
    Prints a list of donors, sorted by total historical donation
    amount.  Includes donor name, total donated, number of donations,
    and average donation amount.
    '''
    print("\nDonor Name" + " "*15 + "|  Total Given  | Num Gifts |   "
          "Average Gift")
    print("- "*36)
    for row in get_report_text():
        print(row)
    print()


def get_report_text():

    def sort_key(donor):
        # sorting by the sum of donations
        return sum(donors[donor])

    keys_by_sum = sorted(donors, key=sort_key, reverse=True)
    text_list = []
    for key in keys_by_sum:
        donor_name = key
        donor_sum = sum(donors[key])
        donor_count = len(donors[key])
        donor_average = donor_sum/donor_count
        text_list.append(f"{donor_name:26}${donor_sum:14,.2f}{donor_count:11}"
                         f"  ${donor_average:16,.2f}")
    return text_list


def write_letters():
    for key in donors:
        with open(f'{key}.txt', 'w') as f:
            f.write(create_email_text(key, donors[key][-1]))
    print()


if __name__ == "__main__":
    '''
    run main prompt
    '''

    main()
