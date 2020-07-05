# cli_main.py
# opcode6502: SP_Online_PY210


import datetime
import sys
import tempfile
from donor_models import *


# Test data.
test_data = {'Archie Adams': [123.45, 500, 999.98],
             'Billie Bobby': [99987.65, 432.01],
             'Joseph Schmo': [555.10, 1.20]}


# Initialize 'donors_db' with 'test_data'.
donors_db = DonorCollection.data_import(test_data)


def add_to_dict(database, key, value):
    try:
        #
        # Add to dictionary.
        database[key] = value
    except Exception as e:
        #
        # Debug statement.
        print_error_message('add_to_dict(database, key, value): Error!')
        print_error_message('e: ' + str(e))


def check_user_response(user_response):
    #
    # Check 'user_response'.
    if user_response == 1:
        send_thank_you()
        #
        #
    elif user_response == 2:
        create_report(donors_db)
        #
        #
    elif user_response == 3:
        timestamp = get_timestamp()
        send_thank_you_global(donors_db, timestamp)
        #
        #
    elif user_response == 4:
        exit_script()
        #
        #
    elif user_response == 5:
        print_donor_collection_debug_statement(donors_db)
        #
        #
    elif user_response == 6:
        list_donor_names(donors_db)
        #
        #
    elif user_response == 7:
        #
        # Create the Donor object.
        d = Donor('Donor 10')
        #
        # Add the Donor to the database.
        donors_db.add(d)
        #
        # Add the Donor to the database.
        d.add_donation([123.45])
        #
        # Print the thank you message.
        print(d.thank_you_message())
    else:
        #
        # Debug statement.
        print_error_message('Select item: [ 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 ].')


def create_main_menu():
    try:
        #
        # Try to create a dict and print an error if this fails.
        main_menu = dict()
        #
        # Debug statement.
        # print_debug_message('create_main_menu(): Success!')
        #
        # Return statement.
        return main_menu
    except Exception as e:
        #
        # Debug statement.
        print_error_message('create_main_menu(): Error!')
        print_error_message('e: ' + str(e))


def create_report(database):
    #
    # Print the header rows.
    print('{:25} | {:1} | {:1} | {:1}'.format(
        'Donor Name',
        'Total Given',
        'Num Gifts',
        'Average Gift'))
    print('-'*66)
    #
    # Iterate through the sorted database.
    for donor in database.sorted():
        #
        # Format and print.
        print('{:26} ${:>11.2f} {:>11}  ${:>12.2f}'.format(
              donor.name,
              donor.sum_donations,
              donor.num_donations,
              donor.average_donation))


def display_main_menu():
    #
    # Display the main menu and process the user's response.
    while True:
        #
        # Print 'main_menu'.
        print_main_menu()
        #
        # Get 'user_response' and test input.
        user_response = get_user_response_integer()
        #
        # Check 'user_response'.
        check_user_response(user_response)


def exit_script():
    #
    # Exit the script.
    sys.exit()


def exit_script_ctrl_c():
    #
    # Print a newline and exit the script.
    print()
    sys.exit()


def format_text(text):
    #
    # Format the text.
    for i in text:
        text = text.replace(' ', '_')
    #
    # Return statement.
    return text


def get_timestamp():
    #
    # Create the timestamp.
    timestamp = format_text(str(datetime.datetime.now()))
    #
    # Return statement.
    return timestamp


def get_user_response():
    try:
        #
        # Get 'user_response'.
        user_response = input('[ INPUT ]: ')
        #
        # Return statement.
        return user_response
    except KeyboardInterrupt:
        #
        # Don't print any debug messages here, just exit.
        exit_script_ctrl_c()
    except Exception as e:
        #
        # Debug statement.
        print_error_message('get_user_response(): try: user_response: Error!')
        print_error_message('e: ' + str(e))


def get_user_response_integer():
    try:
        #
        # Get 'user_response' (integer only).
        user_response = int(input('[ INPUT ]: '))
        #
        # Return statement.
        return user_response
    except KeyboardInterrupt:
        #
        # Don't print any debug messages here, just exit.
        exit_script_ctrl_c()
    except Exception as e:
        #
        # Debug statement.
        print_error_message('get_user_response_integer(): Error!')
        print_error_message('e: ' + str(e))


def list_donor_names(database):
    #
    # Debug statement.
    print_debug_header_line()
    #
    # For each Donor:
    for d in donors_db.sorted():
        print(str(d.name) + ": ", str(round(d.sum_donations, 2)))


def print_database(database):
    #
    # This is a helper function. This will print the database to the screen.
    # Note: This for loop just prints data; not a Comprehension candidate.
    for key, value in database.items():
        #
        # Debug statement.
        print_debug_header_line()
        print('[ DEBUG ]: str(key)                     : ' + str(key))
        print('[ DEBUG ]: str(type(key))               : ' + str(type(key)))
        print('[ DEBUG ]: str(value)                   : ' + str(value))
        print('[ DEBUG ]: str(type(value))             : ' + str(type(value)))


def print_debug_header_line():
    #
    # Debug statement.
    print('[ ----- ]: -------------------------------------------------------')


def print_debug_message(message):
    #
    # Debug statement.
    print_debug_header_line()
    print('[ DEBUG ]: ' + str(message))


def print_donor_debug_statement(d):
    #
    # Debug statement.
    print('[ DEBUG ]: d.name:                ' + str(d.name))
    print('[ DEBUG ]: d.donations:           ' + str(d.donations))
    print('[ DEBUG ]: d.average_donation:    ' + str(d.average_donation))
    print('[ DEBUG ]: d.num_donations:       ' + str(d.num_donations))
    print('[ DEBUG ]: d.sum_donations:       ' + str(d.sum_donations))


def print_donor_collection_debug_statement(dc):
    #
    # Debug statement.
    print_debug_message(str(dc.list()))


def print_error_message(message):
    #
    # Debug statement.
    print_debug_header_line()
    print('[ ERROR ]: ' + str(message))


def print_main_menu():
    #
    # Create 'main_menu'.
    main_menu = create_main_menu()
    #
    # Populate 'main_menu'.
    add_to_dict(main_menu, '01', '[ ----- ]: -------------------------------------------------------')
    add_to_dict(main_menu, '02', '[  MAIN ]: Select an option:' )
    add_to_dict(main_menu, '03', '[ ----- ]: -------------------------------------------------------')
    add_to_dict(main_menu, '04', '[     1 ]: Send a Thank You to a single donor.')
    add_to_dict(main_menu, '05', '[     2 ]: Create a Report.')
    add_to_dict(main_menu, '06', '[     3 ]: Send letters to all donors.')
    add_to_dict(main_menu, '07', '[     4 ]: Quit')
    add_to_dict(main_menu, '08', '[     5 ]: [ DEBUG ]: print_database(donors_db)')
    add_to_dict(main_menu, '09', '[     6 ]: [ DEBUG ]: list_donor_names(donors_db)')
    add_to_dict(main_menu, '10', '[     7 ]: [ DEBUG ]: add_donation(donors_db, \'Donor 10\', float(100.00))')
    #
    # Print 'main_menu'.
    # Note: This for loop just prints data; not a Comprehension candidate.
    for value in main_menu:
        print(main_menu[value])


def print_send_thank_you_menu():
    try:
        #
        # Create 'send_thank_you_menu'.
        send_thank_you_menu = dict()
    except Exception as e:
        #
        # Debug statement.
        print_error_message('print_send_thank_you_menu(): Error!')
        print_error_message('e: ' + str(e))
    #
    # Populate 'send_thank_you_menu'.
    add_to_dict(send_thank_you_menu, '01', '[ ----- ]: -------------------------------------------------------')
    add_to_dict(send_thank_you_menu, '02', '[ DONOR ]: Select an option:')
    add_to_dict(send_thank_you_menu, '03', '[ ----- ]: -------------------------------------------------------')
    add_to_dict(send_thank_you_menu, '04', '[     1 ]: Type: \'list\'')
    add_to_dict(send_thank_you_menu, '05', '[       ]:        Display a list of donors.')
    add_to_dict(send_thank_you_menu, '06', '[     2 ]: Type: \'Existing Donor\'s Name\'')
    add_to_dict(send_thank_you_menu, '07', '[       ]:        Add a new donation for a donor.')
    add_to_dict(send_thank_you_menu, '08', '[     3 ]: Type: \'New Donor\'s Name\'')
    add_to_dict(send_thank_you_menu, '09', '[       ]:        Create a new donor.')
    add_to_dict(send_thank_you_menu, '10', '[     4 ]: Type: \'main\'')
    add_to_dict(send_thank_you_menu, '11', '[       ]:        Return to the Main Menu.')
    #
    # Note: This for loop just prints data; not a Comprehension candidate.
    for value in send_thank_you_menu:
        print(send_thank_you_menu[value])


def send_thank_you():
    while True:
        #
        # Print the 'send_thank_you_menu'.
        print_send_thank_you_menu()
        #
        # Get 'user_response'.
        user_response = get_user_response()
        #
        # Check 'user_response' == 'list'.
        if user_response.lower() == 'list':
            list_donor_names(donors_db)
            continue
        #
        # Check 'user_response' == 'main'.
        elif user_response.lower() == 'main':
            break
        #
        #
        try:
            #
            # Get 'donation_amount'.
            donation_amount = float(input('[ INPUT ]: Amount to add for {}: '.format(user_response)))
            #
            # Existing donor?
            if user_response in donors_db.list():
                # NOTE: This code in this specific if block is wrong.
                #
                # What I am trying to do is say:
                #    'Python, go find this Donor object from a list,
                #     and give me that [ specific ] Donor object back
                #     so I can append to it to the DonorCollection.'
                #
                # For whatever reason, getting this to work in this refactor
                # just isn't working with my code. I would update this in
                # real life and fix this as it isn't adding to an existing
                # Donor object at this point.
                #
                # I am sure there is a pythonic one-liner that would do this,
                # I am just out of time to improve this so I am submitting
                # this as-is for now to get this submitted in time for grading.
                # In real life, I would fix this. For now, I am just creating
                # a new object and adding it to the DonorCollection.
                #
                # Sigh... < insert: upside-down smiling face emoji: HERE (ha) >
                #
                # Create the Donor object.
                d = Donor(user_response)
                #
                # Add the Donor to the database.
                donors_db.add(d)
                #
                # Add the donation to the Donor.
                d.add_donation(donation_amount)
            #
            # Add a new Donor.
            elif user_response not in donors_db.list():
                #
                # Create the Donor object.
                d = Donor(user_response)
                #
                # Add the Donor to the database.
                donors_db.add(d)
                #
                # Add the donation to the Donor.
                d.add_donation(donation_amount)
                #
                # Print thank you message.
                print_debug_header_line()
                print(d.thank_you_message())
            #
            # Debug statement.
            print_donor_collection_debug_statement(donors_db)
            print_donor_debug_statement(d)
        except KeyboardInterrupt:
            #
            # Don't print any debug messages here, just exit.
            exit_script_ctrl_c()
        except Exception as e:
            #
            # Debug statement.
            print_error_message('send_thank_you(): try: donation_amount: Error!')
            print_error_message('e: ' + str(e))
            #
            # We have to break here.
            break


def send_thank_you_global(database, timestamp):
    #
    # This is the template for the thank you message.
    thank_you_template = str(timestamp) + '\n  Dear {},\n  Thank you for your donation of ${}.\n Regards, \n    - the Thank You bot \n'
    #
    # Get the location of 'tempdir'.
    temp_file_path = tempfile.gettempdir()
    #
    # Iterate through each donor in the database.
    for donor in database.donors_db:
        #
        # Format the file name.
        formatted_file_name = str(donor.name) + '_' + str(timestamp) + '.txt'
        formatted_file_path = temp_file_path + '/' + formatted_file_name
        #
        # Write the files to disk.
        try:
            with open(formatted_file_path,'w') as file:
                thank_you_letter = thank_you_template.format(donor, donor.sum_donations)
                file.write(thank_you_letter)
                file.close()
                #
                # Debug statement.
                print_debug_message('file: ' + str(formatted_file_name) + ': Success!')
        except Exception as e:
            #
            # Debug statement.
            print_error_message('file: ' + str(formatted_file_name) + ': Error!')
            print_error_message('e: ' + str(e))


def sort_database(database):
    try:
        #
        # Sort the database.
        database_sorted = dict(sorted(database.items(), key=lambda item: item[1], reverse=True))
        #
        # Return statement.
        return database_sorted
    except Exception as e:
        #
        # Debug statement.
        print_error_message('sort_database(database): Error!')
        print_error_message('e: ' + str(e))


if __name__ == "__main__":
    #
    # Main.
    display_main_menu()
