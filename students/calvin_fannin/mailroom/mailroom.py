#!/usr/bin/env python3
import sys

z = [("John Kestrel", [653772.32, 12.17]),
            ("Jeff Kingbird", [877.33]),
            ("Paul Jacobin", [663.23, 43.87, 1.32]),
            ("Mark Tanager", [1663.23, 4300.87, 10432.0]),
            ("Anna Hummingbird",[4500.00, 800.00, 2350.00])]


donations = [['John Kestrel', [653772.32, 12.17, 4]],
 ['Jeff Kingbird', [877.33]],
 ['Paul Jacobin', [663.23, 43.87, 1.32]],
 ['Mark Tanager', [1663.23, 4300.87, 10432.0]],
 ['Anna Hummingbird', [4500.0, 800.0, 2350.0]],
 ['Calvin Fannin', [645.0]]]

prompt = "\n".join (("Welcome to Mailroom","Choose an option:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit Mailroom",
          " >>> "))

def search_fullname(donor_name):
    for i,name in enumerate(donations):
        if donor_name == (donations[i][0]):
            return True
    return False

def get_name_index(donor_name):
    for i,name in enumerate(donations):
        if donor_name == (donations[i][0]):
            return i

def create_email():
    pass

def add_donation_new_donor(donor_name, amount):
    donations.append([donor_name, [amount]])

def add_donation(name_index, amount):
    donations[name_index][1].append(amount)

def print_donors():
    #[x[0] for x in donations]
    for i,name in enumerate(donations):
        print (donations[i][0])

def send_thankyou():
    name = input("Enter Donors Full name <First> <Last>")
    while name == "list":
        print_donors()
        name = input("Enter Donors Full name <First> <Last>")
    else:
        if search_fullname(name):
            response_amount = float(input ("Enter a dollar amount"))
            #add donation to select user
            add_donation(get_name_index(name),response_amount)
            #compose the email and print to terminal
            create_email()
        else:
            # add user to list
            #add_donor(name)
            response_amount = float(input ("Enter a dollar amount"))
            # add donation to select user
            add_donation_new_donor(name, response_amount)
            #compose email and print to terninal
            create_email()

def


def create_report():
    pass

def quit_program():
    sys.exit()

def main():
    while True:
        response = input(prompt)
        if response == "1":
            send_thankyou()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()
