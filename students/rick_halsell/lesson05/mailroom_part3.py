#!/usr/bin/env python3
import os
import sys
import operator
import time
from operator import itemgetter

#  Mailroom (Part 3) - cleaned up with PEP 8
donors_dictionary = {'Jonny Gill' : [3.00, 15.00, 25.12],
    'Bobby Brown' : [11.75, 45.01], 'Michael Bivins' : [345.99],
    'Ricky Bell' : [232.33, 35.03, 123.78], 'Ronnie DeVoe' : [456.00, 789.00]}

def list_donors_full_func():
        """
        Return the donors and their donations from the
        donors_dictionary database.
        """
        print('\n***** Printing Donors and Donations *****')
        for key, value in donors_dictionary.items():
            print(key, '->', value)
            print()
        entry_function() #  Back to main menu after processing.
        return



def exact_selection_func(selection):
        """
        Return the selected donor's keys and values from donor dictionary.
        """
        print(selection, (donors_dictionary[selection]))
        print()
        donation = float(input('Enter new donation amount: '))
        #  Add new donation to the donor's dictionary value
        donors_dictionary[selection].append(donation)
        print(selection, (donors_dictionary[selection]))
        return


def list_donors_func():
        """
        Return all donors in the donors dictionary database.
        """
        print('\n***** Printing Donors *****')
        for key in donors_dictionary.keys():
            print(key)
            time.sleep(0.5)
        print('*'*25)
        print()
        database_func()
        return


def donor_in_dict_func():
        """
        Return an existing donor in the database
        and add a new donation amount.
        """
        global selection
        selection = input('Search For Donor -> Enter Name: ')
        if selection in donors_dictionary.keys():
            #  Assign to string if donor in dictionary
            found_donor_donations = donors_dictionary.get(selection)
            try:
                #  Join to clean up the output
                cleaned_donations = " ".join(found_donor_donations)
            except TypeError as the_error:
                print(the_error)
            exact_selection_func(selection)
            selection = selection.replace(" ", "") # Cleaning up the output
            database_func() #  Sends user to database menu
        else:
            #  All new donor to be added to dictionary
            donor_not_in_dict_func(selection)
        return


def donor_not_in_dict_func(selection):
        """
        Return new donor addition to donor dictionary.
        """
        if selection not in donors_dictionary.keys():
            print(f"\nDonor Name \'{selection}\' Not Found -- \
                  Adding to List of Donors")
            #  Adding new donor to the dictionary
            donors_dictionary[selection] = selection
            donation = float(input('\nEnter donation amount: '))
            #  Adding donation for new user
            donors_dictionary[selection] = [donation]
            database_func()
        else:
            database_func()
        return


def thank_you_note_func(): #  Need teacher help with aligning text when written to disk
        """
        Return individual thank you note and write it do the disk.
        """
        global thank_you_output_file
        for key, value in donors_dictionary.items():
            #  Cleaning up donation amounts from dictionary
            cleaned_value = ", ".join(map(str, value))
            #  Gives the total num of donations for donor
            total_donations_given = len(value)
            donation_total = sum(value) #  Sums of all donations
            donation_total = float(donation_total)
            #  Limiting float to second decimal place
            donation_total = (f"{donation_total:.2f}")
            #  Formatting letter
            left_aligned_to_line = (f"Dear {key}")
            mid_left_aligned_body = (f"\n\nThank you for your very kind \
                                     donation of ${donation_total}.")
            mid_right_aligned = (f"\n\nIt will be put to very good use.")
            right_aligned_ending = (f"\n\nSincerely, \n-The Team")

            #  Specific donor file to write all thank you letters
            thank_you_output_file = (f"{key}_Thank_You_Letter.txt")
            with open(thank_you_output_file, 'w+') as thank_you_output_data:
                #  Wites letter to files
                thank_you_output_data.write(f"{left_aligned_to_line:<15}, \
                                            {mid_left_aligned_body:^20} \
                                            {mid_right_aligned:>10} \
                                            {right_aligned_ending:>10}")

        #  Gives user feedback on file creation and file location
        number_of_donors = (len(donors_dictionary.items()))
        print(f"\n{number_of_donors} - Thank You Letters Generated...")
        print(f"Thank You Letters Location: {os.getcwd()}")
        database_func()
        return


def full_name_func_default():
        """
        Return user to main menu if switch case entry is not listed.
        """
        entry_function()
        return


def database_func():
        """
        Return Database menu options.
        """
        global selection
        print ("""
        *********************************
        *   Please Enter a Number       *
        *********************************
        0. Return to the Main Menu
        1. To see a full list of donors
        2. Search donor database
        3. Send letters to all donors
        *********************************
        """)
        selection = input('Enter Your Selection: ')
        try:
            #  Variable int needed for dictionary .get.
            selection = int(selection)
        except ValueError:
            print(f"{selection} is not a vaild selection.")
            print("Please select a number from the menu.")
            time.sleep(1.5)
        #  Switch case function dictionary
        full_name_func = {
                0 : entry_function,
                1 : list_donors_func,
                2 : donor_in_dict_func,
                3 : thank_you_note_func
        }
        #  Switch case dictionary with error handle default function
        full_name_func.get(selection, database_func)()
        return


def exit_func():
        """
        Return exit program action.
        """
        print('Exiting Program!')
        time.sleep(0.5)
        sys.exit()
        return


def report_func():
        """
        Return a comprehensive report of donors and donations.
        """
        #  Assigns variables for easy formatting
        left_aligned = "Donor Name"
        center = "Total Given"
        mid_right_aligned = "Num Gifts"
        right_aligned = "Average Gift"
        #  Formatting and printing report header
        print(f"{left_aligned:<15} | {center:^10} | {mid_right_aligned:>10} \
                 | {right_aligned:>13}")
        print('-'*58)
        #  List to hold all donor data extracted from dictionary
        comprehensive_donors_list = []

        #  Extract specific donors from dictionary
        for selection, value in sorted (donors_dictionary.items()):
            specific_donor_list = []
            total_donations_given = len(value) #  Total num of donor donations
            donation_total = sum(value) #  Total sum of all donations
            donation_total = float(donation_total)
            #  Round donation_total to second decimal place
            avg_donation =  round(donation_total / total_donations_given, 2)
            avg_donation = (f"{avg_donation:.2f}") #  Second decimal place
            donation_total = (f"{donation_total:.2f}") #  Second decimal place
             #  Adding all values to sub list
            donor_sub_list_values = [selection, donation_total,
                                     total_donations_given, avg_donation
                                    ]

            for item in donor_sub_list_values:
                specific_donor_list.append(item) #  Adding item to donor's list
                #  Nesting sub list into comprehensive donors list
            comprehensive_donors_list.append(specific_donor_list)

        donor_list_index = 0 #  Initializing donor_list_index at 0
        #  Determining the number of items in list minus 1 to start at 0
        donor_list_index = len(comprehensive_donors_list) - 1
        #  Using lamda to sort list by list index position [3]
        #  position [3] is the total donation amount
        for thing in sorted(comprehensive_donors_list,
                            reverse=True, key=lambda x: float(x[3])):
            #  Extracts donor name from [donor_list_index][0]
            selection = comprehensive_donors_list[donor_list_index][0]
            #  Extracts donor total from [donor_list_index][1]
            donation_total = comprehensive_donors_list[donor_list_index][1]
            #  Extracts donor total from [donor_list_index][2]
            total_donations_given = comprehensive_donors_list[donor_list_index][2]
            #  Extracts average donation from [donor_list_index][3]
            avg_donation = comprehensive_donors_list[donor_list_index][3]
            donor_list_index -= 1 #  Moves to next donor index
            print(*thing, sep=" ") #  Printing out values (Need Formatting Help Here).
        print('-'*58)
        entry_function()
        return


def execute_again_func():
        """
        Return menu to restart or exit program.
        """
        print ("""
        **************************
        *  Execute Script Again? *
        **************************
        0. Execute Again
        1. Exit Program
        **************************
        """)
        run_again = input('Input: ')
        #  Handle non numerical ValueError entries
        try:
            #  Variable int needed for dictionary .get.
            answer = int(run_again)
        except ValueError:
            print(f"{answer} is not a vaild selection")
            print("Please select a number from the menu.")
            time.sleep(2)

        #  Switch case dict .get with error handle default
        switch_execute_again_dict.get(answer    , execute_again_func)()
        return

def entry_function():
        """
        Return Main Menu
        """
        print ("""
        ******* Main Menu ********
        *  Please Enter a Number *
        **************************
        1. Database Menu
        2. Create a Report
        3. Restart Program
        4. Exit Program
        **************************
        """)
        answer = input('Enter a number: ')
        #  Handle non numerical ValueError entries
        try:
            #  Variable int needed for dictionary .get.
            answer = int(answer)
        except ValueError:
            print(f"{answer} is not a vaild selection")
            print("Please select a number from the menu.")
            time.sleep(2)
        print()
        print(f"You Entered: {answer}")
        print()
        #  Switch case dict .get with error handle default
        switch_main_menu_dict.get(answer, full_name_func_default)()
        return answer


#  Using switch case for main menu prompt
switch_main_menu_dict={
    0: entry_function,
    1: database_func,
    2: report_func,
    3: execute_again_func,
    4: exit_func
}

#  Using switch case for run again prompt
switch_execute_again_dict={
    0: entry_function,
    1: exit_func
}


if __name__ == "__main__":
    entry_function()
