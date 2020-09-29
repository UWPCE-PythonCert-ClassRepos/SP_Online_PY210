    #!/usr/bin/env python3

import sys
import os
from operator import itemgetter

donations_per_individual = { 
    'William Gates III' : [50000.0, 500.12], 
    'Mark Zuckerberg' : [20000.0, 8500.99], 
    'Jeff Bezo': [100000.0, 40000.0, 700.99], 
    'Paul Allen': [200000.0, 1440.0, 300.00], 
    'Bill Gates': [30000.0, 70000.0, 450.0]
}

def display_menu():
    """
    Display menu option to user
    """
    print("Welcome to Mail Automator (MA)!")
    print()
    print("[1] Send a Thank You!")
    print("[2] Create a report!")
    print("[3] Send letters to all donors")
    print("[4] Quit!")
    print()

def send_thank_you_letters(): 
    """
    Function, sends a thank you letter to all donor's in the donor DB list,
    by writing thank you letters to the local filesystem.
    """
    print('[+] Generating thank you letters..')

    for donor_name in donations_per_individual:  
        #split and join,to prevent file names with spaces.
        with open('_'.join(donor_name.split()) + '.txt', 'w') as fobj: 
            fobj.write(get_letter_text(donor_name))

    print('[+] Letter generation complete.')
    print('[+] Letters are in your current working directory')

def get_letter_text(donor_name):
    """
    returns formatted string, for content to be written
    in each file.
    """

    # -1, the latest donation in the donor "list"
    email_template = f"""Dear {donor_name},
    Thank you for your kind donation of ${donations_per_individual[donor_name][-1]}. 
        
    It will be put to very good use. 
        
    Sincerely,

    - The Cloud Squad"""
    
    return email_template

def send_thank_you_email(name, amount): 
    """
    composes an email to a selected donor on the donor's list 
    """
    thank_you_note = f"Thank you {name} for your generous donation of $ {amount:.2f} dollars"
    print(thank_you_note)
    return thank_you_note

def prompt_for_donor_name(): 
    """
    Function, asks user for a donar name. The user can opt to
    list all the donors in the donor DB list. 
    """
    donor_name = input("Enter donor's full name or 'list' to list donors: ")

    while donor_name == 'list': 
        print(get_donor_list(donor_name))
        donor_name = input("Enter donor's full name or 'list' to list donors: ")
    
    add_donar_to_list(donor_name)
    
def get_donor_list(donor_name): 
    """
    Gets a current listing of donors 
    Param: donor_name: if list, return a list of donors
    """
    if donor_name == 'list': 
        return list(donations_per_individual) #list of donors

def add_donar_to_list(donor_name):
    """
    After user is prompted for donor name, function checks if 
    it's a known or unknown donor. If unknown, a new record is 
    added to the main donation DB list

    return: if donor is in the DB list or not, function returns the donor name 
    for further use
    """

    donor = donor_name

    #check if donor is in DB.
    donor_in_db = donations_per_individual.get(donor)
    #If an unknown donor, "None", add donor to donation database
    if donor_in_db is None: 
        donations_per_individual[donor] = []
    
    prompt_for_donation_amount(donor)

def prompt_for_donation_amount(donor_name):
    """
    function asks user for donor, donar amount, 
    and proceeds to send a thank you to the donor
    """
    response = input(f"How much would {donor_name} like to donate? ")
    donation_amount = float(response) 

    add_to_donation_database(donor_name, amount=donation_amount) 

def add_to_donation_database(donor_name, amount=0.0): 
    #add donation to donor history, in donation DB list
    donations_per_individual.get(donor_name).append(amount)

    #send a thank you email
    send_thank_you_email(donor_name, amount)

def get_report():
    """
    function creates a report based on donor database list. 
    it calculates the total, average and number of gifts a 
    donar has contributed
    """
    
    # collection for donor statistical summaries for easy sorting
    summary_of_donations = [ 
        ( 
            donor, 
            sum(donations_per_individual[donor]), 
            len(donations_per_individual[donor]), 
            sum(donations_per_individual[donor]) / len(donations_per_individual[donor])
        )
        for donor in list(donations_per_individual)
    ]

    # sort summary_of_donations by average, which is indexed at 3 i.e 
    # [("bill", 10, 2, 20.5)], save results in descending order.
    summary_of_donations_sorted = sorted(summary_of_donations, key=itemgetter(3), reverse=True)

    padding = 20

    summary = [ 
        f"{name:{padding}} $ {total:10.2f} {num_gifts:14} $ {average:10.2f}" 
        for name, total, num_gifts, average in summary_of_donations_sorted 
        ]

    return summary
 
def display_report(): 
    '''
    Display report to the user
    ''' 
     #boarder column headers and divider. 
    donor_name_header = "Donor Name"
    total_give_header = "Total Given" 
    num_gifts_header  = "Num Gifts"
    average_gift_header = "Average Gift"
    padding=20
    boarder = '-'

    print(f"{donor_name_header:<{padding}} |  {total_give_header} | {num_gifts_header} | {average_gift_header}")
    print(boarder * 62)

    for row in get_report(): 
        print(row)

def quit_program():
    """
    function quits the program, if the user selects
    quit as an option in the menu display
    """

    print("Mail Automator (MA), signing off, Bye!")
    sys.exit()

def main(): 
    """
    main program entry prompt. prompts the user for an option in the menu

    """
    display_menu()

    # dispatch dictionary. Key to function mapping. 
    
    dispatch_dict = { 
        1 : prompt_for_donor_name, 
        2 : display_report, 
        3 : send_thank_you_letters,
        4 : quit_program
    }

    while True:
        response = input("Choose a number from, [1..4]: ")
        try:
            response = int(response)
            dispatch_dict[response]()
        except ValueError:
            print("Input must be an integer, try again")
            continue
        except KeyError:
            print("Option outside the range of [1..4], try again!")
            continue
    
if __name__ == '__main__':
    main()
