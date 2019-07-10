# Author: Brian Minsk
donor_db = [("Dee Zaster", [10000.00, 1500.00]), 
            ("Owen Money", [7000.00]), 
            ("Shanda Lear", [100.00, 900.00, 1500.00]), 
            ("Joe King", [500.00, 700.00, 500.00]),
            ("Artie Choke", [1600.00, 1800.00])]

main_prompt = "\n".join(("Please choose an option:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Quit",
          ">>> "))
thank_you_prompt = "\n".join(("Please type a donor name or type 'list' to show all the donor names:",
          ">>> "))

donation_amount_prompt = "\n".join(("Please type the donation amount:",
          ">>> "))

def send_thank_you():
    """ Prompt the user to type a name or type 'list'. 
    - If the user types 'list' show a list of the donor names and re-prompt.
    - If the user types a name not in the list, add that name to the data structure and use it.
    - If the user types a name in the list, use it.
    Once a name has been selected, prompt for a donation amount.
    - Convert the amount into a number.
    - Add that amount to the donation history of the selected user.
    Compose an email thanking the donor for their generous donation. 
    Print the email to the terminal and return to the original prompt.
    """
    donation_amount = None

    while True:
        response = input(thank_you_prompt).lower()
        if response == "list":
            show_donor_list()
        else:
            if not is_existing_donor(response):
                add_donor(response)
            donation_amount = add_donation(response)
            thank_you_message(response, donation_amount)
            break
            
def show_donor_list():
    """ Print donor names to the screen.
    """
    for donor in donor_db:
        print(donor[0])

def is_existing_donor(donor_name):
    """ Iterate through the donor db to see if the donor_name matches a donor. If so, return True. If not, return False.

    Keyword arguments:
    donor_name - string to match against the donor names in the donor db.
    """
    for donor in donor_db:
        if donor[0].lower() == donor_name.lower():
            return True
    return False

def add_donation(donor_name):
    """ Find the matching donor, prompt the user for a donation amount, 
    and add the donation to the matching donor in the donor db.
    Return the donation amount.

    Keyword arguments:
    donor_name - string to match against the donor names in the donor db.
    """
    selected_donor = None
    for donor in donor_db:
        if donor[0].lower() == donor_name.lower():
            selected_donor = donor

    donation_amount = input(donation_amount_prompt)
    
    selected_donor[1].append(float(donation_amount))

    return float(donation_amount)  

def add_donor(donor_name):
    """ Add a donor to the donor db with empty donation amounts

    Keyword arguments:
    donor_name - string representing the donor name to add to the donor db.
    """
    donor_db.append((donor_name, []))

def thank_you_message(donor_name, donation_amount):
    """ Print a thank you message to the terminal.

    Keyword arguments:
    donor_name = name of the donor
    donation_amount = donation amount as a float
    """
    print("Dear {},".format(donor_name.title()))
    print("Thank you very much for your generous donation of ${:.2f}.".format(donation_amount))
    print("You ROCK!")
    
def main():
    """ Prompt the user to select an option (send a thank you, create a report, or quit), 
    which invokes the appropriate function.
    """
    while True:
        response = input(main_prompt)
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Please type '1', '2', or '3' to select one of the available options.")

if __name__ == "__main__":
   main()
