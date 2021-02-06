#!/usr/bin/env python3
#-------------------------------------------#
#Tittle: mailroom_oo.py, PYTHON210 - Assignment 8
#Desc: Create thank you letters for donors. 
#      Store donor information.
#Change Log: (Who, When, What)
#Brent Kieszling, 2021-Jan-25, created file
#-------------------------------------------#

from donor_modles import Donor, Donors
#DATA---------------------------------------
main_menu = "Main Menu\n\n[1] Write a thank you letter.\n[2] Display current donor rankings.\
\n[3] Write thank you letters for all donors.\n[4] Exit program.\n"

ty_menu = "Thank You Menu\n\n[1] Create thank you for existing donor.\n[2] Create thank you for new donor.\n\
[3] View and edit donor information.\n[4] Return to main menu.\n"

save_file = "donor_profiles.dat"

#PROCESS------------------------------------
donor_history = Donors()
donor_history.load(save_file)

def menu_selection(menu, dispatch):
    """Navigate a menu.
    
        Args:
            menu(str): Display menu
            dispatch(dict): Dictionary controlling menu options
    """
    while True:
        response = input(menu)
        try:
            response = int(response)
        except ValueError:
            print("Please only use numbers.")
        else:
            if dispatch.get(response)() == "Exit":
                break

def option_1_mm():
    """Write thank you"""
    dict_ty_menu = {1: option_1_ty, 2: option_2_ty, 3: option_3_ty, 4: option_exit}
    menu_selection(ty_menu, dict_ty_menu)

def option_2_mm():
    """Display donor rankings"""
    print(donor_history)
    print()
    
def option_3_mm():
    """Send a letter to each donor."""
    donor_history.thank_yous()
    print("Thank you letters have been created")
    print()

def option_exit():
    return "Exit"

def option_1_ty():
    """Create thank you for existing donor."""
    while True:
         name = input("Enter the donor's name or type 'exit' to return to the\
 Thank You Menu:\n")
         if name == "exit":
             return
         else:
             try:
                 donor = donor_history.find_donor(name)
                 break
             except IndexError:
                 print("Donor not found")
             
    while True:
         donation = input("Enter the new donation ammount: ")
         try:
             donation = float(donation)
         except ValueError:
             print("Please use a numerical entry (ex: 1000.00)")
         else:
             break
    donor.new_donation(donation)
    print("The following has been saved to file:")
    print((donor.thank_you()))
    print()
    donor_history.save(save_file)
    donor.create_file()

def option_2_ty():
    """Create a thank you for a new donor."""
    name = input("Please enter the donor's name: ")
    while True:
        donation = input("Enter the new donation ammount: ")
        try:
            donation = float(donation)
        except ValueError:
            print("Please use a numerical entry (ex: 1000.00)")
        else:
            break
    donor_history.new_donor(name, donation)
    donor_history.save(save_file)
    print((donor_history.find_donor(name).thank_you()))

def option_3_ty():
    """View and edit current donor information"""
    print(donor_history)
    print()
    while True:
        name = input("Please enter the name of the donor you would like to edit: ")
        try:
            donor = donor_history.find_donor(name)
        except IndexError:
            print("Donor not found.")
        else:
            print(donor)
            print()
            break
    while True:
        choice = input("Enter 1 to change the name or 2 to modify a previous donation:\n")
        try:
            choice = int(choice)
            if choice == 1 or 2:
                break
        except ValueError:
            pass
        print("Please use the number 1 or 2.")
    if choice == 1:
        new_name = input("Please enter the new name: ")
        donor.person = new_name
        name = new_name
    if choice == 2:
        while True:
            donation_selection = input("Please enter the donation to be changed (ex: 1, 2, 3, ...):\n")
            try:
                donation_selection = int(donation_selection)
            except ValueError:
                print("Please use numbers only")
            else:
                if donation_selection > donor.gifts:
                    print("That is not a valid selection")
                else:
                    break
        while True:
            new_donation = input("Please enter the new amount (ex: 100.11): ")
            try:
                new_donation = float(new_donation)
            except ValueError:
                print("Please use numbers only")
            else:
                break
        donor.change_donation(donation_selection, new_donation)
    donor_history.save(save_file)
    print("Donor information updated.")
    print(donor_history.find_donor(name))
    print()






#PRESENTATION INPUT/OUTPUT------------------

dict_main_menu = {1: option_1_mm, 2: option_2_mm, 3: option_3_mm, 4: option_exit}

if __name__ == '__main__':
    menu_selection(main_menu, dict_main_menu)