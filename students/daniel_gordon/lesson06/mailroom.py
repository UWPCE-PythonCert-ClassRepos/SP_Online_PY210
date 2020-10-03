#!/bin/user/env python3

import pathlib

DEBUG = False

#I focused on Exceptions surrounding user input and writing to a file
#I did not find any cases to use Comprehensions
#Please let me know if I missed any opportunities to practice these skills

def menu_dispatch(prompt, menu):
    """prints prompt and uses response to call functions from a dictionary"""
    while True: 
        try:
            response = input(prompt).upper()
            if menu[response]() == "quit":
                break
        except KeyError:
            print(f"{response} is not an option")

def make_list(donors):
    return list(donors.keys())
    
def add_donation(name, money):
    """Add donation to records"""
    donors.setdefault(name,[]).append(money)
    return True

def thank_you(name, money):
    """Create thank you text"""
    return f"Thank you {name} for your generous donation of {money}"

def get_key(donor):
    """Extracts the sum of list form donor"""
    return get_total(donor[1])

def get_total(nums):
    """Adds together all of the elements of a list"""
    total = 0
    for num in nums:
        total += num
    if DEBUG: print(total)
    return total

def report_entry(donor):
    """Generate a line for the report"""
    total = get_total(donor[1])
    num = len(donor[1])
    average = total / num
    return f"{donor[0]:<25}  ${total:>11.2f} {num:>11}  ${average:>12.2f}"

def make_path(path):
    """Make a directory at the given path"""
    path = pathlib.Path(path)
    if not path.exists(): path.mkdir() 
    return True

def write_letter(donor):
    """Generate the text for a letter"""
    letter = f"Dear {donor},\n\n"
    letter += f"\tThank you for your donation of {donors[donor][-1]}\n\n"
    letter += "\tSincerly,\n"
    letter += "\t\tThe Team"
    return letter

def send_thank_you():
    """Records a new donation and thanks the donor"""
    #Find out who to thank
    name = 'List'
    while name == 'List':
        print(make_list(donors))
        #Ensure correct capitalization
        while True:
            try:
                name = input("Enter Doners Full Name> ").title()
                if DEBUG: print(f"name: {name}")
                break
            except EOFError:
                #If this happens, the user may be trying to quit
                print("End of file detected, leaving program")
                return False
    #Allow user to leave mid task
    if name == 'Q': return False
    #Enter ammount
    while True:
        try:
            money = float(input("Enter ammount donated> "))
            break
        except ValueError:
            print("Please enter a number")
    add_donation(name, money)
    print(thank_you(name, money))
    return True
    
def create_a_report():
    """Prints report of contributions recived so far"""
    title_str = f"{'Donor Name':<25} | Total Given | Num Gifts | Average Gift"
    print(title_str)
    print('-'*len(title_str))
    #I could have used Comprehensions here to make the list of sorted keys
    #However useing the prexisting sorted() makes more sense
    for donor in sorted(donors.items(), key = get_key, reverse = True):
        print(report_entry(donor))
    return True

def send_letters():
    """Creates a letter for each donor thanking them for there latest donation"""
    make_path("./letters")
    for donor in donors:
        with open(f"./letters/{donor}.txt", "w") as file:
            file.write(write_letter(donor))
    return True

def exit_menu():
    return "quit"


#Generate list of donors
donors = {"Nick Esen": [1800, 720],
          "Sabina": [1500],
          "Marceline Theodosia": [30000, 500000, 100],
          "Rafat Rein": [1500000],
          "Kevin Both": [150, 1200, 750]}

main_menu = {'S': send_thank_you,
             'C': create_a_report,
             'L': send_letters,
             'Q': exit_menu}

main_prompt = "(S)end a Thank you | (C)reate a Report | Send (L)etters to all donors | (Q)uit >"

if __name__ == "__main__":
    menu_dispatch(main_prompt, main_menu)
        