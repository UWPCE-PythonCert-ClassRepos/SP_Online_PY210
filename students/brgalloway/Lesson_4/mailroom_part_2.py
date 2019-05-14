from operator import itemgetter, attrgetter

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
        if dispatch_dict[response]() == "quit":
            sys.exit()

def quit_app():
    return "quit"

def list_names():
    for i in sorted(donors_list.keys()):
        print(i)
    return find_donor()

def find_donor():
    print("*" * 24)
    fullname = input("type list to display names or quit to exit to main menu\n" \
                    "Enter full name of donor: ")
    
    while True:
        if fullname == "list":
            return list_names()
        elif fullname in donors_list.keys():
            print("Selecting Donor " + fullname)
            return send_thankyou(fullname)
        elif fullname == "quit":
            return menu_selection()
        else:
            donor_fields = ("donation_total", "times_donated","average_donation")
            print(f"Adding new user {fullname}")
            for i in donor_fields:
                donors_list.setdefault(fullname, {})[i] = 0
            return send_thankyou(fullname,donors_list)

# Generate report based on menu choice
# and return user to the menu prompt
def generate_report(donors_list):
    sorted_list = sorted(donors_list, key=itemgetter(1), reverse=True)
    print("{:<20}|{:^18}|{:^15}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
    print("-" * 70)
    for i in sorted_list:
        print(f"{i[0]:<20}${i[1]:>14.2f}{i[2]:^18}${i[3]:>12.2f}".format())
    return user_prompt(donors_list)

# This function sends the formatted email
# records donation amounts and adds new users 
# and their donaitons to the database
def send_thankyou(fullname, donors_list):
    donation_amount = float(input(f"Donation amount: "))
    for i in range(len(donors_list)):
        if fullname in str(donors_list[i]):
            if len(donors_list[i]) == 1:
                donors_list[i].extend((donation_amount, 0, 0))
            else:
                add_donation = donors_list[i][1] + donation_amount
                donors_list[i].pop(1)
                donors_list[i].insert(1,add_donation)
                
    email = f"Dear {fullname},\n\nThank you for your very kind donation of ${donation_amount:.2f}.\n\n" \
             "It will be put to very good use.\n\n" \
             "Sincerely,\n" \
             "-The Team"
    print(email)

    return user_prompt(donors_list)

def bulk_thankyou(fullname, donors_list=donors_list, times_donated=0, average_donation=0):
    donation_amount = float(input(f"Donation amount: "))
    for i in range(len(donors_list)):
        if fullname in str(donors_list[i]):
            if len(donors_list[i]) == 1:
                donors_list[i].extend((donation_amount, 0, 0))
            else:
                add_donation = donors_list[i][1] + donation_amount
                donors_list[i].pop(1)
                donors_list[i].insert(1,add_donation)
                
    email = f"Dear {fullname},\n\nThank you for your very kind donation of ${donation_amount:.2f}.\n\n" \
             "It will be put to very good use.\n\n" \
             "Sincerely,\n" \
             "-The Team"
    print(email)

    return user_prompt(donors_list)

main_menu = "Choose one of the following options. \n\n" \
            "1 - Send a Thank You to a single donor \n" \
            "2 - Create a Report \n" \
            "3 - Send letters to all donors \n" \
            "4 - Quit \n" \
            ">> "
main_dispatch = {
    "1": find_donor,
    "2": generate_report,
    "3": bulk_thankyou,
    "4": quit_app
}

if __name__ == '__main__':
    menu_selection(main_menu, main_dispatch)