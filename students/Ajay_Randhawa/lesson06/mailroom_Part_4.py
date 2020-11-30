#Lesson 5 assignment
import sys
from operator import itemgetter
#Initial donor list
donorlist = {"William Gates": [150, 2, 75], 
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


def menu_selection(dispatch_dict):
    while True:
        
        response = input(prompt)
        
        try:
            #execute the dispatch function with the input from user
            if dispatch_dict[response]() == "exit_program":
                break
        except KeyError:
            print('\nVALID INPUTS ARE 1, 2, 3 OR 4. PLEASE TRY AGAIN.\n')
            

def send_thankyou():
    #Store name of donor
    response = input("Enter Full Name:")
    decode_input(response)


def decode_input(full_name):
    #'response_type 0 indicates a restricted input is not used. Ex. "list"'
    response_type = 0
    #displays the list of all donors if the user inputs list
    if full_name == "list":
        list_donor()
        response_type = 1
    if response_type == 0:
        donor_amount(full_name)
    return response_type


def list_donor():
    for donor in donorlist.keys():
        print("\n ", donor)
    print('\n')
    return donorlist.keys()


def donor_amount(donor_name):
    try:
        #store the donation amount as an int
        amount = int(input("Donation amount:"))
    except ValueError:
        print('\nONLY INTEGERS ARE VALID INPUTS. PLEASE TRY AGAIN.\n')
    donor_addition(donor_name, amount)


def donor_addition(donor_name, donor_amount):
    if(donor_amount > 0):
        #Goes through each name in list to find a match, then updates the values.
        for donor, donations in donorlist.items():
            if donor == donor_name:
                donations[0] += donor_amount
                donations[1] += 1
                donations[2] = round(donations[0] / donations[1])
                break
        else:
            # if donor is not found, adds new
            donorlist[donor_name] = [donor_amount, 1, donor_amount]
        
        print(f'\nThank you {donor_name} for your generous donation of {donor_amount}\n')


def create_report():
    sorted_list = sorted(donorlist.items())
    # defining common symbols
    symbol = '$'
    symbol1 = '|'
    #displaying header text for the table
    string_header = '{:19}{:1}{:13}{:1}{:10}{:1}{:10}'.format("Donor Name", symbol1, " Total Given ", symbol1, " Num Gifts ", symbol1, " Average Gift ")
    get_report(string_header, sorted_list, symbol, symbol1)
    return print(string_header)

def get_report(string_header, sorted_list, symbol, symbol1):
    print("\n")
    print(string_header)
    print("-----------------------------------------------------------")
    #printing the values in the donorlist
    for donor, (total, number, average) in sorted_list:
        string = '{:20}{:>2}{:10}{:11}{:>5}{:11}'.format(donor, symbol, total, number, symbol, average)
        print(string)
        print("\n")

def lettersToAllDonors():
    for donor, (total, number, average) in donorlist.items():
        filename = donor.replace(" ", "_") + ".txt"
        with open(filename, 'w') as g:
            g.write(str(get_letter_text(donor, total)))

def get_letter_text(name, amount):
    letter = "Dear %s,\n\n    Thank you for your very kind donation of %s.\n    It will be put to very good use.\n\nSincerely, \n-The Team"%(name, amount)
    return letter


def exit_program():
    #exits the script
    print("Exiting....")
    sys.exit()


main_dispatch = {"1": send_thankyou,
                 "2": create_report,
                 "3": lettersToAllDonors,
                 "4": exit_program
                 }


if __name__ == "__main__":
    menu_selection(main_dispatch)
        



