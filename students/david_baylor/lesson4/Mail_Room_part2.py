#!/usr/bin/env python3

"""
Mail_room_part1.py
By David Baylor on 12/3/19
uses python 3

Automates writing an email to thank people for their donations.
"""


def send_thank_you(data):
    name = input("Enter a full name or type 'list' to vew current list: ")
    if name.upper() == "LIST":
        for i in range(len(data)):
            print(data[i]["name"].capitalize())
        return data
    else:
        for i in range(len(data)):
            if name.upper() == data[i]["name"].upper(): 
                print("This personn has alredy donated add another donation under their name.")
                donation = float(input(f"How much did {name.capitalize()} donate: $"))
                data[i]["total"] += donation
                data[i]["num gifts"] += 1
                data[i]["average gift"] = data[i]["total"]/data[i]["num gifts"]
                write_email(name, donation)
                return data               
        donation = float(input(f"How much did {name.capitalize()} donate: $"))
        data += [{"name":name, "total":donation, "num gifts":1, "average gift":donation}]
        write_email(name, donation)
        return data

def create_report(data):
    print("""
Donor Name                | Total Given | Num Gifts | Average Gift
--------------------------|-------------|-----------|-------------""")
    for i in range(len(data)):
        make_row(data[i]["name"].capitalize(), data[i]["total"], data[i]["num gifts"], data[i]["average gift"])

def make_row(name, total, num_gift, ave_gift):
    print("{:26}|${:12}|{:11}|${:12}".format(name, total, num_gift, ave_gift))

def send_all(data):
    for i in range(len(data)):
        write_all(data[i]["name"], data[i]["total"])


def write_email(name, donation):
    print("Here is the email:")
    print(f"""
Dear {name.capitalize()},

Thank you for your generous donnation of ${donation}.

                    -The Team""")

def write_all(name, donation):
    file_name = f'letter_to_{name}.txt'
    with open(file_name, "w") as file:
        file.write(f"""Dear {name.capitalize()},

Thank you for your generous donnation of ${donation}.

                    -The Team""")
    print(f"Sent to {name}")

def exit_program(data):
    return "exit"

if __name__ == "__main__":
    pass
    data = [{"name":"Bill", "total":100, "num gifts":2, "average gift":50},
    {"name":"John", "total":75, "num gifts":3, "average gift":25},
    {"name":"Joe", "total":150, "num gifts":3, "average gift":50},
    {"name":"Fred", "total":3.5, "num gifts":1, "average gift":3.5}]
    while True:
        choice = input("""
What would you like to do?

1) Send a Thank You 
2) Create a Report
3) Send a Thank You to all donors
4) Quit
""")
        dispatch_dict = {"1":send_thank_you, "2":create_report, "3":send_all, "4":exit_program}
        if choice in dispatch_dict:
            if dispatch_dict[choice](data) == "exit":
                break
        


