#!/usr/bin/env python

"""
The Mailroom assignment, command line interface.

Added options to save data and load data.

The remaining features follow the assignment instructions, with recommendations on erroneous user input.
"""

import io
import ast
from sys import exit

from donor_models import Donor as D
from donor_models import DonorCollection as DC

# This was originally a list of lists.  I changed it based on the recommendation in the notes.
donor_set = DC(**{'Bob': [17.56], 'Billy': [500.00, 1000.00], 'Joe Schmoe': [2.00, 0.03, 45.00],
        'This Guy': [1.00, 100000], 'That Gal': [9876.54]})

prompt = """\nPlease choose between the following option numbers:
(enter the digit only)
'1' - Send a Thank You
'2' - Create a Report
'3' - Send letters to all donors
'4' - Save data
'5' - Load data
'6' - Quit
: """


# This was originally a single function called 'Part1()' which called another function to add
# donations.  It worked, but I restructured it based on the recommendation in the notes.
def main():
    """Prompot the user for an option, which will be handled by the  switch dict."""
    while True:
        answer = input(prompt)
        try:
            Switch_dict.get(int(answer))(donor_set)
        # These could have been handled with a catch-all exception, resulting in a message...
        # ...to use the correct input, but I opted for error-specific exceptions in...
        # ...accordance with the lesson material.
        except TypeError:
            print("\n Integer input was not '1', '2', '3', '4', '5', or '6'. Please use only one of these.")
        except ValueError:
            if answer.isalpha():
                print("\n Input was an alphabet character(s). Please use only '1', '2', '3', '4', '5', or '6'.")
            else:
                try:
                    float(answer)
                    print("\n Input was a float. Please use only '1', '2', '3', or '4', '5', or '6'.")
                except ValueError:
                    print("\n Input was a mixed string. Please use only '1', '2', '3', or '4', '5', or '6'.")


def send_single(donor_set):
    """Prompt the user for a donor name, which will call a helper function to process donations.
    
    Print the letter after the processing the donor and donations."""
    outer_loop = True
    while outer_loop == True:
        input_name = input("""\nPlease provide a full name (case sensitive).
    'list will show the list of donor names.
    'quit' exits script.
    : """)
        if input_name == 'list':
            print('\n')
            for name in donor_set.names:
                print(name)
        elif input_name == 'quit':
            quit_program(donor_set)
        elif input_name not in donor_set.names:
            inner_loop = True
            while inner_loop == True:  # added logic for verifying name input here
                ans_name_check = input("""Donor not found
                    If all characters and spaces are correct, type 'yes'
                    If not all characters and spaces are correct, type 'no'
                    : """)
                if ans_name_check == 'yes':
                    donor_set.add_donor(input_name)
                    inner_loop = False
                    outer_loop = False
                elif ans_name_check == 'no':
                    inner_loop = False
                else:
                    print ("Please enter 'yes' or 'no'")
        else:
            outer_loop = False
    donor_set, donations = read_donations(input_name, donor_set)
    if donations != []:
        print(donor_set.data[input_name].compose_letter)
    else:
        print('\nzero donation input, no donation counted')
    return donor_set
            
            
def read_donations(input_name, donor_set):
    """Helper function to process donation data."""
    donation_input = ''
    donations = []
    while donation_input != 'none':
        donation_input = input("""\nPlease provide the donation amount in ssv format
***(enter 'none' for no additional donation, 'quit' to exit script): """)
        if donation_input == 'quit':
            quit_program(donor_set)
        if donation_input != 'none':
            donation_struct = donation_input.split()
            try:
                for val in donation_struct:
                    if val != '0':
                        donations.append(float(val))
            except ValueError:
                donation = []
                print('\ninput was not a number, all characters discarded')
            else:
                donor_set.data[input_name].add_donations(donations)
                break
    return donor_set, donations


def create_a_report(donor_set):
    """Ingest data from the new structure, and print a report."""
    report_data, key1, key2, key3, key4 = donor_set.new_structure
    print("\n\n {:^28}|{:^18s}|{:^7s}|{:^18s}".format(key1, key3, key2, key4))
    print("-" * 75)
    for row in report_data:
        print(" {:28s}|{:17,.2f} |{:6d} |{:>18,.2f}".format(row[key1], row[key3], row[key2], row[key4]))


def send_all(donor_set):
    """Prompt the user for a letter directory, and write a letter per user, based on the new structure."""
    report_data = donor_set.new_structure[0]
    dst_dir = input(r"Please enter destination directory for the letter files (include closing '\' or '/'): ")
    for donor in report_data:
        letter_path = dst_dir + donor['Donor Name'] + '.txt'
        letter_text = donor_set.data[donor['Donor Name']].mass_letter
        with open(letter_path, 'w') as letter:
                letter.write(letter_text)
    return letter_text
    
    
def save_data(donor_set):
    """Save the current data to a text file."""
    save_structure = {value.name: value.donations for value in donor_set.data.values()}
    dst_dir = input(r"Please enter a destination director for the data file (include closing '\' or '/'): ")
    file_name = input(r"Please enter a filename with no extension: ")
    file_path = dst_dir + file_name + '.txt'
    with open(file_path, 'w') as file:
        file.write(str(save_structure))
        

def load_data(donor_set):
    """Load existing data from a text file."""
    while True:
        src_dir = input(r"Please enter destination directory for the data file (include closing '\' or '/'): ")
        file_name = input(r"Please enter a filename with no extension: ")
        file_path = src_dir + file_name + '.txt'
        try:
            with open(file_path, 'r') as file:
                start_data = ast.literal_eval(file.read())
                donor_set.__init__(**start_data)
            break
        except FileNotFoundError:
            print('\n Path not found.  Pleaes enter a valid directory and filename.')
    return donor_set


def quit_program(data):
    """Exit the program using the function from sys."""
    print('\n\ngoodbye\n\n')
    exit()


Switch_dict = {1: send_single, 2: create_a_report, 3: send_all, 4: save_data, 5: load_data, 6: quit_program}

if __name__ == "__main__":
    main()
