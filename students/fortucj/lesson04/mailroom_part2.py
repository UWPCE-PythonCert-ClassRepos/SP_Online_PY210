#!/usr/bin/env python

"""
The Mailroom assignment.

Part 1 info:
The data is a global list.
Appending donations was repetitive, so was made into its own function 'add_donations()'
A separate data structure (a list of lists) was built from the original data (a list of \
tuples, which contain strings and lists) to facilitate report writing.

Part 2 info:
The original data was converted to a dict, with the strings now as keys and the lists now as \
values.
The separate data structure was converted to a list of dicts, with each dict corresponding to \
a donor.
The letter template already used .format().  Now it pulls data from the dict.
"""

import sys

# This was originally a list of lists.  I changed it based on the recommendation in the notes.
Data = {'Bob': [17.56], 'Billy': [500.00, 1000.00], 'Joe Schmoe': [2.00, 0.03, 45.00],
        'This Guy': [1.00, 100000], 'That Gal': [9876.54]}

Prompt = """\nPlease choose between the following option numbers:
(enter the digit only)
'1' - Send a Thank You
'2' - Create a Report
'3' - Send letters to all donors
'4' - Quit
: """


# This was originally a single function called 'Part1()' which called another function to add
# donations.  It worked, but I restructured it based on the recommendation in the notes.
def main():
    while True:
        Switch_dict.get(int(input(Prompt)))(Data)


def send_single(Data):
    full_name = 'list'
    while full_name == 'list':  # loop if 'list' is provided
        full_name = input("""Please provide a full name (case sensitive).
                          'list will show the list of donor names.
                          'quit' exits script.
                          : """)
        if full_name == 'quit':  # exit option, break while loop
            Quit_Program(Data)
        elif full_name == 'list':
            print('\n\n')
            for name in Data:
                print(name)
    if full_name not in Data:
        Data[full_name] = []  # Add name to original data, and empty donation list
        Data, don_sum = add_donations(full_name, Data)  # call function to add donation info
    elif full_name in Data:  # Select name already on list
        Data, don_sum = add_donations(full_name, Data)  # call function to add donation info
    print("\n\nHi {},\n\nThank you for your total donation of ${:,.2f}.\n\n\nVR\n\nThe Mailroom\n(555) 555-5555".format(full_name, don_sum))


def create_a_report(Data):
    report_List, key1, key2, key3, key4 = new_structure(Data)
    print("\n\n {:^28}|{:^18s}|{:^7s}|{:^18s}".format(key1, key3, key2, key4))
    print("-" * 75)
    for row in report_List:
        print(" {:28s}|{:17,.2f} |{:6d} |{:>18,.2f}".format(row[key1],
            row[key3], row[key2], row[key4]))


def send_all(Data):
    dst_dir = input(r"Please enter destination directory for the letter files (include closing '\' or '/'): ")
    report_List, key1, key2, key3, key4 = new_structure(Data)
    for donor in report_List:
        letter_path = dst_dir + donor['Donor Name'] + '.txt'
        with open(letter_path, 'w') as letter:
            letter.write("\nHi {},\n\nThank you for your lifetime donations of ${:,.2f}.\n\n\nVR\n\nThe Mailroom\n(555) 555-555".
                format(donor['Donor Name'], donor['Total Given($)']))


def quit_program(Data):
    print('\n\ngoodbye\n\n')
    sys.exit()


def add_donations(full_name, Data):  # function that adds donation info
    donation = ''
    don_sum = 0
    while donation != 'none':
        # query for amount, with option for no donation or exit parent function
        donation = input("""Please provide the donation amount
***(enter 'none' for no additional donation, 'quit' to exit script): """)
        if donation == 'quit':
            quit_program(Data)
        if donation != 'none':
            # add individual donation to original
            Data[full_name].append(float(donation))
            don_sum += float(donation)  # keep sum of donations
    return Data, don_sum  # return the updated original data and the sum of donations


def new_structure(Data):
    key1 = 'Donor Name'
    key2 = '# Gifts'
    key3 = 'Total Given($)'
    key4 = 'Average Gift'
    report_list = []  # create empty dataset of for reporting, to be populated by dicts
    # start populating dataset in accordance with the original data
    for i, name in enumerate(Data):
        num_don = len(Data[name])  # number of donations
        report_list.append({key1: name, key2: num_don})
        sum_individual = 0
        report_list[i][key3] = sum(Data[name])
        if num_don != 0:
            # determine average donation
            report_list[i][key4] = sum_individual / num_don
        else:
            report_list[i][key4] = sum_individual  # prevent division by zero

    def sort_total(val):  # define key for sorting
        return val[key3]
    report_list.sort(key=sort_total, reverse=True)  # sort by descending sum of donations
    return report_list, key1, key2, key3, key4


Switch_dict = {1: send_single, 2: create_a_report, 3: send_all, 4: quit_program}

if __name__ == "__main__":
    main()
