#!/usr/bin/env python3

# Starting list of donors and their donation amounts
donor_history = [
    ["Lana Kane", [2999.99]],
    ["Cheryl Tunt", [150.20, 98192.10]],
    ["Cyril Figgis", [819.25, 998.62, 10.50]],
    ["Pam Poovey", [74926.10, 2675.87, 3289.33]],
    ["Ray Gillette", [3820.90]]
]

def main_menu():
    """ Prompt a user to selection an action to take, 
    and call the appropriate function """
    
    # Prompt the user and set the selection
    while True:
        selection = input("""
Please enter a number to select the action:
1 - Send a Thank You
2 - Create a Report
3 - quit
> """)

        # Evaluate the selection
        if int(selection) == 1:
            print("Let's send a thank you!")
            send_a_thank_you()
        elif int(selection) == 2:
            print("Let's create a report!")
            create_a_report()
        elif int(selection) == 3:
            print("Quitting...")
            break
        else:
            print("Please select a valid number...")

def prompt_donor_name():
    """ Prompt for a donor name, list if needed, add if not found """

    while True:
        # Prompt the user for the full name
        full_name = input("Please enter the full name of a donor (type 'list' for current donor names) > ")

        # If the name is 'list' print the full list of names
        if full_name.lower() == "list":
            for donors in donor_history:
                print(donors[0])
        elif full_name == "":
            return "NODATA"
        else:
            # Check for existing name in the list
            found_match = False
            for donors in donor_history:
                if full_name in donors:
                    print("Found existing donor...")
                    found_match = True
                    return full_name
            # If not match found, add new
            if found_match == False:
                print("Adding new donor to list...")
                donor_history.append([full_name, []])
                return full_name

def prompt_donation_amount(full_name):
    """ Prompt for a donation amount and add it for the donor """
    
    while True:
        # Prompt for the amount
        donation_amount = input("Please enter the donation amount > ")

        # Evalute the value entered
        if donation_amount == "":
            return "NODATA"
        elif donation_amount == 0:
            print("Please enter a non-zero value")
        else:
            # Convert amount to float
            float_amount = float(donation_amount)

            # Add the donation to the donor's list of donations
            for donors in donor_history:
                if donors[0] == full_name:
                    print("Adding new donation of {} from {}".format(donation_amount, full_name))
                    donors[1].append(float_amount)
            
            # Return the donation amount
            return float_amount

def send_a_thank_you():
    """ Generate a thank you letter for a given donor and amount """

    # Prompt for donor's full name
    full_name = prompt_donor_name()

    # Return to main menu
    if full_name == "NODATA":
        print("No data.  Returning to main menu...")
        return

    # Prompt for the donation amount
    donation_amount = prompt_donation_amount(full_name)

    # Return to main menu
    if donation_amount == "NODATA":
        print("No data.  Returning to main menu...")
        return

    # Print out a letter customized for the donor and amount
    print(f"""
Dear {full_name},

Thank you for your generous donation of ${donation_amount:.2f}!

Sincerely,

The Owners""")

def create_a_report():
    """ Print a summary report of donors and their donations """
    
    # Print the header row
    header_row = "{0:<20} | {1} | {2} | {3}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header_row)
    print("-" * len(header_row))
    
    # Loop through the donor history and summarize the values
    for donors in donor_history:
        if sum(donors[1]) > 0:
            print(f"{donors[0]:<20} ${sum(donors[1]):>13,.2f} {len(donors[1]):>11} {sum(donors[1])/len(donors[1]):>13,.2f}")
        # Handle zero in case they entered a new donor but no donations
        else:
            print(f"{donors[0]:<20} ${0:>13,.2f} {0:>11} {0:>13,.2f}")

if __name__ == '__main__':
    main_menu()