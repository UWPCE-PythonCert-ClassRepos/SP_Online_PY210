#!/usr/bin/env python3

import sys
from operator import itemgetter

donations_per_individual = [
    ("William Gates, III", [50000.0, 500.12]), 
    ("Mark Zuckerberg", [20000.0, 8500.99]), 
    ("Jeff Bezo", [100000.0, 40000.0, 700.99]), 
    ("Paul Allen", [200000.0, 1440.0, 300.00]), 
    ("Bill Gates", [30000.0, 70000.0, 450.0]),
]

def display_menu():
    """
    Display menu option to user

    """
    print("Welcome to mail automator!")
    print()
    print("[1] Send a Thank You!")
    print("[2] Create a report!")
    print("[3] Quit!")
    print()

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
    index = 0 
    while index < len(donations_per_individual): 
        donor_list.append(donations_per_individual[index][0])
        index = index + 1
    
    # add unknown donor to the main donation DB list
    if donor not in donor_list:
        donations_per_individual.append((donor, []))
    
    return donor

def prompt_for_donation_amount():
    """
    function asks user for donor, donar amount, 
    and proceeds to send a thank you to the donor
    """

    donor_name = add_donar_to_list()
    response = input(f"How much would {donor_name} like to donate? ")
    donation_amount = float(response) 

    #add donation to donor history
    for individual in donations_per_individual: 
        if donor_name in individual: 
            individual[1].append(donation_amount)

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
        donor_name = donor[0]
        total_given = sum(donor[1])
        num_gifts = len(donor[1])
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

    print("Bye!")
    sys.exit()

def main(): 
    """
    main program entry prompt. prompts the user for an option in the menu

    """
    display_menu()

    response = input("Choose one of the above options, [1..3]: ")
    response = int(response)

    while response not in (1, 2, 3): 
        print("Invalid Option!")
        response = input("Choose one of the following options, [1..3]: ")
        response = int(response)
        
    if response == 1: 
        prompt_for_donation_amount()
    if response == 2: 
        create_report()
    if response == 3: 
        quit_program()
    
if __name__ == '__main__':
    main()
