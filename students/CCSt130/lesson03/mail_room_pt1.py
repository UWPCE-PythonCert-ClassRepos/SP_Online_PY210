# -*- coding: utf-8 -*-
""" This code allows a user to update a list of donors, print
all donations, average donations, and print a thank you email. 
"""

"""
Lesson03 :: Mailroom Part 1
@author: Chuck Stevens :: CCSt130
Created on Sun Jun 16 19:32:15 2019
"""

import datetime # dates needed for comparison

from collections import Counter

from statistics import mean

if __name__ == "__main__":
    
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
        
        usr_input = ""
        
        while True:
            # Displaying menu header
            print()
            print(48 * '*')
            print()
            print(17 * '*', "Menu Options", 17 * '*')
            print()

            # Display menu options
            print(" 1. Create a Report of all Donations")
            # print(" 2. Print Thank You Emails for all Donors") TBA
            print(" 2. Print a List of Donors' Donation Averages")
            print(" 3. Print a List of all Donor Names")
            print(" 4. Print a Thank You Email for a Donor")
            print(" 5. Add a New Donation")
            print()
            print(" Enter 'Q' to Quit")        
            
            print()
            print(48 * '*')
            # Prompt user for input
            input_msg = "Please choose a Menu Option [1-8]: "
            # Capture user choice 
            usr_input = str(input(input_msg))

            # Other functions launch based on menu selection
            if usr_input == '1':
                prn_all_donations(all_donations)
            
            elif usr_input == '2':
                prn_donor_avg(all_donations)

            elif usr_input == '3':
                list_donor_names(all_donations)

            elif usr_input == '4':
                # add_new_donation()
                # print()
                donor_choice = donor_sub_menu(all_donations)
                # Organized in this fashion so hypothetical user
                # ...could email existing donor for a new donation
                add_new_donor(all_donations, donor_choice)
                prn_an_email(all_donations, donor_choice)

            elif usr_input == '5':
                a_new_donor = new_donor_input()
                all_donations = add_new_donor(all_donations, a_new_donor)
                # print()

            elif usr_input == 'Q' or usr_input == 'q':
                break

            else: 
                print()
                print("Invalid entry--try again!")
                print()

        print()
        print("### Program Exit ###")

def new_donor_input():
    """ Takes user's choice of donor and returns it. """
    while True:
        # Prompt user for input
        input_msg = "Please type the name of an Organization: "
        # Capture user choice 
        usr_input = str(input(input_msg))
        print()
        # Could put a loop here to allow correction
        print("You entered: {}".format(usr_input))

        # Strip white space for comparison
        input_strip = usr_input.replace(' ', '')

        # Filter out non-alpha entry            
        if input_strip.isalpha():
            break 
        else:
            print()                
            print("Invalid entry--try again!")
            print()

    return(usr_input)

def donor_sub_menu(upd_donation_list): # updated donation list
        """ Displays 'nested' menu of donors. """
        while True:
            # Displaying menu header
            print()
            print()
            print(48 * '*')
            print()
            print(17 * '*', "Choose Donor", 17 * '*')

            list_donor_names(upd_donation_list)
            
            # print()
            # print("Enter 'Q' to Quit Sub-Menu")        
            print()
            print(48 * '*')

            # Launch function to capture user choice 
            new_donor = new_donor_input()

            print()
            return(new_donor)

def prn_all_donations(donations):
    """ Prints formatted donation details for all donors. """

    # Sort based on first element
    donations.sort()
    # Find length of list
    donor_len = len(donations)
    # Column labels
    header1 = ['Date', 'Donor', 'Amount']

    print()
    print("Donation History:") 
    print()
    # Print header
    print('{:<13} {:<36} {}'.format(*header1))
    print(65 * '-')
   
    d = 0 # While loop counter and index
    
    # Print formatted list of each donation date, donor, amount of donation
    while(d < donor_len):    
        # Seems best to pass formatted date to a new name
        # pull this out into a function
        formatted_date = (datetime.date(donations[d][0], donations[d][1], donations[d][2]))
        # For an array, especially a 2D array, the .format syntax seems easier to implement        
        # Print date first with 4 spaces on the end
        print('{}'.format(formatted_date), end = "    ")
        # Print donor name and amount
        print('{:<36} ${:>13,.2f}'.format(donations[d][3], donations[d][4]))
    
        d+=1 # Increment counter

    print()        

def list_donor_donations(all_donations, a_donor):
    """ Prints formatted donation details for a specific donor. """
    # Sort based on first element
    all_donations.sort()
    
    # This could be its own function
    # Column labels
    header1 = ['Date', 'Donor', 'Amount']

    print("Your Donation History") 
    print()
    # Print header
    print('{:<13} {:<36} {}'.format(*header1))
    print(65 * '-')

    for donor in all_donations:
        if(donor[:][3] == a_donor):
            # Add donor name only to new list

            formatted_date = (datetime.date(donor[0], donor[1], donor[2]))
            
            # Print date first with 4 spaces on the end
            print('{}'.format(formatted_date), end = "    ")
            # Print donor name and amount
            print('{:<36} ${:>13,.2f}'.format(donor[3], donor[4]))

    return

# Email print with only contributions from Donor X
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
       
    print("Dear {},\n".format(donor_selected))
    # print("Dear Sir or Madam:")
    
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

def add_new_donor(donation_list, new_donor):
    """ Allows user to add a new donation. """
    
    # Need current date for comparison
    from datetime import date
    the_date = (date.today())

    # Test
    # temp_list = [[2017,7,7,"Fastbuck Corporation",55000]]
    temp_list = []
    # print("Donor name was not found. ", end = "")
    print()
    print("Would you like to enter a new Donation? Y/N")

    while True:
        input_msg = "Please choose 'Y' for Yes and 'N' for No. [Y/N]: "
        # Capture user choice 
        usr_input = str(input(input_msg))
        
        if(usr_input == 'Y' or usr_input == 'y'): # Why, yes!
            break
        elif(usr_input == 'N' or usr_input == 'n'): # Well, no.
            print()
            print("No Donation Added.")
            return
        elif(usr_input == 'Q' or usr_input == 'q'): # Outta here
            return
        elif usr_input.isdigit(): 
            print("Invalid entry--try again!") # A for effort
            print()
        else: 
            print("Invalid entry--try again!")
            print()

    # Note: I suspect there is a more efficent way to check and enter dates into a list of lists
    # YYYY, MM, DD broken up to avoid errors with separators, etc.
    while True:
        print()
        year_input = input("Enter Year of donation YYYY: ")
        # print ()
        if year_input.isdigit():
            # Cast to int
            new_year = int(year_input)

            # Set boundaries for year
            future_date = the_date.year+1
            past_date = the_date.year-1

            if(past_date <= new_year <= future_date): # <= current year
                 # Add to list
                temp_list.append(new_year)
                break
            else:
                print()
                print("Year is out of range--try again!")
                print()
        else:
            print("Invalid entry--try again!")
            print()
    
    while True:
        mth_input = input("Enter Month of donation MM [1-12]: ")      
        # print()
        if mth_input.isdigit():
            new_mth = int(mth_input)
            # Only nesting worked here
            if(new_mth > 0 and new_mth <= 12): # Let's try to get legit int
                temp_list.append(new_mth)
                break
            else:
                print()
                print("There are 12 months in a year--try again!")
                print()            
        else:
            print()
            print("Invalid entry--try again!")
            print()

    while True:
        day_input = (input("Enter Day of donation DD [1-31]: "))    
        #print()
        if day_input.isdigit():
            new_day = int(day_input)
            # This doesn't account for February
            if (new_day > 0  and new_day <= 31): # Only valid input
                # add to list
                temp_list.append(new_day)
                break
            else:
                print()
                print("No less than 1 and no more than 31 days in a month--try again!")
                print()
        else:
            print()
            print("Invalid entry--try again!")
            print()

    # Include donor name already entered
    if(new_donor != ""):
        print()
        print("A Donation from '{}' will be entered into our list...".format(new_donor)) # Add date
        # print()
        temp_list.append(new_donor)

    while True:
        amt_input = (input("Enter amount of donation without separators (e.g. '12333444'): "))   
        # print()
        if amt_input.isdigit():
            new_amt = float(amt_input)
            if(new_amt > 0 and new_amt < 1000000000): # n < billion
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
    donation_list.append(temp_list)
    
    # Test
    # print(all_donations)
    print("Donation Has Been Entered.") # This could be try/except
    print()
    print("###")
    print()
    print()
    
    return(donation_list)

def prn_donor_avg(donations):
    """ Prints a list of donors with their donation count and avg donation. """
    # Hold list of donor names
    donor_names = []
    # Collect list of unique individual donor names
    for donor in donations:
        if not donor[:][3] in donor_names:
            #donor[:][3] = temp_donor 
            donor_names.append(donor[:][3])
    
    donor_name_list = []

    temp_donor_list = []
    
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

    print()
    header2 = ['Donor', 'CT', 'TTL Given', 'AVG Gift']
    print()
    # Print header
    print('{:<34} {:<3} {:<16} {}'.format(*header2))
    print(70 * '-')

    for ea_name in donor_names:

        temp_list = []

        for donor in donations:
            if donor[:][3] == ea_name:
                # Append donation amounts found for individual donor to a list
                temp_list.append(donor[:][4])
                # Count or sum of tl individual donations for each donor
                donation_ctr = (len(temp_list))

                donation_ttl = (sum(temp_list))
                
                # Find the average of the donations
                donation_avg = mean(temp_list)

                search = ea_name
                
                for sublist in donation_count:
                    if sublist[0] == search:
                        if((sublist[1]) == (donation_ctr)):
                            # Replace below with formatted string
                            """
                            print("Result: ", end = "")
                            print(ea_name, end = " ")
                            print(donation_count, end = " ")
                            print(donation_avg)
                            """
                            # Print formatted string of donations
                            print('{:<34} {:>2}  ${:>14,.2f}  ${:>13,.2f}'.format(ea_name, donation_ctr, donation_ttl, donation_avg))
    print()

def list_donor_names(all_donations):
    """ Collects a list of unique individual donor names. """
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
           
    print()
    # Return tuple
    return(donor_list)

main()  


