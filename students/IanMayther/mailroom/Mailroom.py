#!/usr/bin/env python3

import pathlib
import io
from collections import defaultdict, namedtuple

#DELIVERABLES
'''
Use comprehensions where appropriate

Use dicts where appropriate.
See if you can use a dict to switch between the user’s selections.
See if you can use a dict to switch between the users selections. see Using a Dictionary to switch for what this means.
Convert your main donor data structure to be a dict.
Try to use a dict and the .format() method to produce the letter as one big template, rather than building up a big string that produces the letter in parts.
'''

#Donors
donors = {"Morgan Stanely": [0.01, 20.00],
            "Cornelius Vanderbilt": [800, 15, 10.00],
            "John D. Rockefeller": [7000, 150.00, 25],
            "Stephen Girard": [60000],
            "Andrew Carnegie": [0.04, 999.99]}

#DefaultDict
'''
donor = namedtuple('Name', [])
dd = defaultdict(tuple)
dd['this'].append(23)
'''

#Single Thank You
def receiver():
    viable_ans = False
    #Determine Previous Donor
    while viable_ans == False:
        new_vs_ex = input("New Donor [Y/N/Quit]? ")

        if new_vs_ex.lower() == "y":
            name = new_donor()
            if name.lower() == "quit":
                name = "quit"
            viable_ans = True
        elif new_vs_ex.lower() == "quit":
            name = "quit"
            viable_ans = True
        elif new_vs_ex.lower() == "n":
            #to replace with comprehension
            i = 1
            temp_list = [key for key in sorted(donors.keys())]
            for key in sorted(donors):
                print(f"[{i}] - {key}")
                i += 1
                #"Commented" for comprehension => temp_list.append(key)

            donor_name = input("Who gave the donation [#]? ")

            if donor_name.lower() == "quit":
                name = "quit"

            name = temp_list[int(donor_name)-1]
            don_val = gift()
            donors[name].append(don_val)
            viable_ans = True
        else:
            print("Please enter a viable answer.")

    #Didn't use comprehension because, only wanted 1 set of values
    for k, v in donors.items():
        if k == name:
            don_val = sum(v)
            print("\n" + email(name, don_val))

    return name


#New Donor
def new_donor():
    name_of_new = input("What is the New Donor's Name: ")
    if name_of_new.lower() == "quit":
        name_of_new = "quit"
    elif name_of_new not in donors:
        dol_val = gift()
        donors[name_of_new] = [dol_val]

    return name_of_new

'''
Not need since using a dictionary for collection
#Donor Verification
def ver_don(giver):
    exist = False
    for i in range(len(donors)):
        if giver == donors[i][0]:
            exist = True
        else:
            exist = False
    return exist
'''
#Get Value of Donation
def gift():
    while True:
        try:
            value = float(input("What is the value of the donation: "))
            break      
        except ValueError:
            print("Not a valid donation value")
    return value


#Print Email
def email(to_donor, gift_amount):
    name = to_donor
    donation = gift_amount
    body = f"""Greetings {name}\n
\n
Thank you so much for your generous contribution to our charity.\n
It is donors like you who make our work of building schools for ants' possible.\n
With your gift of ${donation}, means (10) or (20) more schools can be built to help the ants learn to read.\n
\n
Sincerely,\n
Derek Zoolander\n
Founder and C.E.O. of Derek Zoolander Charity for Ants Who Can't Read Good (DZCAWCRG)\n"""
    return body


#Create Reportmy_List = {}
def print_report():
    #Header
    print("\n")
    print("{0:<25s}|{1:^15s}|{2:^15s}|{3:>12s}".format("Donor Name", "Total Given", "# of Gifts","Avg. Gift"))
    print("-" * 72)
    
    #Table Data
    '''
    for k, v in sorted(donors.items(), key=lambda t: sum(t[1]), reverse=True):
        #Process Data 
        total = sum(v)
        #Gift Count  
        No_Gifts = len(v)
        #Calc Average
        Ave_Gift = total / No_Gifts
        #Print Table
        print("{0:<25s}${1:>14.2f}{2:>17d}  ${3:>11.2f}".format(k, total, No_Gifts, Ave_Gift, end =''))
    '''
    #Replaced with comprehension
    new_dict = {k: [sum(v), len(v), sum(v)/len(v)] for k, v in sorted(donors.items())}
    for k in sorted(new_dict.items(), key=lambda t: t[1], reverse=True):
        print("{0:<25s}${1:>14.2f}{2:>17d}  ${3:>11.2f}".format(k[0], k[1][0], k[1][1], k[1][2], end =''))
    print("\n") 
    return

#Send Letter
def send_letter():
    path = pathlib.Path.cwd()
    for k, v in donors.items():
        file_name = k + '_Thank you Letter.txt'
        with open(file_name, 'w') as l:
            l.write(email(k, sum(v)))
    print(f"Sending Letters to disk: {path}\n")
    pass

#Quit
def quit():
    print("Quitting, Thank you.")
    return "quit"

#Main Menu Options
def main_menu(prompt, dict_choice):
    while True:
        choice = input(prompt)
#Try to handle non-list selections        
        try:
            if dict_choice[choice]() == "quit":
                break
        except KeyError:
            print("Please enter a number from the list.")

choice_menu = ("Choose an Action:\n"
            "\n"
            "1 - Send Thank You to Single Donor.\n"
            "2 - Create Report.\n"
            "3 - Send Letters to ALL Donor.\n"
            "4 - Quit.\n")

main_selections = {"1" : receiver,
                    "2" : print_report,
                    "3" : send_letter,
                    "4" : quit,
                    }
    

#Main Exicutable
if __name__ == '__main__':
    main_menu(choice_menu, main_selections)