from donor_models import *
import sys

donor_list = {'William Gates': [1500.99, 3500, 800.25],
              'Jeff Bezos': [145.72, 1350.25],
              'Paul Allen': [250.00, 57.00],
              'Mark Zuckerberg': [600.00]}


dc = DonorCollection(donor_list)


def print_donor_report():

    row = '| {name:20} | {sign_1:1}  {amount:>15,.2f} | {num_gifts:^10} | {sign_2:1} {avg_gift:>15,.2f} |'.format

    print('| {:20} | {:1}  {:^15} | {:^10} | {:1} {:^15} |'.format('Donor Name', ' ', 'Total Given', 'Num Gifts', '',
                                                                   'Average Gift'))
    print('-' * 78)
    for donor in dc.sorted():
        print(row(name=donor, sign_1='$', amount=dc.total(donor), num_gifts=dc.times(donor), sign_2='$',
                  avg_gift=dc.total(donor) / dc.times(donor)))


def thank_you_letter():
    while True:
        user_input = str(input('''What is the name of donor? or type 'list' to see the current list: ''')).title()
        if user_input.lower() == 'back':
            return False
        elif user_input.lower() == 'list':
            print('The current list of names are:')
            print(dc.donor_name_list())
            continue
        try:
            first, last = user_input.split()
        except ValueError:
            print('Please Enter First and Last Name !!!')
            continue
        thx_amount = input('How much did ' + user_input + ' donate? $ ')
        if str(thx_amount.lower()) == 'back':
            return False
        elif user_input not in dc.donor_name_list():
            new_donor = input('Do you want to add {} as a new donor? (YES or NO) '.format(user_input.title()))
            if new_donor.lower() == 'back':
                return False
            elif new_donor.upper() == 'NO':
                continue
            else:
                thx_name = user_input
                try:
                    dc.add_new_donor(thx_name, float(thx_amount))
                except ValueError:
                    print('Please Enter Numbers Only !!!')
                    continue
                break
        else:
            thx_name = user_input
            try:
                dc.add_amount_same_donor(thx_name, float(thx_amount))
            except ValueError:
                print('Please Enter Numbers Only 1 !!!')
                continue
            break
    print('\nEMAIL CONTENT: \n')
    do = Donor(thx_name, float(thx_amount))
    print(do.send_letter())


def print_menu_task():
    print('''
    Menu of Options
    1) Send a Thank You letter to a single donor
    2) Create a Report
    3）Send letters to all donors
    4) Quit
    Note: You can type 'back' to return to Main Menu
    ''')


def send_letters_all():
    dc.send_letters_to_all()
    print('Letters all sent !!!\n')


def input_menu_choice():
    choice = input('Which choice would you to perform? [1 to 4]: ')
    print()
    return choice


def exit_program():
    print('Exit the Program')
    sys.exit()


def main_menu():
    switch_dict = {1: thank_you_letter, 2: print_donor_report, 3: send_letters_all, 4: exit_program}
    while True:
        print_menu_task()
        option = input_menu_choice()
        try:
            switch_dict.get(int(option))()
        except TypeError:
            print('Please Enter from 1 to 4 only !!!!!')
        except ValueError:
            print('Please Enter Number only !!!!!')


if __name__ == '__main__':
    main_menu()
