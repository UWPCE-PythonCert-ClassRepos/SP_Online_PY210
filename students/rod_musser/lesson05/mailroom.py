#!/usr/bin/env python3
import sys
from os import path

donors = {
    'Carmelo Anthony': [1, 50],
    'Damien Lillard': [100.50, 99, 10000],
    'CJ McCollum': [24000, 70, 100, 5, 300],
    'Hassan Whiteside': [10000],
    'Terry Stotts': [500, 500, 100, 100, 100],
}


welcome_prompt = "\n".join(("Welcome to the Local Charity Mail Room System",
                  "Please choose from the following options:",
                  "1 - Send a Thank You",
                  "2 - Create a Report",
                  "3 - Send Letters To All Donors",
                  "4 - Quit",
                  ">>> "))

letter_template = "Dear {first_name} {last_name},\n\n\
Thank you for your generous support of Rod's Early \
Retirement Fund.\n\nYour {num_donations} donation(s) \
totaling ${total_donation:.2f} makes Rod's early retirement \
dreams a reality.  Your generous support will enable Rod \
to perform critical early retirement tasks like \n\n\t- \
Mai Tais on the beach \n\t- First class airline travel \
\n\t- Alpine skiing.  \n\nAgain, thank you {first_name} \
for your generous support. \n\nSincerely, \n\nRod Musser \
\nChairperson\nRod's Early Retirement Fund"


def main():
    """
    Provides an menu in which to input what the user would like to do.
    """
    while True:
        response = input(welcome_prompt)
        try:
            response = int(response)
        except ValueError:
            print("Input must be a number.  Please try again.")
            continue
        menu_selection = main_menu_dict.get(response)
        if menu_selection is None:
            print("Not a valid option!")
        else:
            menu_selection()


def list_donors():
    """
    Prints a list of donor names.
    """
    newLine = '\n'
    print(f"{newLine.join(donors.keys())}")


def send_thank_you():
    """
    Asking this user to enter the name of a donor
    and prints out a thank you letter for the donation.

    If the donor does no exist in the donor database,
    it will add it to the donor database.

    If the user types 'list',
    it will list all the donors int eh donor database.
    """
    response = input("Please enter a full name: ")
    if response.lower() == "list":
        list_donors()
        send_thank_you()
    else:
        need_amount = True
        while need_amount:
            amount = input("Please enter the donation amount: ")
            try:
                amount = float(amount)
            except ValueError:
                print("Donation amount must be a number.  Please try again.")
                continue
            need_amount = False
            add_donation(response, amount)


def add_donation(donor_name, amt):
    """
    Records a donation and prints a thank you email.
    Expects a list which contains a donor and a list of amounts.
    """
    donors.setdefault(donor_name, []).append(amt)
    letter_data = {}
    first_last = donor_name.split(' ')
    v = donors[donor_name]
    letter_data['first_name'] = first_last[0]
    letter_data['last_name'] = first_last[1]
    letter_data['total_donation'] = sum(v[:])
    letter_data['num_donations'] = len(v)
    print(get_letter_text(letter_data))


def sort_key(donor_summary):
    """
    Returns which attribute to support a colleciton of
    donor_summary by.  In this case, donors
    should be sorted by total donated.

    :param donor_summary: A set of information about a donor including name,
     total amount donated, number of donations,
     and average donation.
    """
    return donor_summary[1]


def create_donor_summary(name, donations):
    """
    Return a set of summary donor info: name,
    total amount donated, number of donations,
    and average donation

    :param name: The full name of the donor
    :param donations: A list of donation amounts.
    """
    total_amount = sum(donations[:])
    number_of_gifts = len(donations)
    average_gift = round(total_amount / number_of_gifts, 2)
    donor_summary = [name, total_amount, number_of_gifts, average_gift]
    return donor_summary


def create_report():
    """
    Using the donor databases, creates a report of
    all donors by decending total donations
    """
    report = [create_donor_summary(name, donations) for name, donations in donors.items()]
    print_report(sorted(report, key=sort_key, reverse=True))


def print_report(report):
    """
    Formats and prints the report

    :param report: A set of information about donors
    including name, total donated, number of donations,
    and average gift
    """
    print("Donor Name" + (' ' * 16) + ("| Total Given | Num Gifts | Avergage Gift"))
    print("-" * 68)
    row = "{name:<26s} ${total:=12.2f}  {num:10d} ${avg:14.2f}".format
    for donor in report:
        print(row(name=donor[0], total=donor[1], num=donor[2], avg=donor[3]))


def send_letters():
    """
    Asks the user for directory to write a letter as a txt file
    to each donor in the donor database.
    """
    need_valid_directory = True
    letter_directory = ''
    while need_valid_directory:
        letter_directory = input("Which directory shall I write the letters in?: ")
        if not letter_directory.endswith('/'):
            letter_directory = letter_directory + '/'
        if path.isdir(letter_directory):
            need_valid_directory = False
        else:
            print(letter_directory + ' is not a valid directory.  Please try again.')

    all_letter_data = create_letter_data()
    for letter_data in all_letter_data[:]:
        letter_file_name = letter_directory + '{first_name}_{last_name}.txt'.format(**letter_data)
        with open(letter_file_name, 'w') as f:
            f.write(get_letter_text(letter_data))


def get_letter_text(letter_data):
    """
    Return a formatted string with data from letter_data
    inserted into the letter_template template.
    """
    return letter_template.format(**letter_data)


def create_letter_data():
    """
    Creates a collection of dicts to input into the letter template
    """
    all_letter_data = [build_letter_data(name, donations) for name, donations in donors.items()]
   # for k, v in donors.items():
   #     letter_data = {}
   #     first_last = k.split(' ')
   #     letter_data['first_name'] = first_last[0]
   #     letter_data['last_name'] = first_last[1]
   #     letter_data['total_donation'] = sum(v[:])
   #     letter_data['num_donations'] = len(v)
   #     all_letter_data.append(letter_data)
    return all_letter_data


def build_letter_data(name, donations):
    """
    Return a dic of summary donor info: name,
    total amount donated, number of donations,
    and average donation

    :param name: The full name of the donor
    :param donations: A list of donation amounts.
    """
    letter_data = {}
    first_last = name.split(' ')
    letter_data['first_name'] = first_last[0]
    letter_data['last_name'] = first_last[1]
    letter_data['total_donation'] = sum(donations[:])
    letter_data['num_donations'] = len(donations)
    return letter_data

def exit_program():
    """
    Closes the program
    """
    print("You made a difference today.  Have a good one!")
    sys.exit()


main_menu_dict = {
    1: send_thank_you,
    2: create_report,
    3: send_letters,
    4: exit_program
}

if __name__ == "__main__":
    main()
