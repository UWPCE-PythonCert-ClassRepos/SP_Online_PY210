import sys
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
    # TODO Fix KeyError when user presses enter
    # causing an empty string to be sent as response
    while True:
        response = input(prompt)
        if dispatch_dict[response]() == "quit":
            sys.exit()
        else:
            print("Enter a valid response")

def quit_app():
    return "quit"

def list_names():
    for i in sorted(donors_list.keys()):
        print(i)
    return find_donor()

# sub menu for selecting donors
def find_donor():
    while True:
        fullname = input("type list to display names or quit to exit to main menu\n" \
                         "Enter full name of donor: ")
        if fullname == "list":
            return list_names()
        elif fullname:
            return send_thankyou(fullname)
        elif fullname == "quit":
            return menu_selection(main_menu, main_dispatch)
        else:
            print("Enter a valid response")

# helper function to sort by total
def sort_donors(a_dict):
    return a_dict[1]["donation_total"]

# Generate report based on menu choice
# and return user to the menu prompt    
def generate_report(donors_list=donors_list):
    sorted_list = sorted(donors_list.items(), key=sort_donors, reverse=True)
    print("{:<20}|{:^15}|{:^15}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
    print("-" * 70)
    for donors in sorted_list:
        name = donors[0] 
        total = donors[1]["donation_total"] 
        times = donors[1]["times_donated"] 
        average = donors[1]["average_donation"]
        print(f"{name:<20}${total:>14.2f}{times:^18}${average:>12.2f}".format())

# This function sends the formatted email
# records donation amounts and adds new users 
# and their donaitons to the database
def send_thankyou(fullname, donors_list=donors_list):
    donation_amount = float(input("Donation amount: "))
    # TODO write email to file
    for fullname in donors_list.keys():
        print("Selecting Donor " + fullname)
    #     if fullname == donor[0]:
    #         donor[1] = donor[1] + donation_amount
    #         donor[2] = donor[2] + 1
    #         donor[3] = donor[1] / donor[2]
    #         donors_list[donors_list.index(donor)] = [donor[0], donor[1], donor[2], donor[3]]
    #         break
    else:
        print(fullname, "not found")
    #     donors_list.append([fullname, donation_amount, 1, donation_amount])
    #     donor_fields = ("donation_total", "times_donated","average_donation")
    #     print(f"Adding new user {fullname}")
    #     for i in donor_fields:
    #         donors_list.setdefault(fullname, {})[i] = 0
    #     return send_thankyou(fullname,donors_list)
            
    email = f"Dear {fullname},\n\nThank you for your very kind donation of ${donation_amount:.2f}.\n\n" \
             "It will be put to very good use.\n\n" \
             "Sincerely,\n" \
             "-The Team"
    
    print(email)

def bulk_thankyou(fullname, donors_list=donors_list, times_donated=0, average_donation=0):
    # TODO write all donors to file
    # donation_amount = float(input("Donation amount: "))
    # for donor in donors_list:
    #     if fullname == donor[0]:
    #         donor[1] = donor[1] + donation_amount
    #         donor[2] = donor[2] + 1
    #         donor[3] = donor[1] / donor[2]
    #         donors_list[donors_list.index(donor)] = [donor[0], donor[1], donor[2], donor[3]]
    #         break
    # else:
    #     donors_list.append([fullname, donation_amount, 1, donation_amount])
            
    # email = f"Dear {fullname},\n\nThank you for your very kind donation of ${donation_amount:.2f}.\n\n" \
    #          "It will be put to very good use.\n\n" \
    #          "Sincerely,\n" \
    #          "-The Team"
    
    # print(email)
    pass

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