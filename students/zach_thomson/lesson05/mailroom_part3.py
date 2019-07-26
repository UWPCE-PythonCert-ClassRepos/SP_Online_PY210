#!/usr/bin/env python3

import sys

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
def thank_you():
    ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
    try:
        ty_prompt = float(ty_prompt)
    except ValueError:
        while ty_prompt.lower() == 'list':
            print(donor_db.keys())
            ty_prompt = input('Please enter a full name or type list to see all the current donors: ')
        else:
            donation_amount = input('Please enter a donation amount: ')
            try:
                donation_amount = float(donation_amount)
            except ValueError:
                print('Please enter an integer for the donation amount.')
            else:
                for donor in donor_db.keys():
                    if donor == ty_prompt:
                        donor_db[ty_prompt].append(donation_amount)
                        break
                else:
                    donor_db[ty_prompt] = [donation_amount]
                donation_email = "\nDear {},\nThank you for your generous donation of ${:.2f}!\n"
                print(donation_email.format(ty_prompt, donation_amount))
    else:
        print('Please enter a name and not a number')


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


#make a function to send letters to all donors
FORM_LETTER = "Dear {},\n\n\tThank you for donating ${:.2f}!\n\n\tThe kids will greatly appreciate it.\n\n\tSincerely,\n\t  -Our Team"


def send_letters():
    for key in donor_db:
        with open(str(key) + '.txt', 'w') as f:
            f.write(FORM_LETTER.format(key, sum(donor_db[key])))


#make a function to exit the program
def exit_program():
    print('Have a nice day!')
    sys.exit() # exit the interactive script


switch_dict = {1: thank_you,
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
