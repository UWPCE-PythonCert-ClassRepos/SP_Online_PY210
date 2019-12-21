#!/usr/bin/env python
import sys
import pathlib
from operator import itemgetter

"""
lesson 5 
mailroom part 3
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

# main menu         
user_prompt = "\n".join(("","{:^50}".format("Select from one of the options shown below:"),
    "\t'1'  Send a Thank You to a single donor", 
    "\t'2'  Create a Report", 
    "\t'3'  Send letters to ALL donors",
    "\t'4'  Quit",
    "\n\tEnter option >>> "))   


def send_letters():
    # get current working directory
    cur_dir = pathlib.Path('./').absolute()
    try:
        # create new folder in cwd to save letters in 
        new_dir = 'thank_you_letters'    
        (cur_dir / new_dir).mkdir()
    except FileExistsError:
        print("\n\tERROR: Files already exist!")
    else:
        for donor, donations in donor_dict.items():
            # define letter content 
            msg = "\n".join(("Dear {},\n".format(donor), 
            "\tThank you for your {} generous donation(s), totaling ${:.2f}.\n".format(len(donations),sum(donations)), 
            "\tIt will be put to very good use.\n",
            "\t\tSincerely,",
            "\t\t  -The Team"))
            
            # generate file name for letter 
            file_name = ('_'.join(donor.split(' ')))+".txt"
            
            # write letter to file 
            with open( (cur_dir / new_dir / file_name ), 'w') as f:
                f.write(msg)


def report():
    # print header of table 
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    cw1 = 20
    cw2 = 13
    cw3 = 11
    cw4 = 13
    head = "|".join(("{:<{}}".format(header[0],cw1),"{:^{}}".format(header[1],cw2),"{:^{}}".format(header[2],cw3),"{:^{}}".format(header[3],cw4)))
    print("\n".join(("\n", head, (cw1+cw2+cw3+cw4+2)*"-")))
    
    # create new list to include report values
    report = []
    [ report.append([i, sum(j), len(j), sum(j)/len(j)]) for i, j in donor_dict.items() ]
     
    # sort new list by total donated amount
    sorted_report = sorted(report, key=itemgetter(2))
    sorted_report.reverse()
    
    # print report 
    for don,tot,num,avg in sorted_report:
        print("{:<{}}${:>{}.2f}{:>{}}  ${:>{}.2f}".format(don,cw1+1,tot,cw2-2,num,cw3+1,avg,cw4-2))    
    

def thank_you():   
    quit_request = ('q', 'quit')
    
    # prompt user for name input 
    prompt_name = "\tEnter full name >>>  "
    name = input(prompt_name).title()
    
    # return to main menu if user opts to quit 
    if name.lower() in quit_request:
        return 
    
    # show list of donor names if user selects 'list' and reprompt
    while name == "List":
        print((len(donor_dict)*"{}\n").format(*donor_dict))
        name = input(prompt_name).title()
        if name.lower() in quit_request:
            return
  
    # if user does not select 'list' (assume it's a name), ask for donation amount
    prompt_amount = "\tEnter donation amount >>>  "
    try: 
        amount = float(input(prompt_amount))
    except ValueError:
        print("\n\tERROR: Must be a valid numerical amount.")
    else:
        # if the name is already on the list, add donation amount to history 
        if name in donor_dict:
            donor_dict[name].append(amount)
            email(name,amount)
        else:
            donor_dict[name] = amount
            email(name,amount)


def email(name,amount):
    # print email with thank you 
    head = "{:^50}".format("".join(((17*"-")," COMPOSE EMAIL: ",(17*"-"))))
    end = "{:^50}".format("".join(((22*"-"),"[END]",(23*"-"))))
    body = "\n".join(("Dear {},\n".format(name), 
        "\tThank you for your generous donation of ${:.2f}.\n".format(float(amount)), 
        "\tIt will be put to very good use.\n",
        "\t\tSincerely,",
        "\t\t  -The Team"))
    print("\n".join((head,body,end)))


def quit_program():
    msg = "{:^50}".format("".join(((20*"~")," GOODBYE! ",(20*"~"))))
    print("\n".join(("\n",msg)))
    sys.exit()
                 

def main():
    # display welcome screen 
    msg = "{:^50}".format("".join(((20*"*")," WELCOME! ",(20*"*"))))
    ln = "{:^50}".format(50*"*")
    print("\n".join((ln,msg)))
 
    switch_dict = {
        '1': thank_you,
        '2': report,
        '3': send_letters,
        '4': quit_program,
        'q': quit_program,
        'quit': quit_program
        }
    
    while True: 
        response = (input(user_prompt)).lower()
        
        if response in switch_dict:
            switch_dict.get(response)()
        else:
            print("\n\tERROR: Invalid option. Please try again!")
    
    
if __name__ == "__main__":
    main()