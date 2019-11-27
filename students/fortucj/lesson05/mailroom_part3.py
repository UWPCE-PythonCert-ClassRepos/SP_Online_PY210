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

Part 3 info:
The structure, style, and documentation was updated per lesson05 content.
Exceptions were added at each point where a user's input resulted in an error.
A comprehension was implemented to build the separate data structure.
"""

from sys import exit  # Import only one item, since only one item needed.

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
    """Prompot the user for an option, which will be handled by the  switch dict."""
    while True:
        answer = input(Prompt)
        try:
            Switch_dict.get(int(answer))(Data)
        # These could have been handled with a catch-all exception, resulting in a message...
        # ...to use the correct input, but I opted for error-specific exceptions in...
        # ...accordance with the lesson material.
        except TypeError:
            print("\n Integer input was not '1', '2', '3', '4'. Please use only one of these.")
        except ValueError:
            if answer.isalpha():
                print("\n Input was an alphabet character(s). Please use only '1', '2', '3', '4'.")
            else:
                try:
                    float(answer)
                    print("\n Input was a float. Please use only '1', '2', '3', or '4'.")
                except ValueError:
                    print("\n Input was a mixed string. Please use only '1', '2', '3', or '4'.")


def send_single(Data):
    """Prompt the user for a donor name, which will call a helper function to process donations."""
    input_name = 'list'
    while input_name == 'list':
        input_name = input("""Please provide a full name (case sensitive).
                          'list will show the list of donor names.
                          'quit' exits script.
                          : """)
        if input_name == 'quit':
            quit_program(Data)
        elif input_name == 'list':
            print('\n\n')
            for name in Data:
                print(name)
    if input_name not in Data:
        Data[input_name] = []
        Data, don_sum = add_donations(input_name, Data)  # helper function here
    elif input_name in Data:
        Data, don_sum = add_donations(input_name, Data)
    print("\n\nHi {},\n\nThank you for your total donation of ${:,.2f}.\n\n\nVR\n\nThe Mailroom\n(555) 555-5555".format(input_name, don_sum))


def create_a_report(Data):
    """Ingest data from the new structure, and print a report."""
    report_data, key1, key2, key3, key4 = new_structure(Data)
    print("\n\n {:^28}|{:^18s}|{:^7s}|{:^18s}".format(key1, key3, key2, key4))
    print("-" * 75)
    for row in report_data:
        print(" {:28s}|{:17,.2f} |{:6d} |{:>18,.2f}".format(row[key1],
            row[key3], row[key2], row[key4]))


def send_all(Data):
    """Prompt the user for a letter directory, and write a letter per user, based on the new structure."""
    status = True
    while status == True:
        dst_dir = input(r"Please enter destination directory for the letter files (include closing '\' or '/'): ")
        report_data, key1, key2, key3, key4 = new_structure(Data)
        for donor in report_data:
            letter_path = dst_dir + donor['Donor Name'] + '.txt'
            try:
                with open(letter_path, 'w') as letter:
                    letter.write("\nHi {},\n\nThank you for your lifetime donations of ${:,.2f}.\n\n\nVR\n\nThe Mailroom\n(555) 555-555".
                        format(donor['Donor Name'], donor['Total Given($)']))
            except OSError:  # This won't catch non-existent paths, just invalid input
                print('\n Invalid input. Please enter a valid path.')
                break
            else:
                status = False


def quit_program(Data):
    """Exit the program using the function from sys."""
    print('\n\ngoodbye\n\n')
    exit()


def add_donations(input_name, Data):
    """Helper function to process donation data."""
    donation = ''
    don_sum = 0
    while donation != 'none':
        donation = input("""Please provide the donation amount
***(enter 'none' for no additional donation, 'quit' to exit script): """)
        if donation == 'quit':
            quit_program(Data)
        if donation != 'none':
            try:
                Data[input_name].append(float(donation))
            except ValueError:
                print('\ninput was not a number, value tossed out\n')
            else:
                don_sum = sum(Data[input_name])
    return Data, don_sum


def new_structure(Data):
    key1 = 'Donor Name'
    key2 = '# Gifts'
    key3 = 'Total Given($)'
    key4 = 'Average Gift'
    # leveraged comprehensions and exceptions here!
    try:
        report_data = [{key1: name, key2: len(Data[name]), key3: sum(Data[name]), key4:
            sum(Data[name]) / len(Data[name])} for name in Data]
    except ZeroDivisionError:
        report_data = [{key1: name, key2: len(Data[name]), key3: sum(Data[name]), key4:
            sum(Data[name])} for name in Data]
    def sort_total(val):
        return val[key3]
    report_data.sort(key=sort_total, reverse=True)
    return report_data, key1, key2, key3, key4


Switch_dict = {1: send_single, 2: create_a_report, 3: send_all, 4: quit_program}

if __name__ == "__main__":
    main()
