#!/usr/bin/env python3
#Lesson 3 exercise "the mailroom", created by Niels Skvarch

#Import Modules needed to run
import sys


#define global variables
donor_db = [("Bob Johnson", [3772.32, 512.17]),
            ("Fred Billyjoe", [877.33, 455.50, 23.45]),
            ("Harry Richard", [1.50]),
            ("Old Gregg", [1663.23, 4300.87, 10432.0]),
            ("Jerry Vars", [19.95, 653.21, 99.00]),
            ]

menu = ("\n".join(("Welcome to the Mailroom.",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Run a report",
          "3 - Exit",
          ">>> ")))

#define functions		 
def print_report(data_lines):
    """Takes in a dataset and re-organizes it then displays it"""
    sizes = [0]*len(data_lines[0])
    for line in data_lines:
        for item_index, item in enumerate(line):
            if len(item) > sizes[item_index]:
                sizes[item_index] = len(item)

    for line in data_lines:
        print(line[0].ljust(sizes[0]) + "    $    " + line[1].ljust(sizes[1]) + "    " + line[2].rjust(sizes[2]) + "    \t    " + line[3].rjust(sizes[3]))


    #  biggest_name = max(len(i[0]) for i in data_lines)
    #  biggest_donation = max(len(str(sum(i[1]))) for i in data_lines
    #  biggest_count = max(len(str(len(i[1]))) for i in data_lines
    #  biggest_average = max(len(str(round(sum(i[1]) / len(i[1]), 3))) for i in data_lines
    

def run_report(donor_db):
    """take in the list of doners, then sort and display the sorted data"""
    data_lines = [("Name", "Total Donated", "Times Donated", "Average Donation")]
    for donor in donor_db:
        data_lines.append((donor[0], str(max(donor[1])), str(len(donor[1])), str(max(donor[1]) / len(donor[1]))))
    print_report(data_lines)
        

def thanks():
    """create a thank you note customized to the name provided, 
    if the name was not in the list already, add the name and promt for a donation ammount"""
    name = input("\nPlease enter the name of the person donating: ")
    ammount = float(input("\nPlease enter the ammount donated:  "))  #forcing the float here will need error catch as invalid input crashes currently


    for donor in donor_db:
        donor_name = donor[0]
        if name.lower() == donor_name.lower():
            donor[1].append(ammount)
            print_thankyou(donor)
            return 
			
    donor = add_new_donor(name, ammount)
    print_thankyou(donor)

def print_thankyou(donor):
    """Takes in the name and donation ammount and organizes the valuses into a thank you letter"""
    nl = "\n"
    print(f"Dear {donor[0]},{nl}" +
                    f"    Thank you for your donation of $ {donor[1][-1]}. We {nl}" +
                    f"appreciate your contribution.{nl}{nl}    Your total donation amount is now " +
                    f"$ {sum(donor[1])}.{nl}{nl}" +
                    f"Sincerely,{nl}" +
                    f"Your Charity of Choice")


def add_new_donor(name, ammount):
    """add a donor not in the list to the list"""
    new_donor = (name, [ammount])
    donor_db.append(new_donor)
    return new_donor


def exit_program():
    """use the sys module to clean-exit the script"""
    print("Good bye")
    sys.exit()
    

def main():
    """"main while loop for the program to occupy while running"""
    while True:
        response = input(menu)
        if response == "1":
            thanks()
        elif response == "2":
            run_report(donor_db)
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")






#main program name-space
if __name__ == "__main__":
    main()
	


