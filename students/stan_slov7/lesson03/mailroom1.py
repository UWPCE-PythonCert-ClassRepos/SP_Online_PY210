#!/usr/bin/env python3

#+--------------------------+
#| Mailroom pt.1 - Lesson 3 |
#+--------------------------+

import sys  #used to cleanly exit out of the program should the user select to.

#from operator import itemgetter  
#to easily perform basic sort based on chosen index of all tuple objects in a list

#main data structure will be a list of tuples, containing lists for donor name and donation values,
#since need a collection that holds lists of different types of varying sizes for each donor.

#using tuple to hold donor info because immutable and set expectation that each
#donor will only have two items as part of the tuple: a string i.e. list of chars for the name,
# and a list for the 1 - 3 donation values, stored in global namespace.


#the initialized list of tuple objects data structure
donor_data = [('Jeff Bridges', [1309.45, 7492.32]), 
              ('Alice Summers', [3178.67, 9823.00]), 
              ('Henry Cavill', [9132.92, 7837.50]), 
              ('Evie Styles', [4592.25, 2145.90, 7314.87]), 
              ('Harvey Dent', [14503.70])]


main_prompt = "\n".join(("Welcome to the Mailbox part 1.",
          "Please choose one of the following options:",
          "1 - Send a Thank You.",
          "2 - Create a Report",
          "3 - Quit Program",
          ">>> "))

          
def send_thank_you():

    prompt_name = "\n".join(("Please enter the full name of a donor currently in the database.",
                "Otherwise, enter a new full name to add a new (donor, donations[]) entry in that name.",
                "(You may type 'list' to see all the current donor names in the database)",
                ">>> "))  
    while True:
        donor_name = input(prompt_name) 
        if donor_name.lower() == 'list':
            view_donor_names()
            print()
        elif donor_name.lower() == 'q':
            return    #If user wants to return to main prompt during sending thank you email
        else:
            break
    #Add function defs next:
    check_name(donor_name)
    new_donation = get_amount()
    add_donation(donor_name, new_donation)
    print_email(donor_name, new_donation)

  
def view_donor_names():
    print("The database contains the following donor names:\n")
    for entry in donor_data:
        print(entry[0])


def check_name(name_input):
    pass
    
    
def get_amount():
    pass
    
    
def add_donation(d_name, n_donation):
    pass


def print_email(new_donor, new_donation):
    print("Dear {:s},\n\n\tThank you for the generous donation of ${:.2f}!\n\n"
          "You will forever hold a place in our hearts, have a wonderful day!\n".format(new_donor.title(), new_donation))


def sort_key(hist_tup):
    return hist_tup[1]   
    #to sort by total (historical) donation amount


def quit_program():
    print("Thank you, this program will now terminate.")
    sys.exit()
    

def main():
    #Loop collecting user input
    while True:                   
        response = input(main_prompt)  
        # redirect to feature functions based on the user selection
        if response == "1":
            send_thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            quit_program()
        else:
            print(response, " is not a valid selection. Please enter a valid option value.\n")

if __name__ == "__main__":
    # don't forget this block to guard against your code running automatically if this module is imported
    main()