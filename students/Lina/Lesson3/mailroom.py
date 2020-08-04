#! python

#------------------------------------------------
# Lesson 3 - Assignment 1: Mailroom, Part 1
#------------------------------------------------

import sys
from operator import itemgetter
from datetime import date

#This list contains the donor names and a history of their donation amounts.
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("Oprah Winfrey", [3312.00, 5500.00]),
            ("Joe Smith", [250.75, 120.00, 55.50, 100.50])
            ]

def show_donor_list():
    #This function will show all donors in the list.
    for row in donor_db:
        print(row[0])

def verify_donor(name):
    #This function will check if the donor is in the list. If not there,
    #it will add to the list.
    new_donor = True
    for row in donor_db:
        if row[0] == name:
            new_donor = False
            break

    if new_donor:
        donor_db.append((name, []))

def add_donation(name, amount):
    #This function will add a donation amount of a donor.
    for i in range(len(donor_db)):
        if donor_db[i][0] == name:
            donor_db[i][1].append(amount)
            break

def email_donor(name, amount):
    #This function will compose a 'Thank You' note and email (print) to the donor who
    #has just made a donation. The note will include the amount and today's date.
    content = "\n".join(("Dear {0},",
              "Thank you for your generous gift of ${1:.2f} to support the work of ChangeALife. Your donation will remain in your local community",
              "and be used by ChangeALife to provide programs and services to those in need.  On behalf of those whose lives will be impacted, ",
              "please accept our sincere gratitude. May you know the deep satisfaction of having made a difference in the lives of others.",
              "",
              "",
              "",
              "Below is a summary of your gift.",
              "",
              "Amount: ${1:.2f}",
              "Date: {2:%m-%d-%Y}"
              "",
              "",
              "",
              "Tiffany Kurnett",
              "President & CEO")).format(name.split(' ')[0], amount, date.today())
    print(content)
    print()


def send_a_thank_you():
    #This function will first prompt user for a donor's name, or type list to see
    #all donors. After a name is entered, it will prompt for a donation amount.
    #Then it will call some functions to verify the donor and add the donation
    #amount to the list associated with the donor. At the end, a 'Thank You' email
    #will go out to the donor. The user may choose to quit at anytime by typing 'q'
    #at the prompt, and it will take the user back to the main menu.
    prompt1 = "\n".join(("Please enter a full name or type 'list' to see all donors:",
              "(Type 'q' to quit)",
              ">>> "))
    prompt2 = "\n".join(("Please enter a donation amount:",
              "(Type 'q' to quit)",
              ">>> "))

    prompt_user = True
    while prompt_user:
        name = input(prompt1)
        if name == 'list':
            show_donor_list()
        elif name == "q":
            return
        else:
            prompt_user = False

    amount = input(prompt2)
    if amount == "q":
        return
    verify_donor(name)
    add_donation(name, float(amount))
    email_donor(name, float(amount))

def create_a_report():
    #This function will create a summary report to list all donors, their total donation
    #amount, number of donations and average amount. It will show in the order of total
    #donation amount from highest to lowest.
    summary = []             #Contains a tuple (donor name, total donated, number of donations)
    for i in range(len(donor_db)):
        total_donated = 0
        for amount in donor_db[i][1]:
            total_donated += amount
        summary.append((donor_db[i][0], total_donated, len(donor_db[i][1])))
    summary = sorted(summary, key=itemgetter(1), reverse=True)  #Sort by total donated from highest to lowest

    header = "{:<25s} | {:11s} | {:9s} | {:12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header)
    print(f"{'-'*len(header):s}")  #or print("{:s}".format('-'*len(header)))

    row = "{name:<25s}  ${total_donated:11.2f}  {gift_count:10d}  ${avg_amount:12.2f}".format
    for col in summary:
        print(row(name=col[0], total_donated=col[1], gift_count=col[2], avg_amount=col[1]/col[2]))
    print()

def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    #This function will prompt user to select a task from the menu, it then will
    #call the function associated with the task to execute.
    prompt = "\n".join(("Welcome to the ChangeALife mail room!",
             "Please choose from below options:",
             "1 - Send a Thank You",
             "2 - Create a Report",
             "3 - Exit",
             ">>> "))

    while True:
        response = input(prompt)
        if response == "1":
            send_a_thank_you()
        elif response == "2":
            create_a_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main()
