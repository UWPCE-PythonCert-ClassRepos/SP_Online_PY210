# Isabella Kemp
# Mailroom part 4
# 2/24/2020

import sys
import pathlib
import time

# List of donors and the amounts they have donated
donors = {"John": [150080.00, 41.28],
          "Irene": [1600.00, 24.47],
          "Rob": [19000.00, 200.47],
          "Kathy": [819.00, 34.5],
          "Laureen": [830.00, 47.00, 982.13],
          "Miles": [24.50, 87.00, 193.00]}

main_prompt = ("\n\nWelcome to the Mailroom! Please choose an option from the menu:"
               "\n1. Send a Thank you"
               "\n2. Create a Report"
               "\n3. Send letters to all donors"
               "\n4. Quit"
               "\n\n ----> ")


# Common function to get input from user, call with a prompt string
def get_user_input(prompt_string):
    response = input(prompt_string)
    return response


# User can enter 'list' to get list of existing donors
# User can enter 'listall' to get list of donors and their donations
# User can enter existing donor name, new donation, donation is added to list
# User can enter a new donor, new donation, user and donation is added to list
# We finish with a thank you
def thank_you():
    while True:
        name = get_user_input("Enter a donor name to send a thank you letter, "
                              "'list' or 'listall' for list of donors, '4' will exit: ")
        if name == "list":
            print(list(donors))
        elif name == "listall":
            # entire record name with donations
            for key in donors:
                print("{0} {1}". format(key, donors[key]))
        elif name == '4':  # quit and return to main menu
            print("Finished processing thanks to donors...\n\n")
            return
        else:
            donation = get_donation()
            if donor_exists(name):
                # donor is in our list,
                # Adding donation to the existing donor name
                add_donation(name, donation)
            else:
                # new donor is not in our list, add the donor to our list
                # get donation amount, add donation to list, send thank you
                add_Donor(name, donation)

            email(name, donation)

# end thank_you


# Determines if donor name is in donors dict. Returns True or False
def donor_exists(name):
    if donors.get(name):
        return True
    else:
        return False


# Checks to see if provided name is in our donor list
# returns donor record if found, else None
def get_donor(donor_name):
    return donors.get(donor_name)


# get donation amount
def get_donation():
    while True:
        money = get_user_input("Please enter a donation amount: $ ")
        try:
            amount = float(money)
            if amount <= 0:
                print("Invalid value")
            else:
                return amount
        except ValueError:
            print("Invalid value")


# Adding a donor with their donation
def add_Donor(donor_name, donation):
    donors[donor_name] = [donation]


# Adding donation to a donors name
def add_donation(name, donation):
    record = donors[name]
    record.append(donation)
    donors[name] = record


# Send thank you to donor
def email(name, amount):
    formatted_email = ("Thank you {}, for your generous donation of ${:.2f} !".format(name, amount))
    print(formatted_email)
    return formatted_email


# Content that sending_letters uses to format letters for each donor name
def write_letter(first_name):
    charity = sum(donors[first_name])

    letters = ('Dear {0},\n'
                        'Thank you for your donations totaling '
                        '$ {1:,}. We very much appreciate it.\n'
                        'All the best,\n'
                        '- Izzy (Charity President)').format(first_name, charity)
    return letters


# Sends a thank you letter for each donor and writes each letter to disk as a text file.
def sending_letters():
    print("Sending a letter to all donors...")

    pth = pathlib.Path('./')
    folder = pth.absolute()

    for donor in donors.keys():
        first_name = donor.split()[0]
        file_format = "{0}.txt".format(first_name)
        file_path = folder / file_format
        try:
            print(file_path)
            with open(file_path, 'w') as write_file:             
                write_file.write(write_letter(first_name))
        except IOError:
            print("Unable to write to file")

    print("Letters have been sent to all donors. Thank you.")


def sort_reportdata(donors):
    # Takes donors and sorts it representing each item in the list
    donors_list = list(donors.items())
    sort_donor = sorted(donors_list, key=sort_key, reverse=True)
    return sort_donor


def format_report(sort_donor):
    # For loop going through donors and calculating sum, number of donations, and average donations
    rows = []
    for donor in sort_donor:
        total = sum(donor[1])
        num_donations = len(donor[1])
        average = total/num_donations
        row_string = ('{:<20} ${:>11,.2f}{:>13}            ${:>11,.2f}'.format(
            donor[0], total, num_donations, average))
        rows.append(row_string)
    return rows


# Creates a report of donor name, total donated, number of donations, and avg donation.
def print_report():
    print("Generating report of all donors...")
    print("\n{:<19}| {:<13} | {:<13} | {:>13}".format('Donor Name', 'Total Donated',
                                                      'Number of Donations',
                                                      'Avg. Donation Amount'))
    print("-" * 80)
    for row in format_report(sort_reportdata(donors)):
        print(row)


# define sort key
def sort_key(donor):
    return sum(donor[1])


def exit_menu():
    print("Thank you, Goodbye...")
    sys.exit()


def main():
    switch_func_dict = {
        "1": thank_you,
        "2": print_report,
        "3": sending_letters,
        "4": exit_menu,
    }

    while True:
        try:
            num = get_user_input(main_prompt)
            switch_func_dict.get(num)()
        except TypeError:
            print("Main menu input is invalid, enter 1 2 3 4 only please")
        finally:
            time.sleep(1)


if __name__ == "__main__":
    main()
