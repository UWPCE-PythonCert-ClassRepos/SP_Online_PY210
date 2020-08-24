#! bin/user/env python3
import sys
from operator import itemgetter
"""
Program Part4:
Add a full suite of unit tests:

“Full suite” means all the code is tested. In practice, it’s very hard to test the user interaction,
but you can test everything else. Therefore you should make sure that there is as little logic and 
untested code in the user interaction portion of the program as possible.
"""

# Donor name, donation amount, donation history
donor_list = {
    "John Doe": [2000, 2],
    "Jane Doe": [3000, 3],
    "George Washington": [1, 1],
    "Andrew Jackson": [20, 2],
    "Benjamin Franklin": [100, 3]
}

# Main options menu for user to pick from
def main():
    while True:
        options()  # Display each option to the user
        try:
            choice = int(input("What would you like to do? "))
            # Using a dictionary for as a switch case
            switch_func_dict = {
                1: thank_you,
                2: get_report,
                3: all_letters,
                4: quit
            }
            switch_func_dict.get(choice)()
        except ValueError as error_message:
            print(error_message)
        except TypeError:
            print("Not a valid option, please select again.")

# Menu of options for the user in the script
def options():
    print("You have 4 options to choose from: ", "\n"
        "1) Send Thank you", "\n"
        "2) Create Report", "\n"
        "3) Send a Thank you note to all donors", "\n"
        "4) Exit", "\n"
          )

# Ask for a donor name and donation amount, send an email to that donor once completed
def thank_you():
    name = input("Enter a first and last name (type 'list' to see existing donors): ").title()
    if name.lower() == "list":
        print(donor_list)
        thank_you()
    try:
        gift = float(input("Enter a donation amount: "))
    except ValueError as error_message:  # Catch if the user doesn't input a number
        print(error_message)
    update_donor_list(name, gift)

    # Thank you email to the donor
    print(thank_you_letter(name, gift))

def update_donor_list(name, gift):
    if name in donor_list.keys():  # check if name is in the dict
        donor_list[name] = [(donor_list[name][0] + gift), (donor_list[name][1] + 1)]  # Use the key to update the values using a list
    else:  # add the new donor and their donation amount with 1 donation history
        donor_list.update({name: [gift, 1]})
    return donor_list

def thank_you_letter(name, donation):
    email = f"Thank you {name} for your generous donation of ${donation:.2f}, your kindness is very appreciated." + "\n"
    return email

def display_report():
    for row in get_report():
        print(row)

# Show a list of current donor's in the list and sorted by total number of donations
def get_report():
    fields = ["Donor Name", "Total Given", "Num Gifts", "Average Gift"]  # report headers
    report_list = []  # temp list used later in order to sort by number of total gifts
    # format headers to have a uniform look
    print(f"{fields[0]:<20} | {fields[1]:<11} | {fields[2]:<3} | {fields[3]}")
    # line break for report
    print("{}".format('-' * 61))
    for item in donor_list:
        donation_total = donor_list[item][0]
        donation_trans = donor_list[item][1]
        avg_donation = donation_total / donation_trans
        temp_list = [item, donation_total, donation_trans, avg_donation]  # Taking the dictionary copying over to a temp list in order to sort
        report_list.append(temp_list)
    sorted_donors = sorted(report_list, key=itemgetter(1), reverse=True)  # Sorting list based on the total donation for each donor
    for donor in sorted_donors:
        print(f"{donor[0]:<20} $ {donor[1]:>11.2f} {donor[2]:>11} $ {donor[3]:>11.2f}")
    return sorted_donors

# Create a text file using the name of the donor for each file name
def all_letters():
    for name in donor_list:
        with open(f"thank_you_{name.lower()}.txt", 'w') as fh:
            fh.write(f"Dear {name.title()},\nThank you for your very generous donation of ${(donor_list[name.title()][0]):.2f}." \
            f"Your help will go a long way in supporting our foundation." \
            f"\n\nThank you,\nYour Non-Profit Team\n\n")

def quit():
    print("Closing script")
    sys.exit()

if __name__ == "__main__":
    print("Mailroom script has been started. ")
    main()