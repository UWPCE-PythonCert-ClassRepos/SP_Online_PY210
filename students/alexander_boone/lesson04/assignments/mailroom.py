#!/usr/bin/env python
import os
import sys

# global variables

# prepare initial data structure for donor data
donors = [{'first_name': 'Arnold', 'last_name': 'Schwarzenegger',
           'donation_total': 100000, 'donation_count': 1},
          {'first_name': 'Lebron', 'last_name': 'James',
           'donation_total': 1000000, 'donation_count': 1},
          {'first_name': 'Elon', 'last_name': 'Musk',
           'donation_total': 2000000, 'donation_count': 1},
          {'first_name': 'Walter', 'last_name': 'White',
           'donation_total': 500000, 'donation_count': 1},
          {'first_name': 'Gordon', 'last_name': 'Ramsay',
           'donation_total': 1280000, 'donation_count': 1}]

# Note: donor_data is a LIST of TUPLES with each tuple
# containing (dict of first/last name, [donation total,
# donation count])

# functions


def thank_you():
    """Send a thank you email to the donor."""

    print("Who would you like to send a thank you to?")

    # input donor name
    name = 'list'
    while name == 'list':
        name = input("Type 'list' to see a list of names or enter a name: ")

        # run if user inputs 'list'
        if name == 'list':
            list_names = list()
            for item in donors:
                list_names.append(item['first_name'] + ' ' + item['last_name'])
            print(list_names)
        # run if name that user inputs is not already in the donor list
        elif not any(donor['first_name'] == name.split(' ')[0] and
                     donor['last_name'] == name.split(' ')[1] for
                     donor in donors):
            firstName = name.split(' ')[0]
            lastName = name.split(' ')[1]
            donors.append({'first_name': firstName, 'last_name': lastName,
                           'donation_total': 0, 'donation_count': 0})
            index = len(donors) - 1
        # run if name that user inputs is already in the donor list
        else:
            firstName = name.split(' ')[0]
            lastName = name.split(' ')[1]
            for i in range(len(donors)):
                if (donors[i]['first_name'] == firstName and
                        donors[i]['last_name'] == lastName):
                    index = i
                    break

    # enter donation amount
    donation = float(input("Enter a donation amount: "))
    donors[index]['donation_total'] += donation
    donors[index]['donation_count'] += 1

    # write email (using formatted dict values)
    email = ('\nDear {first_name} {last_name},\n\nThank you for '
             + 'your generous donations, totaling ${donation_total}.'
             + ' We are very grateful.\n\nBest, \n\nLocal Charity\n'
             ).format(**donors[index])
    print(email)


def create_report():
    '''Create a report of donor data, including total donated, number of
    donations, and average donation amount.'''

    h = ['Donor Name', '|', 'Total Given', '|', 'Num Gifts',
         '|', 'Average Gift']
    # create table heading
    report_headers = '{:<25}{:^5}{:<15}{:^5}{:<10}{:^5}{:<15}'.format(*h)
    table_divider = '-' * 71
    print('\n', report_headers)
    print(table_divider)

    # sort donor data by donations
    def sort_key(donors_data):
        return donors_data['donation_total']

    donors_sorted = sorted(donors, key=sort_key, reverse=True)

    # print donor data
    for i in range(len(donors_sorted)):
        first_name = donors_sorted[i]['first_name']
        last_name = donors_sorted[i]['last_name']
        donation_avg = (donors_sorted[i]['donation_total'] /
                        donors_sorted[i]['donation_count'])
        print(('{:<25}{:^5}${:>14,.2f}{:^5}{:>10}{:^5}${:>14,.2f}'
               ).format(first_name + ' ' + last_name, ' ',
                        donors_sorted[i]['donation_total'], ' ',
                        donors_sorted[i]['donation_count'], ' ',
                        donation_avg
                        )
              )

    # remain on page until user decides to return to main menu
    q = 'Z'
    while q != 'Q' and q != 'q':
        q = input("\nEnter Q to Quit and return to the main menu: ")


def letters_to_all():
    '''Write a letter to every donor and save each one to a
    file on the disk.'''

    # write a letter to a text file for each donor
    for donor in donors:
        with open("{first_name}_{last_name}.txt".format(**donor),
                  'w+') as new_file:
            letter_body = ('{first_name} {last_name},\n\nThank you'
                           + ' for donating ${donation_total}. You '
                           + 'are so kind.\n\nBest,\n\nLocal Charity'
                           ).format(**donor)
            new_file.write(letter_body)


def quit_program():
    '''Print exit message and quit the program'''
    exit_message = "Closing the mailroom for the day..."
    print(exit_message)
    sys.exit()


# main code
if __name__ == '__main__':

    response_dict = {1: thank_you, 2: create_report, 3: letters_to_all,
                     4: quit_program}
    response = 0
    while response != 4:
        response = 0
        # display main menu with options
        options = ["1. Send a Thank You to a single donor", "2. Create a"
                   + " Report", "3. Send letters to all donors",
                   "4. Quit"]
        print(f"----- Main Menu -----\n{options[0]}\n{options[1]}"
              + f"\n{options[2]}\n{options[3]}")

        # get and run user response
        while int(response) not in [1, 2, 3, 4]:
            response = int(input("Enter a number: "))
        if response == 4:
            response_dict.get(response)()
