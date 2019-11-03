#!/usr/bin/env python3

# ------------------------------ #
# Lesson 9 (Mailroom OO) for Python 210
#   Main program flow
# Dev: Breeanna Planica
# ChangeLog: (who, when, what)
#   BPA, 10/23/2019, Created module - refactor from mailroom4.py
# ------------------------------ #

import sys
from donor_models import Donor, DonorCollection


# ----- DATA ----- #
# ---------------- #
dict_menu = {} #holds menu options (dispatch)
str_menu = ("""\n--------------------
Please select the action you would like to perform:
1 - View a list of current Donors
2 - Add a new donor/donation amount
3 - Remove a donor
4 - Send an individual 'Thank You' letter
5 - Send a 'Thank You' letter to all current Donors
6 - Create a summarized report
7 - Save changes
8 - Quit
--------------------

Response: """) #holds menu options

dict_menu2 = {} #holds menu options (dispatch)
str_menu2 = ("""\n--------------------
Please select the action you would like to perform:
1 - View a list of current Donors
2 - Add a new donor
3 - Add a new donation amount for a current donor
4 - Return to the main menu
--------------------

Response: """) #holds menu options

obj_collection = DonorCollection() #collection/management of Donor objects


# ----- PROCESSING ----- #
# ---------------------- #

def load_names():
    """load donor names from database, create Donor objs, add to Collection obj"""
    try:
        obj_file_name = "./DonorNamesDB.txt"
        with open(obj_file_name, "r") as outfile: #open file in read only mode
            next(outfile) #skip header line
            for row in outfile:
                elements = row.split(",") #split by csv
                donor_id = elements[0].strip()
                donor_name = elements[1].strip()
                donor = Donor(donor_id, donor_name) #create donor obj
                obj_collection.append_collection(donor) #add new obj to collection
    except FileNotFoundError:
        with open(obj_file_name, "w") as outfile:
            outfile.write("DonorID, DonorName") #add header line


def load_donations():
    """load donation amts and append to Donor attribute"""
    try:
        obj_file_name = "./DonationsDB.txt"
        with open(obj_file_name, "r") as outfile: #open file in read only mode
            next(outfile) #skip header line
            for row in outfile:
                elements = row.split(",") #split by csv
                donor_id = int(elements[0].strip())
                donor_amt = float(elements[1].strip())
                for obj in obj_collection.collection: #search all donor objs
                    if obj.id == donor_id: #find corresponding id
                        obj.add_donation(donor_amt) #append donation amt
    except FileNotFoundError:
        with open(obj_file_name, "w") as outfile:
            outfile.write("DonorID, DonationAmt") #add header line


def main():
    """main menu"""
    while True: #display a menu of choices to the user
        try:
            response = int(input(str_menu)) # refers to preset menu declared under Data
            dict_menu.get(response)()
        except TypeError:
            print("\nPlease choose an action from the below list.")
            print("Type the menu number associated with the action you would like to perform.")
        except ValueError:
            print("\nPlease choose an action from the below list.")
            print("Type the menu number associated with the action you would like to perform.")


def list_current_main():
    """print list current method of collection class"""
    print(obj_collection.list_current()) #call funtion from dispatch menu


def add_don():
    """secondary menu - options to add a new donor and/or donation amount"""
    while True:
        response = int(input(str_menu2)) #refers to preset menu declared under Data
        dict_menu2.get(response)() #call funtion from dispatch menu


def add_donor():
    """add a new donor to the database"""
    print("\nType 'exit' to return the main menu")
    name = input("Enter the name of the donor you would like to add: ").title().strip()
    if name.upper() == "EXIT": return
    switch = ""
    for obj in obj_collection.collection: #search all Donor objs in collection
        if name == obj.name:
            switch = "Found"
            print(f"This donor name already exists in the database as DonorID: {obj.id}")
            response = input("Would you like to continue adding a new entry? (Y/N): ")
            if response.upper() == "Y":
                obj_collection.create_obj(name)
                print("Donor has been added!")
            elif response.upper() == "N":
                return
            else:
                print("Please enter a valid response (Y/N)")
    if switch != "Found": 
        obj_collection.create_obj(name)
        print("Donor has been added!")


def add_donation():
    """add a new donation amount an existing Donor obj"""
    try:
        list_current_main()
        print("\nType 'exit' to return the main menu.")
        donor_id = input("Please enter the DonorID you would like to add a donation for: ")
        if donor_id == "EXIT": return
        for obj in obj_collection.collection:
            if obj.id == int(donor_id):
                donation = input(f"Please enter the donation amount for {obj.name}: ").strip()
        if donation == "EXIT": 
            return
        else:
            donation = float(donation)
            for obj in obj_collection.collection:
                if obj.id == int(donor_id):
                    obj.add_donation(donation) #append donation to attribute
                    print("Donation has been added!")
    except ValueError:
        print("Please enter a valid DonorID and/or donation amount. \n")
    except UnboundLocalError:
        print("Please enter a valid DonorID")


def remove_don():
    """remove a donor and all donations from the databases"""
    try:
        list_current_main()
        print("\nType 'exit' to return the main menu.")
        donor_id = input("Please enter the DonorID you would like to remove: ")
        if donor_id == "EXIT": return
        switch = ""
        for obj in obj_collection.collection:
            if obj.id == int(donor_id):
                switch = "Found"
                print("Please note, removing a donor will remove all corresponding donations.")
                response = input(f"Would you like to continue removing {obj.name}? (Y/N): ")
                if response.upper() == "Y":
                    obj_collection.collection.remove(obj) #remove obj from collection
                    print("Donor has been removed!")
                    break
                elif response.upper() == "N":
                    print("Donor has not been removed.")
                    return
                else:
                    print("Please enter a valid response (Y/N)")
        if switch != "Found": print("Please enter a valid DonorID")
    except ValueError:
        print("Please enter a valid DonorID")


def send_one_main():
    """writes and saves thank you letter to a single donor"""
    try:
        list_current_main()
        print("\nType 'exit' to return the main menu.")
        donor_id = int(input("Please enter the DonorID you would like send a letter to: "))
        if donor_id == "EXIT": 
            return
        else:
            obj_collection.send_one(donor_id)
            print("Letter has been saved!")
    except UnboundLocalError:
        print("Please enter a valid DonorID")
    except ValueError:
        print("Please enter a valid DonorID")


def send_all_main():
    """writes and saves thank you/mailer letter to all current donors"""
    obj_collection.send_all()
    print("Letters have been saved!")


def reporting_main():
    """displays summarized report sorted by donation amt"""
    print(obj_collection.create_report())


def quit_program():
    sys.exit()


# ----- PRESENTATION ----- #
# ------------------------ #
if __name__ == '__main__':
    dict_menu = {1: list_current_main,
        2: add_don,
        3: remove_don,
        4: send_one_main,
        5: send_all_main,
        6: reporting_main,
        7: obj_collection.save_changes,
        8: quit_program} #holds menu options (dispatch)
    dict_menu2 = {1: list_current_main,
        2: add_donor,
        3: add_donation} #holds menu options for option 2 in the main menu (dispatch)

    load_names() #load donor data from the database
    load_donations() #load donation data from the database
    print("\n\n**********************************")
    print("*** Welcome to DonorManagement ***")
    print("**********************************")
    main() #run main
