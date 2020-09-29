#!/bin/user/env python3

DEBUG = False

def get_names(record):
    """Extracts the first element from each list in a list of lists"""
    names = []
    for item in record:
        names.append(item[0])
    return names

def get_total(items):
    """Adds together all of the elements of a list, except the zeroth element"""
    total = 0
    for num in items[1:]:
        total += num
    if DEBUG: print(f"{items[0]} | {total}")
    return total

def send_thank_you():
    """Records a new donation and thanks the donor"""
    #Find out who to thank
    d_names = get_names(donors)
    name = input("Enter Donors Full Name> ").title()
    if DEBUG: print(f"name: {name}")
    while name == 'List':
        print(d_names)
        #Ensure correct capitalization
        name = input("Enter Doners Full Name> ").title()
        if DEBUG: print(f"name: {name}")
    #Allow user to leave mid task
    if name == 'Q':
        return False
    #Identify existing donor
    elif name in d_names:
        send_to = d_names.index(name)
    #Make new donor
    else:
        send_to = len(donors)
        donors.append([name])
    #Enter ammount
    money = input("Enter ammount donated> ")
    #Allow user to leave mid task
    if money.upper() == 'Q':
        if [name] in donors: donors.remove([name])
        return False
    #Add donation to records
    donors[send_to].append(int(money))
    #Send thank you
    print(f"Thank you {name} for your generous donation of {money}")
    return True
    
def create_a_report():
    """Prints report of contributions recived so far"""
    donors.sort(reverse = True, key = get_total)
    title_str = f"{'Donor Name':<25} | Total Given | Num Gifts | Average Gift"
    print(title_str)
    print('-'*len(title_str))
    for donor in donors:
        total = get_total(donor)
        num = len(donor) - 1
        average = total / num
        print(f"{donor[0]:<25} $ {total:>11.2f} {num:>11} $ {average:>12.2f}")
    return True

#Generate list of donors
#I'm inclined to use a dictonary of lists, but we haven't covered that yet
donors = [["Nick Esen", 1800, 720],
          ["Sabina", 1500],
          ["Marceline Theodosia", 30000, 500000, 100],
          ["Rafat Rein", 1500000],
          ["Kevin Both", 150, 1200, 750]]
if __name__ == "__main__":
    #I try to avoid while true
    option = ''
    while option != 'Q':
        #Promt user to select action
        menu = "(S)end a Thank You | (C)reate a Report | (Q)uit > "
        actions = ['S', 'C', 'Q']
        option = input(menu).upper()
        #catch unrecognized actions
        while option not in actions:
            print("That is not an option")
            option = input(menu).upper()
        if DEBUG: print(f"{option} is chosen")

        if option == 'S':
            send_thank_you()
        elif option == 'C':
            create_a_report()
        