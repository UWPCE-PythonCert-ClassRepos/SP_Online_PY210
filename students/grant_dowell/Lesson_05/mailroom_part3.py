# -*- coding: utf-8 -*-
"""
Mailroom Part 3
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

import sys

def sortby_amt(entry):
    return sum(entry[1])

def generate_letter(name=None):
    """ Builds a letter using the global database"""

    template = "Dear {name},\n\n" + \
               "Thank you for your most recent donation of " + \
               "${last_donation}. We greatly appreciate it.\n\n" + \
               " ~ The Treasurer"
    donor_info = {'name':name.title(), 'last_donation':db[name][-1]}
    letter = template.format(**donor_info)
    return letter

def thanks():
    """ Generates a Thank You message for a new donation, and adds donation
        to database """

    thank_you = ""
    vld_name = False
    while vld_name is False:
        name = input("Please enter a Full Name or 'List': ").lower()
        if name == 'list':
            for name in db.keys():
                print(name.title())
        elif name == 'quit':
            break
        else:
            vld_name = True
            if db.get(name):
                continue
            else:   # If name not found in db, add it
                db[name] = []
    else:
        vld_donation = False
        while vld_donation is False:
            donation = input("Please enter a donation amount: ")
            if donation.lower() != 'quit':  #Check if user is attempting to quit
                try:
                    db[name].append(float(donation))
                except ValueError:
                    print("Please enter a number or 'quit'")
                else:
                    vld_donation = True
        thank_you = generate_letter(name)
        print("\n" + thank_you + "\n")

def report():
    """Generates report of donors and donation statistics, sorted by total
       given."""

    print("Donor Name            | Total Given | Num Gifts | Average Gift")
    print("--------------------------------------------------------------")
    for key, value in sorted(db.items(), key=sortby_amt, reverse=True):
        print("{:<21}  ${:11.2f}   {:9d}  ${:12.2f}".format(key.title(),
              sum(value), len(value), (sum(value)/len(value))))
    print('\n\n')

def log_all_letters():
    """ Generates a letter for every person in the global database and saves
        it as a separate file."""
    for name in db:
        file_name = name + '.txt'
        with open(file_name, 'w') as outfile:
            outfile.write(generate_letter(name))

def quitter():
    print('Goodbye!')
    sys.exit()



# Init the donor database
db = {"william gates, iii": [653772.32, 12.17],
      "jeff bezos": [877.33],
      "paul allen": [663.23, 43.87, 1.32],
      "mark zuckerberg": [1663.23, 4300.87, 10432.0],
      "john doe": [1.00, 2.00, 3.00, 4.00]}

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
    while True:
        print('Select an Operation:')
        print("  1) Send Thank You")
        print("  2) Create a Report")
        print("  3) Generate Thank You Letter for All")
        print("  4) Quit\n")
        cmd = input('> ')
        try:
            menu[cmd]()
        except KeyError:
            print("\nInput MUST be a number\n")
#            
