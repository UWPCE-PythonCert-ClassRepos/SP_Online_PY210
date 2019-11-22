#!/usr/bin/env python3
import os
import sys
import time

#  Mailroom (Part 4) - cleaned up with PEP 8
donors_dictionary = {'Jonny Gill' : [3.00, 15.00, 25.12],
    'Bobby Brown' : [11.75, 45.01], 'Michael Bivins' : [345.99],
    'Ricky Bell' : [232.33, 35.03, 123.78], 'Ronnie DeVoe' : [456.00, 789.00]}


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
        time.sleep(0.2)
    print('*'*25)
    print()
    main_menu_function()
    return key


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
            cleaned_donations = " ".join(str(found_donor_donations))
        except TypeError as the_error:
            print(the_error)
        exact_selection_func(selection)
        selection = selection.replace(" ", "") # Cleaning up the output
    else:
        #  Add new donor to donor dictionary
        donor_not_in_dict_func(selection)
    return


def donor_not_in_dict_func(selection):
    """
    Add new donor to donor dictionary.
    """
    if selection not in donors_dictionary.keys():
        print(f"\nDonor \'{selection}\' Not Found - Adding to Donors")
        #  Adding new donor to the dictionary
        donors_dictionary[selection] = selection
        try:
            donation = float(input('\nEnter donation amount: '))
        except ValueError as the_error:
            print(f"Error: {the_error}")
            print("Donor not added to database: Please try again.")
        #  Adding donation for new user
        donors_dictionary[selection] = [donation]
        print(f"\nThank you {selection} for your donation of ${donation}.")
        main_menu_function()
    else:
        main_menu_function()
    return


def thank_you_note_func(): #  Need help with aligning text when written to disk
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
    letter_confirmation_func()
    return


def letter_confirmation_func():
    """
    Return a confirmation message and file path.
    """
    #  Gives user feedback on file creation and file location
    number_of_donors = (len(donors_dictionary.items()))
    print(f"\n{number_of_donors} - Thank You Letters Generated...")
    print(f"\nSaved Location: {os.getcwd()}")
    main_menu_function()
    return


def exit_func():
    """
    Return exit program action.
    """
    print('Exiting Program!')
    time.sleep(0.5)
    sys.exit()
    raise SystemExit(code)
    return


def report_func():
    """
    Return donors and donation data.
    """
    global comprehensive_donors_list
    print('-'*58)
    #  List to hold all donor data extracted from dictionary
    comprehensive_donors_list = []
    #  Extract specific donors from dictionary
    for selection, value in sorted (donors_dictionary.items()):
        specific_donor_list = []
        total_donations_given = len(value) #  Total num of donor donations
        values_list = []
        values_list = list(map(float, value))  # Map used for change to float
        donation_total = sum(values_list)
        avg_donation = round(donation_total / total_donations_given, 2)
        avg_donation = (f"{avg_donation:.2f}") #  Second decimal place
        donation_total = (f"{donation_total:.2f}") #  Second decimal place
        #  Adding all values to sub list
        donor_sub_list_values = [selection, donation_total,
                                 total_donations_given, avg_donation
                                ]

        for item in donor_sub_list_values:
            specific_donor_list.append(item) #  Adding item to donor's list
            #if item in specific_donor_list:
            #    pass
            #else:

            #  Nesting sub list into comprehensive donors list
        comprehensive_donors_list.append(specific_donor_list)
    print_report()
    main_menu_function()
    return


def print_report():
    """
    Return formatted report
    """
    #  Formats and prints out data from donor's list
    template = "{0:<15} | {1:^10} | {2:>10} | {3:>13}"
    print(template.format("Donor Name", "Total Given", "Num Gifts",  "Average Gift"))
    print('_'*58)
    for args in sorted(comprehensive_donors_list,
                        reverse=True, key=lambda x: float(x[3])):
                        print(template.format(*args))
    print('-'*58)
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


def main_menu_function():
    """
    Return Main Menu
    """
    print ("""
    **************************************
    *  Main Menu - Please Enter a Number *
    **************************************
            0. Create A Report
            1. List All Donors
            2. Search Database
            3. Create Thank You Letter
            4. Restart Program
            5. Exit Program
    **************************************
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
    switch_main_menu_dict.get(answer, main_menu_function)()
    return answer
    assert answer == 1

#  Using switch case for main menu prompt
switch_main_menu_dict={
    0: report_func,
    1: list_donors_func,
    2: donor_in_dict_func,
    3: thank_you_note_func,
    4: execute_again_func,
    5: exit_func
}

#  Using switch case for run again prompt
switch_execute_again_dict={
    0: main_menu_function,
    1: exit_func
}
main_menu_function()


if __name__ == "__main__":
    main_menu_function()
