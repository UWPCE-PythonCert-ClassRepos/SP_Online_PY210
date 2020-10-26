#if __name__ == '__main__'



donor_list = [
    {"Donor Name": "William Gates, III", "Total Given": 653784.49, "Num Gifts": 2, "Average Gift": 326892.24},
    {"Donor Name": "Mark Zuckerberg", "Total Given": 16396.10, "Num Gifts": 3, "Average Gift": 5465.37},
    {"Donor Name": "Jeff Bezos", "Total Given": 877.33, "Num Gifts": 1, "Average Gift": 877.33},
    {"Donor Name": "Paul Allen", "Total Given": 708.42, "Num Gifts": 3, "Average Gift": 236.14},
    {"Donor Name": "Elon Musk", "Total Given": 50.00, "Num Gifts": 2, "Average Gift": 25.00}
]


# Processing Functions
def add_donation_amount(donor, donation, db):
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


# I/O  Functions
def menu_options():
    print('''
    ******OPTIONS MENU*******
    Option 1: Send a Thank You
    Option 2: Create a Report
    Option 3: Exit \n''')

def show_names(db):
    for i, entry in enumerate(db):
        print(str(i + 1) + ".", "Donor Name:", entry["Donor Name"])

def prompt_menu_option():
    menu_option = input("Please select an option from the menu (1-3): ")
    return menu_option

def enter_name():
    name = input("Please enter a donor's full name: ")
    return name

def enter_donation(name):
    donation = round(float(input("Please enter the donation amount from {}: ".format(name_string))), 2)
    return donation

def thank_you_letter(name, donation):
    print("""
    Dear {},
    Thank you for your recent donation of ${} to our organization. 
    We rely on the generous contributions of kind people like you to help fund our cause and make the world a better place.
    Sincerely,
    Kyle at Kelby Doggo Inc.""".format(name, donation))

def get_total_given(donor_list):
    return donor_list["Total Given"]

def create_report(db):
    db.sort(key=get_total_given, reverse=True)
    heading = "| {dn:<20s}\t| {tg:<10s}\t| {ng:<10s} | {ag:<10s} |".format
    row = "{dn:<20s} \t {ds:<1s} {tg:>9.2f} \t {ng:>10d} \t {ds2:<1} {ag:>9.2f} ".format
    print(heading(dn="Donor Name", tg="Total Given", ng="Num Gifts", ag="Average Gift"))
    print("---------------------------------------------------------------------")
    for entry in db:
        print(row(dn=entry["Donor Name"], ds="$", tg=entry["Total Given"], ng=entry["Num Gifts"], ds2="$", ag=entry["Average Gift"]))


def welcome_message():
    print("\nWelcome to the Mailroom App!")


def close_app():
    print("Closing Mailroom App...Goodbye!")

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



