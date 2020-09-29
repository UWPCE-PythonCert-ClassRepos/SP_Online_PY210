#!/usr/bin/env python3

# Dominic Divakaruni
# Lesson03 - Mailroom Part 1

import sys

#Initialize list of donors
donor_db = [("William Gates", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

def prompts():
    #provide a list of options and accept response
    prompt = "\n".join(("\n Welcome to the Donor Gratitude program!",
          "Please choose one of the following options:",
          "Enter '1' to send a Thank You",
          "Enter '2' to create a report",
          "Enter '3' - Quit"))
    print(prompt)
    response = input(">>>")
    return response

def append_amount(name):
    #add donation amount to the donation database if Donor name is on the list
    amount = float(input("Please enter a donation amount: "))
    for entry in donor_db:
        if name.title() == entry[0]:
            entry[1].append(float(amount))
            print("Thank you Dear,", name, "for your generous donation of", amount, "\n\nSincerely,\nThe Donor Gratitude Program \n")
            break

def add_name(name):
    #add Donor name to the list if missing
    new_name = (name.title(), [])
    donor_db.append(new_name)
    print(name.title(), "Added to the donors list")

def check_name(name):
    #check if donor name is on the list
    for entry in donor_db:
        if name == entry[0]:
            return True


def ty_note():
    """workflow that : 1) retrieves list of donors, 2) adds new donors to the database, 
       3) saves new donation amounts, and 4) prints thank you notes! """
    while True:
        name = input("\n Please enter a Donors name, or enter 'List' if you'd like to see the list of donors, or to exit say 'Main Menu' \n>>> ")
        if name == 'List':
            print("Here's the list of donors: \n")
            for i, v in enumerate(donor_db):
                print(v[0])
            continue
        elif name == "Main Menu":
            break
        else:
            if check_name(name) == True:
                append_amount(name)
            else:
                add_name(name)
                append_amount(name)

def gen_report():
    #Generate list of donors
    print("\n{:<20}|{:^15}|{:^15}|{:>15}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("-"*68)
    for i in donor_db:
        total_given = sum(i[1])
        num_gifts = len(i[1])
        if total_given >0:
            avg_gift = total_given/num_gifts
        else:
            avg_gift = 0
        print("{:<20} ${:>15,.2f} {:>15}  ${:>12,.2f}".format(i[0], total_given, num_gifts, avg_gift))
    print("\n")


def exit_prog():
    #quit the interractive script
    print("Bye!")
    sys.exit()  # exit the interactive script

def main():
    while True:
        # continuously collect user selection and redirect to feature functions based on the user selection
        choice = int(prompts())
        if choice == 1:
            ty_note()
        elif choice == 2:
            gen_report()
        elif choice == 3:
            exit_prog()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()

