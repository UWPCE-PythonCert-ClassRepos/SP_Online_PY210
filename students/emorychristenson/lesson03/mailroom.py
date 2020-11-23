#!/usr/bin/env python3

# Collection of existing donor data
donors = [("John Jacob", [5.00, 1000.00, 4.25]),
              ("Jingleheimer Schmidt", [240.50]),
              ("Chanandler Bong", [15000.00, 4000.00]),
              ("Jimni Christmas", [12.00]),
              ("S. Claus", [7000.00, 14000.00, 200.00])]

# Message that displays when script is run
main_prompt = """
Please choose from the below options.\n
1 - Send a thank you
2 - Create a report
3 - Quit\n
Type a number to select: """

# Allows user to select existing donor, add a new donor, or list all donors from the collection
def thank_you():
    print("\nSend a thank you!\n")
    response = input("""Please type the name of the donor you'd like to thank.\n
Use 'list' to view current donors, or 'quit' to return to the menu: """)
    while response.lower() == "list":
        for name in donors:
            print("\n",name[0])
        response = input("\nPlease enter a donor name: ")
    if response.lower() == "quit":
        main()
    else:
        amount = float(input("\nEnter a donation amount: "))
        
    for donor in donors:
        if response.lower() == donor[0].lower():
            donor[1].append(float(amount))
        else:        
            donor = (response, [amount])
            donors.append(donor)
        send_email(donor, amount)

def send_email(donor, amount):
    # Print donor name and amount into thank you email
    print(f"""\n
    Dear {donor[0]},

    Thank you for your donation of {amount:.2f}!
    We really appreciate your support!
    
    Sincerely,
        The Black Mesa Research Foundation""")
    main()

def sum_donations(donations):
    # Sorts by total amount given
    return sum(donations[1])

def generate_report():
      # Print formatted header
    print('\n{:<20} {:>15} {:>15} {:>15}'.format('Donor Name', 'Total Given','Num Gifts', 'Average Gift'))
    print('-'*70)
    # Sort the donor list
    donors.sort(key = sum_donations, reverse = True)
    # Calculate sum of donations, number of donations, and average donation, then print them nicely
    for donor in donors:
        total = sum(donor[1])
        num = len(donor[1])
        average = total/num
        print('{:<20} {:>5}{:>9.2f}{:>13} {:>9}{:>8.2f}'.format(donor[0], '$', total, num, '$', average))
    main()

def main():
    # Prompt user for option, run related function
    response = input(main_prompt)
    while response not in ["1", "2", "3"]:
        response = input("Not a valid selection, please choose again: ")
    if response == "1":
        thank_you()
    elif response == "2":
        generate_report()
    elif response == "3":
        exit()


if __name__ == "__main__":
    print("Welcome to the donors list!")
    main()