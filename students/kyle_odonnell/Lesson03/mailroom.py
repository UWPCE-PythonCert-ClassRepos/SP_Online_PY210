# ------------------------------------------------------------------------ #
# Title: mailroom.py
# Description: Assignment for Lesson03
# KODonnell,10.25.2020,created script
# KODonnell,11.10.2020, updated script to use lists instead of dicts
# ------------------------------------------------------------------------- #


# Data -------------------------------------------------------------------- #

# Database for donor information
donor_list = [
    ["William Gates, III", 653784.49, 2, 326892.24],
    ["Mark Zuckerberg", 16396.10, 3, 5465.37],
    ["Jeff Bezos", 877.33, 1, 877.33],
    ["Paul Allen", 708.42, 3, 236.14],
    ["Elon Musk", 50.00, 2, 25.00]
]

# List of cancel words
CANCEL_LIST = ["cancel", "nevermind", "stop", "menu", "never mind"]


# Processing  ------------------------------------------------------------- #
def add_donation_amount(name, donation, db):  # Add new donation to database
    """ Add new donation to database
    :param name: (string) with name of donor:
    :param donation: (float) amount of donation:
    :param db: (list) of dictionaries with donation information:
    :return: (list) of dictionaries
    """
    for entry in db:
        if name.lower() == entry[0].lower():
            total = float(donation) + float(entry[1])
            num = int(entry[2]) + 1
            average = round((total/num), 2)
            entry[1] = total
            entry[2] = num
            entry[3] = average
            break
    else:
        new_entry = [name.title(), donation, 1, donation]
        db.append(new_entry)
    return db


# Presentation (Input/Output)  -------------------------------------------- #
def menu_options():  # Display menu options
    """ Print menu for users
    :return: nothing
    """
    print('''
    ******MENU OPTIONS*******
    Option 1: Send a Thank You
    Option 2: Create a Report
    Option 3: Exit \n''')


def show_names(db):  # Display list of donor names
    """ Print list of donor names
    :param db: (list) of dictionaries with donation information
    :return: nothing
    """
    for i, entry in enumerate(db):
        print(str(i + 1) + ".", "Donor Name:", entry[0])


def prompt_menu_option():  # Elicit menu option
    """ Prompt menu option
    :return: string
    """
    menu_option = input("Please select an option from the menu (1-3): ")
    return menu_option


def enter_name():  # Elicit donor name
    """ Prompt donor name
    :return: string
    """
    name = input("Please enter a donor's full name: ")
    return name


def enter_donation(name):  # Elicit donation amount
    """ Prompt donation amount for donor
    :param name: (string) with name of donor:
    :return: float
    """
    donation = round(float(input("Please enter the donation amount from {}: ".format(name))), 2)
    return donation


def thank_you_letter(name, donation):  # Print thank you letter
    """ Print thank you letter for donors
    :param name: (string) with name of donor
    :param donation:  (float) with amount of donation
    :return: nothing
    """
    print("""
    Dear {},
    Thank you for your recent donation of ${:.2f} to our organization.
    We rely on the generous contributions of kind people like you to help fund our cause and make the world a better place.
    Sincerely,
    Kyle at Kelby Doggo Inc.""".format(name, donation))


def get_total_given(db):  # Return total total donated amount per donor
    """ Get total donations per donor
    :param db: (list) of dictionaries with donor information
    :return: float
    """
    return db[1]


def create_report(db):  # Generate report based on donor database
    """ Print report of donor database
    :param db: (list) of dictionaries with donor information
    :return: nothing
    """
    db.sort(key=lambda x:x[1], reverse=True)  # Sort table by total donated amount
    heading = "| {dn:<20s}\t| {tg:<10s}\t| {ng:<10s} | {ag:<10s}   |".format
    row = "{dn:<20s} \t {ds:<1s} {tg:>9.2f} \t {ng:>10d} \t {ds2:<1} {ag:>9.2f} ".format
    print(heading(dn="Donor Name", tg="Total Given", ng="Num Gifts", ag="Average Gift"))
    print("-----------------------------------------------------------------------")
    for entry in db:
        print(row(dn=entry[0], ds="$", tg=entry[1],
                  ng=entry[2], ds2="$", ag=entry[3]))


def welcome_message():  # Display welcome message
    """ Print welcome message when program is launched
    :return: nothing
    """
    print("\nWelcome to the Mailroom Program!")


def close_app():  # Display message when user leaves
    """ Print goodbye message when user closes program
    :return: nothing
    """
    print("Closing Mailroom App...Goodbye!")


# Main Body of Script  ---------------------------------------------------- #
if __name__ == '__main__':
    welcome_message()
    while True:
        menu_options()
        choice = prompt_menu_option()
        if choice == "1":  # Prompt donation information
            while True:
                name_string = enter_name()
                if name_string.lower() in CANCEL_LIST:  # Cancel task
                    break
                elif name_string.lower().strip() == "list":  # Print donor names
                    show_names(donor_list)
                else:
                    try:
                        donation_amount = enter_donation(name_string)  # Prompt donation amount
                        donor_list = add_donation_amount(name_string, donation_amount, donor_list)
                        thank_you_letter(name_string, donation_amount)
                        break
                    except ValueError:
                        print("Entry failed: Donations must be entered as a number!")
                        break
        elif choice == "2":
            create_report(donor_list)
        elif choice == "3":
            close_app()
            break
        else:
            pass
