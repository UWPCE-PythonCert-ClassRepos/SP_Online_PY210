#! python
#----------------------------------------------------
# Lesson 9 - Assignment 8: Mailroom - Object Oriented
#            User interface cli_main.py
#----------------------------------------------------

import sys
from donor_models import Donor, DonorCollection
from operator import itemgetter
from datetime import date

dc = DonorCollection()

def menu_selection(prompt, dispatch):
    #This function will ask the user to choose an option from the menu,
    #and call the associated function in the dispatch dictionary.
    while True:
        response = input(prompt)
        if response in dispatch:
            dispatch[response]()
        else:
            print("That is not a valid option!")

def send_a_thank_you():
    #This function will first prompt user for a donor's name, or type list to see
    #all donors. After a name is entered, it will prompt for a donation amount to
    #be added. At the end, a 'Thank You' letter will go out to the donor. The user
    #may choose to quit at anytime by typing 'q' at the prompt, and it will take
    #the user back to the main menu. For now, the letter will print to the terminal.
    prompts = {1 : "Please enter first and last name or type 'list' to see all donors or q to quit:",
               2 : "Name contains invalid character(s), please try again:",
               3 : "Please enter first and last name only:",
               5 : "Please enter a donation amount or q to quit:",
               6 : "Please enter a valid amount greater than zero or q to quit:",
               7 : "Amount cannot have more than two decimal places, please try again:",
               8 : "Is the amount {:.2f} correct? (Y/N)",
               9 : "Invalid response, please re-enter the donation amount or q to quit:"
              }
    symbol = ">>>"

    #Asks user to enter a donor name
    name_list = dc.donor_list()
    prompt = prompts[1]
    while True:
        in_prompt = "\n".join((prompt, symbol))
        name = input(in_prompt)
        if name == 'list':
            print("\n".join(name_list))
            continue
        elif name == "q":
            return
        else:
            prompt_num, name = check_input_name(name, name_list)
            if prompt_num > 0:         #invalid input
                prompt = prompts[prompt_num]
                continue
            else:
                break

    #Asks user to enter a donation amount
    prompt = prompts[5]
    while True:
        in_prompt = "\n".join((prompt, symbol,))
        amount = input(in_prompt)
        if amount == "q":
            return
        try:
            amount = float(amount)
        except ValueError:
            prompt = prompts[6]
            continue
        else:
            if amount <= 0:
                prompt = prompts[6]
                continue
            elif str(amount)[::-1].find('.') > 2:
                prompt = prompts[7]
                continue
            else:
                #ask user to confirm the amount
                in_prompt = "\n".join((prompts[8], symbol)).format(amount)
                response = input(in_prompt)
                if response.lower() == "n":
                    prompt = prompts[5]
                    continue
                elif response.lower() == "y":
                    break
                elif response == "q":
                    return
                else:
                    prompt = prompts[9]
                    continue

    dc.add_donation(name, amount)
    d = Donor(name)
    print(d.thank_you_letter(d.first_name, amount))

def check_input_name(name, name_list):
    #Checks if the name is acceptable.
    #If the name is in the name_list, returns that name so that it can match
    #the 'database' when adding a donation.
    #For new name, capitalize the first character of first and last name
    # (it does not capitalize the letter after the dash)
    prompt_num = 0
    new_name = name
    name = " ".join(name.split())  #remove any excessive spaces
    words = name.split()
    if len(words) > 2:
        prompt_num = 3
    elif len(words) < 2:
        prompt_num = 1
    else:
        name_from_list = [donor for donor in name_list if donor.lower() == name.lower()]
        if name_from_list:
            new_name = name_from_list[0]
        elif all_valid_chars(words[0]) and all_valid_chars(words[1]):
            new_name = words[0].capitalize() + " " + words[1].capitalize()
        else:
            prompt_num = 2
    return prompt_num, new_name

def all_valid_chars(word):
    #Dash is the only valid non-alpha and it cannot have more than one
    if word.isalpha():
        valid = True
    elif word.count("-") == 0:   #dash is the only valid non-alpha 
        valid = False
    elif word.count("-") == 1 and word[0] != "-" and word[-1:] != "-":
        valid = True
    else:
        valid = False            #too many dashes or dash is in unexpected location
    return valid

def create_a_report():
    #Gets the report from DonorCollection class and prints to the terminal.
    #It will show in the order of total donation amount from highest to lowest.
    print(dc.donors_summary_report())
    print()

def send_letters_to_all_donors():
    #Writes a letter to each donor into a file, and the file will be
    #created in the directory that the program is running on.
    letters = dc.letters_to_all_donors()
    for letter in letters:
         filename = letter[1].replace(" ", "_") + ".txt"   #use donor name for filename
         with open(filename, 'w') as out_file:
             out_file.write(letter[0])

def exit_program():
    print("Exiting the Mailroom program...")
    sys.exit()  # exit the interactive script

def main():
    #Calls the menu_selection to prompt user to choose a task from the menu
    prompt = "\n".join(("Welcome to the ChangeALife Mailroom!",
             "Please choose from below options:",
             "1 - Send a Thank You to a donor",
             "2 - Create a Report",
             "3 - Send letters to all donors",
             "4 - Exit",
             ">>> "))
    dispatch = {"1" : send_a_thank_you,
                "2" : create_a_report,
                "3" : send_letters_to_all_donors,
                "4" : exit_program
               }
    menu_selection(prompt, dispatch)



if __name__ == "__main__":
    main()
