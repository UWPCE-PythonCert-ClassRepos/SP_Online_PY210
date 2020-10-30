#!/usr/bin/env python3
# ---------------------------------------------------------------------------- #
# Title: Lesson 03
# Description: Mailroom Part 1
# ChangeLog (Who,When,What):
# Kate Golenkova, 10/20/2020, Created script
# Kate Golenkova, 10/23/2020, Changed script
# Kate Golenkova, 10/26/2020, Changed script
# ---------------------------------------------------------------------------- #
import sys
# Data ----------------------------------------------------------------------- #
# Variables ------------------------------------------------------------------ #
full_list = [
            [ "John Smith", [30.00, 50.00]],
            [ "Tom Brown", [8.00, 12.00]],
            [ "Emma Dall", [25.00, 50.00, 100.00]],
            [ "Greg Stern", [10.00, 20.00, 10.00]],
            [ "Andrew Brugge", [15.00]]
            ]

# Functions for block Thank You ----------------------------------------------- #
def check_name(full_name):
    for i in full_list:
        if full_name == i[0]:
            return True


def add_name(full_name):
    name = [full_name, []]
    full_list.append(name)
    print("New donor " + str(name[0]) + " has been added to the list of donors")


def add_donation(full_name):
    donation = float(input("Please type a donation amount: "))
    for i in full_list:
        if full_name == i[0]:
            i[1].append(donation)
    print("New donation amount has been added")
    print("This email has been sent to {}".format(full_name))


def send_email(full_name):
    print('''
            Dear {},

            Thank you so much for your generous donation!
            We are so thankful that you have helped us.

            Please let us know if you have any questions.
            _____________________________________________
         '''.format(full_name))


def thank_you():
    while True:
        full_name = input("Please provide full name of donor, type 'list' to see all donors or 'exit' to get back to the Menu: ").title()
        if full_name.lower() == "list":
            print("Full list of donors: ")
            for i in full_list:
                print(i[0])

        elif full_name.lower() == "exit":
            break

        else:
            if check_name(full_name):
                print("This donor is in the list.")
            else:
                add_name(full_name)

            add_donation(full_name)
            send_email(full_name)
            break

# Functions for block Create Report ------------------------------------------ #
def create_report():
    print("\n{:20} | {:10} | {:10} | {:10}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    print("_"*62)
    full_list.sort(key=lambda x: -sum(x[1]))
    for i in full_list:
        total_given = sum(i[1])
        num_gifts = len(i[1])
        average = total_given/num_gifts

        print("\n{:20} | {:10} | {:10} | {:10.2f}".format(i[0], total_given, num_gifts, average))
        print("-" * 62)


# Function to exit the program ----------------------------------------------- #
def exit_program():
    print("Exiting the program")
    sys.exit()

# Main Script ---------------------------------------------------------------- #

# While loop to display Menu with options
def main():
    while True:
        # Menu options
        print('''
            Please choose from below options:
            
                1. Send a Thank You
                2. Create a Report
                3. Quit

        ''')
        choice = input("Enter an Option: ")
        if choice == "1":
            thank_you()
        elif choice == "2":
            print("Full report: ")
            create_report()
        elif choice == "3":
            exit_program()
        else:
            print("Please use any number from 1 to 3")

if __name__ == "__main__":
    main()

