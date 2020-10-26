#if __name__ == '__main__'

donor_list = [
    {"Donor Name": "William Gates, III", "Total Given": 653784.49, "Num Gifts": 2, "Average Gift": 326892.24},
    {"Donor Name": "Mark Zuckerberg", "Total Given": 16396.10, "Num Gifts": 3, "Average Gift": 5465.37},
    {"Donor Name": "Jeff Bezos", "Total Given": 877.33, "Num Gifts": 1, "Average Gift": 877.33},
    {"Donor Name": "Paul Allen", "Total Given": 708.42, "Num Gifts": 3, "Average Gift": 236.14}
]


# Processing Functions
def add_donation_amount(donor, donation, db = donor_list):
    in_list = False
    for entry in db:
        if donor.lower() == entry["Donor Name"]:
            entry["Total Given"] = donation + entry["Total Given"]
            in_list = True
    if in_list == False:
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

def show_names(db = donor_list):
    for i, entry in enumerate(donor_list):
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


def welcome_message():
    print("Welcome to the Mailroom App!")

welcome_message()

while True:
    menu_options()
    choice = int(prompt_menu_option())
    if choice == 1:
        while True:
            name_string = enter_name()
            if name_string.lower().strip() == "list":
                show_names()
            else:
                break
        donation_amount = enter_donation(name_string)
        donor_list = add_donation_amount(name_string, donation_amount)
        thank_you_letter(name_string, donation_amount)
    else:
        break



