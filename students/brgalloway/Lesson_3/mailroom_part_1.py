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
def user_prompt(donors_list):
    display_menu = "Choose one of the following options. \n\n" \
                "1 - Send a Thank You \n" \
                "2 - Create a Report \n" \
                "3 - Quit \n"
    print(display_menu)
    prompt = input("Enter a choice to continue: ")   
    while True:
        if prompt == "1":
            find_donor()
            break
        elif prompt == "2":
            generate_report(donors_list)
            break
        else: 
            break
# Generate report based on menu choice
# and return user to the menu prompt
def generate_report(donors_list):
    sorted_list = sorted(donors_list, key=itemgetter(1), reverse=True)
    print("{:<20}|{:^18}|{:^15}|{:^15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gifts"))
    print("-" * 70)
    for i in sorted_list:
        print(f"{i[0]:<20}${i[1]:>14.2f}{i[2]:^18}${i[3]:>12.2f}".format())
    return user_prompt(donors_list)

# this function only finds the users 
# in the donor database. if the user
# is not found it will then pass that 
# value to the send_thankyou letter 
# where new users are added and recorded
def find_donor():
    fullname = input("Enter the full name of the donor or type list to display names: ")
    # inner function for displaying list
    # and recalling the send_thankyou() function
    def list_names():
        donors_list.sort()
        for i in range(len(donors_list)):
            print(donors_list[i][0])
        return find_donor()

    while fullname != "quit":
    # check what the user has entered
        if fullname == "list":
            return list_names()
        elif fullname in str(donors_list):
            print("Selecting Donor " + fullname)
            for i in range(len(donors_list)):
                if fullname in str(donors_list[i]):
                    fullname = donors_list[i][0]  
            return send_thankyou(fullname)
        elif fullname == "quit":
            return user_prompt()
    # Else user not in database send new 
    # user to the send_thankyou function
        else:
            donors_list.append([fullname])
            for i in range(len(donors_list)):
                if fullname in str(donors_list[i]):
                    fullname = donors_list[i][0]
            return send_thankyou(fullname,donors_list)
    
# This function sends the formatted email
# records donation amounts and adds new users 
# and their donaitons to the database
def send_thankyou(fullname, donors_list=donors_list, times_donated=0, average_donation=0):
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


if __name__ == '__main__':
    user_prompt(donors_list)