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
    print("\nSend a thank you!\n")
    response = input("""Please type the name of the donor you'd like to thank.\n
Use 'list' to view current donors, or 'quit' to return to the menu: """)
    while response.lower() == "list":
        for name in donors.keys():
            print("\n",name)
        response = input("\nPlease enter a donor name: ")
    if response.lower() == "quit":
        pass
    else:
        amount = float(input("\nEnter a donation amount: "))
        
    for donor in donors.keys():
        if response.lower() == donor.lower():
            donors[donor].append(amount)
        else:        
            donors[response] = [amount]
        send_email(donor, amount)

def send_email(donor, amount):
    # Print donor name and amount into thank you email
    print(thanks_letter(donor, amount))
    exit()

def sum_donations(donations):
    # Sorts by total amount given
    return sum(donations[1])

def generate_report():
      # Print formatted header
    print('\n{:<20} {:>15} {:>15} {:>15}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift'))
    print('-'*70)
    # Sort the donor list
    sorted_donors = dict(sorted(donors.items(),
                              key=sum_donations,
                              reverse=True))
    # Calculate sum of donations, number of donations, and average donation, then print them nicely
    for donor, amounts in sorted_donors.items():
        name = donor
        total = sum(amounts)
        num = len(amounts)
        average = total/num
        print('{:<20} {:>5}{:>9.2f}{:>13} {:>9}{:>8.2f}'.format(name, '$', total, num, '$', average))
    main()

def send_all_thanks():
    print("Sending a thank you note to all donors!")
    for donor, amount in donors.items():
        total = sum(amount)
        filename = ('./' + donor + '.txt')
        with open(filename, 'w') as f:
         f.write(thanks_letter(donor, total)) 


def quit_program():
    exit()

def main():
    menu = {1: thank_you, 2: generate_report, 3: send_all_thanks, 4: quit_program}
    while True:
        # Prompt user for option, run related function
        print(main_prompt)

        response = int(input("Please enter a number: "))
        if response in menu:
            menu[response]()
        else:
            response = int(input(f"{response} is not a valid input: "))


if __name__ == "__main__":
    print("Welcome to the donors list!")
    main()