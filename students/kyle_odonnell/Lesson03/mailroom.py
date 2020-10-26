



# if __name__ == '__main__':

# Data -------------------------------------------------------------------- #
donor_list = [
    {"Donor Name": "William Gates, III", "Total Given": 653784.49, "Num Gifts": 2, "Average Gift": 326892.24},
    {"Donor Name": "Mark Zuckerberg", "Total Given": 16396.10, "Num Gifts": 3, "Average Gift": 5465.37},
    {"Donor Name": "Jeff Bezos", "Total Given": 877.33, "Num Gifts": 1, "Average Gift": 877.33},
    {"Donor Name": "Paul Allen", "Total Given": 708.42, "Num Gifts": 3, "Average Gift": 236.14},
    {"Donor Name": "Elon Musk", "Total Given": 50.00, "Num Gifts": 2, "Average Gift": 25.00}
]


# Processing  ------------------------------------------------------------- #
def add_donation_amount(donor, donation, db):
    """ Add new donation to database
    :param donor: (string) with name of donor:
    :param donation: (float) amount of donation:
    :param db: (list) of dictionaries with donation information:
    :return: (list) of dictionaries
    """
    in_list = False
    for entry in db:
        if donor.lower() == entry["Donor Name"].lower():
            total = float(donation) + float(entry["Total Given"])
            num = int(entry["Num Gifts"]) + 1
            average = round((total/num), 2)
            entry["Total Given"] = total
            entry["Num Gifts"] = num
            entry["Average Gift"] = average
            in_list = True
    if not in_list:
        new_entry = {"Donor Name": donor.title(), "Total Given": donation, "Num Gifts": 1, "Average Gift": donation}
        db.append(new_entry)
    return db


# Presentation (Input/Output)  -------------------------------------------- #
def menu_options():
    """ Print menu for users
    :return: nothing
    """
    print('''
    ******OPTIONS MENU*******
    Option 1: Send a Thank You
    Option 2: Create a Report
    Option 3: Exit \n''')


def show_names(db):
    """ Print list of donor names
    :param db: (list) of dictionaries with donation information
    :return: nothing
    """
    for i, entry in enumerate(db):
        print(str(i + 1) + ".", "Donor Name:", entry["Donor Name"])

def prompt_menu_option():
    """ Prompt menu option
    :return: string
    """
    menu_option = input("Please select an option from the menu (1-3): ")
    return menu_option


def enter_name():
    """ Prompt donor name
    :return: string
    """
    name = input("Please enter a donor's full name: ")
    return name


def enter_donation(name):
    """ Prompt donation amount for donor
    :param name: (string) with name of donor:
    :return: float
    """
    donation = round(float(input("Please enter the donation amount from {}: ".format(name))), 2)
    return donation


def thank_you_letter(name, donation):
    """ Print thank you letter for donors
    :param name: (string_ with name of donor
    :return: string
    """
    print("""
    Dear {},
    Thank you for your recent donation of ${} to our organization. 
    We rely on the generous contributions of kind people like you to help fund our cause and make the world a better place.
    Sincerely,
    Kyle at Kelby Doggo Inc.""".format(name, donation))


def get_total_given(db):
    """ Get total donations per donor
    :param db: (list) of dictionaries with donor information
    :return: float
    """
    return donor_list["Total Given"]


def create_report(db):
    """ Print report of donor database
    :param db: (list) of dictionaries with donor information
    :return: nothing
    """
    db.sort(key=get_total_given, reverse=True)
    heading = "| {dn:<20s}\t| {tg:<10s}\t| {ng:<10s} | {ag:<10s} |".format
    row = "{dn:<20s} \t {ds:<1s} {tg:>9.2f} \t {ng:>10d} \t {ds2:<1} {ag:>9.2f} ".format
    print(heading(dn="Donor Name", tg="Total Given", ng="Num Gifts", ag="Average Gift"))
    print("---------------------------------------------------------------------")
    for entry in db:
        print(row(dn=entry["Donor Name"], ds="$", tg=entry["Total Given"], ng=entry["Num Gifts"], ds2="$", ag=entry["Average Gift"]))


def welcome_message():
    """ Print welcome message when program is launched
    :return: nothing
    """
    print("\nWelcome to the Mailroom App!")


def close_app():
    """ Print goodbye message when user closes program
    :return: nothing
    """
    print("Closing Mailroom App...Goodbye!")



# Main Body of Script  ---------------------------------------------------- #

welcome_message()

while True:
    menu_options()
    choice = int(prompt_menu_option())
    if choice == 1:
        while True:
            name_string = enter_name()
            if name_string.lower().strip() == "list":
                show_names(donor_list)
            else:
                break
        donation_amount = enter_donation(name_string)
        donor_list = add_donation_amount(name_string, donation_amount, donor_list)
        thank_you_letter(name_string, donation_amount)

    elif choice == 2:
        create_report(donor_list)

    elif choice == 3:
        close_app()

    else:
        pass



