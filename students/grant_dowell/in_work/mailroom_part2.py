# -*- coding: utf-8 -*-
"""
Mailroom Part 2
Grant Dowell
"""

# Data structure requirements:
#  - Name, history of donation amounts

# Program Utilites
#  1) Send Thank You
#     - Prompt for full name
#     - if
#  2) Create a Report
#  3) Quit

def sortby_amt(entry):
    return sum(entry[1])

def thanks(db):
    thank_you = ""
    vld_name = False
    while vld_name is False:
        name = input("Please enter a Full Name or 'List': ")
        if name.lower() == 'list':
            for item in db:
                print(item[0])
        elif name.lower() == 'quit':
            break
        else:
            vld_name = True
            for entry in db:    # Check for name in db
                if entry[0].title() == name.title():
                    break
            else:   # If name not found in db, add it
                entry = (name.title(),[])
                db.append(entry)
    else:
        donation = input("Please enter a donation amount: ")
        if donation.lower() != 'quit':  #Check if user is attempting to quit
            entry[1].append(float(donation))
            thank_you = f"Dear {name.title()},\n\nThank you for your donation of ${donation:.2f}!"
            
    return db, thank_you 

def report(db):    
    print("Donor Name            | Total Given | Num Gifts | Average Gift")
    print("--------------------------------------------------------------")
    for entry in sorted(db, key=sortby_amt, reverse=True):
        print("{:<21}  ${:11.2f}   {:9d}  ${:12.2f}".format(entry[0], sum(entry[1]), len(entry[1]), (sum(entry[1])/len(entry[1]))))
    print('\n\n')

def quitter():
    backout = True
    return backout
    
# Init the donor database
donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ("John Doe", [1.00, 2.00, 3.00, 4.00])
           ]

if __name__ == '__main__':
    
    menu = {1:thanks(donor_db), 2:report(donor_db), 3:quitter()}
    backout = False
    
    while backout == False:
        cmd = input("Select an Option (#):\n"
                    "1) Send a Thank You\n"
                    "2) Create a Report\n"
                    "3) Quit\n"
                    "> ")
    
        menu.get(cmd)
        
    
    while True:
        print('Select an Operation:')
        print("  1) Send Thank You")
        print("  2) Create a Report")
        print("  3) Quit\n")
        
        cmd = input('> ')
        if cmd == '3' or cmd.lower() == 'quit':
            print('Goodbye!')
            break
        elif cmd == '1' or cmd.lower() == 'send thank you':
            donor_db, note = thanks(donor_db)
            print(note)
            print('\n')
        elif cmd == '2' or cmd.lower() == 'create a report':
            report(donor_db)
        else:
            continue
             