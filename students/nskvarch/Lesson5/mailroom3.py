#!/usr/bin/env python3
# Lesson 5 exercise "the mailroom part 3", created by Niels Skvarch

# Import Modules needed to run
import sys
import os

# define global variables
donor_db = {"Bob Johnson": [3772.32, 512.17],
            "Fred Billyjoe": [877.33, 455.50, 23.45],
            "Harry Richard": [1.50],
            "Old Gregg": [1663.23, 4300.87, 10432.0],
            "Jerry Vars": [19.95, 653.21, 99.45],
            }

menu = ("\n".join(("Welcome to the Mailroom.",
                   "Please choose from below options:",
                   "1 - Add a new contribution and display sample thank you letter",
                   "2 - Display a donor Report",
                   "3 - Create a thank you letter for all donors",
                   "4 - Exit",
                   "--> ")))


# define functions
def print_report(data_lines):
    """Take in a table in the form of a list and display it"""
    sizes = [0] * len(data_lines[0])
    for line in data_lines:
        for item_index, item in enumerate(line):
            if len(item) > sizes[item_index]:
                sizes[item_index] = len(item)

    for line in data_lines:
        print(line[0].ljust(sizes[0]) + "    $    " + line[1].ljust(sizes[1]) + "    " + line[2].rjust(
            sizes[2]) + "    \t    " + line[3].rjust(sizes[3]))
    print("\n")


def run_report():
    """take in the donor database, create organize and sort a table in the form of a list and then hand the table off
    to the printer function """
    data_lines = []
    for name in donor_db:
        data = donor_db[name]
        data_lines.append((name, str(sum(data)), str(len(data)), str(sum(data) / len(data))))

    to_print = [("Name", "Total Donated", "Times Donated", "Average Donation")] + \
               sorted(data_lines, key=lambda x: float(x[1]), reverse=True)
    print_report(to_print)


def thanks():
    """create a thank you note customized to the name provided,
    if the name was not in the donor database already, add the name and prompt for a donation amount"""
    while True:
        response = input("\nPlease enter the name of the person donating or type 'List' for a list of donors: ")

        if response.lower() == "list":
                run_report()
        else:
            while True:
                try:
                    amount = float(input("\nPlease enter the amount donated:  "))
                    break
                except ValueError:
                    print("\nOops! Something went wrong. Please enter a numerical value.")
            for donor_name in donor_db:
                if response.lower() == donor_name.lower():
                    donor_db[donor_name].append(amount)
                    print_thankyou(donor_name)
                    return donor_db

        donor_name = add_new_donor(response, amount)
        print_thankyou(donor_name)
        return donor_db


def print_thankyou(donor_name):
    """Takes in the name and donation amount and organizes the values into a sample thank you letter and displays
    it on the screen """
    nl = "\n"
    print(f"Dear {donor_name},{nl}" +
          f"    Thank you for your donation of $ {donor_db[donor_name][-1]}. We {nl}" +
          f"appreciate your contribution.{nl}{nl}    Your total donation amount is now " +
          f"$ {sum(donor_db[donor_name])}.{nl}{nl}" +
          f"Sincerely,{nl}" +
          f"Your Charity of Choice")


def create_thankyou_all():
    """Takes in the name and donation ammount for all donors and creates a thank you text document
    in the same folder the program is run from for each donor, unless a specific directory is specified"""
    nl = "\n"

    custom = input("Press Enter to create the letters in the directory the Mailroom has been run from"
                          " or type 'custom' to specify a directory")
    # I had to get creative here as the error catch needs to come before
    # the Open operator so I can request input again rather than a try loop around the 'with open'
    if custom != "":
        while True:
            customdir = input("Please specify a custom directory path:  ")
            tested = os.path.exists(customdir)
            if tested == True:
                break
            elif tested == False:
                print("That directory or path does not exist, please specify a valid directory")
        cwd = customdir

    elif custom == "":
        cwd = os.getcwd()
    for donor_name in donor_db:
        filename = donor_name.replace(" ", "") + ".txt"
        full_filename = os.path.join(cwd, filename)
        with open(full_filename, 'w') as f:
            f.write(f"Dear {donor_name},{nl}" +
                    f"    Thank you for your donation of $ {donor_db[donor_name][-1]}. We {nl}" +
                    f"appreciate your contribution.{nl}{nl}    Your total donation amount is now " +
                    f"$ {sum(donor_db[donor_name])}.{nl}{nl}" +
                    f"Sincerely,{nl}" +
                    f"Your Charity of Choice"
                    )


def add_new_donor(name, amount):
    """add a donor not in the donor database to the database"""
    donor_db.update({name: [amount]})
    return name


def exit_program():
    """use the sys module to clean-exit the script"""
    print("Good bye")
    sys.exit()


def main():
    """"main loop for the program to occupy while running, includes the main menu"""
    while True:
        response = input(menu)
        switch_dict = {"1": thanks, "2": run_report, "3": create_thankyou_all}
        if response in switch_dict:
            switch_dict[response]()
        elif response == "4":
            exit_program()
        else:
            print("Not a valid option!")


# main program name-space
if __name__ == "__main__":
    main()
