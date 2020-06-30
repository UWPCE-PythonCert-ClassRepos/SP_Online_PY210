# mailroom_04.py
# opcode6502: SP_Online_PY210


import datetime
import sys
import tempfile


def add_donation(database, donor_name, donation_amount):
    try:
        database[donor_name] = float(donation_amount)
        # print_debug_message('add_donation(database, donor_name, donation_amount): Success!')
        return True
    except Exception as e:
        print_error_message('add_donation(database, donor_name, donation_amount): Error!')
        print_error_message('e: ' + str(e))


def add_to_dict(database, key, value):
    try:
        database[key] = value
    except Exception as e:
        print_error_message('add_to_dict(database, key, value): Error!')
        print_error_message('e: ' + str(e))


def check_user_response(user_response):
    #
    # Check 'user_response'.
    if user_response == 1:
        send_thank_you()
    elif user_response == 2:
        create_report(donors_db)
    elif user_response == 3:
        timestamp = get_timestamp()
        send_thank_you_global(donors_db, timestamp)
    elif user_response == 4:
        exit_script()
    #
    # [ DEBUG ]: menu items.
    elif user_response == 5:
        print_database(donors_db)
    elif user_response == 6:
        list_donor_names(donors_db)
    elif user_response == 7:
        add_donation(donors_db, 'Donor 10', float(100.00))
    elif user_response == 8:
        comprehensions_test()
    #
    # [ ERROR ]: message.
    else:
        print_error_message('Select item: [ 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 ].')


def create_donor(database, donor_name):
    try:
        database[donor_name] = float(0.00)
        # print_debug_message('create_donor(donor_name): ' + str(donor_name) + ': Success!')
    except Exception as e:
        print_error_message('create_donor(donor_name): Error!')
        print_error_message('e: ' + str(e))


def create_donors_db():
    #
    # Try to create a dict and print an error if this fails.
    try:
        donors_db = dict()
        #
        # print_debug_message('create_donors_db(): Success!')
        return donors_db
    except Exception as e:
        print_error_message('create_donors_db(): Error!')
        print_error_message('e: ' + str(e))


def create_main_menu():
    #
    # Try to create a dict and print an error if this fails.
    try:
        main_menu = dict()
        # print_debug_message('create_main_menu(): Success!')
        return main_menu
    except Exception as e:
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
    # Initialize 'donors_db_sorted'.
    donors_db_sorted = dict()
    #
    # Sort the donor list.
    donors_db_sorted = sort_database(database)
    #
    # Print the sorted donors list.
    # Note: This for loop just prints data; not a Comprehension candidate.
    for key, value in donors_db_sorted.items():
        donor_name = key
        donor_total = value
        number_of_gifts = 1 # len(donor[1])
        average_gift = float(donor_total) / float(number_of_gifts)
        # average_gift = donor_total / number_of_gifts
        print('{:26} ${:>11.2f} {:>11}  ${:>12.2f}'.format(
              donor_name,
              donor_total,
              number_of_gifts,
              average_gift))


def display_main_menu():
    #
    # Display the main menu and process the user's response.
    while True:
        #
        # Print the 'main_menu'.
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
    for i in text:
        text = text.replace(' ', '_')
    return text


def get_timestamp():
    timestamp = format_text(str(datetime.datetime.now()))
    return timestamp


def get_user_response():
    # Get 'user_response' (any input) and test input.
    try:
        user_response = input('[ INPUT ]: ')
        return user_response
    except KeyboardInterrupt:
        exit_script_ctrl_c()
    except Exception as e:
        print_error_message('get_user_response(): try: user_response: Error!')
        print_error_message('e: ' + str(e))


def get_user_response_integer():
    # Get 'user_response' (integer only) and test input.
    try:
        user_response = int(input('[ INPUT ]: '))
        return user_response
    except KeyboardInterrupt:
        exit_script_ctrl_c()
    except Exception as e:
        print_error_message('get_user_response_integer(): Error!')
        print_error_message('e: ' + str(e))


def list_donor_names(database):
    #
    print_debug_header_line()
    #
    # Initialize 'donors_db_sorted'.
    donors_db_sorted = dict()
    #
    # Sort the donor list.
    donors_db_sorted = sort_database(database)
    #
    # Print the sorted donors database to the screen.
    # Note: This for loop just prints data; not a Comprehension candidate.
    for key, value in donors_db_sorted.items():
        print('{:10}'.format(str(key)), end='')
        print('{:10.2f}'.format(value))
    #
    # pytest: Additions.
    # This return statement will be ignored when called from
    # check_user_response(user_response).
    # However, we want this return statement here so we can test with pytest.
    return donors_db_sorted


def print_database(database):
    #
    # This is a helper function. This will print the database to the screen.
    # Note: This for loop just prints data; not a Comprehension candidate.
    for key, value in database.items():
        print_debug_header_line()
        print('[ DEBUG ]: str(key)                     : ' + str(key))
        print('[ DEBUG ]: str(type(key))               : ' + str(type(key)))
        print('[ DEBUG ]: str(value)                   : ' + str(value))
        print('[ DEBUG ]: str(type(value))             : ' + str(type(value)))


def print_debug_header_line():
    #
    # Debug message.
    print('[ ----- ]: -------------------------------------------------------')


def print_debug_message(message):
    #
    # Debug message.
    print_debug_header_line()
    print('[ DEBUG ]: ' + str(message))


def print_error_message(message):
    #
    # Debug message.
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
    add_to_dict(main_menu, '11', '[     8 ]: [ DEBUG ]: comprehensions_test()')
    #
    # Print the 'main_menu'.
    # Note: This for loop just prints data; not a Comprehension candidate.
    for value in main_menu:
        print(main_menu[value])


def print_send_thank_you_menu():
    #
    # Create 'send_thank_you_menu'.
    try:
        send_thank_you_menu = dict()
    except Exception as e:
        print_error_message('create_donors_db(): Error!')
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


def print_thank_you_message(key, donation_amount):
    print_debug_header_line()
    print(f'\n'
    'Dear {},\n\n'
    'Thank you for your donation of ${}.\n\n'
    '  Regards,\n'
    '  - the Thank You bot\n'.format(key, donation_amount))


def send_thank_you():
    while True:
        #
        # Print the 'send_thank_you_menu'.
        print_send_thank_you_menu()
        #
        # Get user_response.
        user_response = get_user_response()
        #
        # Check user_response.
        if user_response.lower() == 'list':
            list_donor_names(donors_db)
            continue
        elif user_response.lower() == 'main':
            break
        for key, value in donors_db.items():
            if user_response == key:
                #
                # Get the donation amount.
                try:
                    donation_amount = input('[ INPUT ]: Amount to add for {}: '.format(user_response))
                except KeyboardInterrupt:
                    exit_script_ctrl_c()
                except Exception as e:
                    print_error_message('send_thank_you(): try: donation_amount: Error!')
                    print_error_message('e: ' + str(e))
                    break
                #
                # Add the donation; check for success.
                if add_donation(donors_db, user_response, donation_amount):
                    #
                    # If we succeeded, print the thank you mail.
                    print_thank_you_message(key, donation_amount)
                #
                # We have to break here.
                break
        else:
            create_donor(donors_db, user_response)


def send_thank_you_global(database, timestamp):
    #
    # This is the template for the thank you message.
    thank_you_template = str(timestamp) + '\n  Dear {},\n  Thank you for your donation of ${}.\n Regards, \n    - the Thank You bot \n'
    #
    # Get the location of 'tempdir'.
    temp_file_path = tempfile.gettempdir()
    # print_debug_message('temp: ' + str(temp_file_path))
    #
    # Iterate through each donor in the database.
    for key, value in database.items():
        #
        # Format to keep things neat on disk.
        formatted_key = format_text(key)
        formatted_file_name = str(formatted_key) + '_' + str(timestamp) + '.txt'
        formatted_file_path = temp_file_path + '/' + formatted_file_name
        #
        # Format and write the files to disk.
        try:
            with open(formatted_file_path,'w') as file:
                thank_you_letter = thank_you_template.format(key,value)
                file.write(thank_you_letter)
                file.close()
                print_debug_message('file: ' + str(formatted_file_name) + ': Success!')
        except Exception as e:
            print_error_message('file: ' + str(formatted_file_name) + ': Error!')
            print_error_message('e: ' + str(e))


def sort_database(database):
    try:
        database_sorted = dict(sorted(database.items(), key=lambda item: item[1], reverse=True))
        return database_sorted
    except Exception as e:
        print_error_message('sort_database(database): Error!')
        print_error_message('e: ' + str(e))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def comprehensions_test():
    print_debug_message('This is a test of comprehensions!')
    #
    # Try a list comprehension.
    new_list_01 = [i for i in range(10)]
    print_debug_message(new_list_01)
    #
    # Try comprehensions with items in our database.
    new_dict_01 = { d.lower() : donors_db.get(d.lower(), 0) for d in donors_db.keys() }
    new_dict_02 = { d.upper() : donors_db.get(d.upper(), 0) for d in donors_db.keys() }
    print_debug_message(new_dict_01)
    print_debug_message(new_dict_02)
    #
    # This really isn't what comprehensions are for but I wanted to test
    # out comprehensions in deeper detail.
    print_debug_header_line()
    fizzbuzz = [
        print('[  FIZZ ]: n: ' + str(n) + ' fizzbuzz') if n % 3 == 0 and n % 5 == 0
        else print('[  FIZZ ]: n: ' + str(n) + ' fizz') if n % 3 == 0
        else print('[  FIZZ ]: n: ' + str(n) + ' buzz') if n % 5 == 0
        else print('[  FIZZ ]: n: ' + str(n))
        for n in range(101)
    ]
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


if __name__=='__main__':

    # Create 'donors_db'.
    donors_db = create_donors_db()
    #
    # Populate 'donors_db'.
    add_donation(donors_db, 'Donor 01', float(100.00))
    add_donation(donors_db, 'Donor 02', float(222.22))
    add_donation(donors_db, 'Donor 03', float(333.33))
    add_donation(donors_db, 'Donor 04', float(499.99))
    #
    # Smoke test: This _should_ generate an error in the console.
    # add_donation(donors_db, 'Donor 01', 'z')

    # Call display_main_menu().
    display_main_menu()
