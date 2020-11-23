##!/usr/bin/env python3

#+----------------------------------------------+
#| Mailroom Part 5 (Object Oriented) - Lesson 9 |
#+----------------------------------------------+


import sys, os.path
# import donor_models # data and model object go into that module - use explicit donor_models. namespace
from donor_models import * # use implicit module namespace


# current directory for file operations
cur_dir = os.getcwd()


prompt = "\n".join(("> Welcome to the donation Manager!",
          "Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Print Report",                    
          "3 - Send letters to all Donors",
          "4 - Exit",
          ">>> "))

# ======== Main functions ===============

def getmydir():
    return cur_dir

def safe_input(prompt = ''):
    try:
        result = input(prompt+"\n")
    except (KeyboardInterrupt, EOFError):
        result = None
    return result


# cli 
def get_name(donors):

    np = "> Enter new Donor's Full Name, type 'list' to see all Donors:\n>>> "
    name = safe_input(np) # input errors
    while name.lower() == "list":
        # create_report()
        # print_list()
        print(donors.list)
        name=safe_input(np) # input errors
    return(name.title())


# cli
def get_amount(): # add error handling on not numbers, and input errors
 
    np = "> Enter a Donation amount:\n>>> "
    try:
        amt = float(safe_input(np))     # input errors
    except (ValueError):
        print("Not valid amount")
        amt = 0 
        
    while amt <= 0 :
        try:
            amt = float(safe_input(np)) # input errors
        except (ValueError):
            print("Not valid amount")
            amt = 0 
        
    return(amt)


# === Functions for the Main Menu

def send_thankyou(donors):
    new_name = get_name(donors)
    new_amount = get_amount()
    resstr = donors.add_donation(new_name, new_amount)
    print(resstr)

def create_report(donors):        
    print(donors.report)
        

def send_letters(donors):
    print(donors.send_letters())

# cli
def exit_program(donors):
    print("Good Bye...")
    sys.exit(0)

# cli
main_args = {
            1: send_thankyou, # done
            2: create_report, # done
            3: send_letters,
            4: exit_program} # done



def main_program(): # main loop
    # comment out before submission
    os.chdir(cur_dir) # change to my working directory
    
    # Create Donors and populate
    donors = DonorCollection()
    donors.add(Donor("Albert Einstein", [1535.2, 15]))
    donors.add(Donor("Richard Feinman", [150, 17]))
    donors.add(Donor("Lev Landau", [53, 121, 35, 79]))
    donors.add(Donor("Niels Bohr", [135.2, 15]))
    donors.add(Donor("Ilya Prigogine", [15.2, 10]))
    
    # print(donors) # sanity check
  
    while True:
        try:            # Error handling on range and input errors
            response = int(safe_input(prompt))  # continuously collect user selection
        except(ValueError):
            print("Input error!")            
            response = 0
       
        if response in main_args:
            main_args.get(response)(donors) # execute option from main_args passing the donors collection object as a parameter
        else:
            print("Not a valid option!")          
 
if __name__ == "__main__":
    main_program()
