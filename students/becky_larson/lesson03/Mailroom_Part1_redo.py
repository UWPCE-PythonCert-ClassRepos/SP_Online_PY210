#!/usr/bin/env python """
import sys
"""Mailroom"""

# Prompt user to choose from menu of 3 actions:
# Send a Thank You, Create a Report or quit.

run_program = True

selection_text = "\n".join(("**  Please Select Valid Option Listed:  **",
                            "       1: Send a Thank You",
                            "       2: Create a Report",
                            "       3: Quit",
                            "       Please enter your choice:"
                            " > "))


# Send a Thank You

# use string formatting to compose email thanking donor for generous donation.
#     Print email to terminal and return to original prompt.
# Ok for now for program not to store names of new donors that had been added


def print_donor_list():
    print("***** List of current donors ******")
    for donor in donor_db:
        print(donor[0])
    print("***********************************")


def print_email(name, amount):
    #  print email
    email_text = 'Thank you for your generous donation of'
    print(f"\n\nDear {name},\n\n{email_text} ${amount:.2f}.\n\nBecky\n")


def send_thank_you_new():

    response = ""

    while(True):
        response = input("""Enter Full name or 'ist to see names or exit: """)
        if(response == 'exit'):
            break
        elif response.lower() == "list":
            print_donor_list()
        else:
            break

    if(response != "exit"):
        for donor in donor_db:
            if donor[0] == response.title():
                prompted_donation = input("Please enter an amount to donate >")
                donor[1].append(float(prompted_donation))
                print_email(response.title(), int(prompted_donation))
                break
        else:
            prompted_donation = input("Please enter an amount to donate >")
            new_donor = (response.title(), [float(prompted_donation)])
            donor_db.append(new_donor)
            print_email(response.title(), int(prompted_donation))


def sort_total_donations(donations):
    #  sort by total donations

    return sum(donations[1])


def write_report():
    # print list of donors, sorted by total historical donation amount
    print("** You've selected to write a report.  **")
    col1 = 'Donor Name'
    col2 = 'Total Given'
    col3 = 'Num Gifts'
    col4 = 'Average Gift'
    print(f'{col1:25} | {col2:13} | {col3:11} | {col4:13}')
    print('-'*70)

    donor_db.sort(key=sort_total_donations, reverse=True)

    for donor in donor_db:
        count = len(donor[1])
        name = donor[0]
        total = sum(donor[1])
        avg = total/count
        print(f'{name:25}  ${total:13.2f}   {count:11}  ${avg:12.2f}')
    return


# data structure to hold list of donors & history of amounts donated
# populated with at least five donors, with between 1 & 3 donations each
# store that data structure in the global namespace ?belarson


# donor db
donor_db = [
    ("Cher", [1000.00, 2000.00]),
    ("Drew Barrymore", [25000.00]),
    ("Charlie Brown", [25.00, 50.01, 100.00]),
    ("Jack Black", [256.00, 752.50, 10101.00]),
    ("Sam Smith", [5500.00, 24.00])]

if __name__ == '__main__':
    while(run_program):
        choice = input(selection_text)
        if choice == '1':
            send_thank_you_new()
        elif choice == '2':
            write_report()
        elif choice == '3':
            print("Thank you")
            run_program = False
