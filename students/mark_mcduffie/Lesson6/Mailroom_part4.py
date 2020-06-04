'''
Mark McDuffie
5/25/19
Mailroom part 4

'''

import operator
import os

#Original Donor list, used and added upon in the program
#conatins two columns for first and last name, and up to 3 more for donation amounts
def donors():
    return{
          "Jim Johnson": [20000.0, 3500.0, 1600.0],
          "Mike Lee": [10000.0, 450.0, 1000.0],
          "Joe Smith": [100.0, 50.0],
          "Bob Miller": [900.0, 1200.0],
          "Steve James": [100000.0]
          }

#The script should prompt the user (you) to choose from a menu of 3 actions:
#“Send a Thank You”, “Create a Report” or “quit”
def prompt():
    choice = input("You have the following options: \n 1: Send a Thank You \n 2: Send Letters to all Donors "
                   "\n 3: Create a Report \n 4: Quit \n")
    return choice

#Prints a nicely formatted email to donor
def print_email(name, amount):
    email = (f'Dear {name},'
             f'\n \tThank you for your donation of ${amount:,.2f}. '
             '\nYour generosity is greatly appreciated, we '
             '\nlook forward to hearing from you again. '
             "\nCheers, \nThe Mailroom")
    return email

#Used in Thank you method, allows us to access just a list of donor names to check
def donor_names(donors):
    namesList =[]
    for key in donors.keys():
        namesList.append(key)
    return namesList

#thank you method allows user to add donor and/or donation amount to the list
#Calls other methods print_list, and exists, to show formatted list, and check if donor exists
def single_thank_you():
    donor = input("Please enter Donor name (first and last), \nor enter 'list' if you want to see the full list of Donors. \n")
    try:
        if donor.lower() == 'list':         #shows formatted list if user wants to check
            print(donor_names(donors))
        else:
            amount = float(input("How much did " + donor + " donate? "))
            if donor in donors:
                donors[donor].append(amount)
            else:
                donors[donor] = [amount]      #Appends new donor and amount if donor does not exist
            print(print_email(donor, amount))  #Method to end official letter once name and donation are entered
    except ValueError as error_message:
        print(error_message)
    return main()

#Sends a thank you to ever donor on the list, creating individual text files
def write_files():
    for donor in donors:
        amount = sum(donors.get(donor))
        with open(f'{donor}.txt', 'w') as f:
            f.write(print_email(donor, amount))

#Checks to see if directory exists, and sends files
def send_all():
    try:
        write_files()
    except FileExistsError as error_message:
        print(error_message)
    print("Letter were created and are in the {} directory.".format(os.getcwd()))

#Creates a well formatted report, counting every person's donation and calcuting their average
def report():
    sorted_donors = sorted(donors.items(), key=operator.itemgetter(1), reverse=True)
    print("Donor Name" + " " * 16 + "| Total Given | Num Gifts | Average Gift")
    print("-" * 66)
    for i in sorted_donors:
        print("{:<25} ${:>12.2f}  {:>9d}   ${:>11.2f}".format(i[0], sum(i[1]), len(i[1]), sum(i[1])/len(i[1])))
        #generates statistics for each row in the report
        # adds all donations for each name
        # counts the total number of gifts for each donor
        #calculates average donation
    return main()

#Main function for interactions
def main():

    while True:
        choice = int(prompt())
        choice_Dict = {
            1: single_thank_you,
            2: send_all,
            3: report,
            4: quit
        }
        if choice in choice_Dict:
            choice_Dict.get(int(choice))()
        else:
            print("Please enter a choice number between 1 and 4")


if __name__ == '__main__':
    donors = donors()
    main()