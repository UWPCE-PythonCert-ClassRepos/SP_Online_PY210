#-------------------------------------------#
#Tittle: mailroom_part_03, PYTHON210 - Assignment 02
#Desc: Mailroom Part 3
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Nov-29>, Created file. Updated option_1_ty(), option_2_ty(),
# menu_selection(), and load_donors() for error handling. Updated create_thank_you_file()
# using list comprehension, old code left as comments for future understanding
#-------------------------------------------#

import pickle
#DATA---------------------------------------


main_menu = "Main Menu\n\n[1] Send a thank you letter.\n[2] Create a report.\
\n[3] Write thank you letters for all donors.\n[4] Exit program.\n"

ty_menu = "Thank You Menu\n\n[1] Create thank you for existing donor.\n[2] Create thank you for new donor.\n\
[3] View current donor list.\n[4] Return to main menu.\n"

data_file = "donor_history.dat"

#PROCESS------------------------------------
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
    """Display report"""
    donors = load_donors(data_file)
    donor_stats(donors)
    display_report(donors)
    
def option_3_mm():
    """Send a letter to each donor."""
    donors = load_donors(data_file)
    save_files = create_thank_you_file(donors)
    n = 0
    for item in donors:
        #Get personalized thank you letter
        letter = thank_you(item)
        with open(save_files[n], 'w') as file:
            file.write(letter)
        n += 1

def option_exit():
    return "Exit"

def option_1_ty():
    """Create thank you for existing donor."""
    donors = load_donors(data_file)
    while True:
        name = input("Please enter the donor's name: ")
        donor = find_donor(donors, name)
        if name == "exit":
            return
        elif donor == None:
            print("Donor not found. Please use an existing donor. Or type\
 'exit' to return to the Thank You Menu.")
        else:
            break
    while True:
        donation = input("Enter the new donation ammount: ")
        try:
            donation = float(donation)
        except ValueError:
            print("Please use a numerical entry (ex: 1000.00)")
        else:
            break
    #Update donor list with new information
    donors = update_donors(donors, name, donation)
    #Save updated donor history
    save_donors(donors, data_file)
    #Display thank you
    print(thank_you(donor))
    
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
    donors = load_donors(data_file)
    #Create new donor and at to the donor list
    donors.append(new_donor(name, donation))
    #Save updated donor history
    save_donors(donors, data_file)
    #Display thank you
    print(thank_you(find_donor(donors, name)))

def option_3_ty():
    """Display current donors."""
    donors = load_donors(data_file)
    display_donors(donors)

def save_donors(lst_group, save_file_b):
    """Save the current list of donors to a binary file
    
        Args:lst_group(list): List of dictionaries containing donors and their contribution.
            save_file_b(str): Data file name
    """
    with open(save_file_b, 'wb') as fileObj:
        pickle.dump(lst_group, fileObj)

def load_donors(save_file_b):
    """Load donor history from file
    
        Args:
            save_file(str): Data file name
        
        Returns:
            lst_group(list): List of dictionaries containing donors and their contribution.
    """
    try:
        with open(save_file_b, 'rb') as fileObj:
            lst_group = pickle.load(fileObj)
    #If nothing is saved to file return an empty list
    except FileNotFoundError:
        lst_group = []
    return lst_group

def create_thank_you_file(lst_group):
    """Creates a list of thank you file names.
    
        Args:
            lst_group(list): List of dictionaries containing donors and their contribution.
        Returns:
            lst_files(list): List of text files based on donor names
    """
    lst_files = [(donor["Name"].replace(" ", "_") + ".txt") for donor in lst_group]
    #Comprehension allowed above to replace the following:
        #lst_files = []
        #for item in lst_group:
        #    name = item["Name"]
        #    name = name.replace(" ", "_")
        #    name += ".txt"
        #    lst_files.append(name)
    return lst_files

def new_donor(person, money):
    """Create a new dictionary containing a donor and donation history
    
        Args:
            person(str): Name of donor.
            money(float): Donation ammount.
        
        Returns:
            a_new_donor(dict): Dictionary containing a donor and donation history
    """
    a_new_donor = {"Name": person, "Donation": [money], "Total": money, "Average": money, "Gifts": 1}
    return a_new_donor

def update_donors(lst_group, person, money):
    """Update a list of donors with a new donation
    
        Args:
            lst_group(list): List of dictionaries containing donors and their contribution.
            person(str): Name of donor.
            money(float): Most recent donation.

        Returns:
            lst_group(list): Updated list of donors.
    """
    for item in lst_group:
        if item["Name"] == person:
            item["Donation"].append(money)
            item["Total"] += money
            item["Gifts"] += 1
            item["Average"] = item["Total"]/item["Gifts"]
    return lst_group

def thank_you(donor_specs):
    """Display a thank you letter for a donor.
    
        Args:
            donor_specs(dict): Dictionary containing a donor and their donation information
        Returns:
            letter(str): Thank you letter for a donor.
    """
    letter = """
    Dear {donor},
    
    Thank you for your most recent donation of ${last:.2f}. We are humbled by your 
    lifetime contribution of ${total:.2f}.
    
    Sincerly,
    Making Good Things Happen"""
    return letter.format(donor = donor_specs["Name"], last = donor_specs["Donation"][-1], total = donor_specs["Total"])
    
def find_donor(lst_group, person):
    """Update a list of donors with a new donation
    
        Args:
            lst_group(list): List of lists containing donors and their contribution.
            person(str): Name of donor.
            
        Returns:
            lst_person(list): List containing a donor and their donations.
    """
    for item in lst_group:
        if person == item["Name"]:
            dict_person = item
            return dict_person

def display_donors(lst_group):
    """Display all donors on record.
    
        Args:
            lst_person(list): List of dictionaries containing a donor and their donations.
            
        Returns:
            None
    """
    print("Current donors are:")
    for item in lst_group:
        print(item["Name"])

def display_report(lst_people):
    """Format a list of dictionaries containing donor metrics.
    
    Args:
        lst_people (list): List of lists containing a donor's name, total
            contribution, number of contributions, and anverage contribution.
        
    Returns:
        None
    """
    
    formatted_header = "{name:<20} | {total:<10} | {gifts:<9} | {average:<10}"
    formatted_row = "{:<20} $ {:<10.2f}   {:^9n}  $ {:>10.2f}"

    print('==================== Donor Report: ==========================')
    print(formatted_header.format( name = "Donor Name", total = "Total Given",\
                                  gifts = "Num Gifts", average = "Average Gift"))
    print('-------------------------------------------------------------')
    for item in lst_people:
        n, d, t, a, g = item.values()
        print(formatted_row.format( n, t, g, a))
    print('==============================================================')
    print()

def donor_stats(lst_group):
    """Sort a list of dictionaries about key "Total" in high to low order.
    
        Args:
            lst_group(list): List of dictionaries containing donors and their contribution.
        
        Returns:
            lst_group(list): Sorted list of dictionaries containing donors and their contribution.
    """
    lst_group.sort(reverse = True, key = lambda y: y["Total"])
    return lst_group

#PRESENTATION INPUT/OUTPUT------------------

dict_main_menu = {1: option_1_mm, 2: option_2_mm, 3: option_3_mm, 4: option_exit}

if __name__ == '__main__':
    menu_selection(main_menu, dict_main_menu)



