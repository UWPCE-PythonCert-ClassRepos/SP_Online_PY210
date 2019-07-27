# -*- coding: utf-8 -*-
""" This code allows a user to update a list of donors, print
all donations, average donations, and print a thank you email. 
"""

"""
Lesson03 :: Mailroom Part 1
@author: Chuck Stevens :: CCSt130
Edited Sun July 21 19:32:15 2019

This is a reworked (2x), shorter Part1 that follows the directions.

"""

import datetime # dates needed for comparison

from collections import Counter # Count of donations

from statistics import mean # Calc AVG

from datetime import date # Need current date for new donations


def main():
    """ Contains list of donors and displays Menu. """
    all_donations = [[2018,8,26,"Bill and Melinda Gates Foundation",48405000], \
                      [2014,8,14,"Stichting INGKA Foundation",40338000], \
                      [2013,7,12,"Stichting INGKA Foundation",31837000], \
                      [2014,8,16,"Buffet Foundation",27940000], \
                      [2014,8,17,"Bill and Melinda Gates Foundation",26340000], \
                      [2017,8,19,"Bill and Melinda Gates Foundation",23049002], \
                      [2016,8,19,"Bill and Melinda Gates Foundation",22737329], \
                      [2018,8,26,"Bill and Melinda Gates Foundation",21455000], \
                      [2016,8,20,"Bill and Melinda Gates Foundation",20670300], \
                      [2019,2,11,"Bezos Family Foundation",18938000], \
                      [2015,2,6,"Bezos Family Foundation",19554000], \
                      [2014,6,27,"Stichting INGKA Foundation",19474000], \
                      [2016,8,20,"Walton Family Foundation",18947775], \
                      [2015,8,13,"Buffet Foundation",18603000], \
                      [2016,3,11,"Walton Family Foundation",17914000], \
                      [2015,8,17,"Walton Family Foundation",17789000], \
                      [2015,8,17,"Walton Family Foundation",17440000], \
                      [2011,8,21,"Walton Family Foundation",18254000], \
                      [2017,8,18,"Stichting INGKA Foundation",15966000], \
                      [2014,8,16,"Walton Family Foundation",16066000], \
                      [2017,8,19,"Walton Family Foundation",14841309], \
                      [2013,11,21,"Buffet Foundation",15381000], \
                      [2015,12,10,"Buffet Foundation",15115000], \
                      [2017,8,19,"Walton Family Foundation",14391572], \
                      [2015,8,13,"Buffet Foundation",14534000], \
                      [2016,8,19,"Bill and Melinda Gates Foundation",14354375], \
                      [2016,8,20,"Walton Family Foundation",14093386]]
        
    # Main Menu choice
    usr_input = ""

    # This name used for Quit option--main menu error handling
    quit_opt = ["Q", "q", "Quit", "quit", "QUIT", "qUIT"]
        
    while True:
        # Displaying menu header
        print()
        print()
        print(50 * '*')
        print()
        print(18 * '*', "Menu Options", 18 * '*')
        print()
        # Display menu options
        print(" 1. Send a Thank You")
        print(" 2. Create a Report")
        print(" 3. Quit")                    
        print()
        print(50 * '*')
        
        # Prompt user for input
        input_msg = "Please choose a Menu Option [1,2 or Q to Quit]: "

        # Capture user choice 
        usr_input = str(input(input_msg))

        # Other functions launch based on menu selection
        if usr_input == '1':
            new_donor = donor_sub_menu(all_donations)
            prn_an_email(all_donations, new_donor)

        elif usr_input == '2':
            prn_donor_avg(all_donations)
        # Quit        
        elif usr_input == '3':
            break
        # Quit
        elif usr_input in quit_opt:
            break
        # Catch-all
        else: 
            print()
            print("Invalid entry--try again!")
            print()

    print()
    print("### Program Exit ###")

def list_donor_names(all_donations):
    """ Makes a list of unique individual donor names from data. """
    # List holds donations from donor selected
    donor_names = []
    # List holds enumerated list
    donor_list = []
    
    for donor in all_donations:
        if not donor[:][3] in donor_names:
            # Add donor name only to new list
            donor_names.append(donor[:][3])

    # Convert to numbered list
    num_list = enumerate(donor_names,1)
    
    print()
    print("Our Donors:")
    print()
    
    # Convert enumerated list to tuple and print
    for names in num_list:
        donor_list.append(names)
        print(f' {names[0]}. {names[1]}')

    return

def donor_sub_menu(upd_donation_list): # updated donation list
    """ Displays 'nested' menu of donors.
        Takes user's choice of donor and returns it.
        Allows user to add a new donation. """
    
    # Error handling if user wants to see list again
    list_opt = ["L", "l", "List", "list", "LIST", "lIST"]

    # Used to hold new donation before appending
    temp_list = []

    # Displaying menu header
    print()
    print()
    print(50 * '*')
    print()
    print(18 * '*', "Choose Donor", 18 * '*')
    
    list_donor_names(upd_donation_list)
    
    while True:
        print()
        print(50 * '*')

        # Prompt user for input
        input_msg = "Please type the name of an Organization: "
        # Capture user choice 
        new_donor = str(input(input_msg))
        print()
        # Could put a loop here to allow correction
        print("You entered: {}".format(new_donor))

        # Strip white space for comparison
        input_strip = new_donor.replace(' ', '')

        if new_donor in list_opt:
            list_donor_names(upd_donation_list)

        # Filter out non-alpha entry            
        elif input_strip.isalpha():
            break 
        else:
            print()                
            print("Invalid entry--try again!")
            print()

    # New donation option
    print()
    print("Would you like to enter a new Donation?")

    while True:
        input_msg = "Please choose 'Y' for Yes and 'N' for No. [Y,N]: "
        # Capture user choice 
        usr_input = str(input(input_msg))
        
        if usr_input == 'Y' or usr_input == 'y': # Why, yes!
            break
        elif usr_input == 'N' or usr_input == 'n': # Well, no.
            print()
            print("No Donation Added.")
            return(new_donor)
        elif usr_input == 'Q' or usr_input == 'q': # Outta here
            return
        elif usr_input.isdigit(): 
            print("Invalid entry--try again!") # A for effort
            print()
        else: 
            print("Invalid entry--try again!")
            print()

    the_date = (date.today())
    # Append today's date as date of donation
    temp_list.append(the_date.year)
    temp_list.append(the_date.month)
    temp_list.append(the_date.day)

    # Include donor name already entered
    if new_donor != "":
        print()
        print("A Donation from '{}' will be entered into our list...".format(new_donor))
        # print()
        temp_list.append(new_donor)
    # Prompt for donation amount
    while True:
        amt_input = (input("Enter amount of donation without separators (e.g. '12333444'): "))   
        # print()
        if amt_input.isdigit():
            new_amt = float(amt_input)
            if new_amt > 0 and new_amt < 1000000000: # n < billion
                # add to list
                print()
                temp_list.append(new_amt)
                break
            else:
                print()
                print("Amount must be greater than zero and less than a billion--try again!")
                print()
        else:
            print()
            print("Invalid entry--try again!")
            print()
    
    # Add to master list
    upd_donation_list.append(temp_list)

    print("Donation Has Been Entered.") # This could be try/except
    print()
    print("###")
    print()
    print()
    
    return(new_donor)

def list_donor_donations(all_donations, a_donor):
    """Prints formatted donation details for a specific donor. """
    # Sort based on first element
    # all_donations.sort()
    # Column labels
    header1 = ['Date', '| Donor', '| Amount']

    print("Your Donation History") 
    print()
    # Print header
    print('{:<11} {:<36} {}'.format(*header1))
    print(66 * '-')

    for donor in all_donations:
        if donor[:][3] == a_donor:
            # Add donor name only to new list

            formatted_date = (datetime.date(donor[0], donor[1], donor[2]))
            
            # Print date first with 4 spaces on the end
            print('{}'.format(formatted_date), end = "    ")
            # Print donor name and amount
            print('{:<36} ${:>14,.2f}'.format(donor[3], donor[4]))
    return

def prn_an_email(all_donations, donor_selected):
    """ Prints formatted email template to screen with donation details. """
    # For today's date to be printed in email
    from datetime import date
    
    the_date = str(date.today())

    # Email template for donors
    email_body = ("We are thrilled to have been the recipient of your generosity!\n"
                  "Everyone here at the Foundation for Feline Intestinal Health lept\n"
                  "for joy when I showed them your most recent check.\n"
                  "\n"
                  "You can be confident that FfFIH will make good use of the funds\n"
                  "which you've chosen to share with us--your donations will help\n"
                  "us continue to make Felines all over the World be healthier, happier,\n"
                  "and live longer lives.\n"
                  "\n"
                  "With great thankfulness, we acknowledge the following contribution(s): ")
    print()
    print()
    print(the_date)
    print()
    print()
       
    print("Dear {},\n".format(donor_selected))
   
    print(email_body)
    print()
    
    # List all relevant donations in the email generated
    list_donor_donations(all_donations, donor_selected)

    # Signature block   
    print()
    print("Blessings,\n")
    
    print("Chuck Stevens\n"
          "Director Emeritus\n"
          "Foundation for Feline Intestinal Health")
    print()

def findKey(ttl):
    """ Determines key to sort in AVG list. """
    return ttl[1] # key to sort

def prn_donor_avg(donations):
    """ Prints a list of donors with their donation count and avg donation. """

    # Holds the names of donors
    donor_name_list = []
    # Temp list for loop
    temp_donor_list = []
    # Holds the total number of donations for a donor
    donation_count = []
    
    # Put each instance of a donor name into a list
    # This will allow collection of each donation amount
    for donor in donations:
        temp_donor_list.append(donor[:][3])
        
    # Put Counter output into a name
    # To determine count of each donor's donations 
    donor_name_list = Counter(temp_donor_list)
    
    # Get into a list of tuples
    donation_count = donor_name_list.most_common()
    
    # Sort list of donor tuples
    donation_count.sort()

    # Report header
    print()
    header1 = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    print()
    # Print header
    print('{} {:>37} {:>16} {}'.format(*header1))
    print(83 * '-')

    # This list is used to pull ea. donor's records from data set
    donor_names = []
    # Collect list of unique individual donor names
    for donor in donations:
        if not donor[:][3] in donor_names:
            donor_names.append(donor[:][3])

    usd = "$" # USD!
    # Big list of all AVGs
    master_list = []

    for ea_name in donor_names:
        # Holds new donor and donation so it can be appended to list
        temp_list = []
        # loop through the name field
        for donor in donations:
            if donor[:][3] == ea_name:
                # Append donation amounts found for individual donor to a list
                temp_list.append(donor[:][4])
                # Count or sum of tl individual donations for each donor
                donation_ctr = (len(temp_list))
                # Sum all donor's donations
                donation_ttl = (sum(temp_list))
                # Find the average of the donations
                donation_avg = mean(temp_list)
                # Name used to find donor in tuple
                search = ea_name
                # Temp list holding Total, Num Gifts, AVG
                donor_ttl_avg = []
                
                for sublist in donation_count:
                    if sublist[0] == search:
                        if sublist[1] == donation_ctr:
                            # Sortable list holding Total, Num Gifts, AVG
                            donor_ttl_avg.append(ea_name)
                            donor_ttl_avg.append(donation_ttl)
                            donor_ttl_avg.append(donation_ctr)
                            donor_ttl_avg.append(donation_avg)
                            master_list.append(donor_ttl_avg)
    
    # Sort by second item in sublist
    master_list_sorted = sorted(master_list, key = findKey, reverse = True)
    
    for sublist in master_list_sorted:
        print('{:<36} {:>} {:>14,.2f} {:>3} {:>11} {:>13,.2f}'.format(sublist[0], usd, sublist[1], sublist[2], usd, sublist[3]))

    print()
    print()
        
if __name__ == "__main__":

    main()  


