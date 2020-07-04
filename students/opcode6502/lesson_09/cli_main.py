# cli_main.py
# opcode6502: SP_Online_PY210


import sys


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
    # elif user_response == 2:
    #     create_report(donors_db)
    # elif user_response == 3:
    #     timestamp = get_timestamp()
    #     send_thank_you_global(donors_db, timestamp)
    # elif user_response == 4:
    #     exit_script()
    # #
    # # [ DEBUG ]: menu items.
    # elif user_response == 5:
    #     print_database(donors_db)
    # elif user_response == 6:
    #     list_donor_names(donors_db)
    # elif user_response == 7:
    #     add_donation(donors_db, 'Donor 10', float(100.00))
    # #
    # # [ ERROR ]: message.
    # else:
    #     print_error_message('Select item: [ 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 ].')
    print('To be implemented.')


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
    # Print the 'main_menu'.
    # Note: This for loop just prints data; not a Comprehension candidate.
    for value in main_menu:
        print(main_menu[value])


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


def print_send_thank_you_menu():
    #
    # Create 'send_thank_you_menu'.
    try:
        send_thank_you_menu = dict()
    except Exception as e:
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


if __name__=='__main__':

    # Call display_main_menu().
    display_main_menu()
