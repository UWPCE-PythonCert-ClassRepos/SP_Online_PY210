#!/usr/bin/env python3
from donor_models import  Donor, DonorCollection
import sys

#prompts (alphabetical)
donation_prompt = "Please enter the amount of the donation. \n"

thank_you_prompt = "Please enter the full name of the donor or type 'list' for list of names. \n"

write_location_prompt = "Please enter the directory name to save to, or type 'no' for temp directory. \n"

main_prompt = "\n".join(("Please choose from the following options:",
          "1 - Create a report",
          "2 - Send thank you letter to one donor",
          "3 - Exit \n"
          ))

def display_thank_you():
    #keep doing this until further notice
    while True:
        #ask for name or to print list of names
        donor_name = input(thank_you_prompt)
        #print out names
        if donor_name == 'list':
            print(DonorCollection().list_donors())
            #skip loop to reprompt
            continue
        
        #ask for the donation amount
        donor_amount = input(donation_prompt)
        #set as a numeric value
        donor_amount = float(donor_amount)
        
        print(Donor(donor_name, donor_amount).send_thank_you())
        DonorCollection.add_donor(donor_name, donor_amount)
        break
    
def exit_program():
    #It's all there, black and white, clear as crystal! 
    #You stole fizzy lifting drinks! 
    #You bumped into the ceiling which now has to be washed and sterilized, so you get nothing! 
    #You lose!
    print("Good day!")
    sys.exit()
    
def print_report():
    print(DonorCollection().donor_report())
    
main_menu = {
        1 : print_report,
        2 : display_thank_you,
        3 : exit_program
        }

def main():
    #keep doing this until further notice
    while True:
        #print out main menu for user choice
        try:
            response = int(input(main_prompt))
        except ValueError:
            print("Please input valid number.")
            pass

        try:    
            #main_menu.get(response)() prob more clear than the comprehension.  save for future
            {v() for (k,v) in main_menu.items() if k == response}
        except TypeError:
            print("Please select a number from the list.")
            pass   

if __name__ == '__main__':
    main()
    
