#!/usr/bin/env python3

import io
import math

from Donor_Models import *  

'''Initial setup'''
#Default Values
don_col = Donor_Collect()
MS = Donor("Morgan Stanley")    
CV = Donor("Cornelius Vanderbilt")
JDR = Donor("John D. Rockefeller")
SG = Donor("Stephen Girard")
AC = Donor("Andrew Carnegie")
don_col.append(MS)
don_col.append(CV)
don_col.append(JDR)
don_col.append(SG)
don_col.append(AC)
MS.append([0.01, 20.00])
CV.append([800, 15, 10.00])
JDR.append([7000, 150.00, 25])
SG.append([60000])
AC.append([0.04, 999.99])

#Single Thank You
def receiver():
    viable_ans = False

    while viable_ans == False:
        new_vs_ex = input("Donor Name, List, Quit? ")
        name = new_vs_ex
        if new_vs_ex.lower() == "quit":
            name = "quit"
            viable_ans = True
            break
        elif new_vs_ex.lower() == "list":
            don_col.print_don_list()
            don_num = int(input("Select # above: "))
            try:
                name = don_col.donors[don_num-1]
            except IndexError:
                print("Must select a value from the list!")
                name = "quit"

        if new_vs_ex.lower() != "quit":
            donation_value = input("What is the value of the donation? ")            
            if donation_value.lower() == "quit":
                    name = "quit"
                    viable_ans = True
            elif isinstance(donation_value, float):
                    viable_ans = True                
        
        if name in don_col.donors: 
            name.append(float(donation_value))
            viable_ans = True
        else:
            #need string modification work here
            name = Donor(name)
            name.append(float(donation_value))
            don_col.append(name)
            viable_ans = True
    try:
        print("\n" + name.thank_you() + "\n")
    except AttributeError:
        name = "quit"    

    return name

#Send Letter
def send_letter():
    '''
    path = pathlib.Path.cwd() / 'mailroom'
    for k, v in donors.items():
        file_name = k + '_Thank you Letter.txt'
        with open(os.path.join(path, file_name), 'w') as l:
            l.write(email(k, sum(v)))
    print(f"Sending Letters to disk: {path}\n")
    '''
    pass

def report_bro():
    don_col.print_report()
    return

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
                    "2" : don_col.print_report,
                    "3" : send_letter,
                    "4" : quit,
                    }


if __name__ == "__main__":
    main_menu(choice_menu, main_selections)
    
    print(don_col.calc_report())