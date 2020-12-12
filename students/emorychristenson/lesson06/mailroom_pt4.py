#!/usr/bin/env python3

# Collection of existing donor data
donors = {
    "John Jacob": [5.00, 1000.00, 4.25],
    "Jingleheimer Schmidt": [240.50],
    "Chanandler Bong": [15000.00, 4000.00],
    "Jimni Christmas": [12.00],
    "S. Claus": [7000.00, 14000.00, 200.00]
}

# Message that displays when script is run
main_prompt = """
Please choose from the below options.\n
1 - Send a thank you
2 - Create a report
3 - Send thanks to all donors
4 - Quit\n
"""
def thanks_letter(donor, amount):
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
        for name in donors.keys():
            print("\n",name)
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
        
    if donors.get(response):
        add_donation(response, amount)
        #donors[response].append(amount)
    else:    
        add_donor(response)    
        add_donation(response, amount)
        #donors[response] = [amount]
    send_email(response, amount)

def add_donor(donor):
    """ Adds a new donor to the dict """ 
    if not donors.get(donor):
        donors[donor] = []

def add_donation(donor, amount):
    """ Appends donation to donor's history """
    donors[donor].append(amount)
    return amount


def send_email(donor, amount):
    """ Sends a donor name and amount to be formatted to thank you letter """ 
    # Print donor name and amount into thank you email
    print(thanks_letter(donor, amount))

def sum_donations(donations):
    """ Sums the donations for a given donor """
    # Sorts by total amount given
    return sum(donations[1])

def generate_report():
    """ Generate report of donors and their donations """
    # Sort the donor list
    sorted_donors = dict(sorted(donors.items(),
                              key=sum_donations,
                              reverse=True))
    # Calculate sum of donations, number of donations, and average donation, then print them nicely
    report = []
    for donor, amounts in sorted_donors.items():
        name = donor
        total = sum(amounts)
        num = len(amounts)
        average = total/num
        report.append('{:<20} {:>5}{:>9.2f}{:>13} {:>9}{:>8.2f}'.format(name, '$', total, num, '$', average))
    return report

def display_report():
    """ Print the report to the screen """
    # Print formatted header
    print('\n{:<20} {:>15} {:>15} {:>15}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift'))
    print('-'*70)
    for line in generate_report():
        print(line)

def send_all_thanks():
    """ Saves a thank you letter to all donors on the local disk """ 
    for donor, amount in donors.items():
        total = sum(amount)
        filename = ('./' + donor + '.txt')
        try:
            with open(filename, 'w') as f:
                f.write(thanks_letter(donor, total))
        except IOError:
            print("Unable to save letter to {} in {}".format(donor, filename)) 

def quit_program():
    exit()

def main():
    menu = {1: thank_you, 2: display_report, 3: send_all_thanks, 4: quit_program}
    while True:
        # Prompt user for option, run related function
        print(main_prompt)
        try:
            selection = int(input("Please enter a number: "))
            menu[selection]()
        except KeyError:
            selection = int(input(f"{selection} is not a valid input: "))


if __name__ == "__main__":
    print("Welcome to the donors list!")
    main()