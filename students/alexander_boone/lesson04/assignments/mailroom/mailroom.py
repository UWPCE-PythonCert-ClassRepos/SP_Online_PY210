#!/usr/bin/env python
import os
import sys

donors = {'Arnold Schwarzenegger': [100000, 1],
          'Lebron James': [1000000, 1],
          'Elon Musk': [2000000, 1],
          'Walter White': [500000, 1],
          'Gordon Ramsay': [1280000, 1]}

# functions


def thank_you():
    """Send a thank you email to the specified donor."""

    print("Who would you like to send a thank you to?")

    # input donor name
    name = 'list'
    while name == 'list':
        name = input("Type 'list' to see a list of names or enter a name: ")

        # run if user inputs 'list'
        if name == 'list':
            list_names = []
            for item in donors.keys():
                list_names.append(item)
            print(list_names)

        # run if name that user inputs is not already in the donor list
        elif name not in donors.keys():
            donors[name] = [0, 0]

    # enter donation amount
    donation = float(input("Enter a donation amount: "))
    donors[name][0] += donation
    donors[name][1] += 1

    # write email (using formatted dict values)
    email = ('\nDear {0},\n\nThank you for '
             + 'your generous donations, totaling ${1:,.2f}.'
             + ' We are very grateful.\n\nBest, \n\nLocal Charity\n'
             ).format(name, donors[name][0])
    print(email)


def create_report():
    """Create a report of donor data, including total donated, number of
    donations, and average donation amount.
    """

    h = ['Donor Name', '|', 'Total Given', '|', 'Num Gifts',
         '|', 'Average Gift']

    # create table heading
    report_headers = '{:<25}{:^5}{:<15}{:^5}{:<10}{:^5}{:<15}'.format(*h)
    table_divider = '-' * 71
    print('\n', report_headers)
    print(table_divider)

    # sort donor data by donation_total
    def sort_key(donors_data):
        return donors_data[1][0]

    donors_sorted = sorted(donors.items(), key=sort_key, reverse=True)

    # print donor data row-by-row
    for donor in donors_sorted:
        donation_avg = (donor[1][0] /
                        donor[1][1])
        print(('{:<25}{:^5}${:>14,.2f}{:^5}{:>10}{:^5}${:>14,.2f}'
               ).format(donor[0], ' ',
                        donor[1][0], ' ',
                        donor[1][1], ' ',
                        donation_avg
                        )
              )

    # remain on page until user decides to return to main menu
    q = ''
    while q != 'Q' and q != 'q':
        q = input("\nEnter Q to Quit and return to the main menu: ")


def letters_to_all():
    """Write a letter to every donor and save each one to a
    file on the disk.
    """

    script_dir = os.path.dirname(__file__)

    # write a letter to a text file for each donor
    for donor in donors.keys():
        first_name = donor.split()[0]
        last_name = donor.split()[1]
        relative_path = "letters/{0}_{1}.txt".format(first_name, last_name)
        abs_file_path = os.path.join(script_dir, relative_path)
        with open(abs_file_path,
                  'w+') as new_file:
            letter_body = ('{0} {1},\n\nThank you'
                           + ' for donating ${2:,.2f}. You '
                           + 'are so kind.\n\nBest,\n\nLocal Charity'
                           ).format(first_name, last_name, donors[donor][0])
            new_file.write(letter_body)


def quit_program():
    """Print exit message and quit the program"""

    exit_message = "Closing the mailroom for the day..."
    print(exit_message)
    sys.exit()


# main code
if __name__ == '__main__':

    response_dict = {1: thank_you, 2: create_report, 3: letters_to_all,
                     4: quit_program}
    response = 0
    while True:
        response = 0

        # display main menu with options
        options = ["1. Send a Thank You to a single donor", "2. Create a"
                   + " Report", "3. Send letters to all donors",
                   "4. Quit"]
        print(f"----- Main Menu -----\n{options[0]}\n{options[1]}"
              + f"\n{options[2]}\n{options[3]}")

        # ask for and run user response
        while int(response) not in response_dict:
            response = int(input("Enter a number: "))
            if response not in response_dict:
                print('Invalid Response. Enter 1, 2, 3, or 4.')
        response_dict.get(response)()
