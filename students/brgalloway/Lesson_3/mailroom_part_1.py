import sys
from operator import itemgetter, attrgetter

# TODO
# It should have a data structure that holds
# a list of your donors and a history of the 
# amounts they have donated. This structure should 
# be populated at first with at least five 
# donors, with between 1 and 3 donations each. 

# The script should prompt the user (you) to choose 
# from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”.

donors_list = [
    ["Jeff Bezos", 877.33, 1, 877.33],
    ["Paul Allen", 708.42, 3, 236.14],
    ["William Gates, III", 653784.49, 2, 326892.24],
    ["Bill Ackman", 2354.05, 3, 784.68],
    ["Mark Zuckerberg", 16396.10, 3, 5465.37] 
]

# Main function to get users input
def main_prompt():
    display_menu = "Choose one of the following options. \n\n" \
                "1 - Send a Thank You \n" \
                "2 - Create a Report \n" \
                "3 - Quit \n"
    while True:
        print(display_menu)
        prompt = input("Enter a choice to continue: ")  
        if prompt == "1":
            sub_menu()
        elif prompt == "2":
            generate_report(donors_list)
        elif prompt == "3":
            sys.exit()
        else:
            print("Enter a valid response")

def sub_menu():
    while True:
        fullname = input("Enter the full name of the donor or type list to display names\n" \
                        "Typing quit will take you to the main menu\n" \
                        ">> ")
        if fullname == "list":
            return list_names()
        elif fullname == "quit":
            return main_prompt()
        elif fullname:
            return send_thankyou(fullname,donors_list)
        else:
            print("Enter a valid response")

def list_names():
        donors_list.sort()
        for i in donors_list:
            print(i[0])
        print("-" * 12)
        return sub_menu()

# Generate report based on menu choice
# and return user to the menu prompt
def generate_report(donors_list):
    sorted_list = sorted(donors_list, key=itemgetter(1), reverse=True)
    print("{:<20}|{:^18}|{:^15}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
    print("-" * 70)
    for i in sorted_list:
        print(f"{i[0]:<20}${i[1]:>14.2f}{i[2]:^18}${i[3]:>12.2f}".format())

# This function sends the formatted email
# records donation amounts and adds new users 
# and their donaitons to the database
def send_thankyou(fullname,donors_list=donors_list):
    donation_amount = float(input("Donation amount: "))
    while True:
        if fullname in donors_list:
            print("inside if", fullname)
            #print(float([i][2] + 1))
            # print(i[1] + donation_amount)
            # print(i[3] / i[2] + 1)
        break
    else:
        print("user not found")
        donors_list.append((fullname, donation_amount, 1, donation_amount))

                
    email = f"Dear {fullname},\n\nThank you for your very kind donation of ${donation_amount:.2f}.\n\n" \
             "It will be put to very good use.\n\n" \
             "Sincerely,\n" \
             "-The Team"
    
    print(email)
    print()
    return main_prompt()


if __name__ == '__main__':
    main_prompt()