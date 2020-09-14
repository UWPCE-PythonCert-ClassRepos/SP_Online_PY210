#!/usr/bin/env python
import donor_model as d
import sys

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

donor_db= d.DonorCollection(d.Donor("William Gate,III",[100000.00,45000.00]),
                            d.Donor("Mark Zuckerbergs",[16000.00,2300.00]),
                            d.Donor("Jeff Bezos",[23400.00,1200.00]),
                            d.Donor("Paul Allen",[2345.00,1200.00])
                            )


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
        if damt < 0:
            raise negativeValueError("Invalid value")
            
    
    except (ValueError) as err:
        print('\n Not a valid amount, try again')
    except:
        print("Negative Value not allowed")
    else:
        mgr=donor_db.add_donor(dname,damt)
        print (mgr)
    return damt
    

########Generate Report######################

def sort_key(line):
    return int(sum(line[1]))

def create_report():
    top='{:20}| {:>20}|{:>20}| {:>20}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift')
    print(top)
    print('-'*100)
    lines=donor_db.create_report()
    #print(type(lines))
    #for line in lines:
    for line in sorted(lines,key=lambda item:item[1], reverse=True):
        print(line)
    return lines
    #print('')


###############Send Letter#########################
def send_letter():
    print("i am in send letter")
    donor_db.send_letter()


######################Exit Program#################

def quit_pgm():
    ''' exit the program cleanly'''
    print("Bye!")
    sys.exit()

###################Decision Section#################

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


def main():
    '''Main block of the code'''
    while True:
        answer = input(prompt_msg)
        main_decision(answer)

if __name__ == "__main__":
    main()
