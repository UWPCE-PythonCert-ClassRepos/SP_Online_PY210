#!/usr/bin/env python3

from donor_models import * 

def mailroom04(reply, action):
    while True:
        try:
            resp = input(reply)
            if action[resp]() is None or False:
                pass
            elif action[resp]() == "exit menu":
                break
        except KeyError:
            keyerror()
        except KeyboardInterrupt:
            keyboardinterrupt()

def add_donor():
    print()
    full_name = str(input("Please enter 'list' to view donor names or 'q' to quit or full name of the donor: "))
    dn = Donor(full_name)
    dn.new_donation()

def n_don():
    print()
    don = int(input("Please enter the donation amount: "))
    return don

def new_donor():
    print()
    new_don = int(input("No matches found, if this is a new donor please enter the donation amount or 'q' to exit: "))
    if new_don == "q":
        return
    else:
        return new_don

def send_ty_note():
    try:
        print()
        don_name = input("Enter donor's name: ")
        dn = Donor(don_name)
        dn.ty_note()              
    except KeyboardInterrupt:
        keyboardinterrupt()

def create_report():
    DonorCollection.report()

def print_list():
    DonorCollection.list()

def quit():
    return "exit menu"

def valueerror():
    print()
    print("The donation amount has been incorrect or not entered.")
    print()

def keyerror():
    print()
    print("Wrong entery, please try again!")
    
def keyboardinterrupt():
    print()
    print("Keyboard interrupt doesn't work here ;)")
    print("please use apropriate method to exit this program")
    print(">>>> Hint: 'q'")

main_reply = ("\nChoose an action: \n"
               "\n"
			   "1 - Send a Thank You note to a single donor.\n"
			   "2 - Add new donation.\n"
			   "3 - Create a Report.\n"
			   "4 - To see the LIST of donor names.\n"
			   "q - Quit\n"			   
			   ">>>")

main_action = {"1" : send_ty_note,
               "2" : add_donor,
               "3" : create_report,
               "4" : print_list,
               "q" : quit
               }

if __name__ == "__main__":
    mailroom04(main_reply, main_action)


