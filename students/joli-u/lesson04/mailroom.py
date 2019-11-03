#!/usr/bin/env python
import sys
import pathlib

"""
assignment 2: mailroom 
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
    new_dir = 'thank_you_letters'
    
    # create new folder in cwd to save letters in 
    (cur_dir / new_dir).mkdir()
    
    for donor, donations in donor_dict.items():
        # calculate donor contribution 
        total = sum(donations)
        num = len(donations)
        # define letter content 
        msg = "\n".join(("Dear {},\n".format(donor), 
        "\tThank you for your {} generous donation(s), totaling ${:.2f}.\n".format(num,float(total)), 
        "\tIt will be put to very good use.\n",
        "\t\tSincerely,",
        "\t\t  -The Team"))
        
        # generate file name for letter 
        file_name = ('_'.join(donor.split(' ')))+".txt"
        
        # write letter to file 
        with open( (cur_dir / new_dir / file_name ), 'w') as f:
            f.write(msg)


def report():
    header = ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    col_wid1 = 20
    col_wid2 = 13
    col_wid3 = 11
    col_wid4 = 13
    print("\n")
    print("|".join(("{:<{}}".format(header[0],col_wid1),"{:^{}}".format(header[1],col_wid2),"{:^{}}".format(header[2],col_wid3),"{:^{}}".format(header[3],col_wid4))))
    print((col_wid1+col_wid2+col_wid3+col_wid4+2)* "-")
    
    # create new list to include report values
    report_list = []
    for i,j in donor_dict.items():
        total = round(sum(j),2)
        number = len(j)
        average = round((total/number),2)
        report_list.append([i,j,total,number,average])
     
    # sort new list by total donated amount
    from operator import itemgetter
    sorted_list = sorted(report_list, key=itemgetter(2))
    sorted_list.reverse()
    
    # print report 
    for a,b,c,d,e in sorted_list:
        print("{:<{}}${:>{}.2f}{:>{}}  ${:>{}.2f}".format(a,col_wid1+1,c,col_wid2-2,d,col_wid3+1,e,col_wid4-2))    
    

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
    amount = input(prompt_amount)
    if amount.lower() in quit_request:
        return 
        
    # if the name is already on the list, add donation amount to history    
    elif name in donor_dict:
        donor_dict[name].append(float(amount))
        email(name,amount)
            
    # for names not already on the list, add the new name and donation 
    else: 
        donor_dict[name] = [float(amount)]
        email(name,amount)


def email(name,amount):
    # print email with thank you 
    msg_head = "{:^50}".format("".join(((17*"-")," COMPOSE EMAIL: ",(17*"-"))))
    msg_end = "{:^50}".format("".join(((22*"-"),"[END]",(23*"-"))))
    
    body = "\n".join(("Dear {},\n".format(name), 
        "\tThank you for your generous donation of ${:.2f}.\n".format(float(amount)), 
        "\tIt will be put to very good use.\n",
        "\t\tSincerely,",
        "\t\t  -The Team"))
    print("\n".join(("\n",msg_head,body,msg_end)))


def quit_program():
    msg = "{:^50}".format("".join(((20*"~")," GOODBYE! ",(20*"~"))))
    print("\n"+msg+"\n")
    sys.exit()
                 

def main():
    # display welcome screen 
    msg = "{:^50}".format("".join(((20*"*")," WELCOME! ",(20*"*"))))
    ln = "{:^50}".format(50*"*")
    print("\n"+msg+"\n"+ln)
 
    switch_dict = {
        '1': thank_you,
        '2': report,
        '3': send_letters,
        '4': quit_program,
        'q': quit_program
        }
    
    while True: 
        response = input(user_prompt)
        
        if response in switch_dict:
            switch_dict.get(response)()
        else:
            print("Invalid option. Please try again!")
            response = input(user_prompt)
    
    
if __name__ == "__main__":
    main()