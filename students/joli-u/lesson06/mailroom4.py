#!/usr/bin/env python
import sys
import pathlib
from operator import itemgetter

"""
mailroom part 4
lesson 6
joli umetsu
python210
"""

# define initial dictionary with donors and donation amounts 
donor_dict = {
    'Peregrin Took': [3002.50,100.25],
    'Gandalf the Grey': [5000.00, 580.00],
    'Smeagol': [45.01],
    'Samwise Gamgee': [500.53, 10000.89],
    'Frodo Baggins': [850.95,9000.30]
    }

# quit commands
quit_request = ('q', 'quit')

# main menu         
main_menu = "\n".join(("","{:^50}".format("Select from one of the options shown below:"),
    "\t'1'  Send a Thank You to a single donor", 
    "\t'2'  Create a Report", 
    "\t'3'  Send letters to ALL donors",
    "\t'4'  Quit",
    "\n\tEnter option >>> "))   

_w = 55


def letter_text(name,total):
   # define letter content 
    text = "\n".join(("Dear {},\n".format(name), 
        "\tThank you for your generous donations totaling ${:.2f}.\n".format(total), 
        "\tIt will be put to very good use.\n",
        "\t\tSincerely,",
        "\t\t  -The Team"))
    return text
    

def send_letters(d=donor_dict):
   # get current working directory
    cur_dir = pathlib.Path('./').absolute()
    try:
       # create new folder in cwd to save letters in 
        new_dir = 'letters'    
        (cur_dir / new_dir).mkdir()
    except FileExistsError:
        print("\n\tERROR: Files already exist!")
        return None 
    else:
        for donor, donations in d.items():
           # get contents of letter
            letter = letter_text(donor,sum(donations))
           # generate file name for letter 
            file_name = ('_'.join(donor.split(' ')))+".txt"
           # write letter to file 
            with open( (cur_dir / new_dir / file_name ), 'w') as f:
                f.write(letter)

def get_report(d=donor_dict):
   # create report with info in donor dict 
    report = []
    [ report.append([name, sum(donations), len(donations), sum(donations)/len(donations)]) for name, donations in d.items() ]
   # sort list by total donated amount 
    sorted_report = sorted(report, key=itemgetter(2))
    sorted_report.reverse()
    return sorted_report


def report():
   # print header of table 
    column_names = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    _c0w = 20
    _c1w = 13
    _c2w = 11
    _c3w = 13
    row_border = "-"*(_c0w+_c1w+_c2w+_c3w+2)
    header_text = "|".join(("{:<{}}".format(column_names[0],_c0w),
            "{:^{}}".format(column_names[1],_c1w),
            "{:^{}}".format(column_names[2],_c2w),
            "{:^{}}".format(column_names[3],_c3w)))
    print("\n".join(("\n", header_text, row_border)))
   # get full report 
    report = get_report()
   # print report 
    for donor,total,number,average in report:
        print("{:<{}}${:>{}.2f}{:>{}}  ${:>{}.2f}".format(donor,_c0w+1,total,_c1w-2,number,_c2w+1,average,_c3w-2))    

   
def list_donors(d=donor_dict):
    num = len(d)
    list = (num*"{}\n").format(*d)
    return print(list)            
     
     
def email(name,amount):
   # print email with thank you 
    border = "-"*_w
    body = "\n".join(("Dear {},\n".format(name), 
        "\tThank you for your generous donation of ${:.2f}.\n".format(float(amount)), 
        "\tIt will be put to very good use.\n",
        "\t\tSincerely,",
        "\t\t  -The Team"))
    return print("\n".join((border,body,border)))         
         

def update_donors(name,amount,d=donor_dict):
    try: 
        donation = float(amount)
    except ValueError:
        print("\n\tERROR: Must be a valid numerical amount.")
        return None 
    else:
   # if the name is already on the list, add donation amount to history 
        if name in d:
            d[name].append(donation)
            return donation 
        else:
            d[name] = [donation]
            return donation

            
def thank_you():
    while True:
        name = input("\tEnter full name >>>  ").title()
       # if user wants to quit, return to main menu
        if name.lower() in quit_request:
            return
       # if user enters 'list', print list of donors 
        elif name == "List":
            list_donors()
            # go back to top of loop and re-prompt user for name 
            continue
       # if user entered a name
        else:
           # get a donation amount
            amount = input("\tEnter donation amount >>>  ")
           # update donor history 
            donation = update_donors(name,amount)
            if donation == None:
                return 
           # email thank you letter 
            else:
                email(name, donation)
                break 


def quit_program():
   # exit message 
    greeting = " GOODBYE "
    N = (_w - len(greeting))/2
    message = "".join(((int(N)*"~"),greeting,(int(N)*"~")))
    print("\n",message,"\n")
   # quit program
    sys.exit()
                 

def main():
   # display welcome screen 
    greeting = " WELCOME "
    N = (_w - len(greeting))/2
    message = "".join(((int(N)*"*"),greeting,(int(N)*"*")))
    print("\n",message)
 
   # user options 
    switch_dict = {
        '1': thank_you,
        '2': report,
        '3': send_letters,
        '4': quit_program,
        'q': quit_program,
        'quit': quit_program
        }
    
    while True: 
        response = (input(main_menu)).lower()
        if response in switch_dict:
            switch_dict.get(response)()
        else:
            print("\n\tERROR: Invalid option. Please try again!")
    
    
if __name__ == "__main__":
    main()