#!/usr/bin/env python3

import sys
import os

donor_db = {'Eddie Vedder': [10000.00, 20000.00, 4500.00],
            'Chris Cornell': [100.00, 500.00],
            'Kurt Cobain': [25.00],
            'Dave Matthews': [100000.00, 50000.00, 125000.00],
            'Dave Grohl': [50.00]}


prompt = '\n'.join(('Welcome to the mailroom',
         'Please choose from the following options:',
         '1 - Send a Thank You',
         '2 - Create a Report',
         '3 - Send letters to all donors',
         '4 - Quit',
         '> '))


#send a thank you tasks
def initial_input():
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    return ty_prompt


def donation_prompt():
    donation_amount = input('Please enter a donation amount: ')
    try:
        donation_amount = float(donation_amount)
    except ValueError:
        print('Please enter an integer for the donation amount.')
    else:
        return donation_amount


def update_database(name, donation):
    for donor in donor_db.keys():
        if donor == name:
            donor_db[name].append(donation)
            break
    else:
        donor_db[name] = [donation]
    donation_email = "\nDear {},\nThank you for your generous donation of ${:.2f}!\n"
    print(donation_email.format(name, donation))


def test_update_database_current():
    '''Confirm that a donation amount from a donor already in list gets
    properly appended to database'''
    update_database('Kurt Cobain', 1000)
    assert donor_db['Kurt Cobain'] == [25.00, 1000.00]


def test_update_database_new():
    '''Confirm that a donation amount for a new donor gets properly added to database'''
    update_database('Zach Thomson', 250)
    assert donor_db['Zach Thomson'] == [250.00]

def test_ty_letter():
    donation_email = "\nDear {},\nThank you for your generous donation of ${:.2f}!\n"
    assert donation_email.format('Kurt Cobain', 1000) == "\nDear Kurt Cobain,\nThank you for your generous donation of $1000.00!\n"


def thank_you_logic(name):
    if name.lower() == 'list':
        print(donor_db.keys())
    else:
        update_database(name, donation_prompt())


def thank_you_updated():
    return thank_you_logic(initial_input())


#create a report functions
def number_donations(x):
    return len(x)


def average_gift(x):
    return sum(x)/len(x)


def second_sort(elem):
    return elem[1]


def create_table(d):
    """takes the donor database and sorts on total given. also makes a summary
    table with total given, number of gifts and average amount of gift"""
    report_list = [(key, sum(d[key]), number_donations(d[key]), average_gift(d[key])) for key in d.keys()]
    report_list.sort(key=second_sort, reverse=True)
    return report_list


def create_report():
    '''formats create_table into the create_report format'''
    header = ('Donor Name', 'Total Given', 'Num Gifts', 'Average Gift')
    table_header = "{:<20}| {} | {} | {}".format(*header) + '\n' + "-" * 60
    line_format = ("{:<20}" + " $" + "{:>12.2f}" + "{:>11}" + "  $" + "{:>12.2f}")
    print(table_header)
    table = create_table(donor_db)
    for entry in table:
        print(line_format.format(*entry))

def test_create_table():
    '''Confirms entries from database are placed in a list'''
    test_list = create_table(donor_db)
    assert ('Dave Grohl', 50.0, 1, 50.0) in test_list
    assert ('Chris Cornell', 600.0, 2, 300.0) in test_list


def test_table_order():
    '''Confirms entries into list are then sorted in descending order'''
    test_list = create_table(donor_db)
    i = 0
    while i < len(test_list)-1:
        assert test_list[i][1] > test_list[i+1][1]
        i +=1


#make a function to send letters to all donors
FORM_LETTER = "Dear {},\n\n\tThank you for donating ${:.2f}!\n\n\tThe kids will greatly appreciate it.\n\n\tSincerely,\n\t  -Our Team"


def send_letters():
    for key in donor_db:
        with open(str(key) + '.txt', 'w') as f:
            f.write(FORM_LETTER.format(key, sum(donor_db[key])))


def test_letter_creation():
    """tests if send_letters creates a file in the current directory"""
    send_letters()
    for key in donor_db:
        assert os.path.basename(str(key) + '.txt') == (str(key) + '.txt')


def test_letter_content():
    """checks proper content in letter"""
    send_letters()
    expected = "Dear Dave Grohl,\n\n\tThank you for donating $50.00!\n\n\tThe kids will greatly appreciate it.\n\n\tSincerely,\n\t  -Our Team"
    with open('Dave Grohl.txt') as f:
        assert f.read() == expected


#make a function to exit the program
def exit_program():
    print('Have a nice day!')
    sys.exit() # exit the interactive script


switch_dict = {1: thank_you_updated,
               2: create_report,
               3: send_letters,
               4: exit_program,
               }


def main():
    while True:
        response = input(prompt)
        try:
            response = int(response)
        except ValueError:
            print('Please input a valid response')
        else:
            try:
                switch_dict.get(int(response))()
            except TypeError:
                print('Please input a valid response')


if __name__ == "__main__":
    main()
