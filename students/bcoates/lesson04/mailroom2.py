#!/usr/bin/env python3

# Starting list of donors and their donation amounts
donor_history = {
    "donor_1": {"name": "Lana Kane", "donations": [2999.99]},
    "donor_2": {"name": "Cheryl Tunt", "donations": [150.20, 98192.10]},
    "donor_3": {"name": "Cyril Figgis", "donations": [819.25, 998.62, 10.50]},
    "donor_4": {"name": "Pam Poovey", "donations": [74926.10, 2675.87, 3289.33]},
    "donor_5": {"name": "Ray Gillette", "donations": [3820.90]}
}

def main_menu(prompt, prompt_actions):
    """ Prompt a user to selection an action to take, 
    and call the appropriate function """

    # Build a prompt message based on prompt and actions
    prompt_message = prompt
    for item in prompt_actions:
        prompt_message += "\n" + item[0] + " - " + prompt_actions[item]['message']
    prompt_message += "\n> "
    
    # Prompt the user and set the selection
    while True:
        selection = input(prompt_message)
        if selection not in prompt_actions:
            print("Please select a valid number...")
        elif prompt_actions[selection]['action']() == 'quit':
            print("Quitting...")
            break

def prompt_and_add_donor():
    """ Prompt for a donor name, list if needed, add if not found """

    while True:
        # Prompt the user for the full name
        full_name = input("Please enter the full name of a donor (type 'list' for current donor names) > ")

        # If the name is 'list' print the full list of names
        if full_name.lower() == "list":
            for donor in donor_history:
                print(donor_history[donor]['name'])
        elif full_name == "":
            return "NODATA"
        else:
            # Check for existing name in the list
            for donor in donor_history:
                if full_name == donor_history[donor]['name']:
                    print("Found existing donor...")
                    return donor
            else:
                print("Adding new donor to list...")
                new_donor_key = "donor_" + str(len(donor_history)+ 1)
                new_donor = {"name": full_name, "donations": []}
                donor_history[new_donor_key] = new_donor
                return new_donor_key

def prompt_and_add_donation_amount(donor):
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
            print("Adding new donation of {} from {}".format(donation_amount, donor_history[donor]['name']))
            donor_history[donor]['donations'].append(float_amount)
            
            # Return the donation amount
            return float_amount

def send_a_thank_you():
    """ Generate a thank you letter for a given donor and amount """

    # Prompt for donor's full name
    donor = prompt_and_add_donor()

    # Return to main menu
    if donor == "NODATA":
        print("No data.  Returning to main menu...")
        return

    # Prompt for the donation amount
    donation_amount = prompt_and_add_donation_amount(donor)

    # Return to main menu
    if donation_amount == "NODATA":
        print("No data.  Returning to main menu...")
        return

    # Print out a letter customized for the donor and amount
    print(format_thank_you_letter(donor_history[donor]['name'], donation_amount))

def format_thank_you_letter(full_name, donation):
    """ Return a formatted thank you letter """
    letter = f"""
Dear {full_name},

Thank you for your generous donation of ${donation:.2f}!

Sincerely,

The Owners"""
    return(letter)

def create_a_report():
    """ Print a summary report of donors and their donations """
    
    # Print the header row
    header_row = "{0:<20} | {1} | {2} | {3}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift")
    print(header_row)
    print("-" * len(header_row))
    
    # Loop through the donor history and summarize the values into a new list
    donor_summary = []
    for donor in donor_history:
        if sum(donor_history[donor]['donations']) > 0:
            donor_summary.append([donor_history[donor]['name'], 
                sum(donor_history[donor]['donations']), 
                len(donor_history[donor]['donations']), 
                sum(donor_history[donor]['donations'])/len(donor_history[donor]['donations'])])
        # Handle zero in case they entered a new donor but no donations
        else:
            donor_summary.append([donor_history[donor]['name'], 0, 0, 0])

    # Sort the new list descending by total donations and print the output
    donor_summary.sort(key=lambda x: x[1], reverse=True)
    for donor in donor_summary:
        print(f"{donor[0]:<20} ${donor[1]:>13,.2f} {donor[2]:>11} {donor[3]:>13,.2f}")

def send_thank_you_to_all():
    """ Create letters for all donors for their latest donation and save to disk """
    
    # Defin the temp directory
    temp_dir = "/tmp/"

    # Loop through the donor history, create, and save letters
    for donor in donor_history:
        # Set some variables based on the donro information
        full_name = donor_history[donor]['name']
        last_donation = donor_history[donor]['donations'][-1]
        letter = format_thank_you_letter(full_name, last_donation)
        file_name = temp_dir + full_name + ".txt"
        
        # Open a file named for the full_name and write the letter
        print("Saved letter for {} to {}".format(full_name, file_name))
        with open(file_name, "w") as f:
            f.write(letter)
        


# Define dictionary of menu prompt messages and actions
main_menu_prompt_actions = {
    "1": {"message": "Send a Thank You", "action": send_a_thank_you},
    "2": {"message": "Create a Report", "action": create_a_report},
    "3": {"message": "Send Thank You to All Donors", "action": send_thank_you_to_all},
    "4": {"message": "Quit", "action": quit}
}

# Define the main menu prompt
main_menu_prompt = """Please enter a number to select the action:"""

# Run the main program
if __name__ == '__main__':
    main_menu(main_menu_prompt, main_menu_prompt_actions)