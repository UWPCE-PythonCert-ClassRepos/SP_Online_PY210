#!/usr/bin/env python """
import sys
"""Mailroom"""

# Prompt user to choose from menu of 3 actions:
# Send a Thank You, Create a Report or quit.

selection_text = "\n".join(("**  Please Select Valid Option Listed:  **",
                            "       1: Send a Thank You",
                            "       2: Create a Report",
                            "       3: Quit",
                            "       Please enter your choice:"
                            " > "))


def prompt_for_name():
    input_name = input("""Please enter Full name or 'list' to see names: """)

    if (input_name == ""):
        return prompt_for_name()
    elif input_name.lower() == 'list':
        print("***** List of current donors ******")
        for donor in donor_db:
            print(donor[0])

        print("***********************************")
        return prompt_for_name()
    else:
        return input_name.title()


def prompt_for_amount():
    inputAmount = input("""Please enter Amount greater than 0: """)

    # Convert amount to number
    # it is OK to crash if someone types bogus amount
    int_amount = int(inputAmount)
    if int_amount > 0:
        return int_amount
    else:
        prompt_for_amount()


# Send a Thank You

# use string formatting to compose email thanking donor for generous donation.
#     Print email to terminal and return to original prompt.
# Ok for now for program not to store names of new donors that had been added


def send_thank_you():
    print("** You've selected to send a thank you!  **")

    # prompt for a Full Name.
    prompted_name = prompt_for_name()

    # check if name is in list
    prompted_donation = input("Please enter an amount to donate >")
    if prompted_donation.lower() == 'quit':
        return
    for donor in donor_db:
        if donor[0] == prompted_name.title():
            donor[1].append(float(prompted_donation))
            break
    else:
        new_donor = (prompted_name.title(), [float(prompted_donation)])
        donor_db.append(new_donor)

    #  print email
    email_text = 'Thank you for your generous donation of'
    name = prompted_name.title()
    amount = int(prompted_donation)
    print(f"\n\nDear {name},\n\n{email_text} ${amount:.2f}.\n\nBecky\n")


def write_report():
    print("** You've selected to write a report.  **")
    col1 = 'Donor Name'
    col2 = 'Total Given'
    col3 = 'Num Gifts'
    col4 = 'Average Gift'
    print(f'{col1:25} | {col2:13} | {col3:11} | {col4:13}')
    print('-'*70)
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
    choice = input(selection_text)
    if choice == '1':
        send_thank_you()
    elif choice == '2':
        write_report()
    elif choice.lower() == '3':
        print("Thank you")
        sys.exit()
    else:
        choice = input(selection_text)
