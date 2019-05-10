#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tempfile

'''
revised mailroom app using dict switch and dict as a data structure (we used a list in the first version.

Added ability to create letters as text files, in a temp directory, in batch.

'''



def populate_data(donor_db):
    # Add donor records
    donor_db = add_contribution("Daenerys Targaryen", [100.00, 1000], donor_db)
    donor_db = add_contribution("Arya Stark", [65.00, 45.92, 1004, 2008, 7777], donor_db)
    donor_db = add_contribution("Melisandre", [19.00, 100000, 100000, 100000], donor_db)
    donor_db = add_contribution("Cersei Lannister", [10.00], donor_db)
    donor_db = add_contribution("Daenerys Targaryen", [400, 500, 700, 5555], donor_db)
    donor_db = add_contribution("Bran Stark", [666], donor_db)
    donor_db = add_contribution("Bran Stark", 777, donor_db) # We even handle for floats instead of lists, just in case
    return donor_db

def show_donors(donor_db):
    # Write header row
    row = "Donor", "Total", "Gifts", "Average"
    print("{:<25s}{:<20s}{:<10s}{:<13s}".format(*row))
    # Write corresponding ===='s
    print(''.join(("=" * 24 + " ",  # donor
          "=" * 19 + " ",           # total
          "=" * 9 + " ",            # gifts
          "=" * 12)))               # average

    for k, v in donor_db.items():
        # Write out rows: "Donor", "Total", "Gifts", "Average"
        row = k, sum(v), len(v), sum(v)/len(v)
        print("{:<25s}${:<19.2f}{:<10d}${:<13.2f}".format(*row))


def list_donors(donor_db):
    # List current donors in the dictionary as '#. First Last'
    print("{:<4} {:<7}".format("No.", "Name"))
    print("{} {}".format("=" * 4, "=" * 7))
    for i, donor in enumerate(donor_db):
        print("{:<4} {:<7}". format(i + 1, donor))


def print_menu():
    return ''.join((
        "\nMain Menu",
        "\n======================",
        "\n1. Send Thank You",
        "\n2. Create a Report",
        "\n3. Send letters to all donors"
        "\n4. Quit",
        "\n\nEnter Selection (1-4) >>> "
    ))


def record_contribution(donor_db):
    response = ""
    donor_name = ""
    amount = ""
    total_contributions = 0

    while donor_name == "" or donor_name == 'list':
        donor_name = input("Please enter donor full name or type 'list': ")
        if donor_name == 'list':
            list_donors(donor_db)
        else:
            amount = float(input("Please enter donation amount: "))
    else:
        if donor_db.get(donor_name):
                add_contribution(donor_name, amount, donor_db) # Add the contribution
                print(format_email(donor_name, amount, sum(donor_db[donor_name]))) # print mail to terminal
        else:
            response = str(input("Donor {} doesn't exist, add them (y/n)?:".format(donor_name)))
            if response.lower() == 'y':
                add_contribution(donor_name, amount, donor_db)
                print(format_email(donor_name, amount, sum(donor_db[donor_name])))
    return donor_db

def format_email(donor, amount, tc):

    mail_str = ''.join((
        "Dear {},\n\n",
        "Thank you for your recent contribution of ${:.2f}.\n\n",
        "We appreciate your generosity in support of our mission.\n\n",
        "Thank you for your lifetime contributions of ${:.2f}.\n\n"
        "Warmest Regards,\n\n",
        "Charity Staff\n")).format(donor, amount, tc)

    return mail_str

def add_contribution(donor, amount, donor_db):

    if donor_db.get(donor):
        if type(donor_db[donor]) is list:
            if type(amount) is list:
                donor_db[donor].extend(amount)  # when amount is a list
            else:
                donor_db[donor].extend([amount])  # in case we get passed a float for amount
        else:
            donor_db[donor].append(amount) # add new to dict
        # otherwise, add a single contribution with a new user
    else:
        if type(amount) is list:
            donor_db[donor] = amount
        else:
            donor_db[donor] = [amount]
    return donor_db


def send_letter_to_all(donor_db):
    for k, v in donor_db.items():
        tempfilepath = tempfile.gettempdir() + "/" + str(k.replace(' ', "_")) + ".txt"
        with open(tempfilepath, "w") as outputfile:
            print("writing letter and storing in: " + tempfilepath)
            outputfile.writelines(format_email(k, v[len(v)-1], sum(donor_db[k])))
            outputfile.close()

def switcher(arg, donor_db):
    # Use a dictionary as a switch statement!
    switcher = {
        1: record_contribution,
        2: show_donors,
        3: send_letter_to_all,
        4: exit,
    }
    func = switcher.get(arg, lambda: print("Invalid Entry"))
    # print("running " + func)
    if func == exit:
        func()
    else:
        func(donor_db)


def main(donor_db):
    while True:
        switcher(int(input(print_menu())), donor_db)



if __name__ == '__main__':
    # We're not getting imported, run main():
    donor_db = {}  # dict that contains user/donation records
    donor_db = populate_data(donor_db)
    main(donor_db)