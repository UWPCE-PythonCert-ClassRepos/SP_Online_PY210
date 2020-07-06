# mailroom_03.py
# opcode6502: SP_Online_PY210


import datetime
import sys
import tempfile


def add_donation(donor_name, donation_amount):
    try:
        donors_db[donor_name] = float(donation_amount)
        print_debug_message('add_donation(donor_name, donation_amount): Success!')
        return True
    except:
        print_error_message('add_donation(donor_name, donation_amount): Error!')
        return False


def add_to_dict(database, key, value):
    try:
        database[key] = value
        return True
    except:
        print_error_message('add_to_dict(database, key, value): Error!')
        return False


def check_user_response(user_response):
    #
    # Check 'user_response'.
    if user_response == 1:
        send_thank_you()
    elif user_response == 2:
        create_report()
    elif user_response == 3:
        send_thank_you_global()
    elif user_response == 4:
        exit_script()
    #
    # DEBUG menu items.
    elif user_response == 5:
        debug_print_db()
    elif user_response == 6:
        list_donor_names()
    elif user_response == 7:
        add_donation('Donor 01', float(100.00))
    elif user_response == 8:
        test_comprehensions()
    else:
        print_error_message('Select item: [ 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 ].')


def create_donor(donor_name):
    try:
        donors_db[donor_name] = float(0.00)
        print_debug_message('create_donor(donor_name): ' + str(donor_name) + ': Success!')
        return True
    except:
        print_error_message('create_donor(donor_name): Error!')
        return False


def create_report():
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
    donors_db_sorted = sort_database(donors_db)
    #
    # Print the sorted donors list.
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


def debug_print_db():
    # Note: This for loop just prints data; not a Comprehension candidate.
    for key, value in donors_db.items():
        print_debug_header_line()
        print('[ DEBUG ]: str(key)                     : ' + str(key))
        print('[ DEBUG ]: str(type(key))               : ' + str(type(key)))
        print('[ DEBUG ]: str(value)                   : ' + str(value))
        print('[ DEBUG ]: str(type(value))             : ' + str(type(value)))


def display_main_menu():
    while True:
        #
        # Initialize 'user_response'.
        user_response = ''
        #
        # Print the 'main_menu'.
        # Note: This for loop just prints data; not a Comprehension candidate.
        for value in main_menu:
            print(main_menu[value])
        #
        # Get 'user_response' and test input.
        try:
            user_response = int(input('[ INPUT ]: '))
        except KeyboardInterrupt:
            exit_script_ctrl_c()
        except:
            print_error_message('display_main_menu(): Error!')
        #
        # Check 'user_response'.
        check_user_response(user_response)


def exit_script():
    sys.exit()


def exit_script_ctrl_c():
    print()
    sys.exit()


def format_text(text):
    for i in text:
        text = text.replace(' ', '_')
    return text


def get_timestamp():
    timestamp = format_text(str(datetime.datetime.now()))
    return timestamp


def list_donor_names():
    #
    # Initialize 'donors_db_sorted'.
    donors_db_sorted = dict()
    #
    # Sort the donor list.
    donors_db_sorted = sort_database(donors_db)
    #
    # Print the sorted donors database to the screen.
    # Note: This for loop just prints data; not a Comprehension candidate.
    for key, value in donors_db_sorted.items():
        print('{:10}'.format(str(key)), end='')
        print('{:10.2f}'.format(value))


def print_debug_header_line():
    print('[ ----- ]: ------------------------------------------------------- ')


def print_debug_message(message):
    print_debug_header_line()
    print('[ DEBUG ]: ' + str(message))


def print_error_message(message):
    print_debug_header_line()
    print('[ ERROR ]: ' + str(message))


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
        # Note: This for loop just prints data; not a Comprehension candidate.
        for value in send_thank_you_menu:
            print(send_thank_you_menu[value])
        #
        # Initialize 'user_response'.
        user_response = ''
        #
        # Get user_response.
        try:
            user_response = input('[ INPUT ]: ')
        except KeyboardInterrupt:
            exit_script_ctrl_c()
        except:
            print_error_message('send_thank_you(): try: user_response: Error!')
            break
        #
        # Check user_response.
        if user_response.lower() == 'list':
            list_donor_names()
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
                except:
                    print_error_message('send_thank_you(): try: donation_amount: Error!')
                    break
                #
                # Add the donation.
                if add_donation(user_response, donation_amount):
                    #
                    # Print the thank you mail.
                    print_thank_you_message(key, donation_amount)
                #
                # We have to break here.
                break
        else:
            create_donor(user_response)


def send_thank_you_global():
    #
    # This is the template for the thank you message.
    thank_you_template = str(get_timestamp()) + '\n  Dear {},\n  Thank you for your donation of ${}.\n Regards, \n    - the Thank You bot \n'
    #
    # Get the location of 'tempdir'.
    file_path = tempfile.gettempdir()
    print_debug_message('temp: ' + str(file_path))
    #
    # Iterate through each donor in the database.
    for key, value in donors_db.items():
        #
        # Format to keep things neat on disk.
        formatted_key = format_text(key)
        formatted_file_name = str(formatted_key) + '_' + str(get_timestamp()) + '.txt'
        formatted_file_path = file_path + '/' + formatted_file_name
        #
        # Format and write the files to disk.
        try:
            with open(formatted_file_path,'w') as file:
                thank_you_letter = thank_you_template.format(key,value)
                file.write(thank_you_letter)
                file.close()
                print_debug_message('file: ' + str(formatted_file_name) + ': Success!')
        except:
            print_error_message('file: ' + str(formatted_file_name) + ': Error!')


def sort_donation_amount(donation_amount):
    try:
        return dict(sorted(donors_db.items(), key=lambda item: item[1]))
    except:
        print_error_message('sort_donation_amount(donation_amount): Error!')
        return False


def sort_donor_name(donor_name):
    try:
        return dict(sorted(donors_db.items(), key=lambda item: item[0]))
    except:
        print_error_message('sort_donor_name(donor_name): Error!')
        return False


def sort_database(database):
    try:
        database_sorted = dict(sorted(database.items(), key=lambda item: item[1], reverse=True))
        return database_sorted
    except:
        print_error_message('sort_database(database): Error!')
        return False


def test_comprehensions():
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


if __name__=='__main__':

    # Create and populate 'donors_db'.
    donors_db = dict()
    add_donation('Donor 01', float(100.00))
    add_donation('Donor 02', float(222.22))
    add_donation('Donor 03', float(333.33))
    add_donation('Donor 04', float(499.99))
    #
    # Smoke test: This _should_ generate an error in the console.
    add_donation('Donor 01', 'z')

    # Create and populate 'main_menu'.
    main_menu = dict()
    add_to_dict(main_menu, '01', '[ ----- ]: ------------------------------------------------------- ')
    add_to_dict(main_menu, '02', '[  MAIN ]: Select an option: ' )
    add_to_dict(main_menu, '03', '[ ----- ]: ------------------------------------------------------- ')
    add_to_dict(main_menu, '04', '[     1 ]: Send a Thank You to a single donor.')
    add_to_dict(main_menu, '05', '[     2 ]: Create a Report.')
    add_to_dict(main_menu, '06', '[     3 ]: Send letters to all donors.')
    add_to_dict(main_menu, '07', '[     4 ]: Quit')
    add_to_dict(main_menu, '08', '[     5 ]: [ DEBUG ]: debug_print_db()')
    add_to_dict(main_menu, '09', '[     6 ]: [ DEBUG ]: list_donor_names()')
    add_to_dict(main_menu, '10', '[     7 ]: [ DEBUG ]: add_donation(\'Donor 10\', float(100.00))')
    add_to_dict(main_menu, '11', '[     8 ]: [ DEBUG ]: test_comprehensions()')

    # Create and populate 'send_thank_you_menu'.
    send_thank_you_menu = dict()
    add_to_dict(send_thank_you_menu, '01', '[ ----- ]: ------------------------------------------------------- ')
    add_to_dict(send_thank_you_menu, '02', '[ DONOR ]: Select an option: ')
    add_to_dict(send_thank_you_menu, '03', '[ ----- ]: ------------------------------------------------------- ')
    add_to_dict(send_thank_you_menu, '04', '[     1 ]: Type: \'list\'')
    add_to_dict(send_thank_you_menu, '05', '[       ]:        Display a list of donors.')
    add_to_dict(send_thank_you_menu, '06', '[     2 ]: Type: \'Existing Donor\'s Name\'')
    add_to_dict(send_thank_you_menu, '07', '[       ]:        Add a new donation for a donor.')
    add_to_dict(send_thank_you_menu, '08', '[     3 ]: Type: \'New Donor\'s Name\'')
    add_to_dict(send_thank_you_menu, '09', '[       ]:        Create a new donor.')
    add_to_dict(send_thank_you_menu, '10', '[     4 ]: Type: \'main\'')
    add_to_dict(send_thank_you_menu, '11', '[       ]:        Return to the Main Menu.')

    # Call display_main_menu().
    display_main_menu()
