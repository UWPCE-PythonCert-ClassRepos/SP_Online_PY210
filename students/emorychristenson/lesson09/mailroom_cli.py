#!/usr/bin/env python3

from mailroom import *

def main():
    """ Main menu with user prompts """
    menu = {1: thank_you, 2: display_report, 3: send_all_thanks, 4: quit_program}
    while True:
        # Prompt user for option, run related function
        print(main_prompt)
        try:
            selection = int(input("Please enter a number: "))
            menu[selection]()
        except KeyError:
            selection = int(input(f"{selection} is not a valid input: "))

def quit_program():
    """ Exit the program """
    exit()

def thanks_letter(donor, amount):
    """ Creates thank you letter """
    letter = (f"""\n
    Dear {donor},

    Thank you for your donation(s) of {amount:.2f}!
    We really appreciate your support!
    
    Sincerely,
        The Black Mesa Research Foundation""")
    return letter

# Allows user to select existing donor, add a new donor, or list all donors from the collection
def thank_you():
    """ Prompts user for donor name and amount """ 
    print("\nSend a thank you!\n")
    response = input("""Please type the name of the donor you'd like to thank.\n
Use 'list' to view current donors, or 'quit' to return to the menu: """)
    while response.lower() == "list":
        print("\n")
        for donor in donors.list_donors():
            print(donor)
        response = input("\nPlease enter a donor name: ")
    if response.lower() == "quit":
        print("\nReturning to main menu!")
    else:   
        try:
                amount = float(input("\nEnter a donation amount: "))
        except ValueError:
                amount = float(input("\nEnter a number amount: "))
        except ZeroDivisionError:
                amount = float(input("\nDonation must be more than 0: "))
        
    # if response in donors.list_donors():
    #     response.add_donation(amount)
    # else:    
    new_donor = Donor(response, [amount])
    donors.add_donor(new_donor)
    send_email(response, amount)

def send_email(donor, amount):
    """ Sends a donor name and amount to be formatted to thank you letter """ 
    # Print donor name and amount into thank you email
    print(thanks_letter(donor, amount))

def display_report():
    """ Print the report to the screen """
    # Print formatted header
    print('\n{:<20} {:>15} {:>15} {:>15}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift'))
    print('-'*70)
    for line in donors.generate_report():
        print('{:<20} {:>5}{:>9.2f}{:>13} {:>9}{:>8.2f}'.format(line[0], '$', line[1], line[2], '$', line[3]))

def send_all_thanks():
    """ Saves a thank you letter to all donors on the local disk """ 
    for donor in donors.get_donors():
        filename = ('./' + donor.name + '.txt')
        try:
            with open(filename, 'w') as f:
                f.write(thanks_letter(donor.name, donor.sum_donations()))
        except IOError:
            print("Unable to save letter to {} in {}".format(donor, filename))


if __name__ == "__main__":

    print("Welcome to the donors list!\n")
    
    # Populate donor collection
    seed_donors = (
        Donor("John Jacob", [5.00, 1000.00, 4.25]),
        Donor("Jingleheimer Schmidt", [240.50]),
        Donor("Chanandler Bong", [15000.00, 4000.00]),
        Donor("Jimni Christmas", [12.00]),
        Donor("S. Claus", [7000.00, 14000.00, 200.00]))

    donors = DonorCollection()
    for donor in seed_donors:
        donors.add_donor(donor)

    # Message that displays when script is run
    main_prompt = """
    Please choose from the below options.\n
    1 - Send a thank you
    2 - Create a report
    3 - Send thanks to all donors
    4 - Quit\n  
    """
    main()