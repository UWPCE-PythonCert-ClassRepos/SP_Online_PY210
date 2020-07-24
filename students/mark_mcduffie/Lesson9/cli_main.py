#Mark McDuffie
#6/12/20
#Client class

import os
from donor_models import Donor
from donor_models import DonorCollection

donors = DonorCollection.initialize_dict(
    {"Jim Johnson": [20000.0, 3500.0, 1600.0],
          "Mike Lee": [10000.0, 450.0, 1000.0],
          "Joe Smith": [100.0, 50.0],
          "Bob Miller": [900.0, 1200.0],
          "Steve James": [100000.0]})


# Main Menu
def prompt():
    choice = input("You have the following options: \n 1: Send a Thank You \n 2: Send Letters to all Donors "
                   "\n 3: Create a Report \n 4: Quit \n")
    return choice


# Send a Thank you note to Donor
def send_thankyou():
    donor_name = input("Please enter the donor's name (first, last) \nor type 'list' to see current donors \n")
    while donor_name.lower() == "list":
        print(donors.donor_list())
        donor_name = input("Please enter donor's name ")

    try:
        donation = float(input("Enter the Amount for donation "))
    except ValueError:
        print("\n Invalid Amount. Please Enter a valid number \n")
    else:
        if donors.donor_exists(donor_name) is False:
            donor = Donor(donor_name)
            donors.add_donor(donor)
        else:
            donor = donors.donors[donor_name]
        donor.add_donation(donation)
        print(donor.print_thanks())

#Creates full report of current donor list
def create_report():
    print("Charity Donor History")
    print("Donor Name" + " " * 16 + "| Total Given | Num Gifts | Average Gift")
    print("-" * 66)
    for donor in DonorCollection.make_report(donors):
        print("{:<25} ${:>12.2f}  {:>9d}   ${:>11.2f}".format(*donor))

#Sends thanm you letter to every donor
def send_letters():
    donors.send_all()
    print("Letter were created and are in the {} directory.".format(os.getcwd()))

#Prompts the menu of options for the user
def menu():
    while True:
        choice = int(prompt())
        choice_Dict = {
            1: send_thankyou,
            2: send_letters,
            3: create_report,
            4: quit
        }
        if choice in choice_Dict:
            choice_Dict.get(int(choice))()
        else:
            print("Please enter a choice number between 1 and 4")

if __name__ == "__main__":
    menu()