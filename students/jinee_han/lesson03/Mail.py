
# --------------------------------
# 07/02/19 Jinee Han
# Python Programming Lesson 3
# Mailroom Part 1
# ---------------------------------


'''
Program Flow
1. Donor list is saved as a 'Donor_List.txt' file.
2. Display an options list to the user.
 : List 1: Send a Thank you note, 2: Create a List, 3: Exit
# When the user select 1,
a) Ask the user the donor name.
If typed 'list', display the donor name list.
If typed donor's name not listed, add the data to the Donor_List.
If typed donor's name listed, use the name.
b) Ask the user the amount.
Add the amount to the Donor_List.
c) create a thank you email and print to terminal.
d) Return to the original prompt.
'''

import sys

# Donor List
donor_db = [["Kim Kardasian", [653772.32, 12.17]],
            ["Kendal Jenner", [877.33]],
            ["Gigi Hadid", [663.23, 43.87, 1.32]],
            ["Justin Bieber", [1663.23, 4300.87, 10432.0]],
            ["Will Smith",[43.23, 4000.07, 183423.2]]
            ]

# Display options
prompt = "\n".join(("Welcome to the donor list!",
          "Please choose from below options:",
          "1 - Send a Thank you",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))

def send_thank_you_note():
    inputValue = input("Enter a full name. (Type 'list' to see the donor list)")  # Ask the name
    while inputValue == 'list':
        display_list()
        inputValue = input("Enter a full name. (Type 'list' to see the donor list)")

    if not donor_present(inputValue):
        add_donor(inputValue)

    donationName = inputValue
    donationAmount = float(input("Please enter the donation amount: "))
    add_donation_amount(donationName, donationAmount)
    send_thank_you(donationName, donationAmount)

def add_donation_amount(donationName, donationAmount):
    for donator in donor_db:
        if donator[0] == donationName:
            currentDonationList = donator[1]
            currentDonationList.append(donationAmount)
            donator[1] = currentDonationList
            break

def donor_present(donorName):
    donorPresent = False
    for donor in donor_db:
        if donorName == donor[0]:
            donorPresent = True

    return donorPresent

def display_list():
    for lines in donor_db:
        print(lines[0])

def add_donor(donorName):
    donationHistory = []
    newDonator = [donorName, donationHistory]
    donor_db.append(newDonator)

def enter_amount():
    input_amount = ("What is amount of the donation? ")
    return ("You entered "+input_amount)
    thankyou(input_list,input_amount)

def send_thank_you(donator, donationAmount):
    print(f'\nDear {donator.title()},')
    print(f'Thank you for your donation ${donationAmount:,.4f}!' +
          '\n\nWe appreciate your help.,\nThe Mailroom\n')

def create_report():
    """Generate a tabular report of donation history"""
    header ='\n{:^18}|{:^13}|{:^13}|{:>13}'.format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print('-'*len(header))
    donor_sort = sorted(donor_db, key = sort_key, reverse = True)
    for entry in donor_sort:
        total = sum(entry[1])
        num = len(entry[1])
        average = total/num
        print('{:^18} ${:>12,.2f}{:^13}  ${:>12,.2f}'.format(entry[0],total,num,average))
    print('')

def sort_key(entry):
    return sum(entry[1])

def exit_program():
    print("Thank you for your donations!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_thank_you_note()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()