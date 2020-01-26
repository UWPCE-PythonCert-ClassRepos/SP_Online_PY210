# -*- coding: utf-8 -*-
"""
Mailroom Part 1
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

def generate_letter(name=None):
    template = "Dear {name},\n\n" + \
               "Thank you for your most recent donation of " + \
               "${last_donation}. We greatly appreciate it.\n\n" + \
               " ~ The Treasurer"
    donor_info = {'name':name, 'last_donation':db[name][-1]}
    letter = template.format(**donor_info)
    return letter    

def thanks():
    """ Generates a Thank You message for a new donation, and adds donation
        to database """

    thank_you = ""
    vld_name = False
    while vld_name is False:
        name = input("Please enter a Full Name or 'List': ")
        if name.lower() == 'list':
            for name in db.keys():
                print(name)
        elif name.lower() == 'quit':
            break
        else:
            vld_name = True
            for entry in db:    # Check for name in db
                if name.lower == name.lower:
                    break
            else:   # If name not found in db, add it
                db[name] = []
    else:
        print(name)
        donation = input("Please enter a donation amount: ")
        if donation.lower() != 'quit':  #Check if user is attempting to quit
            db[name].append(float(donation))
            thank_you = generate_letter(name)
        print("\n" + thank_you + "\n")
    return db, thank_you

def report():
    """Generates report of donors and donation statistics, sorted by total
       given."""

    print("Donor Name            | Total Given | Num Gifts | Average Gift")
    print("--------------------------------------------------------------")
    for key, value in sorted(db.items(), key=sortby_amt, reverse=True):
        print("{:<21}  ${:11.2f}   {:9d}  ${:12.2f}".format(key,
              sum(value), len(value), (sum(value)/len(value))))
    print('\n\n')

def log_all_letters():
    for name in db:
        print(name)
        file_name = name + '.txt'
        print(file_name)
        with open(file_name, 'w') as outfile:
            outfile.write(generate_letter(name))
            

def quitter():
    print('Goodbye!')

    
    
# Init the donor database
db = {"William Gates, III": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Mark Zuckerberg": [1663.23, 4300.87, 10432.0],
            "John Doe": [1.00, 2.00, 3.00, 4.00]
           }
menu_quit = False

if __name__ == '__main__':
#    while True:
#        print('Select an Operation:')
#        print("  1) Send Thank You")
#        print("  2) Create a Report")
#        print("  3) Quit\n")
#        cmd = input('> ')
#        if cmd == '3' or cmd.lower() == 'quit':
#            print('Goodbye!')
#            break
#        elif cmd == '1' or cmd.lower() == 'send thank you':
#            donor_db, note = thanks(donor_db)
#            print(note)
#            print('\n')
#        elif cmd == '2' or cmd.lower() == 'create a report':
#            report(donor_db)
#        else:
#            continue
             
    menu = {"1":thanks, "2": report, "3":log_all_letters, "4": quitter}
    cmd = None
    while cmd != '4':
        print('Select an Operation:')
        print("  1) Send Thank You")
        print("  2) Create a Report")
        print("  3) Generate Thank You Letter for All")
        print("  4) Quit\n")
        cmd = input('> ')
        menu[cmd]()