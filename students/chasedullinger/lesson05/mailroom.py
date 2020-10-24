#!/usr/bin/env python3
# PY210 Lesson 05 MailRoom 3 - Chase Dullinger

import sys

donor_db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            }


def get_send_thank_you_prompt():
    """Display menu and return selection for send thank you screen.
        :param: None
        :return: Input object
    """
    return input("Enter name of donor or type 'list' for list of current donors.\
'back' returns to main menu'> ")

def get_send_thank_you_selection():
    """Returns a selection dictionary for send thank you screen"""
    return {"list": show_donor_list}


def send_thank_you():
    """Selection to enter a donation and/or add a donor and then generate a
    thank you letter.
        :param: None
        :return: None
    """
    while True:
        user_input = get_send_thank_you_prompt()
        if user_input == "back":
            break
        get_send_thank_you_selection().get(user_input,
                                           add_donation)(user_input)


def show_donor_list(dummy_param):
    """Display donor list by looping through existing donors in donor_db
        :param dummy_param: dummy param to maintain compatibility with
                            add_donation method
        :return: None
    """
    print("\n")
    print("Current donors are:")
    for donor in donor_db:
        print(donor)
    print("\n")


def add_donor(donor):
    """ Adds a donor to the donor database
        :param donor: string containing donor's name
        :return: None
    """
    donor_db[donor] = []


def add_donation(donor):
    """ Adds a donation to a donor in to the donor database, then creates the
    thank you note.
            :param donor: string containing donor's name
            :return: None
    """
    response = input(f"Enter donation amount for {donor} .\
 'back' returns to main menu> ")
    if response == 'back':
        return
    if donor not in donor_db:
        add_donor(donor)
    donor_db[donor].append(float(response))

    print(compose_email(donor, float(response)))


def compose_email(donor, amount):
    """ Writes the email note and prints it to the screen.
    :param donor: string containing the donors name_list
    :param amount: string containing the donation amount
    :return: None """
    return f"\nDear {donor},\n\
Thank you for your generous gift of ${amount:.2f}! It will help Local Charity\
 achieve our mission.\n\
Best regards,\n\
Local Charity\n\n"


def get_donor_stats(donor):
    """Return donor donation stats.
    :param donor: donor item from donor_db (donor_name, [donation list])
    :return total_given: float summation of total gifts given
    :return total_gifts: int number of gifts given
    :return average_gift: float average value of gifts
    """
    total_given = sum(donor_db[donor])
    total_gifts = len(donor_db[donor])
    average_gift = total_given / total_gifts
    return total_given, total_gifts, average_gift


def create_report():
    """Display donor list by looping through existing donors in donor_db and
    and show their donation data.
        :param: None
        :return: None
    """
    print("\n")
    print("Donor Name                | Total Given | Num Gifts | Average Gift\n\
------------------------------------------------------------------")
    total_gift_dict = {}  # will be used later for sorting by most given
    donor_stats = {}
    for donor in donor_db:
        total_given, total_gifts, average_gift = get_donor_stats(donor)
        donor_stats[donor] = {"name": donor,
                              "total_given": total_given,
                              "total_gifts": total_gifts,
                              "average_gift": average_gift
                              }
        # use list to guard against multiple donors giving same total
        total_gift_dict.setdefault(total_given, [])

        total_gift_dict[total_given].append(donor)
    for gift in sorted(total_gift_dict, reverse=True):
        for donor in total_gift_dict[gift]:
            print("{name:<26} $ {total_given:>11.2f} {total_gifts:>10}\
  $ {average_gift:>11.2f}".format(**donor_stats[donor]))

    print("\n")
    return


def create_all_letters():
    """Writes letters for all donors and saves them to disk"""
    for donor in donor_db:
        total_given, total_gifts, average_gift = get_donor_stats(donor)
        with open(f"{donor}.txt", "w") as f:
            f.write(compose_email(donor, total_given))


def quit_program():
    """Cleanly exit the program"""
    sys.exit()


def get_main_prompt():
    """Display menu and return selection.
        :param: None
        :return: Input object
    """
    return input("Select an action:\n\
    1) Send a thank you\n\
    2) Create a report\n\
    3) Send letters to all donors\n\
    4) Quit the program\n\
    \n\
Enter number you wish to choose > ")

def get_main_selection():
    return {"1": send_thank_you,
            "2": create_report,
            "3": create_all_letters,
            "4": quit_program}


def invalid_entry():
    """Informs user of invalid menu selection"""
    print("\nInvalid Entry\n")

def create_menu(prompt, selection_dict):
    """Creates a menu given a prompt and a selection dictionary
    :param prompt: input object with get_prompt
    :param selection_dict: dictionary object user input as keys and methods as
                           values
    """
    user_input = prompt()
    selection_dict.get(user_input, invalid_entry)()

def main():
    """ Main menu
        :param: None
        :return: None
    """
    while True:
        create_menu(get_main_prompt, get_main_selection())

if __name__ == "__main__":
    main()
