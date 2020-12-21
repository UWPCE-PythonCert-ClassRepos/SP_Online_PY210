#! /usr/bin/env python3

## Assignment 4, Mailroom Part 3
## By: B. Matthews
## https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/mailroom-part3.html
## update to: improve by adding exception handling and comprehensions

import sys
import os

## Global variables
#donors = {'Harry Dresden': [10.00],
          #'Queen Mab': [234.10, 1043.50],
          #'Molly Carpenter': [1000.00, 25.99, 321.45],
          #'Carlos Ramirez': [30.50, 30, 10],
          #'Wizard McCoy': [20, 5.00]}

names = ['Harry Dresden', 'Queen Mab', 'Molly Carpenter', 'Carlos Ramirez', 'Wizard McCoy']
donations = [[10.00], [234.10, 1043.50], [1000.00, 25.99, 321.45], [30.50, 30, 10], [20, 5.00]]

donors = {name: amounts for name, amounts in zip(names, donations)}

average = 0
total = 0
sorted_money = []

prompt = "\n".join(("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\nMailroom v.2\n",
                    "Please choose an option:",
                    "1) Send a Thank-you",
                    "2) Create a Report",
                    "3) Send Thank-you letters to all donors (create files)",
                    "4) Quit",
                    "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n> "))

prompt2 = "\n".join(("**********************************\nThank-You Options\n",
                     "What do you want to do?:",
                     "1) Enter a name",
                     "2) List of donor names",
                     "3) Return to Main Menu",
                     "**********************************\n> "))

def safe_input(some_prompt):
    user_string = ''
    try:
        user_string = input(some_prompt)
    except EOFError:
        print("That didn't work\n")
        return
    except TypeError:
        print("That didn't work\n")
        return
    except KeyboardInterrupt:
        print("You really want to quit?\n")
        return
    finally:
        return user_string

def thanks():
    """Prints a donor thank-you to the screen"""

    while True:
        choice = safe_input(prompt2)
        menu2.get(choice)()         # use menu dictionary to select correct function
    return

def sort_me(amounts):
    return sum(amounts[1])

def report():
    """Prints a report to the screen of donors and amounts"""

    print("\n" * 100, "{:<23} | {:<15} | {:<15} | {:>15}".format("Name", "Total Donated ($)",
                                                                   "Number of Donations",
                                                                   "Average Amount ($)"))
    print("-" * 87)

    ## Sort the list of donors in descending total donation amount order
    sorted_money = sorted(donors.items(), key=sort_me, reverse=True)

    for person in sorted_money:
        total = sum(person[1])
        number = len(person[1])
        average = total/number
        print("{:<24} | {:>17,.2f} | {:>19} | {:>15,.2f}".format(person[0], total, number, average))

    print("\n\n")
    return

def exit_menu():
    """Exits out of the interactive menu"""
    print("Goodbye")
    sys.exit()

def thank_files():
    """writes a donor thank-you and puts in a file for each donor"""
    cwd = os.getcwd()       # Current working dir

    for person, amount in donors.items():
        pname = person.replace(' ', '_')
        path = os.path.join(cwd, pname)
        myfile = path + ".txt"
        all = sum(donors[person])

        with open(myfile, 'w') as f:
            f.write("Thank you, %s, for your continuing generous donations of $%.2f.\n"
                    "We appreciate your support. Sincerely, Grateful Team" % (person, all))
            print("created file: ", myfile)

    return

def name_donors():
    """Ask user for name of donor, add it if new, ask for dontation amount, print thanks.
    If the name is found, just add the new donation to their record"""

    name = safe_input("What name?\n")
    what = float(input("How much donated? --> "))
    what_list = [what]

    if name not in donors:
        donors[name] = what_list
        print("\n" * 50, "Dear %s,\n\nThank you for your generous donation of $%.2f. "
                          "We appreciate your support.\n\nSincerely, Grateful Team" % (name, what))
        print("\n" * 5)

    else:
        donors[name].append(what)
        what_list = donors[name]
        all = sum(what_list)
        print("\n" * 50, "Thank you, %s for your continuing generous donations of $%.2f.\n"
                          "We appreciate your support.\n\nSincerely, Grateful Team" % (name, all))
        print("\n" * 5)

def list_donors():
    """prints the donors which are the keys in the donors dictionary"""

    print('People who have donated:\n')
    for person in donors:
        print(person)
    print('\n\n')

menu1 = {
        '1': thanks,
        '2': report,
        '3': thank_files,
        '4': exit_menu
    }

def main():
    """Prints the menu dispay to the screen and gets user input"""

    while True:
        response = safe_input(prompt)    # continuously collect user selection
        try:
            menu1.get(response)()        # use menu dictionary to select correct function
        except TypeError:                ## This quits if user types cntrl-c
            exit_menu()

## Submenu calls main so it has to be here, but I usually like declarations at the top
menu2 = {
        '1': name_donors,
        '2': list_donors,
        '3': main
    }

# If not imported as a module, call the main function
if __name__ == "__main__":
    main()