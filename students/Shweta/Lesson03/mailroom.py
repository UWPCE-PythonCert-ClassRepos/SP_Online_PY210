#!/usr/bin/env python3
#mailroom part 1- from chapter 3

import sys


''' initial donars list '''

donar_db=[("William Gate,III",[100000.00,45000.00]),
          ("Mark Zuckerbergs",[16000.00,2300.00]),
          ("Jeff Bezos",[23400.00,1200.00]),
          ("Paul Allen",[2345.00,1200.00]),
        ]

'''main message displayed on execution of this job'''
prompt_msg="\n".join(("Welcome for Donation Program !!",
                     "Please choose from following:",
                     "1- Send a Thank you",
                     "2- Create a Report",
                     "3- Quit",
                     "Type a number to select >>> "))

'''message displayed for selecting the donors out of list'''
mty_prompt= "\n".join(("Please type the full name of the donar OR",
                       "type 'list' to see a list of donors",
                       "Type input here -->"))

'''thankyou message for donation'''
mty_msg="\n".join(("Thankyou {}",
                   "for your generous donation of {:.2f}",))


def send_thankyou():
    '''task 1 of the mail room- send thankyou for donations'''
    dname=input(mty_prompt)
    if dname == 'list':
        create_report()
    else:
        i=0
        for donars in donar_db:
            if dname not in donars:
                i +=1
            else:
                break
        damt=input("Enter your donation amount in dollars --> ")
        if i == len(donar_db):
            donar_db.append((dname,[float(amt)]))
        else:
            donar_db[i][1].append(float(damt))

        input(mty_msg.format(dname,float(damt)))

        
def create_report():
    '''task 2 of the mailroom - create report'''       
    top='{:20}| {:>20}|{:>20}| {:>20}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift')
    print(top)
    print('-'*100)

    for donor in donar_db:
        line='{:20} ${:>20.2f}   {:20}   ${:20.2f}'.format(donor[0],sum(donor[1]),len(donor[1]),(sum(donor[1])/len(donor[1])))
        print(line)
    print('')


def quit_pgm():
    ''' exit the program cleanly'''
    print("Bye!")
    sys.exit()



def main():
    '''Main block of the code'''      
    while True:
        response = input(prompt_msg)
        if response == "1":
            send_thankyou()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_pgm()
        else:
            print("Please enter valid option!")

if __name__ == "__main__":
    main()
            
            
