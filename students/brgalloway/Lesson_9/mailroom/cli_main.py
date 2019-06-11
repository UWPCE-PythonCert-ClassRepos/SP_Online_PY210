import sys

donors_list = {
    "Jeff Bezos": {
        "donation_total": 877.33,
        "times_donated": 1,
        "average_donation": 877.33
    },
    "Paul Allen": {
        "donation_total": 708.42,
        "times_donated": 3,
        "average_donation": 236.14
    },
    "William Gates, III": {
        "donation_total": 653784.49,
        "times_donated": 2,
        "average_donation": 326892.24
    },
    "Bill Ackman": {
        "donation_total": 2354.05,
        "times_donated": 3,
        "average_donation": 784.68
    },
    "Mark Zuckerberg": {
        "donation_total": 16396.10,
        "times_donated": 3,
        "average_donation": 5465.37
    }
}

def menu_selection(prompt, dispatch_dict): 
    while True:
        response = input(prompt)
        response = response.lower()
        response = response.strip()
        try:
            if dispatch_dict[response]() == "quit":
                sys.exit()
        except KeyError:
            print("\n\ninvalid response\n")

def quit_app():
    return "quit"

# Generate a list of donors from the database
def list_names():
    donor_names = [k for k in sorted(donors_list.keys())]
    return "\n".join(donor_names)

# sub menu for selecting donors
def find_donor():
    while True:
        fullname = input("type list to display names or quit to exit to main menu\n" \
                         "Enter full name of donor: ")
        if fullname == "list":
            output = list_names()
            return print(output)
        elif fullname:
            try:
                donation_amount = float(input("Donation amount: "))
            except ValueError:
                print("not a valid response exiting to donor selection")
            return send_thankyou(fullname,donation_amount)
        elif fullname:
            return bulk_thankyou(donors_list)
        elif fullname == "quit":
            return menu_selection(main_menu, main_dispatch) 
            
# main menu items    
main_menu = "Choose one of the following options. \n\n" \
            "1 - Send a Thank You to a single donor \n" \
            "2 - Create a Report \n" \
            "3 - Send letters to all donors \n" \
            "4 - Quit \n" \
            ">> "

# value returned from choice keys
main_dispatch = {
    "1": find_donor,
    "2": generate_report,
    "3": bulk_thankyou,
    "4": quit_app
}

if __name__ == '__main__':
    menu_selection(main_menu, main_dispatch)