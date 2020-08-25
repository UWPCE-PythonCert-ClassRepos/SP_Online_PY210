#!/usr/bin/env python """
import sys
"""Mailroom"""

# Prompt user to choose from menu of 3 actions:
# Send a Thank You, Create a Report or quit.


def present_menu():
    print()
    print("************MAIN MENU**************")
    print("**                               **")
    print("**     Please Select: T or R     **")
    print("**                               **")
    print("***********************************")
    print()

    choice = input("""
                      T: Send a Thank You
                      R: Create a Report
                      Q: Quit

                      Please enter your choice: """)

    print(choice)
    if choice.lower() == "t":
        send_thank_you()
    elif choice.lower() == "r":
        create_report()
    elif choice.lower() == choice == "q":
        sys.exit
    else:
        print("You must only select either T or R.")
        print("Please try again")
        present_menu()


def check_name(search_value):
    if search_value in donor_name_list:
        return True


def prompt_for_name():
    input_name = input("""Please enter Full name or 'list' to see names: """)

    if (input_name == ""):
        return prompt_for_name()
    elif input_name.lower() == 'list':
        list_names()
        return prompt_for_name()
    else:
        return input_name.title()
   

def prompt_for_amount():
    inputAmount = input("""Please enter Amount greater than 0: """)

    if int(inputAmount) >= 0:
        return inputAmount
    else:
        prompt_for_amount()


def check_name(in_name):
    if in_name == None:
        print("in_name is none")
        # why is it returning none if entering blank name and then fixing belarson
        exit()

    if in_name.lower() == 'list':
        print("3a list entered")
    else:
        # check if name is in list
        name_found = check_name(in_name.title())
        if name_found:
            print(in_name)
        else:
            # Add the name
            donor_name_list.append(in_name.title())
    return in_name


def write_email(name):
    print('write_email to ')
    print({name})

# Send a Thank You
# prompt for a Full Name.
# If user types list, show a list of donor names & re-prompt.
# If user types a name not in list, add name to data structure & use it.
# If user types a name in list, use it.
# Once a name has been selected, prompt for a donation amount.
# Convert amount into number; it is OK to crash if someone types bogus amount.
# Add that amount to donation history of selected user.
# use string formatting to compose email thanking donor for generous donation.
#     Print email to terminal and return to original prompt.
# Ok for now for program not to store names of new donors that had been added


def send_thank_you():
    print("** send_thank_you    **")

    returned_name = prompt_for_name()
    print(returned_name)
    return  # belarson -- left off here

    '''
    if returned_name.lower() == 'list':
        list_names()
        return
    else:
        final_name = check_name(returned_name)
        return
        print(f"Name for Thank you is {final_name}.")
        inputAmount = prompt_for_amount()
        print(f"Amount Input is {inputAmount}.")
        write_email(final_name)  # belarson update to send all values
    '''


def list_names():
    print()
    print("************LIST MENU**************")
    print("**                               **")
    print("**    Names Currently in List    **")
    print("**                               **")
    print("***********************************")
    print()

    for id, info in donor_name_list2.items():
        print(info.get('name'))


def create_report():
    print("** create_report  **")


def get_names_recursively(search_dict, field):
    """Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []

    for key, value in search_dict.items():
        if key == field:
            fields_found.append((value))
        elif isinstance(value, dict):
            results = get_names_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_names_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found

# data structure to hold list of donors & history of amounts donated
# populated with at least five donors, with between 1 & 3 donations each
# store that data structure in the global namespace ?belarson


donors = {
    1: {"name": "Ann", "year": 2004, "amount": 100},
    2: {"name": "Bob", "year": 2007, "amount": 100},
    3: {"name": "Charlie", "year": 2011, "amount": 100}
}

donor_name_list2 = {
    1: {
        'name': 'Lisa',
        'year': '2012',
        'amount': 100
        },
    2: {
        'name': 'Steve',
        'year': '2005',
        'amount': 134.02
        }
    }

for donor_name in donors.values():
    donor_name_list.append(donor_name['name'])
print(donor_name_list)
print(donor_name_list2)

present_menu()

# print(check_name("Bob"))

# https://www.learnbyexample.org/python-nested-dictionary/
'''Employee = {
    'emp1': {
        'name': 'Lisa',
        'age': '29',
        'Designation': 'Programmer'
        },
    'emp2': {
        'name': 'Steve',
        'age': '25',
        'Designation': 'HR'
        }
    }

Employee['emp1']['name'] = 'Kate'
'''
# print(Employee)

# iterate over 
#    for id, info in donor_name_list2.items():
#        print("\n ID:", id)
#        for key in info:
#            print(key + ':', info[key])
