#Lesson 3 assignment
import sys
from operator import itemgetter
#Initial donor list
donorlist = [("William Gates", [150, 2, 75]), ("Mark Zuckerburg", [300, 3, 100]), ("Jeff Bezos", [100, 2, 50]),("Paul Allen", [200, 2, 100]), ("Elon Musk", [500, 2, 250])]

#Prompt Text
prompt = "\n".join(("Please choose from the below options",
    "1 - Send a Thank You", 
    "2 - Create a Report", 
    "3 - Quit",
    ">>> "))

def send_thankyou():
    #Store name of donor
    response = input("Enter Full Name:")
    #empty list created to store only the name information of donors
    donorlist_names = []
    for donor in donorlist:
        donorlist_names.append(donor[0])
    #'response_type 0 indicates a restricted input is not used. Ex. "list"'
    response_type = 0
    #displays the list of all donors if the user inputs list
    if response == "list":
        print(donorlist_names)
        print('\n')
        #variable "response_type" is set for a special input not to be included in donor list
        response_type = 1
        #if a special inpt is not used
    if response_type == 0:
        #store the donation amount as an int
        amount = int(input("Donation amount:"))
        #Goes through each name in list to find a match, then updates the values.
        for donor, donations in donorlist:
            if donor == response:
                donations[0] += amount
                donations[1] += 1
                donations[2] = round(donations[0] / donations[1])
                break
        else:
            # if donor is not found, adds new
            donorlist.append((response, [amount, 1, amount]))

        print(f'\nThank you {response} for your generous donation of {amount}\n')

def create_report():
    sorted_list = sorted(donorlist, key=itemgetter(1), reverse = True)
    # defining common symbols
    symbol = '$'
    symbol1 = '|'
    #displaying header text for the table
    string_header = '{:19}{:1}{:13}{:1}{:10}{:1}{:10}'.format("Donor Name", symbol1, " Total Given ", symbol1, " Num Gifts ", symbol1, " Average Gift ")
    print("\n")
    print(string_header)
    print("-----------------------------------------------------------")
    #printing the values in the donorlist
    for donor in sorted_list:
        string = '{:20}{:>2}{:10}{:11}{:>5}{:11}'.format(donor[0], symbol, donor[1][0], donor[1][1], symbol, donor[1][2])
        print(string)
        print("\n")

def exit_program():
    #exits the script
    print("Exiting....")
    sys.exit()


def main():
    while(True):
        response = input(prompt)
        #redirect to feature functions based on user selections
        if response == "1":
            send_thankyou()
        elif response == "2":
            create_report()
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option! \n")


if __name__ == "__main__":
    main()
