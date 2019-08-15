# --------------------------------
# 08/14/2019 Jinee Han
# Python Programming Lesson 6
# Mailroom Part 4
# ---------------------------------

'''
update
Refactor mailroom to make it testable
'''

import sys, datetime


# Donor List
donor_db = {"Kim Kardasian": [653772.32, 12.17],
            "Kendal Jenner": [877.33],
            "Gigi Hadid": [663.23, 43.87, 1.32],
            "Justin Bieber": [1663.23, 4300.87, 10432.0],
            "Will Smith": [43.23, 4000.07, 183423.2]
            }

# Display options
prompt = "\n".join(("Welcome to the donor list!",
          "Please choose from below options:",
          "1 - Send a Thank you",
          "2 - Create a Report",
          "3 - Send Thank You to All Donors",
          "4 - Exit",
          ">>> "))

def send_thank_you_note():
    '''
    Check for the user input and send a thank you once user entered
    :return: nothing
    '''
    input_value = input("Enter a full name. (Type 'list' to see the donor list)")  # Ask the name
    while input_value == 'list':
        display_list()
        input_value = input("Enter a full name. (Type 'list' to see the donor list)")

    # Store the donor name with the first character as an upper case letter
    donor_name = input_value.title()

    if not donor_present(donor_name):
        add_donor(donor_name)

    donation_amount = None
    while donation_amount is None:
        try:
            donation_amount = float(input("Please enter the donation amount: "))
        except ValueError:
            pass

    add_donation_amount(donor_name, donation_amount)
    save_thank_you_to_file(donor_name, donation_amount, format_thank_you_note(donor_name, donation_amount))


def add_donation_amount(donation_name, donation_amount):
    '''
    Add the donation amount for the current donator
    :param donation_name: donor name
    :param donation_amount: float value
    :return: nothing
    '''
    donor_db[donation_name].append(donation_amount)


def donor_present(donor_name):
    '''
    Check if the donor name is present in the dictionary
    :param donor_name:
    :return: True if donor present, False if not
    '''

    # Use a comprehension to reduce code to check if donor is present
    return len([name for name in donor_db.keys() if name == donor_name]) > 0


def display_list():
    '''
    Display the list of current donors
    :return: prints donor names
    '''
    for keys in donor_db:
        print(keys)


def add_donor(donor_name):
    '''
    Add donor name to the dictionary
    :param donor_name:
    :return: nothing
    '''
    donation_history = []
    donor_db.update({donor_name:donation_history})


def save_thank_you_to_file(donor_name, donation_amount, thank_you_note_formatted):
    '''
    Save the thank you note to file
    :param donor_name: The current donor
    :param donation_amount: The donation amount
    :param thank_you_note_formatted: The formatted note to write to file
    :return: nothing
    '''
    filename = "{}_{}_{}donations.txt".format(donor_name, donation_amount, len(donor_db[donor_name]))

    with open("{}".format(filename), "w") as f:
        f.write(thank_you_note_formatted)


def format_thank_you_note(donator, donation_amount):
    '''
    Format the thank you note before writing to file
    :param donator: The current donator
    :param donation_amount: The donation amount
    :return: a formatted thank you note
    '''
    list_object = []
    list_object.append("Dear {},\n\n".format(donator.title())  )
    list_object.append("\tThank you for your very kind donation of  ${:10.2f}!\n".format(donation_amount)  )
    list_object.append("\tIt will be put to very good use.\n\n")
    list_object.append("\t\t\tSincerely,\n")
    list_object.append("\t\t\t\t\t - The Team")

    return " ".join(list_object)


def get_donation_report_for_donor(donor, donation_amounts):
    '''
    Get the formatted text for the report generation
    :param donor: The donor name
    :param donation_amounts: The donation amounts
    :return: Formatted text for the donation report
    '''
    total = sum(donation_amounts)
    num = len(donation_amounts)
    average = total / num
    return '{:^18} ${:>12,.2f}{:^13}  ${:>12,.2f}'.format(donor, total, num, average)


def create_report():
    '''
    Create a report of all donators, and amounts in sorted order with most donations first
    :return: Prints values to console
    '''
    """Generate a tabular report of donation history"""
    header ='\n{:^18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print('-'*len(header))
    sorted_list = sorted(donor_db.items(), key=lambda x: sum(x[1]), reverse = True)
    for donor in sorted_list:
        print(get_donation_report_for_donor(donor[0], donor[1]))


def send_thank_you_to_all_donors():
    '''
    Send a thank you note to all donors
    :return: nothing
    '''
    for donor in donor_db:
        save_thank_you_to_file(donor, sum(donor_db[donor]), format_thank_you_note(donor, sum(donor_db[donor])))

    print ("All thank you notes saved.")


def exit_program():
    '''
    Exit the program
    :return: nothing
    '''
    print("Thank you for your donations!")
    sys.exit()  # exit the interactive script


input_dict = {1: send_thank_you_note, 2: create_report, 3: send_thank_you_to_all_donors, 4: exit_program}

def main():
    while True:
        try:
            response = int(input(prompt))  # continuously collect user selection
            input_dict.get(response)()
        except TypeError:
            print("Please enter a number between 1 - 4.\n")
        except ValueError:
            print("Please enter a number between 1 - 4.\n")


if __name__ == "__main__":
    main()