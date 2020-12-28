#Lesson 5 assignment
import sys

import donor_models
#Initial donor list
donor_list = {"William Gates": [150, 2, 75], 
            "Mark Zuckerburg": [300, 3, 100], 
            "Jeff Bezos": [100, 2, 50],
            "Paul Allen": [200, 2, 100],
            "Elon Musk": [500, 2, 250]
            }

#Prompt Text
prompt = "\n".join(("Please choose from the below options",
    "1 - Send a Thank You", 
    "2 - Create a Report", 
    "3 - Send letters to all dononrs",
    "4 - Quit",
    ">>> "))

x = 0
database = donor_models.DonorCollection(donor_list)

def menu_selection(dispatch_dict):
    while True:
        
        response = input(prompt)
        
        try:
            #execute the dispatch function with the input from user
            if dispatch_dict[response]() == "exit_program":
                break
        except KeyError:
            print('\n****VALID INPUTS ARE 1, 2, 3 OR 4. PLEASE TRY AGAIN****\n')
            
def send_thankyou():
    #Store name of donor
    response = input("Enter Full Name:")
    decode_input(response)

def decode_input(full_name):
    #'response_type 0 indicates a restricted input is not used. Ex. "list"'
    response_type = 0
    #displays the list of all donors if the user inputs list
    if full_name.lower() == "list":
        list_donor()
        response_type = 1
    if response_type == 0:
        full_name = full_name.title()
        donor_amount(full_name)
    return response_type

def list_donor():
    print('\n----LIST OF DONORS----')
    for donor in database.donorlist.keys():
        print('\n ', donor, '\n')

def donor_amount(donor_name):
    try:
        #store the donation amount as an int
        amount = int(input("Donation amount:"))
        if amount > 0:
            database.add_donation(donor_name, amount)
        else:
            print("\n****ONLY AMOUNTS GREATER THAN 0 ARE ACCEPTED****\n")
    except ValueError:
        print('\n****ONLY INTEGERS ARE VALID INPUTS. PLEASE TRY AGAIN****\n')

def create_report():
    symbol = '$'
    symbol1 = '|'
    #displaying header text for the table
    string_header = '{:19}{:1}{:13}{:1}{:10}{:1}{:10}'.format("Donor Name", symbol1, " Total Given ", symbol1, " Num Gifts ", symbol1, " Average Gift ")
    
    print("\n")
    print(string_header)
    print("-----------------------------------------------------------")

    for donor, (total, number, average) in database.sort_list(database.donorlist):
            string = '{:20}{:>2}{:10}{:11}{:>5}{:11}'.format(donor, symbol, total, number, symbol, average)
            print(string)
            print("\n")

def letters_ToAllDonors():
    database.letters_toAllDonors()
    

def exit_program():
    #exits the script
    print("Exiting....")
    sys.exit()


main_dispatch = {"1": send_thankyou,
                 "2": create_report,
                 "3": letters_ToAllDonors,
                 "4": exit_program
                 }


if __name__ == "__main__":
    menu_selection(main_dispatch)
        



