#!/bin/user/env python3

import pathlib

DEBUG = False

def menu_dispatch(prompt, menu):
    """prints prompt and uses response to call functions from a dictionary"""
    while True: 
        response = input(prompt).upper()
        while response not in menu:
            print(f"{response} is not an option")
            response = input(prompt).upper()
        if menu[response]() == "quit":
            break

def get_total(items):
    """Adds together all of the elements of a list stored in a tuple"""
    """items is a ("name", [list]) pair"""
    total = 0
    for num in items[1]:
        total += num
    if DEBUG: print(total)
    return total

def send_thank_you():
    """Records a new donation and thanks the donor"""
    #Find out who to thank
    name = input("Enter Donors Full Name> ").title()
    if DEBUG: print(f"name: {name}")
    while name == 'List':
        print(list(donors.keys()))
        #Ensure correct capitalization
        name = input("Enter Doners Full Name> ").title()
        if DEBUG: print(f"name: {name}")
    #Allow user to leave mid task
    if name == 'Q': return False
    #Enter ammount
    money = input("Enter ammount donated> ")
    #Allow user to leave mid task
    if money.upper() == 'Q': return False
    #Setup empty list for new donor
    if name not in donors: donors[name] = []
    #Add donation to records
    donors[name].append(float(money))
    #Send thank you
    print(f"Thank you {name} for your generous donation of {money}")
    return True
    
def create_a_report():
    """Prints report of contributions recived so far"""
    title_str = f"{'Donor Name':<25} | Total Given | Num Gifts | Average Gift"
    print(title_str)
    print('-'*len(title_str))
    for donor in sorted(donors.items(), key = get_total, reverse = True):
        total = get_total(donor)
        num = len(donor[1])
        average = total / num
        print(f"{donor[0]:<25} $ {total:>11.2f} {num:>11} $ {average:>12.2f}")
    return True

def send_letters():
    """Creates a letter for each donor thanking them for there latest donation"""
    path = pathlib.Path('./letters')
    if not path.exists(): path.mkdir()
    for donor in donors:
        with open(f"./letters/{donor}.txt", "w") as file:
            file.write(f"Dear {donor},\n\n")
            file.write(f"\tThank you for your donation of {donors[donor][-1]}\n\n")
            file.write("\tSincerly,\n")
            file.write("\t\tThe Team")
    return True

def exit_menu():
    return "quit"


#Generate list of donors
donors = {"Nick Esen" : [1800, 720],
          "Sabina" : [1500],
          "Marceline Theodosia" : [30000, 500000, 100],
          "Rafat Rein" : [1500000],
          "Kevin Both" : [150, 1200, 750]}

main_menu = {'S' : send_thank_you,
             'C' : create_a_report,
             'L' : send_letters,
             'Q' : exit_menu}

main_prompt = "(S)end a Thank you | (C)reate a Report | Send (L)etters to all donors | (Q)uit >"

if __name__ == "__main__":
    menu_dispatch(main_prompt, main_menu)
        