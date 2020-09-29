# !/usr/bin/env python3

import sys
from donor_models import Donor
from donor_models import DonorCollection


donors = DonorCollection.initialize_donors_dict(
    {'Alexander Pushkin' : [200, 100, 340],
     'Mikhail Lermontov' : [300, 100],
     'Leo Tolstoy' : [150, 250, 100],
     'Fyodor Dostoevsky' : [125],
     'Anton Chekhov' : [100, 250],
     'Nikolai Gogol' : [325, 150]})



# Main Menu
def options_menu():
    print("\n".join(("Please select from the following options:",
          "1 - Send a Thank You letter to a single donar.",
          "2 - Create a Report.",
          "3 - Send Letters to All Donors",
          "4 - Quit."
          ">>> ")))
    option = input('')
    return option

def quit_now():
    print("Good bye and see you next time!")
    sys.exit()


# Send a Thank you note to Donor
def send_thank_you():
    mail_to = input ("Enter the full name of a donor or 'list' for current donors \n")
    while mail_to.lower() == "list":
        print(donors.list_of_donors())
        mail_to = input ("Please enter a  full name of a donor \n")
    try:       
        donation_amt = float(input ("Enter the donation amount \n"))             
    except ValueError:
        print("\n Invalid Amount. Please enter a valid number here! \n")
    else:   
        if donors.donor_exists(mail_to) is False:
            donor = Donor(mail_to)
            donors.add(donor)
        else:
            donor = donors.donors[mail_to]        
        donor.add_donation(donation_amt)
        print(donor.print_thank_you_message())    
   

def create_report():
    """Print a report showing donations."""
    donors.create_report()

def send_letters_to_all():
    """Generate a letter for each donor in the collection."""
    donors.send_letters_to_all()
    print('Sending Letters to all donors.\n')

def main_menu():
     switch_dict = {1: send_thank_you, 2: create_report, 3: send_letters_to_all, 4: quit_now }
     while True:
         try:
            option = int(options_menu())
            switch_dict.get(option)()
         except TypeError:
            print("Not a valid option. Please select one of the available options!")


if __name__ == "__main__":
     main_menu()