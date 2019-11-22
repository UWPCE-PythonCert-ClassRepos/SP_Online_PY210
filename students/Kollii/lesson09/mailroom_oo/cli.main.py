import sys
from donor_models import Donor
from donor_models import DonorCollection

donors = DonorCollection.initialize_dict(
    {'William Gates, III' : [653772.32, 12.17],
     'Jeff Bezos': [877.33],
     'Paul Allen': [663.23, 43.87, 1.32],
     'Mark Zuckerberg' : [1663.23, 4300.87, 10432.0]})


# Main Menu
def options_menu():
    print("\n".join(("Welcome to the XYZ Charity!",
          "Please choose from below options:",
          "1 - Send a Thank you Note",
          "2 - Create a Report",
          "3 - Send Letters to All",
          "4 - Quit"
          ">>> ")))
    option = input('')
    return option

def quit_menu():
    print("Good bye")
    sys.exit()


# Send a Thank you note to Donor
def send_thankyou():
    donor_name = input ("Enter the donor's FULL NAME "
                        "or 'List' - to see ALL Donors Names ")

    while donor_name.lower() == "list":
        print(donors.donors_list())
        donor_name = input ("Please enter a  FULL Name ")
       
    try:       
        donation_amt = float(input ("Enter the Amount for donation "))             
    except ValueError:
        print("\n Invalid Amount. Please Enter a valid number \n")
    else:   
        if donors.donor_exists(donor_name) is False:
            donor = Donor(donor_name)
            donors.add(donor)
        else:
            donor = donors.donors[donor_name]        
        donor.add_donation(donation_amt)
        print(donor.print_thanksnote())    
   

def create_report():
    """Display a report showing donations."""
    donors.create_report()

def send_letters_all():
    """Generate a letter for each donor in the collection."""
    donors.send_letters_all()
    print('sending Letters to ALL.\n')

def main_menu():
     switch_dict = {1: send_thankyou, 2: create_report, 3: send_letters_all, 4: quit_menu }
     while True:
         try:
            option = int(options_menu())
            switch_dict.get(option)()
         except TypeError:
            print("\n Invalid Option \n"
                  "Enter a Valid Option from the above list\n")


if __name__ == "__main__":
     main_menu()