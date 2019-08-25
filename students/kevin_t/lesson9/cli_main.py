from mailroom_OO import Donor as D
from mailroom_OO import DonorCollection as DC
import sys

#Opening prompt function
def opening_screen():
    #Tell the user what their options are. Ask for an input.
    print('')
    print('Welcome to the mailroom tool. Please select an action:')
    print('1 - Send a Thank You')
    print('2 - Create a Report')
    print('3 - Send letters to all donors')
    print('4 - Quit')
    #Send user input back to main function to be analyzed.
    return input()

def list_donors(donor_collection):
    #Print each existing donor's name
    donor_collection.list_donors

#'Send thank you' function
def send_thank_you(donor_collection):
    #Ask for a donor's name. If user requests 'list', display existing donors and request action agin.
    while True:
        name = input("Please enter a donor's name to thank (List to see existing donors, Quit to exit): ").title()
        if name == 'List':
            print(donor_collection.list_donors())
        #When user inputs something besides list, pass it on.
        else:
            break
    #If user entered 'quit', skip all this
    if name != 'Quit':
        #Ask the donor's donation amount
        amount = float(input("Please enter donation amount: "))
        donor_collection.new_donation(name, amount)
        print(donor_collection.ty_text(name))

#Print report function
def print_report(donor_collection):
    #Header
    print('{:<20} | {:^10} | {:^10} | {:>10}'.format('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift'))
    print ('-'*65)
    #Print report, iterate through each donor in the existing list
    for donor in donor_collection.donor_list:
        print('{:<20} $ {:>10.2f}   {:>10}   $ {:>10.2f}'.format(donor.name, donor.tot_donations, donor.num_donations, donor.avg_donation))

def send_letters_to_all_donors(donor_collection):
    #Create a .txt file with thank you text for each donor in the existing list
    for donor in donor_collection.donor_list:
        with open(donor.name + '.txt', 'w') as file:
            file.write(donor_collection.ty_text(donor.name))

def quit_program(donor_collection):
    print("Leaving mailroom")
    sys.exit()

#Main function
if __name__ == '__main__':
    #Establish existing donor list
    donors = [D("Bill Gates", [345678, 454540]), D("Mark Zuckerberg", [6487, 4978,5487,1678]), D("Jeff Bezos", [842]), D("Paul Allen", [425, 3523]), D("Kanye West", [4, 1235234])]
    donor_collection = DC()
    for donor in donors:
        donor_collection.new_donor(donor)

    switch_dict = {
        '1': send_thank_you,
        '2': print_report,
        '3': send_letters_to_all_donors,
        '4': quit_program
    }

    #Prompt the user to do something. Stay here unless user selects a quit item.
    while True:
        #Call the opening screen function
        user_selection = opening_screen()
        #Analyze responses and call related function or quit.
        #if user_selection in switch_dict:
        try:
            switch_dict[user_selection](donor_collection)
        except KeyError:
            print('Please select a value 1-4')