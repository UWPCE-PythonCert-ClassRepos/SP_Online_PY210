# ------------------------------------------------------------------------ #
# Title: mailroom.py
# Description: Assignment for Lesson04
# KODonnell,10.25.2020,created script
# KODonnell,11.05.2020 added switch dict menu
# KODonnell,11.07.2020 added function to generate letters
# KODonnell,11.10.2020 split file writing functions into multiple funcs
# KODonnell,11.14.2020 updated to *actually* have a dictionary database
# ------------------------------------------------------------------------- #


# Data -------------------------------------------------------------------- #

# Dictionary database for donor information
donor_dict = {
    "William Gates, III": [653784.49, 2, 326892.24],
    "Mark Zuckerberg": [16396.10, 3, 5465.37],
    "Jeff Bezos": [877.33, 1, 877.33],
    "Paul Allen": [708.42,  3, 236.14],
    "Elon Musk": [50.00, 2, 25.00]
}


# Processing  ------------------------------------------------------------- #
def add_donation_amount(name, donation, db):  # Add new donation to database
    """ Add new donation to database
    :param name: (string) with name of donor:
    :param donation: (float) amount of donation:
    :param db: (dictionary) with donor information:
    :return: dictionary
    """
    if name in db:
        [total, num] = db[name][:2]
        total_update = donation + total
        num_update = num + 1
        average_update = round(total/num_update, 2)
        db[name] = [total_update, num_update, average_update]
    else:
        db[name] = [donation, 1, donation]
    return db


def generate_one_letter(db):  # Create letter file for one donor
    """ Write letter for one donor to file
    :param db: (dictionary) with donor information
    :return: db
    """
    name = input("What donor would you like to write to? ")
    try:
        name_list = (name.replace(",", "")).split(" ")
        file_name = ("_".join(name_list)) + ".txt"
        with open(file_name, "w") as a_file:
            a_file.write(letter_text(name.title(), db[name.title()][0]))
        print("Check your local directory for a letter to {}".format(name))
    except KeyError:
        print("{} is not in your database!".format(name))
    press_enter_to_continue()
    return db


def generate_all_letters(db):  # Create letter file for all donors
    """ Generate letter files for all donors in database
    :param db: (dictionary) with donor information
    :return: db
    """
    for i, v in db.items():
        name_list = (i.replace(",", "")).split(" ")
        file_name = ("_".join(name_list)) + ".txt"
        with open(file_name, "w") as a_file:
            a_file.write(letter_text(i.title(), v[0]))
    print("Check your local directory for letter files!")
    press_enter_to_continue()
    return db


def close_app(db):
    """ Print goodbye message and exit
    :param db: (dictionary) with donor information:
    :return: nothing
    """
    print("Closing the Mailroom Program...Goodbye!")
    exit()


# Presentation (Input/Output)  -------------------------------------------- #
def welcome_message():  # Display welcome message
    """ Print welcome message when program is launched
    :return: nothing
    """
    print("\nWelcome to the Mailroom Program!")


def menu_options():  # Display menu options
    """ Print menu options for users
    :return: nothing
    """
    print('''
    ******MENU OPTIONS*******
    Option 1: Write Letter for New Donation
    Option 2: Generate Letters for Donors
    Option 3: Create a Report
    Option 4: Exit \n''')


def prompt_menu_option():  # Elicit main menu option
    """ Prompt menu option
    :return: string
    """
    menu_option = input("Please select an option from the menu (1-4): ")
    return menu_option


def enter_name():  # Elicit donor name
    """ Prompt donor name
    :return: string
    """
    name = input("Please enter a donor's full name: ")
    return name


def display_names(db):  # Display list of donor names
    """ Print list of donor names
    :param db: (dictionary) with donor information
    :return: nothing
    """
    count = 1
    for i, v in db.items():
        print("{}. Donor Name: {}".format(count, i))
        count += 1


def enter_donation(name):  # Elicit donation amount
    """ Prompt donation amount for donor
    :param name: (string) with name of donor:
    :return: float
    """
    donation = round(float(input("Please enter the donation amount from {}: ".format(name))), 2)
    return donation


def create_report(db):  # Generate report based on database
    """ Print report of donor database
    :param db: (dictionary) with donor information
    :return: db
    """
    sorted_db = sorted(db.items(), key=lambda x: x[1], reverse=True)  # Sort items by total donated amount
    heading = "| {dn:<20s}\t| {tg:<15s}\t| {ng:<10s} | {ag:<15s}   |".format
    row = "{dn:<20s} \t {ds:<1s} {tg:>14.2f} \t {ng:>10d} \t {ds2:<1} {ag:>14.2f} ".format
    print(heading(dn="Donor Name", tg="Total Given", ng="Num Gifts", ag="Average Gift"))
    print("----------------------------------------------------------------------------")
    for i in sorted_db:
        name = i[0]
        print(row(dn=name, ds="$", tg=db[name][0],
                  ng=db[name][1], ds2="$", ag=db[name][2]))
    print("\n")
    press_enter_to_continue()
    return db


def new_donation_letter(db):  # Update database
    """ Add new donation to database and print letter
    :param db: (dictionary) with donor information:
    :return: db
    """
    while True:
        name_string = enter_name().title()
        if name_string.lower() == "cancel":  # Cancel task
            print("Cancelling task...")
            break
        elif name_string.lower().strip() in ["list", "go to list", "show list"]:  # Print donor names
            display_names(db)
        else:
            try:
                donation_amount = enter_donation(name_string)  # Prompt donation amount
                db = add_donation_amount(name_string.strip(" "), donation_amount, db)
                print(letter_text(name_string, donation_amount))
                break
            except ValueError:
                print("Entry failed: Donations must be entered as a number!")
                break
    press_enter_to_continue()
    return db


def generate_letter_choice(db):  # Prompt for letter writing options
    """ Write letters to text files for every donor in database
    :param db: (dictionary) with donor information:
    :return: db
    """
    file_option = int(input("""
    Okay, let's generate some letter files! You can:
    1. Create a letter for a specific donor
    2. Create letters for all donors \n
    Please select an option (1 or 2): """))
    db = switch_func_letter_dict.get(file_option)(db)
    return db


def letter_text(name, value):  # Format string for thank you letter
    """Generate thank you letter text
    :param name: (string) with name of donor
    :param value: (float) with donation amount
    :return: string
    """
    letter = """
    Dear {},
    Thank you for your collective contributions of ${:.2f} over the years.
    Your generous donations have been put to good use!
    Sincerely,
    Kyle at Kelby Doggo, Inc\n""".format(name, value)
    return letter


def press_enter_to_continue():
    """ Prompt user to press enter to continue
    :return: nothing
    """
    input("Press 'Enter' to Continue\n")


# Switch function dictionary for main menu
switch_func_dict = {
    1: new_donation_letter,
    2: generate_letter_choice,
    3: create_report,
    4: close_app
}


# Switch function dictionary for letter writing choice
switch_func_letter_dict = {
    1: generate_one_letter,
    2: generate_all_letters
}


# Main Body of Script  ---------------------------------------------------- #
if __name__ == '__main__':
    welcome_message()
    while True:
        menu_options()
        try:
            choice = int(prompt_menu_option())
            donor_dict = switch_func_dict.get(choice)(donor_dict)
        except ValueError:
            pass
