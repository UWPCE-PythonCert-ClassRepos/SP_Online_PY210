# ------------------------------------------------------------------------ #
# Title: mailroom.py
# Description: Assignment for Lesson04
# KODonnell,10.25.2020,created script
# KODonnell,11.05.2020 added switch dict menu
# KODonnell,11.07.2020 added function to generate letters
# KODonnell,11.10.2020 split file writing functions into multiple funcs
# KODonnell,11.14.2020 updated to *actually* have dictionary database
# ------------------------------------------------------------------------- #


# Data -------------------------------------------------------------------- #

# Dictionary database for donor information
donor_list = {
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
    :return: (list) of dictionaries
    """

    if name in db.keys():
        [total, num] = donor_list[name][:2]
        total_update = donation + total
        num_update = num + 1
        average_update = round(total/num_update,2)
        donor_list[name] = [total_update, num_update, average_update]

    else:
        db[name] = [donation, 1, donation]
    return db


def generate_one_letter(db):
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
    return db


def generate_all_letters(db):
    """ Generate letter files for all donors in database
    :param db: (dictionary) with donor information
    :return: db
    """
    for i, v in db:
        name_list = (i.replace(",", "")).split(" ")
        file_name = ("_".join(name_list)) + ".txt"
        with open(file_name, "w") as a_file:
            a_file.write(letter_text(i.title(), db[v[0].title()]))
    return db


def close_app(db):  # Display message when user leaves
    """ Print goodbye message when user closes program
    :param db: (dictionary) with donor information:
    :return: nothing
    """
    print("Closing Mailroom App...Goodbye!")
    quit()


# Presentation (Input/Output)  -------------------------------------------- #
def welcome_message():  # Display welcome message
    """ Print welcome message when program is launched
    :return: nothing
    """
    print("\nWelcome to the Mailroom Program!")


def menu_options():  # Display menu options
    """ Print menu for users
    :return: nothing
    """
    print('''
    ******MENU OPTIONS*******
    Option 1: Draft a Thank You
    Option 2: Create a Report
    Option 3: Generate Letters
    Option 4: Exit \n''')


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


def display_names(db):  # Display list of donor names
    """ Print list of donor names
    :param db: (list) of dictionaries with donation information
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


def create_report(db):  # Generate report based on donor database
    """ Print report of donor database
    :param db: (list) of dictionaries with donor information
    :return: nothing
    """
    db = sorted(db.items(), key=lambda x:x[1], reverse=True)  # Sort table by total donated amount
    heading = "| {dn:<20s}\t| {tg:<10s}\t| {ng:<10s} | {ag:<10s}   |".format
    row = "{dn:<20s} \t {ds:<1s} {tg:>9.2f} \t {ng:>10d} \t {ds2:<1} {ag:>9.2f} ".format
    print(heading(dn="Donor Name", tg="Total Given", ng="Num Gifts", ag="Average Gift"))
    print("-----------------------------------------------------------------------")
    for i, v in db:
        print(row(dn=i, ds="$", tg=v[0],
                  ng=v[1], ds2="$", ag=v[2]))
    return list(db)


def option_one_func(db):  # Update database
    """ Add new name or new donation to existing name to donor database
    :param db: (dictionary) with donor information:
    :return: db
    """
    while True:
        name_string = enter_name()
        if name_string.lower() == "cancel":  # Cancel task
            break
        elif name_string.lower().strip() == "list":  # Print donor names
            display_names(db)
        else:
            try:
                donation_amount = enter_donation(name_string)  # Prompt donation amount
                db = add_donation_amount(name_string, donation_amount, db)
                print(letter_text(name_string, donation_amount))
                break
            except ValueError:
                print("Entry failed: Donations must be entered as a number!")
                break
    return db


def generate_letter_choice(db):
    """ Write letters to text files for every donor in database
    :param db: (dictionary) with donor information:
    :return: db
    """
    file_option = int(input("""
    Okay, let's create some letters! You can:
    1. Create a letter for a specific donor
    2. Create letters for all donors \n
    Please select an option (1 or 2): """))
    db = switch_func_letter_dict.get(file_option)(db)
    return db


def letter_text(name, value):
    letter = """
    Dear {},
    Thank you for your collective contributions of ${:.2f} over the years.
    Your generous donations have been put to good use!
    Sincerely,
    Kyle at Kelby Doggo, Inc""".format(name, value)
    return letter


switch_func_dict = {
    1: option_one_func,
    2: create_report,
    3: generate_letter_choice,
    4: close_app
}

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
            donor_list = switch_func_dict.get(choice)(donor_list)
        except ValueError:
            pass
