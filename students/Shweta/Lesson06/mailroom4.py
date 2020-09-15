#!/usr/bin/env python
#mailroom part 1- from chapter 3

import sys
import os
from operator import itemgetter

#####################different messages#################

''' initial donars list '''

donar_db={"William Gate,III":[1000.00,4500.00],
          "Mark Zuckerbergs":[16000.00,2300.00],
          "Jeff Bezos":[23400.00,1200.00],
          "Paul Allen":[2345.00,1200.00],
        }

'''main message displayed on execution of this job'''
prompt_msg="\n".join(("Welcome for Donation Program !!",
                     "Please choose from following:",
                     "1- Send a Thank you",
                     "2- Create a Report",
                     "3- Send a letter to all the donors",
                     "4- Quit",
                     "Type a number to select >>> "))

'''message displayed for selecting the donors out of list'''
mty_prompt= "\n".join(("Please type the full name of the donar OR",
                       "type 'list' to see a list of donors",
                       "Type input here -->"))

'''thankyou message for donation'''
mty_msg="\n".join(("Thankyou {}",
                   "for your generous donation of {:.2f}",))


ltr="\n".join(("", "Dear {},",
              "Thank you for your very kind donation of ${:.2f}.",
              "It will be put to very good use.",
              "           Sincerely,",
              "               -The Team"))



#######################Thankyou Function###################
def send_thankyou():
    '''task 1 of the mail room- send thankyou for donations'''
    dname=input(mty_prompt)
    if print_list(dname) == dname:
        damt=input("Enter your donation amount in dollars-->")
        amt_validation(dname,damt)
    
#################create listed data################
def print_list(dname):
    if dname=='list':
        create_report()
    else:
        return dname

######################amt validation###########################
def amt_validation(dname,damt):
    try:
        damt=float(damt)
    except ValueError:
        print('\n Not a valid amount, try again')
    else:
        add_thanks(dname,damt)
    return damt

##############add and thank the new donor###############
def add_thanks(dname,damt):
    if donar_db.get(dname) == None:
        donar_db[dname]=[damt]
    else:
        donar_db.get(dname).append(damt)
    print(mty_msg.format(dname,damt))
    return(mty_msg.format(dname,damt))

########################send letter########################
def send_letter():
    for dn,da in donar_db.items():
        with open(dn.replace(' ','_') + ".txt",'w') as infile:
            infile.write(ltr.format(dn,sum(da)))
           
    print("Your letter is in {} ".format(os.getcwd()))


########################Create Report #####################

def create_report():
    '''task 2 of the mailroom - create report'''       
    top='{:20}| {:>20}|{:>20}| {:>20}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift')
    print(top)
    print('-'*100)
    print(type(donar_db))
    for key,value in sorted(donar_db.items(),key=lambda item:item[1], reverse=True):
        line='{:20} ${:>20.2f}   {:20}   ${:20.2f}'.format(key,sum(value),len(value),(sum(value)/len(value)))
        print(line)
    print('')


######################Exit Program#########################

def quit_pgm():
    ''' exit the program cleanly'''
    print("Bye!")
    sys.exit()

###try_catch added and using dict for selecting out of 4###

def main_decision(answer):
    try:
        dict_options.get(int(answer))()
    except (ValueError,NameError,TypeError):
        print("Please do select between 1-4,try again")

dict_options={
    1: send_thankyou,
    2: create_report,
    3: send_letter,
    4: quit_pgm
    }
    
###########Main block##################
def main():
    '''Main block of the code'''      
    while True:
        answer = input(prompt_msg)
        main_decision(answer)
        
if __name__ == "__main__":
    main()
            
            
