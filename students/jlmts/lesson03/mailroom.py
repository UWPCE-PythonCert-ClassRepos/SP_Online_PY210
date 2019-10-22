#!/usr/bin/env python
import sys

"""
assignment 1: mailroom 
joli umetsu
python210
"""

# define starting list with donors and corresponding donation amounts 
donor_list = [ ('Peregrin Took', [3002.50,100.25]), ('Gandalf the Grey', [5000.00, 580.00]), ('Smeagol', [45.01]), ('Samwise Gamgee', [500.53, 10000.89]), ('Frodo Baggins', [850.95,9000.30]) ]
# main menu         
user_prompt = "\n".join(("","{:^50}".format("Select from one of the options shown below:"), "\t\t'1'  Send Thank You", "\t\t'2'  Create Report", "\t\t'3'  Quit","", "\t\tEnter option >>> "))    


def report(donor_list):
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
    for i,j in donor_list:
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
    

def thank_you(donors):
    
    quit_request = ('q', 'quit')
    # prompt user for name input 
    prompt_name = "\t\tEnter full name >>>  "
    name = input(prompt_name).title()
    if name.lower() in quit_request:
        return 
    
    # show list of donor names if user selects 'list' and reprompt
    while name == "List":
        print((len(donors)*"{}\n").format(*donors))
        name = input(prompt_name).title()
        if name.lower() in quit_request:
            return
        
    # if user does not select 'list' (assume it's a name), ask for donation amount
    prompt_amount = "\t\tEnter donation amount >>>  "
    amount = input(prompt_amount)
    if amount.lower() in quit_request:
        return 
        
    # if the name is already on the list, add donation amount to history    
    if name in donors:
        for i,j in donor_list:
            if i == name:
                j.append(float(amount))
                email(name)
            else: pass 
            
    # for names not already on the list, add the new name and donation 
    else: 
        donor_list.append((name,[float(amount)]))
        email(name)


def email(recipient):
    # print email with thank you 
    _head = "{:^50}".format("".join(((15*"-")," COMPOSE EMAIL: ",(15*"-"))))
    _end = "{:^50}".format("".join(((20*"-"),"[END]",(21*"-"))))
    _line = "{:^50}".format(46*"-")
    body = "\n".join(("\tDear {},\n".format(recipient), "\tThank you for your generous donation.\n", "\tSincerely,","\tJoli"))
    print("\n".join(("\n",_head,_line,body,_line,_end)))


def quit_program():
    print("\n")
    print("{:^50}".format("".join(((20*"~")," GOODBYE! ",(20*"~")))))
    sys.exit()


def main():
    # display welcome screen 
    print("{:^50}".format(50*"*"))
    print("{:^50}".format("".join(((20*"*")," WELCOME! ",(20*"*")))))
    print("{:^50}".format(50*"*"))

    # create subset lists of donor names; donation amounts 
    donors = []
    donations = []
    for each_donor in donor_list:
        donors.append(each_donor[0])
        donations.append(each_donor[1:])   
    
    while True: 
        response = input(user_prompt)
        if response == "1":
            thank_you(donors)
        elif response == "2":
            report(donor_list)
        elif response == "3" or "q".lower():
            quit_program()
        else:
            print("Invalid option. Please try again!")
    
    
if __name__ == "__main__":
    main()