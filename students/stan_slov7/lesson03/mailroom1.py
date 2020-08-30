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
    check_name(donor_name)
    new_donation = get_amount()
    add_donation(donor_name, new_donation)
    print_email(donor_name, new_donation)

  
def view_donor_names():
    print("The database contains the following donor names:\n")
    for entry in donor_data:
        print(entry[0])


def check_name(name_input):
    name_exists = False
    for donor_tup in donor_data:
        if donor_tup[0] == name_input.title():
            name_exists = True
    #If name doesnt exist:
    if not name_exists:
        donor_data.append((name_input.title(), []))
        print(f"Created new donor entry for the name: {name_input.title()}")
        #create new entry for input name and initialize donations to an empty list


def get_amount():
    prompt_amount = "Please enter a $ amount for the associated donation: \n" + ">>> "
    new_amount = float(input(prompt_amount))
    while True:
        if new_amount <= 0:
            print("Donation must be nonzero positive dollar amount, please enter an appropriate value.\n")
            new_amount = float(input(prompt_amount))  
        else:
            break
    return new_amount

    
def add_donation(d_name, n_donation):
    #adding donation happens after its been checked whether input name is in db 
    #(which an entry for name and an empty donation list is instantiated so that adding the amount is the same either way)
    for d_tup in donor_data:
        if d_tup[0] == d_name.title():
            d_tup[1].append(n_donation)
            print("New donation amount of: ${:.2f} has been recorded in the donor database, "
                  "under the associated donor name: {:s}.\n".format(n_donation, d_name.title()))


def print_email(new_donor, new_donation):
    print("Dear {:s},\n\n\tThank you for the generous donation of ${:.2f}!\n\n"
          "You will forever hold a place in our hearts, have a wonderful day!\n".format(new_donor.title(), new_donation))


def create_report():
    donor_history = []
    for d_tuple in donor_data:  
        name = d_tuple[0]
        total = sum(d_tuple[1])
        count = len(d_tuple[1])
        avg = total/count
        donor_history.append((name.title(), total, count, avg))
        
    donor_history = sorted(donor_history, key=sort_key, reverse=True) #reverse=True param sorts by highest to lowest total
    #Set the donor_history to it after having the sorted function applied 
    #sort by 2nd item in tuples i.e. by the total donation amt (couldve also use itemgetter(1))
    
    hdrfmt = "| {:<25s}|{:^18s}|{:^15s}|{:^18s}|".format("Donor Name:", "Total Donated:", "# Donations:", "Donation Avg:")
    divider = "-"*len(hdrfmt) 
    rowfmt = "| {d_name:<25s}|${d_total:^17.2f}|{d_count:^15d}|${d_avg:^17.2f}|".format
    #this uses format as a function to create formatting for each entry
    
    print(divider)
    print(hdrfmt) 
    print(divider)
    for d_entry in donor_history:
        print(rowfmt(d_name=d_entry[0], d_total=d_entry[1], d_count=d_entry[2], d_avg=d_entry[3]))
    print(divider, "\n")


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
    