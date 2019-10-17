#!/usr/bin/env python3
import sys

donations = [("John Kestrel", [653772.32, 12.17]),
            ("Jeff Kingbird", [877.33]),
            ("Paul Jacobin", [663.23, 43.87, 1.32]),
            ("Mark Tanager", [1663.23, 4300.87, 10432.0]),
            ("Anna Hummingbird",[4500.00, 800.00, 2350.00])]

prompt = "\n".join (("Welcome to Mailroom","Choose an option:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit Mailroom",
          " >>> "))

def search_fullname(donor_name):
    for i,name in enumerate(donations):
        if donor_name == (donations[i][0])
            return True
    return False

def create_email():
    pass

def print_donors():
    for i,name in enumerate(donations):
        print (donations[i][0])

def send_thankyou():
    response = print("Enter Donors Full name <First> <Last>")
    if respone == "list":
        print_donors()
        response = print("Enter Donors Full name <First> <Last>")
    else:
        if search_fullname(response):




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
        elif respone == "3":
            quit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()
