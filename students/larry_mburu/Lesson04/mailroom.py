#!/usr/bin/env python3

import sys
import tempfile
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

def letter_validator(file_tmp_dir):
    """
    Function just prints the content of a single letter in file, for 
    validation only, since the send_thank_you_letter_to_all() utilizes 
    tempfile.TempDirectory(), which does not persist files in the file system

    param: file_tmp_dir: temporary directory full path name. 

    return: None

    """

    for file in os.listdir(file_tmp_dir): 
        print(f"[+] Listing contents of file: {file}")
        with open(os.path.join(file_tmp_dir, file)) as fobj:
            for line in fobj:
                if line != '':
                    print(line)
        break # just one file. Avoids reading all files.

def send_thank_you_letter_to_all(validate=False): 
    """
    Function, sends a thank you letter to all donor's in the donor DB list

    param: validation: If set to True, prints the contents of single donor file, 
    since tempfile.TempDirectory() does not persist files, in the file system. 
    It's purely to validate that the letter / formatting was written to file
    correctly.

    return: None 
    """

    with tempfile.TemporaryDirectory() as file_tmp_dir: 
        for donor in donations_per_individual:  

            # -1, the latest donation in the donor "list"
            email_template = f"""
            Dear {donor}, 
                Thank you for your kind donation of ${donations_per_individual[donor][-1]} 

                it will be put to very good use. 

                Sincerely,
                    - The Cloud Squad 
            """
            with open(file_tmp_dir + os.sep + donor + '.txt', 'w') as fobj: 
                fobj.write(email_template)

        if validate == True: 
            letter_validator(file_tmp_dir)

def send_thank_you_email(name, amount): 
    """
    composes an email to a selected donor on 
    the donor's list 
    """
    print(f"Thank you {name} for your generous donation of $ {amount:.2f} dollars")
    print()

    #return to the original prompt 
    main()

def prompt_for_donor_name(): 
    """
    Function, asks user for a donar name. The user can opt to
    list all the donors in the donor DB list. 
    """

    donor_name = input("Enter donor's full name or 'list' to list donors: ") 
    quit = True
    while quit and donor_name == 'list':
        for donar in donations_per_individual: 
            print(donar[0]) 
        donor_name = input("Enter donar full name or 'list' to list donars: ")
        quit = False
    return donor_name

def add_donar_to_list():
    """
    After user is prompted for donor name, function checks if 
    it's a known or unknown donor. If unknown, a new record is 
    added to the main donation DB list

    return: if donor is in the DB list or not, function returns the donor name 
    for further use
    """

    donor = prompt_for_donor_name()
    donor_list = []

    #extract donor names from main donation DB list for in checks. 
    for key in donations_per_individual: 
        donor_list.append(key)
    
    # add unknown donor to the main donation DB list
    if donor not in donor_list:
        donations_per_individual[donor] = []
    
    return donor

def prompt_for_donation_amount():
    """
    function asks user for donor, donar amount, 
    and proceeds to send a thank you to the donor
    """

    donor_name = add_donar_to_list()
    response = input(f"How much would {donor_name} like to donate? ")
    donation_amount = float(response) 

    #add donation to donor history, in donation DB list
    if donor_name in donations_per_individual: 
        donations_per_individual[donor_name].append(donation_amount)

    #send a thank you email
    send_thank_you_email(donor_name, donation_amount)

def create_report():
    """
    function creates a report based on donor database list. 
    it calculates the total, average and number of gifts a 
    donar has contributed
    """
    
    #boarder column headers and divider. 
    donor_name_header = "Donor Name"
    total_give_header = "Total Given" 
    num_gifts_header  = "Num Gifts"
    average_gift_header = "Average Gift"
    padding=20
    boarder = '-'

    print(f"{donor_name_header:<{padding}} |  {total_give_header} | {num_gifts_header} | {average_gift_header}")
    print(boarder * 62)

    # collection for donor statistical summaries for easy sorting
    summary_of_donations = []

    for donor in donations_per_individual:
        donor_name = donor
        total_given = sum(donations_per_individual[donor])
        num_gifts = len(donations_per_individual[donor])
        average_gift = total_given / num_gifts

        summary_of_donations.append((donor_name, total_given, num_gifts, average_gift))

    # sort summary_of_donations by average, which is indexed at 3 i.e 
    # [("bill", 10, 2, 20.5)], save results in descending order.
    summary_of_donations_sorted = sorted(summary_of_donations, key=itemgetter(3), reverse=True)

    for summary in summary_of_donations_sorted: 
        name = summary[0]
        total = summary[1]
        num_gifts = summary[2]
        average = summary[3]
        
        print(f"{name:{padding}} $ {total:10.2f} {num_gifts:14} $ {average:10.2f}")

    print()
    # return to original prompt
    main()
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

    response = input("Choose one of the above options, [1..4]: ")
    response = int(response)

    # valid option numbers, per dipatch_dict
    while response not in (1, 2, 3, 4): 
        print("Invalid Option!")
        response = input("Choose one of the following options, [1..4]: ")
        response = int(response)

    # dispatch dictionary. Key to function mapping. 
    
    dispatch_dict = { 
        1 : prompt_for_donation_amount, 
        2 : create_report, 
        3 : send_thank_you_letter_to_all,
        4 : quit_program
    }

    if response == 1: 
        dispatch_dict.get(response)()
    if response == 2: 
        dispatch_dict.get(response)()
    if response == 3: 
        dispatch_dict.get(response)(validate=True)
    if response == 4: 
        dispatch_dict.get(response)()
    
if __name__ == '__main__':
    main()
