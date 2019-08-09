#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tempfile

'''
revised mailroom app using dict switch and dict as a data structure (we used a list 
in the first version.

Added ability to create letters as text files, in a temp directory, in batch.

Added sorting abilities here. I originally missed this in the first mailroom assignment.

'''


def populate_data():
    '''
    Populate dictionary with initial data
    '''

    add_contribution("Daenerys Targaryen", [100.00, 1000])
    add_contribution("Arya Stark", [65.00, 45.92, 1004, 2008, 7777])
    add_contribution("Melisandre", [19.00, 100000, 100000, 100000])
    add_contribution("Cersei Lannister", [10.00])
    add_contribution("Daenerys Targaryen", [400, 500, 700, 5555])
    add_contribution("Bran Stark", [666])
    add_contribution("Bran Stark", 777) # We even handle for floats instead



def show_donors():
    '''
    Write a report to screen of donors and information about how they've donated

    Return values in descending order from the sum of their historical contributions
    '''

    # Write header row
    row = "Donor", "Total", "Gifts", "Average"
    print("{:<25s}{:<20s}{:<10s}{:<13s}".format(*row))
    # Write corresponding ===='s
    print(''.join(("=" * 24 + " ",  # donor
                   "=" * 19 + " ",  # total
                   "=" * 9 + " ",   # gifts
                   "=" * 12)))      # average

    #  Get a sorted list of donors names sorted by their contributions, descending
    ordered_donors = sorted(donor_db, key=lambda k: sum(donor_db[k]), reverse=True)
    for name in ordered_donors:
        contributions = donor_db.get(name)
        # alphabetical by keys. Write out rows: "Donor", "Total", "Gifts", "Average"
        row = name, sum(contributions), len(contributions), sum(contributions)/len(contributions)
        print("{:<25s}${:<19.2f}{:<10d}${:<13.2f}".format(*row))



def list_donors():
    '''
    Write a numbered list for the purpose of selecting a donor

    Use a list comprehension to print the numbered list
    '''
    # List current donors in the dictionary as '#. First Last'
    print("{:<4} {:<7}".format("No.", "Name"))
    print("{} {}".format("=" * 4, "=" * 7))

    for i, donor in enumerate(sorted(donor_db)):
        print("{:<4} {:<7}".format(i + 1, donor))


def print_menu():
    '''
    Print a menu to the user's screen
    '''
    return ''.join((
        "\nMain Menu",
        "\n======================",
        "\n1. Send Thank You",
        "\n2. Create a Report",
        "\n3. Send letters to all donors"
        "\n4. Quit",
        "\n\nEnter Selection (1-4) >>> "
    ))


def record_contribution():
    '''
    Prompt user for new contribution for a new or existing donor. Return dictionary with any updates

    add_contribution() actually updates the dictionary, it's called from here.
    '''
    donor_name = ""
    amount = ""

    while donor_name == "" or donor_name == 'list':
        donor_name = input("Please enter donor full name or type 'list': ")
        if donor_name == 'list':
            list_donors()
        else:
            amount = float(input("Please enter donation amount: "))
    else:
        if donor_db.get(donor_name):
            add_contribution(donor_name, amount)  # Add the contribution
            print(format_email(donor_name, amount, sum(donor_db[donor_name])))  # print mail
            #  to terminal
        else:
            response = str(input("Donor {} doesn't exist, add them (y/n)?:".format(donor_name)))
            if response.lower() == 'y':
                add_contribution(donor_name, amount)
                print(format_email(donor_name, amount, sum(donor_db[donor_name])))


def format_email(donor, amount, total_contribution):
    '''
    Create a thank you email for a donor.
    '''

    mail_str = ''.join((
        "Dear {},\n\n",
        "Thank you for your recent contribution of ${:.2f}.\n\n",
        "We appreciate your generosity in support of our mission.\n\n",
        "Thank you for your lifetime contributions of ${:.2f}.\n\n"
        "Warmest Regards,\n\n",
        "Charity Staff\n")).format(donor, amount, total_contribution)

    return mail_str


def add_contribution(donor, amount):
    '''
    After record_contribution() prompts user for input, add records to dictionary as needed.

    Do extra handling to account for floats and lists for the amounts
    '''

    if donor_db.get(donor):
        if isinstance(donor_db[donor], list):
            if isinstance(amount, list):
                donor_db[donor].extend(amount)  # when amount is a list
            else:
                #  Append for adding one value, vs above where it's a list...
                donor_db[donor].extend([amount])  # in case we get passed a float for amount
    else:
        # otherwise, add a single contribution with a new user
        if isinstance(amount, list):
            donor_db[donor] = amount
        else:
            donor_db[donor] = [amount]
    return donor_db


def send_letter_to_all(donor_db):
    '''
    Write text files containing letter contents for all donors in the database
    '''

    for key, value in donor_db.items():
        tempfilepath = tempfile.gettempdir() + "/" + str(key.replace(' ', "_")) + ".txt"
        try:
            with open(tempfilepath, "w") as outputfile:
                outputfile.writelines(format_email(key, value[len(value)-1], sum(donor_db[key])))
        except IOError:
            print("IOError: Could not create file:" + tempfilepath)


def switcher(arg):
    '''
    Use a switcher dictionary as a way to present a menu-driven interface for users
    '''

    # Use a dictionary as a switch statement!
    switcher = {
        1: record_contribution,
        2: show_donors,
        3: send_letter_to_all,
        4: exit,
    }
    func = switcher.get(arg, lambda: print("Invalid Entry"))
    func()



def main():
    '''
    main loop, continually present users with menu options
    '''

    while True:
        switcher(int(input(print_menu())))


if __name__ == '__main__':
    # We're not getting imported, run main():
    donor_db = {}  # dict that contains user/donation records
    populate_data()
    main()
