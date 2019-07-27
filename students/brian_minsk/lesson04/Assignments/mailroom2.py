# Author: Brian Minsk

import pathlib
import tempfile

""" Donor database from Mailroom Part 1
donor_db = [("Dee Zaster", [10000.00, 1500.00]), 
            ("Owen Money", [7000.00]), 
            ("Shanda Lear", [100.00, 900.00, 1500.00]), 
            ("Joe King", [500.00, 700.00, 500.00]),
            ("Artie Choke", [1600.00, 1800.00])]
"""

#note: the key for the enclosing dict should not be 0 or it will mess up functions below (since 0 is equivalent to False)
donor_db = {1:({"first_name":"Dee", "last_name":"Zaster", "donations":[10000.00, 1500.00]}),
            2:({"first_name":"Owen", "last_name":"Money", "donations":[7000.00]}),
            3:({"first_name":"Shanda", "last_name":"Lear", "donations":[100.00, 900.00, 1500.00]}),
            4:({"first_name":"Joe", "last_name":"King", "donations":[500.00, 700.00, 500.00]}),
            5:({"first_name":"Artie", "last_name":"Choke", "donations":[1600.00, 1800.00]}),}

main_prompt = "\n".join(("Please choose an option:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Quit",
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
        response = input(thank_you_prompt)
        if response.lower() == "list":
            show_donor_list()
        else:
            if not is_existing_donor(response):
                add_donor(response)
            donation_amount = add_donation(response)
            print(thank_you_message(response, donation_amount))
            break

def send_letters():
    """ Create a message for each donor in the donor_db and save each message to a file. File will be created 
    in a default temp directory and the file name will be the full name of the donor with spaces replaced by underscores.
    """
    destination_path = tempfile.gettempdir() 
    print("Files will be written to {} ".format(destination_path))

    for donor_id in donor_db:
        donor_data = donor_db[donor_id]
        donor_name = "{first_name} {last_name}".format(**donor_data)
        donation_amount = donor_data["donations"][-1] # assume the donation amount to use is the last donation
        message = thank_you_message(donor_name, donation_amount)
        filename = pathlib.Path("{}.txt".format(donor_name.replace(" ", "_")))
        destination_filename = destination_path / filename
        with open(destination_filename, "w") as f:
            f.write(message)
            
def show_donor_list():
    """ Print donor names to the screen.
    """
    for donor_id in donor_db:
        donor_data = donor_db[donor_id]
        print("{first_name} {last_name}".format(**donor_data))

def is_existing_donor(donor_name):
    """ Iterate through the donor db to see if the donor_name matches a donor. If so, return True. If not, return False.
    
    Keyword arguments:
    donor_name - string to match against the donor names in the donor db. Assume donor_name is in the form "Firstname Lastname"
    """
    name_list = donor_name.split()
    for donor_id in donor_db:
        donor_data = donor_db[donor_id]
        if donor_data["first_name"].lower() == name_list[0].lower() and donor_data["last_name"].lower() == name_list[1].lower():
            return donor_id
    return False

def add_donation(donor_name):
    """ Find the matching donor, prompt the user for a donation amount, 
    and add the donation to the matching donor in the donor db.
    Return the donation amount.

    Keyword arguments:
    donor_name - string to match against the donor names in the donor db.
    """
    selected_donor = None
    donor_id = is_existing_donor(donor_name)
    if donor_id:
        selected_donor = donor_db[donor_id]
    else:
        return 0

    donation_amount = input(donation_amount_prompt)
    
    selected_donor["donations"].append(float(donation_amount))

    return float(donation_amount)  

def add_donor(donor_name):
    """ Add a donor to the donor db with empty donation amounts

    Keyword arguments:
    donor_name - string representing the donor name to add to the donor db.
    """
    new_key = len(donor_db) + 1
    names = donor_name.split()
    donor_db[new_key] = {"first_name":names[0], "last_name":names[1], "donations":[]}
    return donor_db[new_key]

def thank_you_message(donor_name, donation_amount):
    """ Create a thank you letter and return as a string.

    Keyword arguments:
    donor_name = name of the donor
    donation_amount = donation amount as a float
    """
    donor = get_donor(donor_name)
    message_line1 = "\nDear {first_name} {last_name},\n".format(**donor)
    return message_line1 + "     Thank you very much for your generous donation of ${:.2f}.\n     You're a ROCK STAR!\n".format(float(donation_amount))

def get_donor(donor_name):
    """ Return a donor from the donor_db dict if one exists.

    Keyword arguments:
    donor_name - String with a name, assumed to be of the form "first_name last_name"
    """
    donor_id = is_existing_donor(donor_name)
    if donor_id:
        return donor_db[donor_id]
    else:
        return None

def create_report():
    """ Print a list of your donors, sorted by total historical donation amount.
    Include Donor Name, total donated, number of donations, and average donation amount as values in each row. 
    The end result should be tabular (values in each column should align with those above and below) and look something like this:

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14
    """
    # print header
    print("{:<26}| {:<11}| {:<10}| {:<12}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    # print header line
    for __ in range(0,65):
        print("-", end = "")
    print("") # get a new line
    create_report_rows()
    print("")

def create_report_rows():
    """ Create the rows (as described in create_report()) with the data from the donor db, 
    sorted by total donation amount (computed by the sort_key function).
    """
    sorted_donor_db = sorted(donor_db, key=sort_key, reverse=True)

    for donor_key in sorted_donor_db:
        donor = donor_db[donor_key]
        total_donation = 0.0
        num_donations = 0
        for donation in donor["donations"]:
            total_donation += donation
            num_donations += 1
        average_donation = 0.0
        if num_donations > 0:
            average_donation = total_donation / num_donations
        whole_name = "{} {}".format(donor["first_name"].title(), donor["last_name"].title())
        print("{:<26} ${:>11.2f} {:>10d}  ${:>12.2f}".format(whole_name, total_donation, num_donations, average_donation))

def sort_key(donor_key):
    total = 0.0
    for donation_amount in donor_db[donor_key]["donations"]:
        total += donation_amount
    return total

def quit_app():
    return "quit"
    
def main():
    """ Prompt the user to select an option (send a thank you, create a report, or quit), 
    which invokes the appropriate function. Except for the "quit" response, the others will return to this prompt after finishing.
    """
    switch_main_dict = {"1": send_thank_you, "2": create_report, "3": send_letters, "4": quit_app}

    while True:
        response = input(main_prompt)
        response_result = switch_main_dict.get(response, False)()
        if not response_result:
            print("Please type '1', '2', '3', or '4' to select one of the available options.")
        if response_result == "quit":
            break

if __name__ == "__main__":
   main()