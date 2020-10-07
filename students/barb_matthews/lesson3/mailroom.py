#! /usr/bin/env python3

## Lesson 3.3 Mailroom Part 1
## By: B. Matthews
## 9/28/2020
## This is the first of a four-part assignment that will keep track of an imaginary charity's
## donors, the donation amounts, and will print a thank you message if desired.

import sys
import copy
import time

huge_list = [('Arthur Dent', [10.00]),
             ('Trillian Hmmm', [234.12, 43.50]),
             ('Zaphod B', [1000.00, 25.99, 321.45]),
             ('James Maxwell', [1.00, 25]),
             ('Grace Hopper', [50.00, 300.00]),
             ('Georg Ohm', [5500.50]),
             ('Cynthia Irvine', [20.00])]

s_mylist = []
average = 0
total = 0
num_of_donations = 1

prompt = "\n".join(("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nMailroom for Lazy Fundraisers\n",
          "Please choose an option:",
          "1) Send a Thank-you",
          "2) Create a Report",
          "3) Quit",
          "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\a> "))

prompt2 = "\n".join(("**********************************\nThank-You Options\n",
          "What do you want to do?:",
          "name - Enter a name",
          "list - List of donor names",
          "   q - Quit",
          "**********************************\n> "))

def thanks():
    """Prints a donor thank-you to the screen, maybe user copies it to email"""
    name = []
    found = 0

    while True:
        choice = input(prompt2)
        if choice.lower() == "name":
            name = input("What name?\n")

            ## check if name is in index, if not then add it
            for i, item in enumerate(huge_list):
                if (name in item):           ## Compare the name fields
                    found = huge_list.index(item)
                    what = input("What donation amount to add?\n")
                    huge_list[found][1].append(float(what))
                    #print(huge_list[found])
                    print("\n" * 100, "Email: Thank you, %s, for your generous donation of $%.2f. "
                                     "We appreciate your support.\n" % (name, float(what)))
                    time.sleep(3)
                    break

                else:
                    donor_record = [name]
                    huge_list.append(donor_record)      ## If new donor, add it to end of list
                    found = len(huge_list) - 1

                    ## prompt for donation amount, add it to name record in the index
                    what = input("What donation amount?\n")
                    huge_list[found].append([float(what)])
                    #print(huge_list)
                    print("\n" * 100, "Email: Thank you, %s for your generous donation of $%.2f. "
                                      "We appreciate your support.\n" % (name, float(what)))
                    time.sleep(3)
                    break

        elif choice.lower() == "list":
            print("The current names are: ")
            ## enumerate through the index and print names
            for i, item in enumerate(huge_list):
                print(item[0])
            print('\n')

        elif choice.lower() == "q":
            break
        else:
            print("Try again.")
    return

def report():
    """Prints a report to the screen of donors and amounts"""
    print("\n" * 100, "\a{:<23} | {:<15} | {:<15} | {:>15}".format("Name", "Total Donated ($)",
                                                                   "Number of Donations",
                                                                   "Average Amount ($)"))
    print("-" * 87)

    ## Sort the list of donors in descending total donation amount order
    s_mylist = sorted(huge_list, key=lambda record : sum(record[1]), reverse=True)

    for person in s_mylist:
        total = sum(person[1])
        number = len(person[1])
        average = total/number
        print("{:<24} | {:>17,.2f} | {:>19} | {:>15,.2f}".format(person[0], total, number, average))

    print("\n\n\n\n")
    return

def exit_menu():
    """Exits out of the interactive menu"""
    print("Ok, later")
    sys.exit()

def main():
    """Prints the menu dispay to the screen and gets user input"""
    while True:
        response = input(prompt)  # continuously collect user selection
        if response == "1":
            thanks()
        elif response == "2":
            report()
        elif response == "3":
            exit_menu()
        else:
            print("\n" * 100)
            print("Try again. Don't give up!\nWhat option?")

# If not imported as a module, call the main function
if __name__ == "__main__":
    main()