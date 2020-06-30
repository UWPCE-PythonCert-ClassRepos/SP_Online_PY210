# mailroom2.py
# opcode6502: SP_Online_PY210


import datetime
import os
import sys
import tempfile


def add_donation(donor_name, donation_amount):
    donors_db[donor_name] = donation_amount


def add_to_dict(database, key, value):
    database[key] = value


def create_donor(donor_name):
    donors_db[donor_name] = float('{:.2f}'.format(0.00))


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
    # Sort the donor list.
    donors_db_sorted = dict(sorted(donors_db.items(), key=lambda item: item[1]))
    #
    # Print the sorted donors list.
    for key, value in donors_db_sorted.items():
        donor_name = key
        donor_total = value
        number_of_gifts = 1 # len(donor[1])
        average_gift = float(donor_total) / float(number_of_gifts)
        average_gift = donor_total / number_of_gifts
        print('{:26} ${:>11.2f} {:>11}  ${:>12.2f}'.format(
              donor_name,
              donor_total,
              number_of_gifts,
              average_gift))


def debug_print_db():
    for key, value in donors_db.items():
        print('[ ----- ]: ------------------------------------------------------- ')
        print('[ DEBUG ]: str(key)                     : ' + str(key))
        print('[ DEBUG ]: str(type(key))               : ' + str(type(key)))
        print('[ DEBUG ]: str(value)                   : ' + str(value))
        print('[ DEBUG ]: str(type(value))             : ' + str(type(value)))


def exit_script():
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
    # Sort 'donors_db'.
    donors_db_sorted = dict(sorted(donors_db.items(), key=lambda item: item[1]))
    #
    # Print the sorted donors database to the screen.
    for key, value in donors_db_sorted.items() :
        print('{:10}'.format(str(key)), end='')
        print('{:10}'.format(str(value)))


def print_menu_error():
    print('[ ERROR ]: Select item: 1, 2, 3 or 4.')


def send_thank_you():
    while True:
        #
        # Print the 'send_thank_you_menu'.
        for value in send_thank_you_menu:
            print(send_thank_you_menu[value])
        #
        # Get user_response.
        user_response = input('[ INPUT ]: ')
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
                donation_amount = input('[ INPUT ]: Amount to add for {}: '.format(user_response))
                #
                # Add the donation.
                add_donation(user_response, float(donation_amount))
                #
                # Print the thank you mail.
                print(f'\n'
                'Dear {},\n\n'
                'Thank you for your donation of ${}.\n\n'
                '  Regards,\n'
                '  - the Thank You bot\n'.format(key,(float(donation_amount))))
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
    #
    # Iterate through each donor in the database.
    for key, value in donors_db.items():
        #
        # Format to keep things neat on disk.
        formatted_key = format_text(key)
        formatted_file_path = file_path + '/' + str(formatted_key) + '_' + str(get_timestamp()) + '.txt'
        #
        # Format and write the files to disk.
        with open(formatted_file_path,'w') as file:
            thank_you_letter = thank_you_template.format(key,value)
            file.write(thank_you_letter)
            file.close()


def sort_donation_amount(donation_amount):
    return dict(sorted(donors_db.items(), key=lambda item: item[1]))


def sort_donor_name(donor_name):
    return dict(sorted(donors_db.items(), key=lambda item: item[0]))


def display_main_menu():
    while True:
        #
        # Print the 'main_menu'.
        for value in main_menu:
            print(main_menu[value])
        #
        # Get 'user_response' and test input.
        try:
            user_response = int(input('[ INPUT ]: '))
        except:
            print_menu_error()
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
        elif user_response == 5:
            debug_print_db()
        else:
            print_menu_error()


if __name__=='__main__':

    # Create and populate 'donors_db'.
    donors_db = dict()
    add_donation('Donor 04', float(400))
    add_donation('Donor 02', float(200))
    add_donation('Donor 03', float(300))
    add_donation('Donor 01', float(100))

    # Create and populate 'main_menu'.
    main_menu = dict()
    add_to_dict(main_menu, '01', '[ ----- ]: ------------------------------------------------------- ')
    add_to_dict(main_menu, '02', '[  MAIN ]: Select an option: ' )
    add_to_dict(main_menu, '03', '[ ----- ]: ------------------------------------------------------- ')
    add_to_dict(main_menu, '04', '[     1 ]: Send a Thank You to a single donor.')
    add_to_dict(main_menu, '05', '[     2 ]: Create a Report.')
    add_to_dict(main_menu, '06', '[     3 ]: Send letters to all donors.')
    add_to_dict(main_menu, '07', '[     4 ]: Quit')
    add_to_dict(main_menu, '08', '[     5 ]: [ DEBUG ]: Print database debug data to screen')

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
