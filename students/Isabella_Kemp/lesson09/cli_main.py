from donor_models import *
import sys
import time

# includes all of the user intereaction functions and main program flow 

donors = {"John": [150080.00, 41.28],
          "Irene": [1600.00, 24.47],
          "Rob": [19000.00, 200.47],
          "Kathy": [819.00, 34.5],
          "Laureen": [830.00, 47.00, 982.13],
          "Miles": [24.50, 87.00, 193.00]}
data = DonorCollection(**donors)
# get donation amount

def get_donation():
    while True:
        money = input("Please enter a donation amount: $ ")
        try:
            amount = float(money)
            if amount <= 0:
                print("Invalid value")
            else:
                return amount
        except ValueError:
            print("Invalid value")
    return amount

#send a thnank you

def thank_you():
    while True:
        name = input("Enter a donor name to send a thank you letter, "
                              "'list' or 'listall' for list of donors, '4' will exit: ")
        if name == "list":
            # comprehension
            print(list(donors))
        elif name == "listall":
            # entire record name with donations
            for key in donors:
                print("{0} {1}". format(key, donors[key]))
        elif name == '4':  # quit and return to main menu
            print("Finished processing thanks to donors...\n\n")
            return
        donation = get_donation()
        if data._data.get(name):
            data._data.get(name).add_donation(donation)
        else:
            data.add_donor(name, donation)
    print(data._data.get(name).thank_you_mail())


def report():
    # Prints report of existing donors
    data.create_report()
    return

def exit_menu():
    print("Thank you, Goodbye...")
    sys.exit()  # terminates the program

def main():
    switch_func_dict = {
        "1": thank_you,
        "2": report,
        "3": exit_menu
    }
    while True:
        task_number = 0
        task_number = input("Welcome to the Mailroom! Please choose an option from the menu: "
                      "\n1. Send a Thank you "
                      "\n2. Create a Report "
                      "\n3. Quit"
                      "\n\n ----> ")
        while True:
            try:
                switch_func_dict.get(task_number)()
            except TypeError:
                print("Main menu input is invalid, enter 1 2 3 4 only please")
            finally:
                time.sleep(1)


if __name__ == "__main__":
    main()
