#Lesson 4 assignment
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
        #executes the dispatch function with the input from user
        if dispatch_dict[response]() == "exit_program":
            break



def send_thankyou():
    #Store name of donor
    response = input("Enter Full Name:")
    #'response_type 0 indicates a restricted input is not used. Ex. "list"'
    response_type = 0
    #displays the list of all donors if the user inputs list
    if response == "list":
        print(donorlist.keys())
        print('\n')
        #variable "response_type" is set for a special input not to be included in donor list
        response_type = 1
        #if a special inpt is not used
    if response_type == 0:
        #store the donation amount as an int
        amount = int(input("Donation amount:"))
        #Goes through each name in list to find a match, then updates the values.
        for donor, donations in donorlist.items():
            if donor == response:
                donations[0] += amount
                donations[1] += 1
                donations[2] = round(donations[0] / donations[1])
                break
        else:
            # if donor is not found, adds new
            donorlist[response] = [amount, 1, amount]
            
                

        print(f'\nThank you {response} for your generous donation of {amount}\n')


def create_report():
    sorted_list = sorted(donorlist.items())
    # defining common symbols
    symbol = '$'
    symbol1 = '|'
    #displaying header text for the table
    string_header = '{:19}{:1}{:13}{:1}{:10}{:1}{:10}'.format("Donor Name", symbol1, " Total Given ", symbol1, " Num Gifts ", symbol1, " Average Gift ")
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
        letter = "Dear %s,\n\n    Thank you for your very kind donation of %s.\n    It will be put to very good use.\n\nSincerely, \n-The Team"%(donor, total)

        filename = donor.replace(" ", "_") + ".txt"
        with open(filename, 'w') as g:
            g.write(str(letter))


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

