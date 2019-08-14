# -*- coding: utf-8 -*-
""" This code allows a user to update a dict of donors, print 
donations, average donations, print a thank you email and letters. 
Per requirements, lists were replaced with dicts where possible.
"""

"""
Lesson04 :: Mailroom Part 2 Revised
@author: Chuck Stevens :: CCSt130
Edited Thu Aug 8 20:27:44 2019

"""

import datetime # dates needed for comparison

from collections import Counter # Count of donations

from datetime import date # Need current date for new donations

# Names capturing current date and time
the_date = (date.today())
time_now = datetime.datetime.now() 


def main():
    """ Contains dict of donors and displays Menu. """
    # Dictionary holding donor names, donation dates and amounts
    all_donations = {'Stichting INGKA Foundation': 
                        {'2014-04-14': 40338000, 
                         '2013-07-12': 31837000, 
                         '2017-08-18': 15966000, 
                         '2014-06-27': 19474000},
                    'Buffet Foundation': 
                        {'2014-08-16': 27940000,
                         '2015-04-13': 18603000,
                         '2013-11-21': 15381000,
                         '2015-12-10': 15115000,
                         '2015-08-15': 14534000},
                    'Bezos Family Foundation': 
                        {'2019-02-11': 18938000,
                         '2015-02-06': 19554000}, 
                    'Bill and Melinda Gates Foundation':
                        {'2016-08-16': 14354375,
                         '2018-04-26': 48405000,
                         '2014-02-17': 26340000,
                         '2017-05-19': 23049002,
                         '2016-03-18': 22737329,
                         '2018-08-23': 21455000,
                         '2016-09-20': 20670300},
                    'Walton Family Foundation':
                        {'2016-08-23': 18947775,
                         '2016-03-11': 17914000,
                         '2015-09-18': 17789000,
                         '2015-04-17': 17440000,
                         '2011-06-21': 18254000,
                         '2014-08-16': 16066000,
                         '2017-03-14': 14841309,
                         '2017-05-15': 14391572,
                         '2016-08-20': 14093386}}

    # Main Menu choice
    usr_input = None

    # Display when user selects 4 (or Q) to Quit
    exit_msg = [time_now, "### Program Exit ###"]

    # dictionary holding main menu options
    menu_opt = {'1': 'Send a Thank You', '2': 'Create a Report', '3': 'Print Donor Letters', '4': 'Quit'}

    # This name used for Quit option--main menu error handling
    quit_opt = ["Q", "q", "Quit", "quit", "QUIT", "qUIT"]
    # Main menu choices
    menu_dict = {"1": print_an_email,
                 "2": prn_donor_avg,
                 "3": print_letters,
                 "4": quit_menu
                 }
    # Display menu and receive user input
    while True:
        # Displaying menu header
        print()
        print()
        print(50 * '*')
        print()
        print(18 * '*', "Menu Options", 18 * '*')
        print()
        
        # Display menu options
        print_dict(menu_opt)
         
        print()
        print(50 * '*') # Footer
        
        # Prompt user for input
        input_msg = "Please choose a Menu Option [1,2,3 or 4 to Quit]: "

        # Capture user choice 
        usr_input = str(input(input_msg))
        # Should user select 'Q','q', etc.
        if usr_input in quit_opt:
            quit_menu(exit_msg)
            break
        elif usr_input == '4':
            quit_menu(exit_msg)
            break
        # Error handling
        if not usr_input in menu_dict:
            print()                
            print("Invalid entry--try again!")
            print()
        # Launch a valid option
        else: menu_dict.get(usr_input)(all_donations)


def quit_menu(exit_strings):
    """ End Program. """
    for ex_str in exit_strings:
        print()
        print(ex_str)

    return


def list_donor_names(upd_donation_list):
    """ Makes a list of unique individual donor names from data. """
    # Initialize empty list
    # Holds keys before appending string to list
    temp_list = []
    
    for key in upd_donation_list:
        temp_list.append(key)
        # Convert to numbered list
        num_list = enumerate(temp_list,1)
    
    # Convert enumerated list to tuple and print
    for names in num_list:
        print(f' {names[0]}. {names[1]}')

    return


def donor_sub_menu(all_donations): # updated donation list
    """ Displays 'nested' menu of donors.
        Takes user's choice of donor and returns it.
        Allows user to add a new donation. """
    
    # Error handling if user wants to see list again
    list_opt = ["L", "l", "List", "list", "LIST", "lIST"]

    # Displaying menu header
    print()
    print()
    print(50 * '*')
    print()
    print(18 * '*', "Choose Donor", 18 * '*')
    print()
    print("Our Current Donors:")
    print()
    # Function prints a list of donors (primary keys)
    list_donor_names(all_donations)
    
    while True:
        print()
        print(50 * '*') # Print footer

        # Prompt user for input
        input_msg = "Please type the name of an Organization: "
        # Capture user choice 
        a_donor = str(input(input_msg))
        print()
        # Could put a loop here to allow correction
        print("\nYou entered: {}".format(a_donor))

        # Strip white space for comparison
        input_strip = a_donor.replace(' ', '')

        if a_donor in list_opt:
            # Display list again per reqs
            list_donor_names(all_donations)

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
            print(">>> No Donation Added. <<<")
            return(a_donor)
        elif usr_input == 'Q' or usr_input == 'q': # Outta here
            return
        elif usr_input.isdigit(): 
            print("Invalid entry--try again!") # A for effort
            print()
        else: 
            print("Invalid entry--try again!")
            print()

    # Assign date to a name
    dt_today = (date.today())
    # Necessary to convert to a string
    # Note that 'by design', only one new donation for a new donor can be added per day
    # ...because I've used dates as subkeys
    date_str = str(dt_today)    
    
    # Include donor name already entered
    if a_donor != None:
        print()
        print("A Donation from '{}' will be entered into our list...".format(a_donor))
    # Prompt for donation amount
    while True:
        amt_input = (input("Enter amount of donation without separators (e.g. '12333444'): "))   
        # Check for numeric entry
        if amt_input.isdigit():
            new_amt = float(amt_input)
            # Error handling should unrealistic amts be entered
            if new_amt > 0 and new_amt < 1000000000: # n < billion
                # append to dict
                if a_donor in all_donations:
                    all_donations[a_donor][date_str] = new_amt
                else: # New key - append new donor
                    all_donations[a_donor] = {date_str: new_amt}
                break
            else:
                print()
                print("Amount must be greater than zero and less than a billion--try again!")
                print()
        else: # Non-numeric entry
            print()
            print("Invalid entry--try again!") 
            print()
    # Inform user
    print()
    print(">>> Donation Has Been Entered for {}. <<<".format(a_donor))
    print()
    print("###")
    
    return(a_donor) # Return user's choice


def list_donor_donations(all_donations, a_donor):
    """Prints formatted donation details for a specific donor. """
    # Print header and column labels
    donation_format = {'Heading1': "Your Donation History:\n",
                       'Column1': 'Date', 
                       'Column2': '| Donor', 
                       'Column3': '| Amount'}

    print()
    print(donation_format['Heading1'])
    # Print column labels        
    print('{:<11} {:<36} {}'.format(donation_format['Column1'], donation_format['Column2'], donation_format['Column3']))
    print(66 * '-') # Print footer
    
    # Print donation dates and amounts (subkeys)
    for gift_dt, gift_amt in sorted(all_donations[a_donor].items()):
        print('{:<13} {:<36} ${:>14,.2f}'.format(gift_dt, a_donor, gift_amt))
            
    return


def print_an_email(all_donations):
    """ Prints formatted email template to screen with donation details. """
    # Launch function to determine donor
    a_donor = donor_sub_menu(all_donations)

    # This if statement will return user to main menu 
    # ...if no donation made after entering a new user--line 200
    if a_donor not in all_donations:
        return

    # For today's date to be printed in email
    # Today's date
    the_date = str(date.today())

    print('\n\n')
    print(the_date)
    print('\n\n')
    # Template for email
    donor_email = {'Salutation': "Dear {},\n",
                   'Body': "We are thrilled to have been the recipient of your generosity! \
                   \nThank you for your donations to FfFH and your dedication to Feline Health. \
                   \nYour donations will be put to good use keeping kitties healthy! ",
                   'Sig_block': "\nBlessings,\n\n\n\nChuck Stevens\nDirector Emeritus\nFoundation for Feline Health"}
    # Print salutation and body of email
    print(donor_email['Salutation'].format(a_donor))
    print(donor_email['Body'])
   
    # List all relevant donations in the email generated
    list_donor_donations(all_donations, a_donor)
    
    # Print signature block   
    print(donor_email['Sig_block'])
    
    return


def print_letters(all_donations):
    """ Creates formatted letters with donation details. """
    # For today's date to be printed in email
    # Today's date
    the_date = str(date.today()) 
    
    # Iterate through donations, assign key to name
    for key in all_donations:
        a_donor = key
        # Thank you (TY) letter name format
        test_file = "TY" + "_" + a_donor + "_" + the_date + ".txt"
        # Open a new file for current donor
        # Preferred method
        with open(test_file, "w") as donor_letter:
        # donor_letter = open(test_file, "w")
        # Begin letter
            donor_letter.write('\n')
            donor_letter.write(the_date)
            donor_letter.write('\n\n\n\n')
            # Dict is a template 
            donor_email = {'Salutation': "Dear {},\n\n",
                           'Body': "We are thrilled to have been the recipient of your generosity! \
                           \nThank you for your donations to FfFH and your dedication to Feline Health. \
                           \nYour donations will be put to good use keeping kitties healthy! ",
                           'Sig_block': "\n\nBlessings,\n\n\n\nChuck Stevens\nDirector Emeritus\nFoundation for Feline Health"}
            # Print salutation and Body of letter
            donor_letter.write(donor_email['Salutation'].format(a_donor))
            donor_letter.write(donor_email['Body'])
            # Print header for donations
            donation_format = {'Heading1': "\n\nYour Donation History:\n\n",
                               'Column1': 'Date', 
                               'Column2': '| Donor', 
                               'Column3': '| Amount'}

            donor_letter.write(donation_format['Heading1'])
            # Print column labels 
            donor_letter.write('{:<11} {:<36} {}'.format(donation_format['Column1'], donation_format['Column2'], donation_format['Column3']))
            donor_letter.write('\n')
            donor_letter.write(66 * '-')
            donor_letter.write('\n')
            # List all relevant donations in the letter generated
            # If prn_donor_avg has been run (Menu Opt.2,), additional subkeys will be printed
            # Formatting fix tba
            for gift_dt, gift_amt in sorted(all_donations[a_donor].items()):
                donor_letter.write('{:<13} {:<36} ${:>14,.2f}'.format(gift_dt, a_donor, gift_amt))
                donor_letter.write('\n')

            # Signature block 
            donor_letter.write(donor_email['Sig_block'])
            # Not needed
            # donor_letter.close() # Close file
            print()
            # Informs letter generated
            print("Donor letter has been saved to current directory for: {}!".format(a_donor))

    return


def print_dict(a_dict):
    """ Generic dictionary printer """
    for k, v in a_dict.items():
        print(k,":",v)


def prn_donor_avg(all_donations):
    """ Prints a sorted list from dict of Donor TTL and AVG. """
    # Currency symbol to use
    usd = "$" # USD!
    # new dict which holds AVGs
    # using rather than append to dict all_donations
    avg_donations = {}
    
    # Report header
    print()
    header1 = ["Donor Name", "| Total Given", "| Num Gifts", "| Average Gift"]
    print()
    # Print header
    print('{} {:>37} {:>16} {}'.format(*header1))
    print(83 * '-') # Print footer
            
    for key in all_donations:
        a_donor = key # name for readability
        # Create dict to determine number of donations for current donor
        donation_dict = Counter(all_donations[a_donor].items())
        # Sum counter values and assign to a name
        donation_ct = sum(donation_dict.values())
        # Sum values in subkeys and assign to a name
        donation_ttl = sum(all_donations[a_donor].values())        
        # Calculate average and assign to a name
        donation_avg = (donation_ttl / donation_ct)        
        
        # Populate dict
        if a_donor not in avg_donations:
            # Create new key in empty dict, add subkey and value (counter) to data structure
            avg_donations[a_donor] = {'Donation Count': donation_ct}
        else: # Key extant
            # Add subkey and value (counter) to data structure
            avg_donations[a_donor]['Donation Count'] = donation_ct

        # Add subkey and value (TTL) to data structure
        avg_donations[a_donor]['Total Donations'] = donation_ttl
        # Add subkey and value (AVG) to data structure
        avg_donations[a_donor]['AVG Donation'] = donation_avg

    # Sort dict by 'Total Donations' descending
    lets_sort = sorted(avg_donations.items(), key = lambda x: x[1]['Total Donations'], reverse = True) 
    
    # Change it back to a dict
    avg_donations_sorted = dict(lets_sort)

    # Iterate over sorted dict    
    for key in avg_donations_sorted:
        temp_donor = key # readability
        # Print formatted TTL, Count, AVG
        print('{:<36} {:>} {:>14,.2f} {:>3} {:>11} {:>13,.2f}'.format(temp_donor, usd, avg_donations_sorted[temp_donor]['Total Donations'], \
              avg_donations_sorted[temp_donor]['Donation Count'], usd, avg_donations_sorted[temp_donor]['AVG Donation']))

        
if __name__ == "__main__":

    main()
    
    
    