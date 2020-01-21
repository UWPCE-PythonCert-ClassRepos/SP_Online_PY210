#!/usr/bin/env python
import sys
from donor_models import DonorCollection

"""
cli_main.py: command line interface
lesson 9
joli umetsu
python210
"""
       
# quit commands
quit_request = ('q', 'quit')

   
def send_letters(donors):
    donors.letters()
    print("\n\tLetters successfully sent.\n")


def report(donors):
    title = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    header = "|".join(("{:<{}}".format(title[0],20),
            "{:^{}}".format(title[1],13),
            "{:^{}}".format(title[2],11),
            "{:^{}}".format(title[3],13)))
    print("\n".join(("\n", header, "-"*59)))
    records = donors.report()
    for donor, total, number, average in records:
        print("{:<{}}${:>{}.2f}{:>{}}  ${:>{}.2f}".format(donor,20+1,total,13-2,number,11+1,average,13-2))    
    return


def email(name, amount):
    text = "\n".join(("-"*55,
        "Dear {},\n".format(name), 
        "\tThank you for your generous donation of ${:.2f}.\n".format(float(amount)), 
        "\tIt will be put to very good use.\n",
        "\t\tSincerely,",
        "\t\t  -The Team",
        "-"*55))
    print(text)
    return


def update_donors(name, amount, donors):
    try: 
        amount = float(amount)
    except TypeError:
        print("\n\tERROR: Must be a valid numerical amount.")
        return None
    except ValueError:
        print("\n\tERROR: Must be a valid numerical amount.")
        return None
    else:
        if name in donors.search_donor(name):
            donors.update_donor(name, amount)
            return amount
        else:
            donors.add_donor(name, amount)
            return amount


def thank_you(donors):
    while True:
        name = input("\tEnter full name >>>  ").title()
        if name.lower() in quit_request:
            return
        elif name == "List":
            print(donors.list_donors())
            continue # go back to top of loop and re-prompt
        elif name == "":
            continue
        else: # if user enters a name
            amount = input("\tEnter donation amount >>>  ")
            donation = update_donors(name, amount, donors)
            if donation == None:
                return
            else:
                email(name, donation)
                break

 
def user_input():
    menu = "\n".join(("","{:^50}".format("Select from one of the options shown below:"),
    "\t'1'  Send a Thank You to a single donor", 
    "\t'2'  Create a Report", 
    "\t'3'  Send letters to ALL donors",
    "\t'4'  Quit",
    "\n\tEnter option >>> "))   
    return input(menu)
    
    
def quit_program(donors): 
    print("\n","~~~~~~~~~~~~~~~~~~~~~~~~~ GOODBYE ~~~~~~~~~~~~~~~~~~~~~~~~~","\n")
    sys.exit()
 
 
def main():
    print("\n","************************* WELCOME *************************","\n")
    
    donors = DonorCollection()
     # menu options dictionary
    options = {
        '1': thank_you,
        '2': report,
        '3': send_letters,
        '4': quit_program,
        'q': quit_program,
        'quit': quit_program
        }
    while True: 
        selection = user_input().lower()
        if selection in options:
            options.get(selection)(donors)
        else:
            print("\n\tERROR: Invalid option. Please try again!")
    
if __name__ == "__main__":
    main()