#!/usr/bin/env python3

"""
Mail_room_part1.py
By David Baylor on 12/3/19
uses python 3

Automates writing an email to thank people for their donations.
"""

def main():
    data = [["bill", 100, 2, 50],["john",75, 3, 25]]
    while True:
        choice = input("""
What would you like to do?

1) Send a Thank You 
2) Create a Report
3) Quit
""")
        if choice == "1":
            data = send_thank_you(data)
        elif choice == "2":
            creat_report(data)
        elif choice == "3":
            break

def send_thank_you(data):
    name = input("Enter a full name or type 'list' to vew current list: ")
    if name.upper() == "LIST":
        for i in range(len(data)):
            print(data[i][0].capitalize())
        return data
    else:
        for i in range(len(data)):
            if name.upper() == data[i][0].upper():
                print("This personn has alredy donated add another donation under their name.")
                donation = float(input(f"How much did {name.capitalize()} donate: $"))
                data[i][1] += donation
                data[i][2] += 1
                data[i][3] = data[i][1]/data[i][2]
                write_email(name, donation)
                return data               
        donation = float(input(f"How much did {name.capitalize()} donate: $"))
        data += [[name, donation, 1, donation]]
        write_email(name, donation)
        return data

def creat_report(data):
    print("""
Donor Name                | Total Given | Num Gifts | Average Gift
--------------------------|-------------|-----------|-------------""")
    for i in range(len(data)):
        make_row(data[i][0].capitalize(), data[i][1], data[i][2], data[i][3])

def make_row(name, total, num_gift, ave_gift):
    print("{:26}|${:12}|{:11}|${:12}".format(name, total, num_gift, ave_gift))

def write_email(name, donation):
    print("Here is the email:")
    print(f"""
Dear {name.capitalize()},

Thank you for your generous donnation of ${donation}.""")

main()

