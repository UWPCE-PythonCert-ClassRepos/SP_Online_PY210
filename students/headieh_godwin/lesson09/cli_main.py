#!/usr/bin/env python3

import sys
import re
import donor_models as dm

_dc = dm.DonorCollection()

# Get money
def valid_money():
    while True:
        r = input("Please enter a donation amount ")
        try:
            amount = float(r)
            if amount < 0.01 or amount > 10000:
                print("Invalid value")
            else:
                return amount
        except ValueError:
            print("Invalid value")


# Get name
def valid_name():
    while True:
        r = input("Please enter a full name ")
        r2= re.sub(r'[^a-zA-Z]+', '', r)
        if r == 'list':
            print (_dc)
        elif r == '':
            print('No name entered')
        elif r2 == '':
            print('Not a valid name')
        else:
            return r


def thanks():
    """adds donation and sends a thanks message"""
    response1 = valid_name()
    if response1 == 'list':
        print(_dc)
    else:
        amount = valid_money()
        if not amount: #if get donation returns nothing, return nothing back to main
            return
        else:
            donor1 = donor_check(response1)
            donor1.add_donation(amount)
            print (donor1.send_thank_you(amount))

def donor_check(r1):
    """revisit and recode this"""
    for i, x in enumerate(_dc.list_donors):
        if x.name == r1:
            return _dc.list_donors[i]
    else:
        donor_new = dm.Donor(r1)
        _dc.add_donors(donor_new)
        return donor_new


def original_prompt():
    answers = input(f"""

Choose an action:

1 - Send a Thank You to a single donor.
2 - Create a Report.
3 - Send letters to all donors.
4 - Quit
""")
    return(answers)

def main():
    options = {
        1: thanks,
        2: report,
        3: thanks_all,
        4: quits
    }

    while True:
        try:
            resp = original_prompt()
            if int(resp) in options:
                options.get(int(resp))()
            else:
                print(' Input is invalid, please input a valid option. ')
        except ValueError:
            print(' Input is invalid, please input a valid option. ')

def quits():
    print("Bye!")
    sys.exit()

def initial():
    """initializes the dataset"""
    d1 = dm.Donor('Karen')
    d2 = dm.Donor('Susan')
    d3 = dm.Donor('Larry')
    d4 = dm.Donor('Curly')
    d5 = dm.Donor('Mo')
    d1.add_donation(20,20,100)
    d2.add_donation(20)
    d3.add_donation(40,50)
    d4.add_donation(20.99,20,100)
    d5.add_donation(2)
    _dc.add_donors(d1,d2,d3,d4,d5)


def report():
    """displays donor report"""
    print(_dc.report())

def thanks_all():
    """sends thanks to everyone"""
    print (_dc.thanks_all())


if __name__ == "__main__":
    initial()
    main()
