#!/usr/bin/env python3
# -*- coding: utf-8 -*-
<<<<<<< HEAD
=======
import sys
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7

'''
Initial data structure. Keep track of donors and the amount(s) they've contributed

Records will look like this:

[('James Butts', (100.0, 2000))]
<<<<<<< HEAD
'''

DONOR_DB = [] # larger table that contains user records

=======


'''

donor_db = [] # larger table that contains user records
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7

def populate_data(donors):
    # Add donor records
    add_contribution("Daenerys Targaryen", [100.00, 1000], donors)
    add_contribution("Arya Stark", [65.00, 45.92, 1004, 2008, 7777], donors)
<<<<<<< HEAD
    # !!! removed donor_db =
    add_contribution("Melisandre", [19.00, 100000, 100000, 100000], donors)
    add_contribution("Cersei Lannister", [10.00], donors)
    add_contribution("Daenerys Targaryen", [400, 500, 700, 5555], donors)
    add_contribution("Bran Stark", 666, donors)
    add_contribution("Bran Stark", 777, donors)
    return donors


def show_donors(donors):
    # Write header row
    print(type(donors))
    #  Do what StackExchange said for the sort. Looking forward to learning about Lambdas!
    donors.sort(key=lambda donations: sum(donations[1]), reverse=True)
=======
    donor_db = add_contribution("Melisandre", [19.00, 100000, 100000, 100000], donors)
    donor_db = add_contribution("Cersei Lannister", [10.00], donors)
    donor_db = add_contribution("Daenerys Targaryen", [400, 500, 700, 5555], donors)
    donor_db = add_contribution("Bran Stark", 666, donors)
    donor_db = add_contribution("Bran Stark", 777, donors)
    return donors

def show_donors(donors):
    # Write header row
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    row = "Donor", "Total", "Gifts", "Average"
    print("{:<25s}{:<20s}{:<10s}{:<13s}".format(*row))
    # Write corresponding ===='s
    print(''.join(("=" * 24 + " ",  # donor
<<<<<<< HEAD
        "=" * 19 + " ",           # total
        "=" * 9 + " ",            # gifts
        "=" * 12)))               # average

    for record in donors:
        # Write out rows: "Donor", "Total", "Gifts", "Average"
        row = record[0], sum(record[1]), len(record[1]), sum(record[1])/len(record[1])
        print("{:<25s}${:<19.2f}{:<10d}${:<13.2f}".format(*row))


def list_donors(donors):
    # add docstring
=======
          "=" * 19 + " ",           # total
          "=" * 9 + " ",            # gifts
          "=" * 12)))               # average

    for r in donors:
        # Write out rows: "Donor", "Total", "Gifts", "Average"
        row = r[0], sum(r[1]), len(r[1]), sum(r[1])/len(r[1])
        print("{:<25s}${:<19.2f}{:<10d}${:<13.2f}".format(*row))

def list_donors(donors):
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    print("{:<4} {:<7}".format("No.", "Name"))
    print("{} {}".format("=" * 4, "=" * 7))
    for i, donor in enumerate(donors):
        print("{:<4} {:<7}". format(i + 1, donor[0]))

<<<<<<< HEAD

def print_menu():
    # add docstring
=======
def print_menu():
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    return ''.join((
        "\nMain Menu",
        "\n======================",
        "\n1. Send Thank You",
        "\n2. Create a Report",
        "\n3. Quit",
        "\n\nEnter Selection (1-3) >>> "
    ))

<<<<<<< HEAD

def get_contribution(donors):
    # add docstring
=======
def get_contribution(donors):
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    response = ""
    donor_name = ""
    amount = ""

    while donor_name == "" or donor_name == 'list':
        donor_name = input("Please enter donor full name or type 'list': ")
        if donor_name == 'list':
            list_donors(donors)
<<<<<<< HEAD
        # !!! linter says this else is useless
        #else:
        #    amount = float(input("Please enter donation amount: "))
    else:
        for record in donors:
            if donor_name == record[0]:
                add_contribution(donor_name, amount, donors)
                print(format_email(donor_name, amount))
=======
        else:
            amount = float(input("Please enter donation amount: "))
    else:
        for r in donors:
            if donor_name == r[0]:
                add_contribution(donor_name, amount, donors)
                print(format_email(donor_name, amount, donors))
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
                break
        else:
            response = str(input("Donor {} doesn't exist, add them (y/n)?:".format(donor_name)))
            if response.lower() == 'y':
                add_contribution(donor_name, amount, donors)
<<<<<<< HEAD
                print(format_email(donor_name, amount))
    return donors


def format_email(donor, amount):
    # add docstring
=======
                print(format_email(donor_name, amount, donors))




    return donors

def format_email(donor, amount, donors):
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7

    mail_str = ''.join((
        "\n\n\n\nDear {},\n\n",
        "Thank you for your contribution of ${}.\n\n",
        "We appreciate your generosity in support of our mission.\n\n",
        "Warmest Regards,\n\n",
        "Charity Staff\n")).format(donor, amount)

    return mail_str

<<<<<<< HEAD

def add_contribution(donor, amount, donors):
    # add docstring

    for record in donors:
        if donor in record[0]:
            if record[1] and isinstance(amount, list): # !!! changed from type(),
                # non-empty eval to true, no len()
                # If there's already a list, use the extend method in case we have been
                # passed another list
                record[1].extend(amount)
            else:
                record[1].append(amount)
            break
    else:
        # Handle being passed a list of contributions for new record
        if isinstance(amount, list):
            DONOR_DB.append((donor, amount))
        # otherwise, add a single contribution with a new user
        else:
            DONOR_DB.append((donor, [amount]))
=======
def add_contribution(donor, amount, donors):
    for r in donors:
        if donor in r[0]:
            if len(r[1]) > 0 and type(amount) is list:
                # If there's already a list, use the extend method in case we have been passed another list
                r[1].extend(amount)
            else:
                r[1].append(amount)
            break
    else:
        # Handle being passed a list of contributions for new record
        if type(amount) is list:
            donor_db.append((donor, amount))
        # otherwise, add a single contribution with a new user
        else:
            donor_db.append((donor, [amount]))
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    return donors


def main():
<<<<<<< HEAD
    # add docstring
=======
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
    response = ""
    while response != 3:
        response = int(input(print_menu()))
        if response == 1:
<<<<<<< HEAD
            get_contribution(DONOR_DB)

        elif response == 2:
            show_donors(DONOR_DB)
=======
            get_contribution(donor_db)

        elif response == 2:
            show_donors(donor_db)

>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7


if __name__ == '__main__':
    # We're not getting imported, run main():
<<<<<<< HEAD
    DONOR_DB = []
    DONOR_DB = populate_data(DONOR_DB)
    main()
=======
    donor_db = []
    donor_db = populate_data(donor_db)
    main()
>>>>>>> fedf8c86a2a2636875db022c6fb2dee41583f9a7
