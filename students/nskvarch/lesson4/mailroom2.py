#!/usr/bin/env python3
# Lesson 4 exercise "the mailroom part 2", created by Niels Skvarch

# Import Modules needed to run
import sys
import os

# define global variables
donor_db = {"Bob Johnson": [3772.32, 512.17],
            "Fred Billyjoe": [877.33, 455.50, 23.45],
            "Harry Richard": [1.50],
            "Old Gregg": [1663.23, 4300.87, 10432.0],
            "Jerry Vars": [19.95, 653.21, 99.00],
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


def run_report():
    """take in the donor database, create organize and sort a table in the form of a list and then hand the table off
    to the printer function """
    data_lines = []
    for name in donor_db:
        data = donor_db[name]
        data_lines.append((name, str(sum(data)), str(len(data)), str(sum(data) / len(data))))

    to_print = [("Name", "Total Donated", "Times Donated", "Average Donation")] +\
               sorted(data_lines, key=lambda x: float(x[1]), reverse=True)
    print_report(to_print)


def thanks():
    """create a thank you note customized to the name provided, 
    if the name was not in the donor database already, add the name and promt for a donation ammount"""
    while True:
        response = input("\nPlease enter the name of the person donating or type 'List' for a list of donors: ")

        if response.lower() == "list":
            run_report()
        else:
            ammount = float(input("\nPlease enter the ammount donated:  "))
            for donor_name in donor_db:
                if response.lower() == donor_name.lower():
                    donor_db[donor_name].append(ammount)
                    print_thankyou(donor_name)
                    return donor_db

            donor_name = add_new_donor(response, ammount)
            print_thankyou(donor_name)
            return donor_db


def print_thankyou(donor_name):
    """Takes in the name and donation ammount and organizes the valuses into a sample thank you letter and displays
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
    cwd = os.getcwd()
    customdir = input("Specify a directory for the letters to go in or press enter to use the current directory : ")
    if customdir != "":
        cwd = customdir
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


def add_new_donor(name, ammount):
    """add a donor not in the donor database to the database"""
    donor_db.update({name: [ammount]})
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
